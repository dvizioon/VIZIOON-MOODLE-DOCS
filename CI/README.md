# CI — templates `moodle-plugin-ci` + segurança

Vários workflows pra copiar pro repo do plugin (`.github/workflows/`). Não precisa baixar Moodle local: o GitHub Actions clona a branch, sobe o banco e roda as checks.

Ferramenta HQ: [moodlehq/moodle-plugin-ci](https://github.com/moodlehq/moodle-plugin-ci).

---

## Qual arquivo usar

| Arquivo | Pra quê | Quando |
|---------|---------|--------|
| [[CI/ci.yml\|ci.yml]] | Suite completa (lint → behat) multi versão/DB | Plugin “oficial” / release |
| [[CI/ci-databases.yml\|ci-databases.yml]] | **Bancos**: Postgres, MariaDB, MySQL (`mysqli`) | SQL/XMLDB, portabilidade |
| [[CI/ci-moodle-versions.yml\|ci-moodle-versions.yml]] | **Versões Moodle** 4.5 → 5.2 | Compatibilidade de API |
| [[CI/ci-security.yml\|ci-security.yml]] | **Segurança**: scan estático + phpcs/validate/mustache | Todo plugin NTI / antes de produção |
| [[CI/ci-quality.yml\|ci-quality.yml]] | Lint rápido (1 job) | PR pequeno / feedback rápido |
| [[CI/scripts/security-scan.sh\|scripts/security-scan.sh]] | Grep de anti-padrões (curl_init, LIMIT, SSL off…) | Usado pelo `ci-security` |

Recomendado no plugin maduro:

```text
.github/workflows/
  ci-quality.yml
  ci-moodle-versions.yml
  ci-databases.yml
  ci-security.yml
scripts/
  security-scan.sh
```

(`ci.yml` full é opcional se já tiver os quatro acima.)

---

## Bancos — o que o Moodle / plugin-ci aguenta

| DB env (`DB=`) | Service GHA | Status |
|----------------|-------------|--------|
| `pgsql` | `postgres:17` | **Suporte oficial** HQ |
| `mariadb` | `mariadb:11` | **Suporte oficial** HQ |
| `mysqli` | `mysql:8.0` | Driver MySQL do Moodle; use o template databases |
| `sqlsrv` | SQL Server | Moodle core ainda tem; **plugin-ci HQ ainda sem** suporte estável (PR aberto) |
| Oracle | — | **Deprecado** no Moodle; HQ fechou suporte no plugin-ci — **não use** |

Se o plugin escreve `LIMIT n` no SQL, o job `pgsql` pode passar e `mysqli`/MariaDB mascarar — a matriz de bancos pega isso (e o security-scan também flagra `LIMIT`).

---

## Versões Moodle (branches)

| Branch | Versão |
|--------|--------|
| `MOODLE_405_STABLE` | 4.5.x |
| `MOODLE_500_STABLE` | 5.0.x |
| `MOODLE_501_STABLE` | 5.1.x |
| `MOODLE_502_STABLE` | 5.2.x |

Ajuste PHP por linha (`8.1`…`8.4`) conforme a tabela oficial PHP × Moodle.  
`$plugin->requires` / `$plugin->supported` no `version.php` devem bater com a matrix.

---

## Segurança — o que o `ci-security` faz

### Job `static-scan` (sem instalar Moodle)

Script [[CI/scripts/security-scan.sh]]:

| Severidade | Exemplos |
|------------|----------|
| Crítico (falha o job) | `curl_init`, SSL verify off, `LIMIT`/`OFFSET` no SQL, `print_error`, gravar `.php` em `dirroot`, secret hardcoded |
| Aviso | `catch (Exception`, `ajax => true`, `PARAM_RAW`, `set_config` volátil, falta privacy |
| Extra no workflow | PHP em `doc/`, `.zip` no repo, privacy se tem `db/install.xml` |

Alinhado a [[4.5.8/Seguranca/Anti-Padroes]] e [[4.5.8/Seguranca/Checklist]].

### Job `moodle-checks`

`phplint` · `phpcs` · `phpdoc` · `validate` · `savepoints` · `mustache` · `phpmd` (warn)

Isso **não substitui** review humano de `validate_context` / `require_capability` — use a skill `moodle-plugin-security` + checklist. O CI pega o que é automatizável.

---

## Como plugar no plugin

1. Repo: `moodle-<tipo>_<nome>` ([[_meta/Nomenclatura-GitHub]]).
2. Copie os YAML desejados → `.github/workflows/`.
3. Para security: copie `CI/scripts/security-scan.sh` → `scripts/security-scan.sh` e `chmod +x`.
4. Edite `moodle-branch` / `php` / remova PHPUnit-Behat se não existirem testes.
5. Push → Actions.

Dependência de outro plugin:

```bash
moodle-plugin-ci install --plugin ./plugin --db-host=127.0.0.1 \
  --extra-plugins ./extra/outro
```

---

## Skills / docs

- Skill Cursor: `moodle-plugin-ci`, `moodle-plugin-security`
- Segurança manual: [[4.5.8/Seguranca/Funcoes]]
- Exemplo real: `report_activities` → `.github/workflows/ci.yml` no core 5.2
