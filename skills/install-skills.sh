#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MANIFEST="$ROOT_DIR/skills.manifest.yaml"
VENDOR="$ROOT_DIR/vendor"

echo "Reading manifest: $MANIFEST"
echo "Vendor directory: $VENDOR"
echo "Installer contract: this script must not auto-install online tools, MCP servers, connectors, or dependencies."
echo "Tavily, Brave, Firecrawl, Context7, and Playwright MCP require an explicit user consent request before any install or enablement."

if [ ! -f "$MANIFEST" ]; then
  echo "Missing skills.manifest.yaml" >&2
  exit 1
fi

mkdir -p "$VENDOR"

if grep -q "<install-command>" "$MANIFEST"; then
  echo "Manifest still contains <install-command> placeholders."
  echo "No real install was attempted. Fill install commands or place local copies under vendor/."
  exit 0
fi

if grep -q "requires-user-consent" "$MANIFEST"; then
  echo "Manifest contains tools that require explicit user consent/API key or connector setup."
  echo "Do not install them automatically. Create a missing-tool install request and stop if the user refuses."
fi

echo "Manifest has no placeholder install commands, but this scaffold does not execute arbitrary installs."
echo "Review each install command manually or replace this script with a project-approved installer."
