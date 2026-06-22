#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MANIFEST="$ROOT_DIR/skills.manifest.yaml"
VENDOR="$ROOT_DIR/vendor"
GLOBAL_SKILLS_DIR="${CODEX_HOME:-$HOME/.codex}/skills"

echo "Verifying manifest: $MANIFEST"
echo "Checking vendor directory: $VENDOR"
echo "Checking global skills directory: $GLOBAL_SKILLS_DIR"

if [ ! -f "$MANIFEST" ]; then
  echo "Missing skills.manifest.yaml" >&2
  exit 1
fi

if [ ! -d "$VENDOR" ]; then
  echo "Missing vendor directory" >&2
  exit 1
fi

PROJECT_ROOT="$(cd "$ROOT_DIR/.." && pwd)"

echo
echo "Checking online research governance references:"
test -f "$PROJECT_ROOT/references/22-html-pre-visual-director.md"
test -f "$PROJECT_ROOT/references/23-online-research-toolchain.md"
grep -R "23-online-research-toolchain" "$PROJECT_ROOT/SKILL.md" "$PROJECT_ROOT/references" >/dev/null
grep -R "外部参考搜索记录" "$PROJECT_ROOT/references/22-html-pre-visual-director.md" >/dev/null
grep -R "联网搜索与外部参考 QA" "$PROJECT_ROOT/references/07-qa-checklist.md" >/dev/null
grep -R "Tavily" "$PROJECT_ROOT/references/08-skill-governance.md" >/dev/null
grep -R "Context7" "$PROJECT_ROOT/references/08-skill-governance.md" >/dev/null
grep -R "Playwright" "$PROJECT_ROOT/references/08-skill-governance.md" >/dev/null
grep -R "Online Research Stack" "$PROJECT_ROOT/references/21-design-skill-stack-integration.md" >/dev/null
grep -R "缺失控件安装提请" "$PROJECT_ROOT/references/23-online-research-toolchain.md" >/dev/null
grep -R "online_toolchain" "$MANIFEST" >/dev/null

if grep -R "是否允许创建 subagent\|用户尚未提到subagent.*提请\|SEL-downgraded" "$PROJECT_ROOT/SKILL.md" "$PROJECT_ROOT/references/00-production-gate.md" "$PROJECT_ROOT/references/16-multi-agent-governance.md" "$PROJECT_ROOT/references/07-qa-checklist.md" >/dev/null; then
  echo "Found stale subagent downgrade/permission wording." >&2
  exit 1
fi

echo "Online research governance references: ok"

echo
echo "Skill availability summary:"

current_name=""
current_role=""
current_required=""
current_verify=""

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

flush_skill() {
  if [ -z "$current_name" ]; then
    return
  fi

  vendor_status="missing"
  if [ -d "$VENDOR/$current_name" ]; then
    vendor_status="present"
  fi

  global_status="missing"
  global_path=""
  if global_path="$(find_global_skill "$current_name")"; then
    global_status="present"
  fi

  verify_status="not-configured"
  case "$current_verify" in
    ""|"<verify-command>"|"\"<verify-command>\"")
      verify_status="not-configured"
      ;;
    *)
      if eval "$current_verify" >/dev/null 2>&1; then
        verify_status="passes"
      else
        verify_status="fails"
      fi
      ;;
  esac

  availability="unproven"
  if [ "$global_status" = "present" ] || [ "$vendor_status" = "present" ] || [ "$verify_status" = "passes" ]; then
    availability="available"
  fi

  if [ -n "$global_path" ]; then
    printf -- "- %s | role=%s | required=%s | global=%s | global_path=%s | vendor=%s | verify=%s | availability=%s\\n" \
      "$current_name" "$current_role" "$current_required" "$global_status" "$global_path" "$vendor_status" "$verify_status" "$availability"
  else
    printf -- "- %s | role=%s | required=%s | global=%s | vendor=%s | verify=%s | availability=%s\\n" \
      "$current_name" "$current_role" "$current_required" "$global_status" "$vendor_status" "$verify_status" "$availability"
  fi

  current_name=""
  current_role=""
  current_required=""
  current_verify=""
}

while IFS= read -r line; do
  case "$line" in
    "online_toolchain:"*)
      flush_skill
      break
      ;;
    "  - name:"*)
      flush_skill
      current_name="${line#*name: }"
      ;;
    "    role:"*)
      current_role="${line#*role: }"
      ;;
    "    required:"*)
      current_required="${line#*required: }"
      ;;
    "    verify:"*)
      current_verify="${line#*verify: }"
      current_verify="${current_verify%\"}"
      current_verify="${current_verify#\"}"
      current_verify="${current_verify%\\\"}"
      current_verify="${current_verify#\\\"}"
      ;;
  esac
done < "$MANIFEST"
flush_skill

echo
echo "Online toolchain summary:"
for tool_name in tavily-search brave-search firecrawl context7 playwright-mcp; do
  if grep -q "name: $tool_name" "$MANIFEST"; then
    printf -- "- %s | install=requires-user-consent | availability=not-verified-by-static-script\\n" "$tool_name"
  else
    echo "Missing online toolchain entry: $tool_name" >&2
    exit 1
  fi
done

echo
echo "Interpretation:"
echo "- global=present means a user-installed skill exists and can be invoked by reading its SKILL.md."
echo "- vendor=missing alone does not mean unavailable; treat a skill as missing only when global=missing, vendor=missing, and verify=not-configured."
echo "- online toolchain entries are not installed by this script; request user consent/API keys/connectors before enabling them."
echo "- Do not promise capabilities for unverified required skills; pause, request install/enablement when appropriate, or record a blocker."
echo "Verification completed."
