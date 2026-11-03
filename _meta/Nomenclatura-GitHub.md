# Nomenclatura GitHub — plugins Moodle

## Regra

```text
moodle-<tipo>_<nome>
```

Tudo **minúsculo**. O `<tipo>_<nome>` é o frankenstyle (`$plugin->component`).

| Tipo plugin | Pasta no Moodle | Repo GitHub |
|-------------|-----------------|-------------|
| `report` | `report/activities/` | `moodle-report_activities` |
| `mod` | `mod/oxymsteams/` | `moodle-mod_oxymsteams` |
| `local` | `local/cataloggate/` | `moodle-local_cataloggate` |
| `block` | `blocks/oxymylib/` | `moodle-block_oxymylib` |
| `tool` | `admin/tool/oxytemppass/` | `moodle-tool_oxytemppass` |
| `theme` | `theme/ceuma/` | `moodle-theme_ceuma` |
| `filter` | `filter/oxymsteams/` | `moodle-filter_oxymsteams` |
| `format` | `course/format/trail/` | `moodle-format_trail` |

Caixa alta tipo `MOODLE-REPORT_ACTIVITIES` pode ser título de README; o **slug do repo** segue o padrão minúsculo da comunidade.

## Conteúdo do repo

A raiz do Git **é** a pasta do plugin (tem `version.php` na raiz).  
CI: `.github/workflows/ci.yml` ← copie de [[CI/ci.yml]].

## Um plugin = um repo

Versões = **tags** / branches (`MOODLE_405_STABLE` no core; no plugin use `v1.2.0`).  
Não versionar pastas irmãs `_v1`…`_v5` no mesmo repositório.

## Skills / rules

- Skill: `moodle-plugin-github`
- Skill CI: `moodle-plugin-ci`
- Rule: `.cursor/rules/moodle-plugin-github.mdc`
