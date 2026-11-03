#!/usr/bin/env python3
"""
Limpa o clone do moodle/devdocs: deixa só Markdown útil (versões do vault).

Uso (raiz APP-MOODLE):
  ./scripts/limpar-devdocs.py
  ./scripts/limpar-devdocs.py --clone
  ./scripts/limpar-devdocs.py --pull
  KEEP_VERSIONS=4.5,5.1,5.2 ./scripts/limpar-devdocs.py
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_URL = os.environ.get("DEVDOCS_REPO", "https://github.com/moodle/devdocs.git")
DEFAULT_KEEP = ("4.5", "5.1", "5.2")

REMOVE_GENERAL = (
    "app_releases",
    "community",
    "releases",
    "app",
    "workplace",
    "projects",
    "designsystem",
    "contentguidelines",
    "_releases",
)
REMOVE_GENERAL_FILES = (
    "app.md",
    "app_releases.md",
    "releases.md",
    "contentguidelines.md",
)
REMOVE_DIRS = (
    ".yarn",
    ".github",
    ".husky",
    ".vscode",
    ".markdownlint",
    "src",
    "static",
    "scripts",
    "config",
    "sidebars",
    "versioned_sidebars",
    "data",
    "node_modules",
    ".git",
)
REMOVE_FILES = (
    "yarn.lock",
    "package.json",
    "package-lock.json",
    "tsconfig.json",
    "jest.config.js",
    "docusaurus.config.js",
    "babel-test.config.js",
    "cspell.config.js",
    "nextVersion.js",
    "migratedPages.js",
    "netlify.toml",
    "project-words.txt",
    "UPGRADING.md",
    "CODEOWNERS",
    "CONTRIBUTING.md",
    "COPYING.txt",
    ".editorconfig",
    ".env.default",
    ".eslintrc.js",
    ".gitattributes",
    ".gitignore",
    ".gitpod.yml",
    ".lintstagedrc.mjs",
    ".markdownlint-cli2.cjs",
    ".nvmrc",
    ".stylelintrc.json",
    ".yarnrc.yml",
    "versions.json",
    "versionsArchived.json",
)


def du_human(path: Path) -> str:
    try:
        out = subprocess.check_output(["du", "-sh", str(path)], text=True)
        return out.split()[0]
    except Exception:
        return "?"


def main() -> int:
    ap = argparse.ArgumentParser(description="Limpa ./devdocs para Markdown enxuto")
    ap.add_argument("--clone", action="store_true", help="Clona se não existir")
    ap.add_argument("--pull", action="store_true", help="git pull antes de limpar")
    args = ap.parse_args()

    root = Path(__file__).resolve().parent.parent
    dd = root / "devdocs"

    env_keep = os.environ.get("KEEP_VERSIONS", "").strip()
    if env_keep:
        keep = tuple(x.strip() for x in env_keep.replace(" ", ",").split(",") if x.strip())
    else:
        keep = DEFAULT_KEEP

    if not dd.is_dir():
        if not args.clone:
            print(f"Pasta {dd} não existe. Rode: ./scripts/limpar-devdocs.py --clone", file=sys.stderr)
            return 1
        print(f"==> Clonando {REPO_URL} → {dd}")
        subprocess.check_call(["git", "clone", "--depth", "1", REPO_URL, str(dd)])

    if args.pull and (dd / ".git").is_dir():
        print(f"==> git pull em {dd}")
        subprocess.call(["git", "-C", str(dd), "pull", "--ff-only"])

    before = du_human(dd)
    print(f"==> Limpando {dd} (antes: {before}) | versões: {', '.join(keep)}")

    vdocs = dd / "versioned_docs"
    if vdocs.is_dir():
        for child in list(vdocs.iterdir()):
            if not child.is_dir() or not child.name.startswith("version-"):
                continue
            ver = child.name[len("version-") :]
            if ver not in keep:
                print(f"    rm versioned_docs/{child.name}")
                shutil.rmtree(child, ignore_errors=True)

    general = dd / "general"
    if general.is_dir():
        for name in REMOVE_GENERAL:
            shutil.rmtree(general / name, ignore_errors=True)
        for name in REMOVE_GENERAL_FILES:
            (general / name).unlink(missing_ok=True)

    for name in REMOVE_DIRS:
        shutil.rmtree(dd / name, ignore_errors=True)
    for name in REMOVE_FILES:
        (dd / name).unlink(missing_ok=True)

    keep_list = ", ".join(keep)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    (dd / "README.md").write_text(
        f"""# Moodle DevDocs (extraído / enxuto)

Markdown offline de https://moodledev.io/ — sem Docusaurus.

Versões: **{keep_list}**

```bash
./scripts/limpar-devdocs.py --clone
./scripts/limpar-devdocs.py --pull
KEEP_VERSIONS=4.5,5.1,5.2,5.3 ./scripts/limpar-devdocs.py
```

Gerado por scripts/limpar-devdocs.py em {now}.
""",
        encoding="utf-8",
    )

    after = du_human(dd)
    print(f"==> Pronto. Antes: {before}  Agora: {after}")
    print("    Pastas:", " ".join(sorted(p.name for p in dd.iterdir())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
