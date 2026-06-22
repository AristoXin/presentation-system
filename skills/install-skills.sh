#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MANIFEST="$ROOT_DIR/skills.manifest.yaml"
VENDOR="$ROOT_DIR/vendor"
GLOBAL_SKILLS_DIR="${CODEX_HOME:-$HOME/.codex}/skills"

INSTALL_MISSING=0
for arg in "$@"; do
  case "$arg" in
    --install-missing)
      INSTALL_MISSING=1
      ;;
    -h|--help)
      cat <<'EOF'
Usage:
  bash skills/install-skills.sh
  bash skills/install-skills.sh --install-missing

Default mode audits required companion skills and prints installation help.
--install-missing installs public GitHub-backed skills known to this repo.

Private/local user skills still require user-owned installation. The script
prints exact missing names so Codex can ask the user before continuing.
EOF
      exit 0
      ;;
    *)
      echo "Unknown argument: $arg" >&2
      exit 2
      ;;
  esac
done

echo "Reading manifest: $MANIFEST"
echo "Vendor directory: $VENDOR"
echo "Global skills directory: $GLOBAL_SKILLS_DIR"
echo "Installer contract: online tools, MCP servers, connectors, API keys, and account-bound skills require explicit user consent."

if [ ! -f "$MANIFEST" ]; then
  echo "Missing skills.manifest.yaml" >&2
  exit 1
fi

mkdir -p "$VENDOR" "$GLOBAL_SKILLS_DIR"

global_skill_candidates() {
  case "$1" in
    html-ppt-skill-main)
      printf '%s\n' "html-ppt-skill"
      ;;
    humanize-ppt-main)
      printf '%s\n' "humanize-ppt"
      ;;
    PPT-Design-DNA-main)
      printf '%s\n' "design-dna"
      ;;
    stylekit-skill)
      printf '%s\n' "stylekit-skill"
      printf '%s\n' "stylekit-style-prompts"
      ;;
    huashu-ppt)
      printf '%s\n' "huashu-slides"
      ;;
    last30days-skill)
      printf '%s\n' "last30days-skill"
      printf '%s\n' "last30days"
      ;;
  esac
  printf '%s\n' "$1"
}

find_global_skill() {
  local skill_name="$1"
  local candidate
  while IFS= read -r candidate; do
    if [ -f "$GLOBAL_SKILLS_DIR/$candidate/SKILL.md" ]; then
      printf '%s' "$GLOBAL_SKILLS_DIR/$candidate"
      return 0
    fi
  done < <(global_skill_candidates "$skill_name")
  return 1
}

install_last30days_skill() {
  local dest="$GLOBAL_SKILLS_DIR/last30days-skill"
  if [ -f "$dest/SKILL.md" ]; then
    echo "last30days-skill already installed: $dest"
    return 0
  fi

  echo "Installing last30days-skill from github.com/mvanhorn/last30days-skill..."

  local installer="$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py"
  if [ -f "$installer" ]; then
    python3 "$installer" \
      --repo mvanhorn/last30days-skill \
      --path skills/last30days \
      --name last30days-skill
    return 0
  fi

  if ! command -v git >/dev/null 2>&1; then
    echo "Cannot install last30days-skill: git is unavailable and Codex skill-installer is missing." >&2
    return 1
  fi

  local tmp
  tmp="$(mktemp -d)"
  trap 'rm -rf "$tmp"' EXIT
  git clone --depth 1 https://github.com/mvanhorn/last30days-skill.git "$tmp/last30days-skill" >/dev/null
  if [ ! -f "$tmp/last30days-skill/skills/last30days/SKILL.md" ]; then
    echo "Cannot install last30days-skill: skills/last30days/SKILL.md was not found." >&2
    return 1
  fi
  mkdir -p "$dest"
  cp -R "$tmp/last30days-skill/skills/last30days/." "$dest/"
}

public_install_supported() {
  case "$1" in
    last30days-skill)
      return 0
      ;;
    *)
      return 1
      ;;
  esac
}

install_public_skill() {
  case "$1" in
    last30days-skill)
      install_last30days_skill
      ;;
    *)
      echo "No public installer is registered for $1." >&2
      return 1
      ;;
  esac
}

missing_local=()
missing_public=()

for skill_name in \
  ppt-master \
  frontend-slides \
  taste-skill \
  stylekit-skill \
  html-ppt-skill-main \
  PPT-Design-DNA-main \
  humanize-ppt-main \
  huashu-ppt \
  guizang-ppt-skill \
  last30days-skill
do
  if found_path="$(find_global_skill "$skill_name")"; then
    printf -- "OK   %-24s %s\n" "$skill_name" "$found_path"
  elif public_install_supported "$skill_name"; then
    printf -- "MISS %-24s public GitHub installer available\n" "$skill_name"
    missing_public+=("$skill_name")
  else
    printf -- "MISS %-24s user/local skill installation required\n" "$skill_name"
    missing_local+=("$skill_name")
  fi
done

if [ "${#missing_public[@]}" -gt 0 ] && [ "$INSTALL_MISSING" -eq 1 ]; then
  echo
  echo "Installing public GitHub-backed missing skills:"
  for skill_name in "${missing_public[@]}"; do
    install_public_skill "$skill_name"
  done
fi

echo
if [ "${#missing_public[@]}" -gt 0 ] && [ "$INSTALL_MISSING" -eq 0 ]; then
  echo "Public installable skills are missing: ${missing_public[*]}"
  echo "Run: bash skills/install-skills.sh --install-missing"
fi

if [ "${#missing_local[@]}" -gt 0 ]; then
  echo "User/local skills still missing: ${missing_local[*]}"
  echo "Codex must help the user install or enable these before claiming the related capability."
  echo "Until then, resolve each as manual_equivalent, not_applicable, or blocked in the Skill Invocation Ledger."
fi

echo "Tavily, Brave, Firecrawl, Context7, and Playwright MCP are not auto-installed here."
echo "For those, Codex must request explicit user consent/API keys/connectors before setup."

if [ "$INSTALL_MISSING" -eq 1 ]; then
  echo "Install pass completed. Restart Codex to pick up newly installed skills."
fi
