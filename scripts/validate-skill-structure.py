#!/usr/bin/env python3
"""Structural checks for the presentation-system Skill.

The validator intentionally uses only the Python standard library. It checks
the lightweight-router architecture, not the full semantics of every rule.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def result(kind: str, message: str) -> None:
    print(f"{kind}: {message}")


def fail(message: str, failures: list[str]) -> None:
    result("FAIL", message)
    failures.append(message)


def warn(message: str, warnings: list[str]) -> None:
    result("WARN", message)
    warnings.append(message)


def passed(message: str) -> None:
    result("PASS", message)


def extract_index_paths(index_text: str) -> list[str]:
    paths: list[str] = []
    for match in re.finditer(r"^\s*path:\s*([^\s#]+)\s*$", index_text, re.MULTILINE):
        paths.append(match.group(1).strip("'\""))
    return paths


def front_matter_present(text: str) -> bool:
    return text.startswith("---\n") and "\n---\n" in text[4:]


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []

    skill_path = ROOT / "SKILL.md"
    skill_text = read(skill_path)
    if not skill_text:
        fail("SKILL.md exists", failures)
    else:
        passed("SKILL.md exists")
        byte_len = len(skill_text.encode("utf-8"))
        line_count = skill_text.count("\n") + 1
        if byte_len > 12_000 or line_count > 180:
            warn(f"SKILL.md is above target size ({byte_len} bytes, {line_count} lines)", warnings)
        else:
            passed(f"SKILL.md size is within target ({byte_len} bytes, {line_count} lines)")

        missing_gates = []
        for gate in [f"G{i}" for i in range(1, 9)]:
            if gate not in skill_text:
                missing_gates.append(gate)
                fail(f"{gate} is defined in SKILL.md", failures)
        if not missing_gates:
            passed("G1-G8 are present in SKILL.md")

        high_pressure = len(re.findall(r"(硬门禁|最高优先级|强制门禁)", skill_text))
        must_count = len(re.findall(r"(必须|不得|强制|never|must)", skill_text, flags=re.IGNORECASE))
        if high_pressure > 6 or must_count > 55:
            warn(f"SKILL.md may still contain dense gate language (hard={high_pressure}, must={must_count})", warnings)
        else:
            passed("SKILL.md does not appear to contain large unnumbered hard-gate blocks")

    index_path = ROOT / "references" / "index.yaml"
    index_text = read(index_path)
    if not index_text:
        fail("references/index.yaml exists", failures)
    else:
        passed("references/index.yaml exists")
        paths = extract_index_paths(index_text)
        if not paths:
            fail("references/index.yaml contains reference paths", failures)
        for rel in paths:
            target = ROOT / rel
            if not target.exists():
                fail(f"Indexed reference exists: {rel}", failures)
        if paths and not any((ROOT / rel).exists() is False for rel in paths):
            passed(f"All indexed references exist ({len(paths)} paths)")

    agents_path = ROOT / "AGENTS.md"
    agents_text = read(agents_path)
    if not agents_text:
        fail("AGENTS.md exists", failures)
    else:
        passed("AGENTS.md exists")
        line_count = agents_text.count("\n") + 1
        if line_count > 120:
            warn(f"AGENTS.md may be too long for an implementation guide ({line_count} lines)", warnings)
        else:
            passed(f"AGENTS.md length is compact ({line_count} lines)")
        if "references/index.yaml" not in agents_text:
            fail("AGENTS.md points agents to references/index.yaml", failures)
        else:
            passed("AGENTS.md points agents to references/index.yaml")

    openai_path = ROOT / "agents" / "openai.yaml"
    if openai_path.exists():
        passed("agents/openai.yaml exists")
    else:
        fail("agents/openai.yaml exists", failures)

    manifest_path = ROOT / "skills" / "skills.manifest.yaml"
    manifest_text = read(manifest_path)
    if not manifest_text:
        fail("skills/skills.manifest.yaml exists", failures)
    else:
        passed("skills/skills.manifest.yaml exists")
        for keyword in ["presentation-system", "headroom", "browser", "visual QA", "online_toolchain", "subagent"]:
            if keyword not in manifest_text:
                fail(f"skills.manifest.yaml declares {keyword}", failures)
        if "required: conditional" in manifest_text and "required: recommended" in manifest_text:
            passed("skills.manifest.yaml distinguishes conditional and recommended capabilities")
        else:
            warn("skills.manifest.yaml may not distinguish conditional/recommended capabilities", warnings)

    template_path = ROOT / "templates" / "current-execution-card.md"
    if template_path.exists():
        passed("templates/current-execution-card.md exists")
    else:
        fail("templates/current-execution-card.md exists", failures)

    scenarios_path = ROOT / "tests" / "scenarios.yaml"
    if scenarios_path.exists():
        scenarios_text = read(scenarios_path)
        scenario_count = len(re.findall(r"^\s*-\s+id:\s*S\d+", scenarios_text, re.MULTILINE))
        if scenario_count >= 12:
            passed(f"tests/scenarios.yaml exists with {scenario_count} scenarios")
        else:
            fail(f"tests/scenarios.yaml has at least 12 scenarios (found {scenario_count})", failures)
    else:
        fail("tests/scenarios.yaml exists", failures)

    reference_files = sorted((ROOT / "references").rglob("*.md"))
    missing_front_matter = [str(path.relative_to(ROOT)) for path in reference_files if not front_matter_present(read(path))]
    if missing_front_matter:
        warn("Some references lack front matter: " + ", ".join(missing_front_matter), warnings)
    else:
        passed("References include front matter")

    print()
    print(f"Summary: {len(failures)} FAIL, {len(warnings)} WARN")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
