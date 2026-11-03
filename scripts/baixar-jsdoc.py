#!/usr/bin/env python3
"""
Baixa TODA a documentação JSDoc do Moodle → Markdown.

Site: https://jsdoc.moodledev.io/

Por padrão baixa **todas** as branches listadas no índice (4.01, 4.04, 4.05,
5.00, 5.01, main, …) e faz crawl BFS das páginas .html (módulos + fontes
`*_amd_src_*.js.html`).

Uso (na raiz do APP-MOODLE):
  ./scripts/baixar-jsdoc.py              # todas as versões
  ./scripts/baixar-jsdoc.py 4.05 5.01    # só algumas
  ./scripts/baixar-jsdoc.py --list
"""
from __future__ import annotations

import argparse
import html as htmlmod
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
from pathlib import Path

BASE = "https://jsdoc.moodledev.io"
UA = "APP-MOODLE-jsdoc-fetch/1.1 (+local; polite)"
MAX_WORKERS = 10
TIMEOUT = 60


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def list_branches() -> list[str]:
    page = fetch(f"{BASE}/")
    return re.findall(r"href=['\"]\./([^'\"/]+)['\"]", page)


def extract_local_html_links(html: str) -> set[str]:
    """Todos os .html locais (module-*, classes, *_amd_src_*.js.html, …)."""
    found: set[str] = set()
    for href in re.findall(r"""href=["']([^"']+)["']""", html, flags=re.I):
        href = href.split("#", 1)[0].strip()
        if not href or href.startswith(("http://", "https://", "//", "mailto:", "javascript:")):
            continue
        href = urllib.parse.unquote(href.lstrip("./"))
        if not href.endswith(".html"):
            continue
        if "/" in href:
            # só páginas flat do JSDoc na raiz da branch
            continue
        found.add(href)
    return found


class JSDocHTMLToMarkdown(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_main = False
        self.main_depth = 0
        self.in_nav = False
        self.in_ignore = False
        self.in_title = False
        self.in_pre = False
        self.in_a = False
        self.a_href = ""
        self.a_text = ""
        self.list_depth = 0
        self.title = ""
        self.out: list[str] = []
        self.text_buf = ""

    def _flush_text(self) -> str:
        t = self.text_buf
        self.text_buf = ""
        if self.in_pre:
            return t
        return re.sub(r"[ \t]+", " ", t)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        ad = {k: (v or "") for k, v in attrs}
        if tag == "title":
            self.in_title = True
            self.text_buf = ""
            return
        if tag in ("script", "style"):
            self.in_ignore = True
            return
        if tag == "nav":
            self.in_nav = True
            return
        if not self.in_main:
            if tag == "div" and ad.get("id") == "main":
                self.in_main = True
                self.main_depth = 1
            return
        if self.in_nav or self.in_ignore:
            return

        chunk = self._flush_text()
        if chunk:
            self.out.append(chunk)

        if tag == "div":
            self.main_depth += 1
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.out.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "p":
            self.out.append("\n\n")
        elif tag == "br":
            self.out.append("  \n")
        elif tag in ("ul", "ol"):
            self.list_depth += 1
            self.out.append("\n")
        elif tag == "li":
            self.out.append("\n" + ("  " * max(self.list_depth - 1, 0)) + "- ")
        elif tag == "pre":
            self.in_pre = True
            self.out.append("\n\n```js\n")
        elif tag == "code" and not self.in_pre:
            self.out.append("`")
        elif tag == "a":
            self.in_a = True
            self.a_href = ad.get("href", "")
            self.a_text = ""
        elif tag == "hr":
            self.out.append("\n\n---\n\n")
        elif tag in ("strong", "b"):
            self.out.append("**")
        elif tag in ("em", "i"):
            self.out.append("*")
        elif tag == "dt":
            self.out.append("\n\n**")
        elif tag == "dd":
            self.out.append(":** ")

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.title = self.text_buf.strip()
            self.text_buf = ""
            self.in_title = False
            return
        if tag in ("script", "style"):
            self.in_ignore = False
            return
        if tag == "nav":
            self.in_nav = False
            return
        if not self.in_main:
            return
        if self.in_nav or self.in_ignore:
            return

        if tag == "a" and self.in_a:
            text = (self.a_text or self.text_buf).strip() or self.a_href
            self.text_buf = ""
            href = self.a_href.split("#", 1)[0]
            if href.endswith(".html"):
                href = href[:-5] + ".md"
            self.out.append(f"[{text}]({href})" if href else text)
            self.in_a = False
            self.a_href = ""
            self.a_text = ""
            return

        chunk = self._flush_text()
        if self.in_a:
            self.a_text += chunk
            return
        if chunk:
            self.out.append(chunk)

        if tag == "div":
            self.main_depth -= 1
            if self.main_depth <= 0:
                self.in_main = False
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6", "p"):
            self.out.append("\n\n")
        elif tag in ("ul", "ol"):
            self.list_depth = max(0, self.list_depth - 1)
            self.out.append("\n")
        elif tag == "pre":
            self.in_pre = False
            self.out.append("\n```\n\n")
        elif tag == "code" and not self.in_pre:
            self.out.append("`")
        elif tag in ("strong", "b"):
            self.out.append("**")
        elif tag in ("em", "i"):
            self.out.append("*")

    def handle_data(self, data: str) -> None:
        if self.in_ignore or self.in_nav:
            return
        if self.in_title:
            self.text_buf += data
            return
        if not self.in_main:
            return
        if self.in_a:
            self.a_text += data
            return
        self.text_buf += data

    def get_markdown(self) -> str:
        chunk = self._flush_text()
        if chunk:
            self.out.append(chunk)
        md = "".join(self.out)
        md = re.sub(r"\*\*\s*\*\*", "", md)
        md = re.sub(r"\n[ \t]+\n", "\n\n", md)
        md = re.sub(r"\n{3,}", "\n\n", md)
        return md.strip() + "\n"


def html_to_markdown(html: str, source_url: str) -> str:
    parser = JSDocHTMLToMarkdown()
    parser.feed(html)
    parser.close()
    title = parser.title or "JSDoc"
    body = parser.get_markdown()
    if not body.strip():
        text = re.sub(r"(?is)<script.*?>.*?</script>", "", html)
        text = re.sub(r"(?is)<style.*?>.*?</style>", "", text)
        text = re.sub(r"(?is)<nav.*?>.*?</nav>", "", text)
        text = re.sub(r"(?s)<[^>]+>", "", text)
        body = htmlmod.unescape(text)
        body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"
    return f"# {title}\n\n> Fonte: {source_url}\n\n{body}"


def crawl_branch_pages(branch: str) -> list[str]:
    """BFS: index → módulos → fontes .js.html etc."""
    start = "index.html"
    seen: set[str] = set()
    q: deque[str] = deque([start])
    while q:
        page = q.popleft()
        if page in seen:
            continue
        seen.add(page)
        url = f"{BASE}/{branch}/{page}"
        try:
            html = fetch(url)
        except Exception as exc:  # noqa: BLE001
            print(f"  WARN crawl {page}: {exc}", file=sys.stderr)
            continue
        for link in extract_local_html_links(html):
            if link not in seen:
                q.append(link)
        # leve pausa pra não martelar o site no crawl
        if len(seen) % 80 == 0:
            print(f"  … crawl {len(seen)} páginas descobertas")
            time.sleep(0.15)
    return sorted(seen)


def download_branch(branch: str, out_root: Path, workers: int) -> int:
    branch_url = f"{BASE}/{branch}/"
    out_dir = out_root / branch
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"==> Branch {branch}")
    print("  Descobrindo páginas (módulos + sources)…")
    try:
        pages = crawl_branch_pages(branch)
    except urllib.error.HTTPError as e:
        print(f"  ERRO HTTP {e.code} em {branch_url}", file=sys.stderr)
        return 0

    print(f"  {len(pages)} páginas para baixar")

    def one(page: str) -> tuple[str, bool, str]:
        url = f"{BASE}/{branch}/{page}"
        try:
            html = fetch(url)
            md = html_to_markdown(html, url)
            # .js.html → .js.md
            if page.endswith(".html"):
                dest_name = page[:-5] + ".md"
            else:
                dest_name = page + ".md"
            dest = out_dir / dest_name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(md, encoding="utf-8")
            return page, True, dest.name
        except Exception as exc:  # noqa: BLE001
            return page, False, str(exc)

    ok = 0
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futs = [pool.submit(one, p) for p in pages]
        done = 0
        for fut in as_completed(futs):
            page, success, info = fut.result()
            done += 1
            if success:
                ok += 1
            else:
                print(f"  FAIL {page}: {info}", file=sys.stderr)
            if done % 50 == 0 or done == len(pages):
                print(f"  … {done}/{len(pages)}")

    lines = [
        f"# Moodle JSDoc — {branch}",
        "",
        f"Espelho Markdown de {branch_url}",
        "",
        f"Páginas: **{ok}** (módulos AMD + fontes `*_amd_src_*.js`)",
        "",
        "## Índice",
        "",
    ]
    for mdfile in sorted(out_dir.glob("*.md")):
        if mdfile.name == "README.md":
            continue
        lines.append(f"- [{mdfile.stem}]({mdfile.name})")
    (out_dir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  OK {ok}/{len(pages)} → {out_dir}")
    return ok


def main() -> int:
    ap = argparse.ArgumentParser(description="Baixa todo JSDoc Moodle → Markdown")
    ap.add_argument("branches", nargs="*", help="vazio = TODAS as do site")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--out", default=None)
    ap.add_argument("--workers", type=int, default=MAX_WORKERS)
    args = ap.parse_args()

    # raiz do vault = pai de scripts/
    root = Path(__file__).resolve().parent.parent
    out_root = Path(args.out) if args.out else root / "jsdoc"

    if args.list:
        print("Branches em", BASE)
        for b in list_branches():
            print(" ", b)
        return 0

    env_b = os.environ.get("BRANCHES", "").strip()
    if args.branches:
        branches = list(args.branches)
    elif env_b:
        branches = [x.strip() for x in re.split(r"[, ]+", env_b) if x.strip()]
    else:
        branches = list_branches()
        if not branches:
            print("Nenhuma branch no índice.", file=sys.stderr)
            return 1

    print(f"Saída: {out_root}")
    print(f"Branches ({len(branches)}): {', '.join(branches)}")
    total = 0
    t0 = time.time()
    for b in branches:
        total += download_branch(b, out_root, workers=args.workers)
        time.sleep(0.2)

    lines = [
        "# Moodle JavaScript Documentation (JSDoc → MD)",
        "",
        f"Espelho local de [{BASE}]({BASE}/).",
        "",
        "Módulos AMD + páginas de fonte (`blocks_…_amd_src_….js.md`).",
        "",
        "## Branches",
        "",
    ]
    for b in branches:
        d = out_root / b
        n = len([p for p in d.glob("*.md") if p.name != "README.md"]) if d.is_dir() else 0
        lines.append(f"- [{b}]({b}/README.md) — {n} páginas")
    lines += [
        "",
        "## Atualizar",
        "",
        "```bash",
        "./scripts/baixar-jsdoc.py           # todas as versões do site",
        "./scripts/baixar-jsdoc.py 4.05 main",
        "./scripts/baixar-jsdoc.py --list",
        "```",
        "",
        f"Gerado em {time.strftime('%Y-%m-%d %H:%M:%S')}.",
        "",
    ]
    out_root.mkdir(parents=True, exist_ok=True)
    (out_root / "README.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Done. {total} páginas em {time.time() - t0:.1f}s → {out_root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
