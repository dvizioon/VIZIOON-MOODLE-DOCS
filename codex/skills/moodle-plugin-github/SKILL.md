---
name: moodle-plugin-github
description: >-
  Names and structures Moodle plugin GitHub repositories (moodle-report_activities
  style), version.php, and CI readiness for upload. Use when creating a GitHub
  repo for a plugin, naming MOODLE-REPORT_ACTIVITIES, frankenstyle, or preparing
  a plugin to publish.
---

# Plugin no GitHub

## Naming (padrão Moodle HQ / plugins directory)

| | Formato | Exemplo (`report_activities`) |
|--|---------|-------------------------------|
| Repo | `moodle-<tipo>_<nome>` | `moodle-report_activities` |
| `$plugin->component` | `<tipo>_<nome>` | `report_activities` |
| Path no site | `<plugindir>/<nome>/` | `report/activities/` |

Outros: `moodle-mod_oxymsteams`, `moodle-local_cataloggate`, `moodle-block_oxymylib`, `moodle-tool_oxytemppass`.

Evitar: `MOODLE-REPORT_ACTIVITIES` em caixa alta no remote (GitHub aceita, mas o padrão da comunidade é **minúsculo** `moodle-report_activities`). Título do README pode ser legível.

## Repo contents (raiz = plugin)

```text
moodle-report_activities/          # raiz do git = pasta do plugin
├── version.php
├── lib.php
├── classes/
├── db/
├── lang/
├── .github/workflows/ci.yml       # skill moodle-plugin-ci
├── README.md
└── LICENSE
```

**Não** colocar `mod/` ou `moodle/` wrapping acima do plugin no mesmo repo (exceto meta-repos).

## version.php must-haves

```php
$plugin->component = 'report_activities';
$plugin->version   = 2026101900;      // YYYYMMDDXX
$plugin->requires  = 2026042000;      // min core
$plugin->supported = [502, 502];      // opcional; matrix CI deve cobrir
$plugin->maturity  = MATURITY_STABLE;
$plugin->release   = '1.3.7';
```

## Before first push

1. Nome do repo = `moodle-<component com underscore>`
2. Adicionar `CI/ci.yml` → `.github/workflows/ci.yml` (skill `moodle-plugin-ci`)
3. Rodar checklist segurança (skill `moodle-plugin-security`)
4. Sem `doc/oldSys`, zips, secrets
5. Um plugin por repo; versões = tags/branches, não pastas `_v5`

## Docs

`_meta/Nomenclatura-GitHub.md` · `CI/README.md`
