---
name: moodle-vault-docs
description: >-
  Writes and maintains APP-MOODLE Obsidian documentation from Moodle source
  checkouts (4.5.8, 5.2, …). Use when documenting Moodle APIs, plugins, forms,
  settings, security, CI, or editing APP-MOODLE markdown.
---

# APP-MOODLE vault docs

## Paths (this repo)

| What | Where |
|------|--------|
| Index | `README.md` |
| Versions | `4.5.8/`, `5.2/`, … |
| Meta | `_meta/` |
| CI guide + template | `CI/` |
| Skills / rules | `.cursor/` (canônico) + espelhos `.opencode/` `.claude/` `.agent/` `.agents/` `codex/` |
| Selos Marketplace | `_meta/Marketplace-Selos.md` · skill `moodle-marketplace-badges` |

## Workflow

1. Ler o arquivo real no checkout (`Projetos/MOODLE/<versão>/…`).
2. Escrever nota em `<versão>/<Assunto>/`.
3. Linkar no README da versão e no README raiz se for tópico/versão nova.
4. PT-BR; APIs em inglês.

## Related skills

- `moodle-plugin-ci` — GitHub Actions
- `moodle-plugin-security` — endurecimento
- `moodle-admin-layout` — UI admin azul
- `moodle-plugin-github` — nome do repo
- `moodle-marketplace-badges` — Privacy friendly / AUTO TEST / Early bird
