#!/usr/bin/env bash
# Espelha .cursor/skills e .cursor/rules para OpenCode, Claude, Agent, Codex.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC_S="$ROOT/.cursor/skills"
SRC_R="$ROOT/.cursor/rules"

for dest in "$ROOT/.opencode/skills" "$ROOT/.claude/skills" "$ROOT/.agent/skills" "$ROOT/.agents/skills" "$ROOT/codex/skills"; do
  mkdir -p "$dest"
  rsync -a --delete "$SRC_S/" "$dest/"
  echo "skills -> $dest"
done

for dest in "$ROOT/.opencode/rules" "$ROOT/.claude/rules" "$ROOT/.agent/rules" "$ROOT/codex/rules"; do
  mkdir -p "$dest"
  rsync -a --delete "$SRC_R/" "$dest/"
  echo "rules  -> $dest"
done

echo "OK — fonte canônica: .cursor/"
