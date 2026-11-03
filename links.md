# Links importantes — Moodle (dev)

## Docs oficiais

| Link | Pra quê |
|------|---------|
| https://moodledev.io/ | DevDocs (APIs, plugins, guides) — espelho local: `devdocs/` |
| https://jsdoc.moodledev.io/ | JSDoc AMD/JS nativo — espelho: `jsdoc/` · script `./scripts/baixar-jsdoc.py` |
| https://jsdoc.moodledev.io/4.05/ | JSDoc linha **4.5** (seu 4.5.8) |
| https://jsdoc.moodledev.io/5.01/ | JSDoc **5.1** (próximo do 5.2; ou use `main`) |
| https://jsdoc.moodledev.io/main/ | JSDoc tip da main |
| https://docs.moodle.org/ | Docs de administração / usuário |
| https://docs.moodle.org/dev/Main_Page | Wiki legacy (muito conteúdo antigo ainda útil) |

## Releases / código

| Link | Pra quê |
|------|---------|
| https://download.moodle.org/releases/latest/ | Downloads |
| https://github.com/moodle/moodle | Core GitHub |
| https://github.com/moodle/moodle/tree/MOODLE_405_STABLE | Branch **4.5** |
| https://github.com/moodle/moodle/tree/MOODLE_502_STABLE | Branch **5.2** |
| https://github.com/moodle/devdocs | Fonte do DevDocs |
| https://moodledev.io/general/releases | Notas de release |

## Plugins / Marketplace

| Link | Pra quê |
|------|---------|
| https://moodle.org/plugins/ | Plugins directory (subir plugin, selos) |
| https://moodle.org/plugins/browse.php?list=category | Por categoria |
| `_meta/Marketplace-Selos.md` | Privacy friendly · AUTO TEST · Early bird |
| `_meta/Nomenclatura-GitHub.md` | Repo `moodle-report_activities` |

## CI / qualidade

| Link | Pra quê |
|------|---------|
| https://github.com/moodlehq/moodle-plugin-ci | CI oficial de plugin |
| https://github.com/moodlehq/moodle-plugin-ci/blob/main/gha.dist.yml | Template GHA |
| `CI/README.md` | Seus templates (bancos, versões, security) |
| `CI/ci-security.yml` + `CI/scripts/security-scan.sh` | Scan anti-padrões |

## Segurança / coding

| Link | Pra quê |
|------|---------|
| https://moodledev.io/general/development/policies/security | Security policy |
| https://moodledev.io/general/development/policies/codingstyle | Coding style |
| https://moodledev.io/docs/apis/subsystems/privacy/ | Privacy API (selo Privacy friendly) |
| `4.5.8/Seguranca/Funcoes.md` | Catálogo local de APIs |
| `4.5.8/Seguranca/Anti-Padroes.md` | Casos NTI |

## Front / JS

| Link | Pra quê |
|------|---------|
| https://moodledev.io/docs/guides/javascript/ | JS no Moodle |
| https://moodledev.io/docs/guides/javascript/amd | AMD |
| https://developer.mozilla.org/en-US/docs/Web/JavaScript | MDN |
| `4.5.8/Frontend/AMD.md` · `5.2/Frontend/React.md` | Notas do vault |

## Guias / comunidade

| Link | Pra quê |
|------|---------|
| https://danielneis.github.io/moodleparadesenvolvedores/ | Moodle pra desenvolvedores (PT) |
| https://moodle.org/mod/forum/view.php?id=44 | Fórum General developer |
| https://tracker.moodle.org/ | Tracker (bugs / issues) |
| https://lang.moodle.org/ | Strings / AMOS |

## Este vault (scripts)

```bash
./scripts/baixar-jsdoc.py          # todas as versões JSDoc → jsdoc/
./scripts/limpar-devdocs.py --clone  # DevDocs enxuto → devdocs/
```

Versões do projeto: **4.5.8** · **5.2** — índices em `4.5.8/README.md` e `5.2/README.md`.
