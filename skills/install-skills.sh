#!/usr/bin/env bash
set -euo pipefail

SCRIPT_PATH="${BASH_SOURCE[0]}"
ROOT_DIR="${SCRIPT_PATH%/*}"
ROOT_DIR="$(cd "$ROOT_DIR" && pwd)"
REGISTRY="$ROOT_DIR/visual-skill-registry.json"
GLOBAL_SKILLS_DIR="${CODEX_HOME:-$HOME/.codex}/skills"
INSTALL_MISSING=0

for arg in "$@"; do
  case "$arg" in
    --install-missing) INSTALL_MISSING=1 ;;
    -h|--help)
      cat <<'EOF'
Usage:
  bash skills/install-skills.sh
  bash skills/install-skills.sh --install-missing

Audits public companion skills known to the canonical registry. Only public
GitHub skills with an explicit public_repository may be installed. Local,
private, account-bound, connector, MCP, or API-key capabilities are never
auto-installed by this script.
EOF
      exit 0
      ;;
    *) echo "Unknown argument: $arg" >&2; exit 2 ;;
  esac
done

PYTHON_BIN=""
for candidate in python python3 py; do
  if command -v "$candidate" >/dev/null 2>&1; then
    PYTHON_BIN="$candidate"
    break
  fi
done
if [ -z "$PYTHON_BIN" ]; then
  echo "No Python runtime found for skill install audit." >&2
  exit 2
fi

"$PYTHON_BIN" - "$REGISTRY" "$GLOBAL_SKILLS_DIR" "$INSTALL_MISSING" <<'PY'
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

registry_path = Path(sys.argv[1])
global_dir = Path(sys.argv[2])
install_missing = sys.argv[3] == "1"
registry = json.loads(registry_path.read_text(encoding="utf-8"))
global_dir.mkdir(parents=True, exist_ok=True)

def installed(candidate_names: list[str]) -> Path | None:
    for name in candidate_names:
        path = global_dir / name
        if (path / "SKILL.md").exists():
            return path
    return None

missing_public = []
missing_local = []
for skill in registry.get("skills", []):
    installation = skill.get("installation", {})
    candidates = installation.get("candidate_names", [])
    path = installed(candidates)
    if path:
        print(f"OK   {skill['id']:<22} {path}")
        continue
    if installation.get("type") == "public-github" and installation.get("public_repository"):
        print(f"MISS {skill['id']:<22} public installer available")
        missing_public.append(skill)
    else:
        print(f"MISS {skill['id']:<22} user/local setup required")
        missing_local.append(skill)

if install_missing:
    for skill in missing_public:
        repo = skill["installation"]["public_repository"]
        dest = global_dir / skill["installation"]["candidate_names"][0]
        if dest.exists():
            continue
        if shutil.which("git") is None:
            raise SystemExit(f"git is required to install {skill['id']} from {repo}")
        with tempfile.TemporaryDirectory() as tmp:
            checkout = Path(tmp) / "repo"
            subprocess.check_call(["git", "clone", "--depth", "1", repo, str(checkout)])
            source = checkout / "skills" / "last30days"
            if not (source / "SKILL.md").exists():
                raise SystemExit(f"{repo} does not contain expected skills/last30days/SKILL.md")
            shutil.copytree(source, dest)
            print(f"INSTALLED {skill['id']} -> {dest}")

if missing_public and not install_missing:
    print("Public installable missing:", ", ".join(skill["id"] for skill in missing_public))
    print("Run with --install-missing after user consent.")
if missing_local:
    print("Local/account-bound missing:", ", ".join(skill["id"] for skill in missing_local))
    print("Record these as manual_equivalent, not_applicable, or blocked before claiming capability.")
PY
