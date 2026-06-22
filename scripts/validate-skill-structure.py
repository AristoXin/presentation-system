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

NEW_REFERENCES = {
    "R24": "references/24-user-asset-intake-and-adaptation.md",
    "R25": "references/25-design-synthesis-governance.md",
    "R26": "references/26-motion-opportunity-governance.md",
    "R27": "references/27-anti-template-governance.md",
    "R28": "references/28-html-experience-governance.md",
    "R29": "references/29-editorial-design-approval.md",
    "R30": "references/30-external-skill-invocation-governance.md",
}

NEW_TEMPLATES = [
    "templates/skill-availability-scan.md",
    "templates/skill-invocation-ledger.md",
    "templates/skill-absorption-matrix.md",
    "templates/manual-equivalent-record.md",
    "templates/source-material-intake.md",
    "templates/design-synthesis-contract.md",
    "templates/motion-opportunity-map.md",
    "templates/anti-template-review.md",
    "templates/html-experience-contract.md",
    "templates/editorial-design-board.md",
    "templates/pre-code-visual-freeze.md",
    "templates/last30days-visual-pulse.md",
]

NEW_SCRIPTS = [
    "scripts/validate-visual-production.py",
    "scripts/validate-skill-invocation.py",
]

SKILL_GATES = ["G6A", "G7A", "G7B", "G7C", "G7D", "G7E"]

AGENTS_SECTIONS = [
    "Pre-Code Visual Production Rule",
    "External Skill Invocation Rule",
    "Editorial Approval Rule",
]


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


def extract_index_ids(index_text: str) -> set[str]:
    return set(re.findall(r"^\s*-?\s*id:\s*(R\d+|RVIS)\s*$", index_text, re.MULTILINE))


def front_matter_present(text: str) -> bool:
    return text.startswith("---\n") and "\n---\n" in text[4:]


def check_multiline_yaml(path: Path, failures: list[str], warnings: list[str]) -> None:
    text = read(path)
    if not text:
        fail(f"{path.relative_to(ROOT)} exists", failures)
        return
    lines = text.splitlines()
    if len(lines) < 8:
        fail(f"{path.relative_to(ROOT)} is normal multi-line YAML", failures)
    else:
        passed(f"{path.relative_to(ROOT)} is multi-line ({len(lines)} lines)")
    very_long = [(idx, line) for idx, line in enumerate(lines, start=1) if len(line) > 800]
    long = [(idx, line) for idx, line in enumerate(lines, start=1) if 500 < len(line) <= 800]
    if very_long:
        fail(f"{path.relative_to(ROOT)} has extremely long lines: {very_long[0][0]}", failures)
    elif long:
        warn(f"{path.relative_to(ROOT)} has long lines above 500 chars", warnings)
    else:
        passed(f"{path.relative_to(ROOT)} has no excessive long lines")


def check_no_excessive_long_lines(warnings: list[str], failures: list[str]) -> None:
    offenders: list[str] = []
    hard: list[str] = []
    for folder in ["references", "templates", "scripts", "tests"]:
        for path in (ROOT / folder).rglob("*"):
            if not path.is_file() or path.suffix.lower() not in {".md", ".yaml", ".yml", ".py"}:
                continue
            for idx, line in enumerate(read(path).splitlines(), start=1):
                if len(line) > 900:
                    hard.append(f"{path.relative_to(ROOT)}:{idx}")
                elif len(line) > 600:
                    offenders.append(f"{path.relative_to(ROOT)}:{idx}")
    if hard:
        fail("Files contain extremely long lines: " + ", ".join(hard[:5]), failures)
    elif offenders:
        warn("Some files contain long lines: " + ", ".join(offenders[:5]), warnings)
    else:
        passed("Markdown/YAML/Python files avoid excessive long lines")


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

        missing_new_gates = [gate for gate in SKILL_GATES if gate not in skill_text]
        if missing_new_gates:
            for gate in missing_new_gates:
                fail(f"{gate} is defined in SKILL.md", failures)
        else:
            passed("G6A and G7A-G7E are present in SKILL.md")

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
        check_multiline_yaml(index_path, failures, warnings)
        paths = extract_index_paths(index_text)
        ids = extract_index_ids(index_text)
        if not paths:
            fail("references/index.yaml contains reference paths", failures)
        for rel in paths:
            target = ROOT / rel
            if not target.exists():
                fail(f"Indexed reference exists: {rel}", failures)
        if paths and not any((ROOT / rel).exists() is False for rel in paths):
            passed(f"All indexed references exist ({len(paths)} paths)")
        for ref_id, rel in NEW_REFERENCES.items():
            if ref_id not in ids:
                fail(f"references/index.yaml contains {ref_id}", failures)
            else:
                passed(f"references/index.yaml contains {ref_id}")
            if rel not in paths:
                fail(f"references/index.yaml routes {rel}", failures)
        for rel in NEW_REFERENCES.values():
            if (ROOT / rel).exists():
                passed(f"New reference exists: {rel}")
            else:
                fail(f"New reference exists: {rel}", failures)

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
        for section in AGENTS_SECTIONS:
            if section not in agents_text:
                fail(f"AGENTS.md contains {section}", failures)
            else:
                passed(f"AGENTS.md contains {section}")

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

    registry_path = ROOT / "skills" / "visual-skill-registry.yaml"
    if registry_path.exists():
        passed("skills/visual-skill-registry.yaml exists")
        registry_text = read(registry_path)
        for skill in ["design-dna", "guizang-ppt-skill", "taste-skill", "stylekit-skill", "last30days-search"]:
            if skill not in registry_text:
                fail(f"visual-skill-registry.yaml declares {skill}", failures)
        if "manual_equivalent_allowed" in registry_text:
            passed("visual-skill-registry.yaml records manual equivalent policy")
        else:
            fail("visual-skill-registry.yaml records manual equivalent policy", failures)
    else:
        fail("skills/visual-skill-registry.yaml exists", failures)

    for rel in NEW_TEMPLATES:
        if (ROOT / rel).exists():
            passed(f"New template exists: {rel}")
        else:
            fail(f"New template exists: {rel}", failures)

    for rel in NEW_SCRIPTS:
        if (ROOT / rel).exists():
            passed(f"New script exists: {rel}")
        else:
            fail(f"New script exists: {rel}", failures)

    scenarios_path = ROOT / "tests" / "scenarios.yaml"
    if scenarios_path.exists():
        check_multiline_yaml(scenarios_path, failures, warnings)
        scenarios_text = read(scenarios_path)
        scenario_count = len(re.findall(r"^\s*-\s+id:\s*S\d+", scenarios_text, re.MULTILINE))
        if scenario_count >= 29:
            passed(f"tests/scenarios.yaml exists with {scenario_count} scenarios")
        else:
            fail(f"tests/scenarios.yaml has at least 29 scenarios (found {scenario_count})", failures)
        for scenario_id in [f"S{i}" for i in range(17, 34)]:
            if f"id: {scenario_id}" not in scenarios_text:
                fail(f"tests/scenarios.yaml contains {scenario_id}", failures)
        if all(f"id: S{i}" in scenarios_text for i in range(17, 34)):
            passed("tests/scenarios.yaml contains S17-S33")
    else:
        fail("tests/scenarios.yaml exists", failures)

    reference_files = sorted((ROOT / "references").rglob("*.md"))
    missing_front_matter = [str(path.relative_to(ROOT)) for path in reference_files if not front_matter_present(read(path))]
    if missing_front_matter:
        warn("Some references lack front matter: " + ", ".join(missing_front_matter), warnings)
    else:
        passed("References include front matter")

    check_no_excessive_long_lines(warnings, failures)

    print()
    print(f"Summary: {len(failures)} FAIL, {len(warnings)} WARN")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
