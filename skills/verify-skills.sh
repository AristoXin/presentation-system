#!/usr/bin/env bash
set -euo pipefail

SCRIPT_PATH="${BASH_SOURCE[0]}"
ROOT_DIR="${SCRIPT_PATH%/*}"
ROOT_DIR="$(cd "$ROOT_DIR" && pwd)"
PROJECT_ROOT="$(cd "$ROOT_DIR/.." && pwd)"
REGISTRY="$ROOT_DIR/visual-skill-registry.json"
RUNTIME_LOCK="$ROOT_DIR/runtime-lock.json"
CODEX_SKILLS_DIR="${CODEX_HOME:-$HOME/.codex}/skills"

echo "Verifying canonical skill registry: $REGISTRY"
echo "Writing runtime lock: $RUNTIME_LOCK"

PYTHON_BIN=""
for candidate in python python3 py; do
  if command -v "$candidate" >/dev/null 2>&1; then
    PYTHON_BIN="$candidate"
    break
  fi
done
if [ -z "$PYTHON_BIN" ]; then
  echo "No Python runtime found for runtime-lock generation." >&2
  exit 2
fi

"$PYTHON_BIN" - "$PROJECT_ROOT" "$REGISTRY" "$RUNTIME_LOCK" "$CODEX_SKILLS_DIR" <<'PY'
from __future__ import annotations

import hashlib
import json
import os
import platform
import socket
import sys
from datetime import datetime, timezone
from pathlib import Path

project_root = Path(sys.argv[1])
registry_path = Path(sys.argv[2])
runtime_lock_path = Path(sys.argv[3])
skills_dir = Path(sys.argv[4])

registry = json.loads(registry_path.read_text(encoding="utf-8"))

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        h.update(handle.read())
    return h.hexdigest()

entries = []
for skill in registry.get("skills", []):
    candidates = skill.get("installation", {}).get("candidate_names", [])
    resolved_path = None
    resolved_alias = None
    for name in candidates:
        candidate = skills_dir / name
        if (candidate / "SKILL.md").exists():
            resolved_path = candidate
            resolved_alias = name
            break
    if resolved_path is None and skill["id"] == "headroom":
        candidate = project_root / "skills" / "vendor" / "headroom"
        if (candidate / "SKILL.md").exists():
            resolved_path = candidate
            resolved_alias = "headroom"
    if resolved_path:
        skill_md = resolved_path / "SKILL.md"
        availability = "resolved"
        verify_result = "pass"
        digest = sha256(skill_md)
    else:
        availability = "unresolved"
        verify_result = "missing"
        digest = None
    entries.append({
        "canonical_skill_id": skill["id"],
        "resolved_alias": resolved_alias,
        "resolved_path": str(resolved_path) if resolved_path else None,
        "availability": availability,
        "skill_md_sha256": digest,
        "verify_result": verify_result
    })

payload = {
    "schema_version": 1,
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "machine": {
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
        "session": os.environ.get("CODEX_SESSION_ID", "unavailable")
    },
    "codex_home": str(Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))),
    "registry_path": str(registry_path),
    "skills": entries
}
runtime_lock_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
for entry in entries:
    print(f"- {entry['canonical_skill_id']} | availability={entry['availability']} | path={entry['resolved_path'] or 'none'}")
print("Runtime lock generated. Missing optional/local skills are capability blockers for tasks that require them, not structure-test failures.")
PY

echo "Verification completed."
