#!/usr/bin/env python3
"""Validate external Skill invocation evidence for visual production.

Run from the skill root, or pass a project/artifact directory:

    python scripts/validate-skill-invocation.py [target_dir]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT

EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "node_modules",
    "templates",
    "references",
    "scripts",
    "tests",
    "skills",
    "agents",
}

FORMAL_EXTS = {".html", ".ppt", ".pptx", ".pdf"}
REQUIRED_EVIDENCE = [
    "skill-availability-scan.md",
    "skill-invocation-ledger.md",
    "skill-absorption-matrix.md",
]

SKILL_ALIASES = {
    "design-dna": [r"design-dna", r"PPT\s*DNA", r"PPT-Design-DNA"],
    "guizang-ppt-skill": [r"guizang", r"归藏"],
    "stylekit-skill": [r"StyleKit", r"stylekit"],
    "taste-skill": [r"\bTaste\b", r"taste-skill"],
    "frontend-slides": [r"frontend-slides"],
    "html-ppt": [r"html-ppt", r"HTML\s*PPT"],
    "huashu-design": [r"huashu", r"花叔"],
    "ppt-master": [r"ppt-master"],
    "humanize-ppt": [r"humanize-ppt"],
    "last30days-search": [r"last30days", r"Last30Days"],
}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(TARGET))
    except ValueError:
        return str(path)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def iter_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in EXCLUDED_DIRS for part in path.relative_to(root).parts[:-1]):
            continue
        files.append(path)
    return files


def emit(kind: str, code: str, message: str) -> None:
    print(f"{kind} {code}: {message}")


def find_named(files: list[Path], name: str) -> list[Path]:
    return [path for path in files if path.name == name]


def mentioned_skills(files: list[Path]) -> set[str]:
    text_parts = []
    for path in files:
        if path.suffix.lower() in {".md", ".html", ".js", ".css", ".json", ".yaml", ".yml"}:
            text_parts.append(read(path))
    joined = "\n".join(text_parts)
    found: set[str] = set()
    for skill, patterns in SKILL_ALIASES.items():
        if any(re.search(pattern, joined, re.I) for pattern in patterns):
            found.add(skill)
    return found


def ledger_has_skill(ledger: str, skill: str) -> bool:
    aliases = SKILL_ALIASES[skill] + [re.escape(skill)]
    return any(re.search(pattern, ledger, re.I) for pattern in aliases)


def called_entries_missing_evidence(ledger: str) -> list[str]:
    missing: list[str] = []
    for line in ledger.splitlines():
        if not re.search(r"\bcalled\b", line, re.I):
            continue
        if not re.search(r"(output|evidence|path|/|\.)", line, re.I):
            missing.append(line.strip()[:120])
    return missing


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []
    files = iter_files(TARGET)
    artifacts = [path for path in files if path.suffix.lower() in FORMAL_EXTS]

    if not artifacts:
        emit("PASS", "NO_FORMAL_ARTIFACTS", f"No HTML/PPT/PDF artifacts found under {TARGET}.")
        print("Summary: 0 FAIL, 0 WARN")
        return 0

    emit("PASS", "FORMAL_ARTIFACTS_FOUND", f"Found {len(artifacts)} formal artifact(s).")

    evidence: dict[str, list[Path]] = {}
    for name in REQUIRED_EVIDENCE:
        matches = find_named(files, name)
        evidence[name] = matches
        if not matches:
            failures.append("SKILL_CAPABILITY_BLOCKER")
            emit("FAIL", "SKILL_CAPABILITY_BLOCKER", f"Formal artifacts exist but {name} is missing.")
        else:
            emit("PASS", "EVIDENCE_FOUND", f"{name} -> {rel(matches[0])}")

    if not evidence.get("skill-invocation-ledger.md"):
        print()
        print(f"Summary: {len(failures)} FAIL, {len(warnings)} WARN")
        return 1

    ledger = "\n".join(read(path) for path in evidence["skill-invocation-ledger.md"])
    absorption = "\n".join(read(path) for path in evidence.get("skill-absorption-matrix.md", []))
    mentioned = mentioned_skills(files)

    for skill in sorted(mentioned):
        if not ledger_has_skill(ledger, skill):
            failures.append("SKILL_CAPABILITY_BLOCKER")
            emit("FAIL", "SKILL_CAPABILITY_BLOCKER", f"{skill} is mentioned but has no ledger entry.")
        elif skill not in absorption:
            failures.append("SKILL_ABSORPTION_MISSING")
            emit("FAIL", "SKILL_ABSORPTION_MISSING", f"{skill} is in ledger but not absorption matrix.")

    for line in called_entries_missing_evidence(ledger):
        failures.append("SKILL_EVIDENCE_MISSING")
        emit("FAIL", "SKILL_EVIDENCE_MISSING", f"called ledger row lacks output/evidence: {line}")

    if re.search(r"\bmanual_equivalent\b", ledger, re.I):
        manual = find_named(files, "manual-equivalent-record.md")
        if not manual:
            failures.append("MANUAL_EQUIVALENT_RECORD_MISSING")
            emit("FAIL", "MANUAL_EQUIVALENT_RECORD_MISSING", "manual_equivalent appears without manual-equivalent-record.md.")
        else:
            warnings.append("MANUAL_EQUIVALENT_USED")
            emit("WARN", "MANUAL_EQUIVALENT_USED", f"Manual equivalent record exists at {rel(manual[0])}.")

    if re.search(r"\bblocked\b", ledger, re.I):
        failures.append("SKILL_CAPABILITY_BLOCKER")
        emit("FAIL", "SKILL_CAPABILITY_BLOCKER", "Ledger contains blocked Skill state while formal artifacts exist.")

    if re.search(r"(absorbed|已吸收|Skill\s*栈已集成)", "\n".join(read(path) for path in files), re.I):
        for skill in sorted(mentioned):
            if skill not in absorption:
                failures.append("SKILL_ABSORPTION_MISSING")
                emit("FAIL", "SKILL_ABSORPTION_MISSING", f"Absorption is claimed but {skill} is missing from matrix.")

    if "last30days" in ledger.lower() and not re.search(r"source|url|query|来源|链接", ledger + "\n" + absorption, re.I):
        failures.append("LAST30DAYS_SEARCH_BLOCKER")
        emit("FAIL", "LAST30DAYS_SEARCH_BLOCKER", "last30days is claimed without query/source evidence.")

    print()
    print(f"Summary: {len(failures)} FAIL, {len(warnings)} WARN")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
