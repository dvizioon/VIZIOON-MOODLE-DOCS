---
name: moodle-plugin-ci
description: >-
  Sets up GitHub Actions moodle-plugin-ci workflows for Moodle plugins: database
  matrix (Postgres/MariaDB/MySQL), Moodle version matrix, security scan, and
  quality lint. Use when the user asks for CI, ci.yml, testar bancos, versões
  Moodle no GitHub, moodle-plugin-ci, ou segurança automatizada do plugin.
---

# moodle-plugin-ci — família de workflows

Templates em `CI/` deste vault. Copiar para `.github/workflows/` no **repo do plugin**.

| Template | Foco |
|----------|------|
| `CI/ci.yml` | Suite completa |
| `CI/ci-databases.yml` | `pgsql` + `mariadb` + `mysqli` |
| `CI/ci-moodle-versions.yml` | `MOODLE_405`…`502` |
| `CI/ci-security.yml` | `scripts/security-scan.sh` + phpcs/validate |
| `CI/ci-quality.yml` | Lint rápido 1 job |

Script: `CI/scripts/security-scan.sh` → `scripts/security-scan.sh` no plugin.

## Bancos

- Oficial HQ: **pgsql**, **mariadb**
- MySQL: `DB=mysqli` + service `mysql:8`
- **Oracle**: deprecado — não configurar
- **SQL Server**: core Moodle sim; plugin-ci HQ ainda sem suporte estável

## Versões

`MOODLE_405_STABLE` · `500` · `501` · `502` — PHP compatível por linha.

## Security job highlights

Crítico (fail): `curl_init`, SSL off, `LIMIT` SQL, `print_error`, PHP em `dirroot`, secrets, PHP em `doc/`, zip no repo, external `execute` sem `validate_context` (heurística).

Não substitui review de capability/sesskey — skill `moodle-plugin-security` + `4.5.8/Seguranca/`.

## Docs

`CI/README.md` · `_meta/Nomenclatura-GitHub.md`
