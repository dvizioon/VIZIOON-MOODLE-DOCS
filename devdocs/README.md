# Moodle DevDocs (extraído / enxuto)

Cópia **só de Markdown** do [moodle/devdocs](https://github.com/moodle/devdocs) para consulta offline neste vault. Sem Docusaurus, yarn, CI nem site.

Fonte online: https://moodledev.io/

## O que ficou

| Pasta | Conteúdo |
|-------|----------|
| `docs/` | Docs “current” (APIs, guides, plugins, testing…) |
| `versioned_docs/version-4.5/` | Docs da linha **4.5** (ex.: 4.5.8) |
| `versioned_docs/version-5.1/` | Docs **5.1** |
| `versioned_docs/version-5.2/` | Docs **5.2** (atual do projeto) |
| `general/development/` | Processo, policies, tools |
| `general/documentation/` | Como a doc oficial funciona |

## O que foi removido

- Site Docusaurus (`src`, `static`, `package.json`, yarn…)
- `version-5.3` (acima do atual usado aqui)
- Releases/app/community/workplace (pesado, pouco uso no dia a dia de plugin)
- `.github`, scripts de build, dados marketplace

## Versões do vault APP-MOODLE

Alinha com [[../4.5.8/README|4.5.8]] e [[../5.2/README|5.2]].

Este diretório continua no `.gitignore` do APP-MOODLE (não versionar o clone no Git do vault).
