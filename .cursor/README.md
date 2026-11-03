# Cursor config — APP-MOODLE

**Source of truth** deste vault. No monorepo `Projetos/MOODLE`, a pasta `.cursor/` é espelho para descoberta das skills.

**Canônico** deste vault. Espelhar com `bash _meta/sync-agent-skills.sh` → `.opencode` `.claude` `.agent` `.agents` `codex`.

| Skills | Rules |
|--------|-------|
| `moodle-vault-docs` | `moodle-project` (always) |
| `moodle-admin-layout` | `moodle-vault-docs` |
| `moodle-plugin-security` | `moodle-plugin-dev` |
| `moodle-plugin-ci` | `moodle-plugin-security` |
| `moodle-plugin-github` | `moodle-plugin-ci` |
| `moodle-marketplace-badges` | `moodle-plugin-github` |
| | `moodle-admin-layout` |
| | `moodle-marketplace-badges` |

Ver `_meta/Cursor-Skills-Rules.md`, `_meta/Marketplace-Selos.md`, `CI/README.md`, `AGENTS.md`.
