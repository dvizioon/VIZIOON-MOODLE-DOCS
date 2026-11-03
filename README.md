# APP-MOODLE — documentação pessoal do código Moodle

Vault Obsidian com notas tiradas **do código fonte** dos checkouts em `/home/daniel/Área de trabalho/Projetos/MOODLE/`. Não é o core instalável: é o mapa de APIs, plugins, forms, settings e segurança pra desenvolver.

## Versões documentadas

Cada pasta `X.Y.Z/` espelha um checkout analisado. Quando baixar outra release, crie a pasta com o mesmo número e copie a estrutura (veja [[_meta/Como-adicionar-versao|Como adicionar uma versão]]).

| Versão | Pasta | Status | Entrada |
|--------|-------|--------|---------|
| **4.5.8** | [[4.5.8/README\|4.5.8/]] | Estável LTS — docs base (mais completas) | PHP 8.1+, AMD + Mustache |
| **5.2** | [[5.2/README\|5.2/]] | Atual do projeto — docs + IOMAD/temas/React | PHP do checkout 5.2; pode ter `public/` |
| 5.1 | — | Placeholder — baixar e documentar | |
| 5.0 | — | Placeholder | |
| 4.4 | — | Placeholder | |
| 4.3 | — | Placeholder | |

Links rápidos:

- [[4.5.8/README|Moodle 4.5.8 — índice]]
- [[5.2/README|Moodle 5.2 — índice]]
- [[relatorios/01-Relatorios-Moodle/README|Relatórios (notas transversais)]]

## Mapa por assunto (todas as versões)

| Assunto | 4.5.8 | 5.2 |
|---------|-------|-----|
| Estrutura / bootstrap | [[4.5.8/Estrutura/Base]] | [[5.2/Estrutura/Base]] |
| Tipos de plugin | [[4.5.8/Plugins/Tipos]] | [[5.2/Plugins/Tipos]] |
| Criar plugin | [[4.5.8/Plugins/Criar]] | [[5.2/Plugins/Criar]] |
| **Forms** (`mod_form`, block, moodleform) | [[4.5.8/Plugins/Forms]] | [[5.2/Plugins/Forms]] |
| **Settings** (`settings.php`, admin) | [[4.5.8/Plugins/Settings]] | [[5.2/Plugins/Settings]] |
| Segurança (funções + checklist) | [[4.5.8/Seguranca/Funcoes]] | [[5.2/Seguranca/Funcoes]] |
| Web services | [[4.5.8/WebServices/Criar]] | [[5.2/WebServices/Criar]] |
| DB / XMLDB | [[4.5.8/DB/Schema]] | [[5.2/DB/Schema]] |
| Eventos / hooks | [[4.5.8/Eventos/Observer]] | [[5.2/Eventos/Observer]] |
| Templates Mustache | [[4.5.8/Templates/Mustache]] | [[5.2/Templates/Mustache]] |
| Front | [[4.5.8/Frontend/AMD]] | [[5.2/Frontend/React]] |
| Admin | [[4.5.8/Admin/Administracao]] | — |
| Helper diário | [[4.5.8/Classes/Helper]] | [[5.2/Classes/Helper]] |
| Report Builder | [[4.5.8/ReportBuilder/Fontes]] | [[5.2/ReportBuilder/Fonte-Atividades]] |
| IOMAD | — | [[5.2/IOMAD/README]] |

## Meta (padrões do time)

- [[_meta/Como-adicionar-versao|Como adicionar uma versão]]
- [[_meta/Layout-Admin-Padrao|Layout admin padrão (azul)]] — Header/Footer estilo OxyMsTeams + CatalogGate
- [[_meta/Nomenclatura-GitHub|Nomenclatura GitHub]] — `moodle-report_activities`
- [[_meta/Cursor-Skills-Rules|Skills e rules]] — `.cursor/` + espelhos OpenCode/Claude/Agent/Codex ([[AGENTS.md]])
- [[_meta/Marketplace-Selos|Selos Marketplace]] — Privacy friendly · AUTO TEST · Early bird
- [[CI/README|CI moodle-plugin-ci]] — bancos · versões Moodle · segurança · quality · [[CI/ci.yml|suite full]]

## Como este vault cresce

1. Baixar o Moodle (zip/git) em `Projetos/MOODLE/<versão>/`.
2. Criar `APP-MOODLE/<versão>/` com as pastas: `Estrutura`, `Plugins`, `Classes`, `DB`, `Eventos`, `WebServices`, `Templates`, `Frontend`, `Seguranca`, `Admin`…
3. Documentar **só o que o código daquela build prova** (paths reais, classes reais).
4. Atualizar a tabela de versões neste README.

## Convenções

- Uma nota = um assunto. Links Obsidian `[[pasta/arquivo|rótulo]]`.
- Preferir exemplos do **core** (`mod/page`, `blocks/html`) ou plugins do projeto nomeados.
- Segurança dos plugins NTI: [[4.5.8/Seguranca/Anti-Padroes]].
- UI admin nova: azul `#1d4ed8` → `#0d6efd` ([[_meta/Layout-Admin-Padrao]]).
- Repo de plugin: `moodle-<tipo>_<nome>` + `.github/workflows/ci.yml` ([[CI/README]]).
- Código Moodle, clone `devdocs/`, `moodledata` **não** entram neste repositório (ver `.gitignore`).
- DevDocs: `./scripts/limpar-devdocs.py` (`--clone` / `--pull`) — só MD 4.5–5.2.
- JSDoc AMD: `./scripts/baixar-jsdoc.py` — **todas** as versões do [jsdoc.moodledev.io](https://jsdoc.moodledev.io/) → `jsdoc/` (módulos + fontes `*.js.html`).

## Estrutura do repositório

```text
APP-MOODLE/
├── README.md
├── .gitignore
├── .cursor/             ← skills + rules (fonte canônica)
├── .opencode/ .claude/ .agent/ .agents/ codex/  ← espelhos AI
├── AGENTS.md · CLAUDE.md
├── CI/                  ← moodle-plugin-ci + security workflows
├── _meta/               ← layout, nomenclatura, selos, sync-agent-skills.sh
├── 4.5.8/
├── 5.2/
├── relatorios/
└── .obsidian/
```
