# AGENTS — APP-MOODLE

Vault de documentação Moodle + skills para Cursor, Claude, OpenCode, Codex e Agent.

## Skills (mesmo conteúdo em todas as pastas)

| Pasta | Runtime |
|-------|---------|
| `.cursor/skills/` | Cursor (canônico + rules `.mdc`) |
| `.opencode/skills/` | OpenCode |
| `.claude/skills/` | Claude Code |
| `.agent/skills/` · `.agents/skills/` | Agent / OpenCode compat |
| `codex/skills/` | Codex |

Skills: `moodle-vault-docs` · `moodle-admin-layout` · `moodle-plugin-security` · `moodle-plugin-ci` · `moodle-plugin-github` · `moodle-marketplace-badges`

## Ao editar skills

1. Edite em **`.cursor/skills/`** (fonte).
2. Rode: `bash _meta/sync-agent-skills.sh`
3. Atualize `_meta/Cursor-Skills-Rules.md` se adicionar skill nova.

## Docs chave

- Selos Marketplace: `_meta/Marketplace-Selos.md`
- CI: `CI/README.md`
- Segurança: `4.5.8/Seguranca/`
