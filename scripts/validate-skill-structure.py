#!/usr/bin/env python3
"""Structural checks for the presentation-system Skill."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
GATES = ["G1", "G2", "G3", "G4", "G5", "G6", "G6A", "G7", "G7A", "G7B", "G7C", "G7D", "G7E", "G8"]
FIXTURES = [
    "blank-evidence-html",
    "static-next-prev-html",
    "valid-interactive-html",
    "blocked-skill-with-artifact",
    "manual-equivalent-real-call-required",
    "pptx-without-html-contract",
    "intentionally-static-valid",
    "motion-required-without-state",
    "duplicate-output-owner",
    "runtime-lock-missing",
]


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def emit(kind: str, message: str, bucket: list[str] | None = None) -> None:
    print(f"{kind}: {message}")
    if kind == "FAIL" and bucket is not None:
        bucket.append(message)


def check_file_exists(rel: str, failures: list[str]) -> None:
    path = ROOT / rel
    emit("PASS" if path.exists() else "FAIL", f"{rel} exists", failures if not path.exists() else None)


def check_index(failures: list[str]) -> None:
    index = load_json(ROOT / "references" / "index.yaml")
    refs = index.get("references", [])
    ref_ids = {ref["id"] for ref in refs}
    for ref in refs:
        if not (ROOT / ref["path"]).exists():
            emit("FAIL", f"Indexed reference exists: {ref['path']}", failures)
    emit("PASS", f"All indexed references exist ({len(refs)})")
    for ref_id in ["R24", "R25", "R26", "R27", "R28", "R29", "R30"]:
        emit("PASS" if ref_id in ref_ids else "FAIL", f"references/index.yaml contains {ref_id}", failures if ref_id not in ref_ids else None)
    owners: dict[str, str] = {}
    for output, spec in index.get("outputs", {}).items():
        owner = spec.get("owner")
        if not owner:
            emit("FAIL", f"{output} has an owner", failures)
        elif output in owners:
            emit("FAIL", f"{output} has duplicate owners", failures)
        else:
            owners[output] = owner
    emit("PASS", f"Required output owners are unique ({len(owners)})")
    max_initial = index.get("load_policy", {}).get("max_initial_references")
    emit("PASS" if max_initial == 8 else "FAIL", "startup max_initial_references is 8", failures if max_initial != 8 else None)
    for ref in refs:
        if ref["id"] in {"R24", "R25", "R26", "R27", "R28", "R29", "R30"} and "production" in ref.get("triggers", []):
            emit("FAIL", f"{ref['id']} still uses broad production trigger", failures)
    emit("PASS", "Specialized R24-R30 references avoid broad production trigger")
    for duplicate in ["R31", "R32"]:
        emit("PASS" if duplicate not in ref_ids else "FAIL", f"{duplicate} was not added", failures if duplicate in ref_ids else None)


def check_execution_card(failures: list[str]) -> None:
    text = read(ROOT / "templates" / "current-execution-card.md")
    for gate in GATES:
        if gate not in text:
            emit("FAIL", f"Current Execution Card contains {gate}", failures)
    schema = load_json(ROOT / "templates" / "current-execution-card.schema.json")
    missing = [gate for gate in GATES if gate not in schema.get("gates", {})]
    emit("PASS" if not missing else "FAIL", "Current Execution Card schema contains all gates", failures if missing else None)


def check_registry_consistency(failures: list[str]) -> None:
    registry = load_json(ROOT / "skills" / "visual-skill-registry.json")
    manifest = load_json(ROOT / "skills" / "skills.manifest.yaml")
    registry_ids = {skill["id"] for skill in registry.get("skills", [])}
    manifest_ids = {skill["id"] for skill in manifest.get("skills", []) if skill.get("id") not in {"presentation-system", "headroom"}}
    missing = registry_ids - manifest_ids
    emit("PASS" if not missing else "FAIL", f"manifest covers registry IDs (missing={sorted(missing)})", failures if missing else None)
    for script in ["skills/verify-skills.sh", "skills/install-skills.sh"]:
        text = read(ROOT / script)
        emit("PASS" if "visual-skill-registry.json" in text else "FAIL", f"{script} reads canonical registry", failures if "visual-skill-registry.json" not in text else None)
    example = load_json(ROOT / "skills" / "skills.lock.example.json")
    bad = "local-installed" in json.dumps(example)
    emit("PASS" if not bad else "FAIL", "skills.lock.example.json does not claim local-installed", failures if bad else None)
    gitignore = read(ROOT / ".gitignore")
    emit("PASS" if "skills/runtime-lock.json" in gitignore else "FAIL", "skills/runtime-lock.json is gitignored", failures if "skills/runtime-lock.json" not in gitignore else None)


def check_validators(failures: list[str]) -> None:
    for rel in [
        "scripts/evidence_lib.py",
        "scripts/resolve-reference-route.py",
        "scripts/validate-skill-invocation.py",
        "scripts/validate-visual-production.py",
        "scripts/run-scenario-tests.py",
    ]:
        check_file_exists(rel, failures)
    invocation = read(ROOT / "scripts" / "validate-skill-invocation.py")
    forbidden = ["mentioned_skills", "skill in text", "ledger_has_skill"]
    found = [token for token in forbidden if token in invocation]
    emit("PASS" if not found else "FAIL", f"skill invocation validator avoids text-scan evidence ({found})", failures if found else None)
    for fixture in FIXTURES:
        check_file_exists(f"tests/fixtures/{fixture}", failures)


def check_front_matter_and_lines(failures: list[str], warnings: list[str]) -> None:
    for path in (ROOT / "references").rglob("*.md"):
        text = read(path)
        if not text.startswith("---\n"):
            warnings.append(str(path.relative_to(ROOT)))
        for idx, line in enumerate(text.splitlines(), 1):
            if len(line) > 900:
                emit("FAIL", f"{path.relative_to(ROOT)}:{idx} has an extremely long line", failures)
    if warnings:
        emit("WARN", "Some references lack front matter: " + ", ".join(warnings[:5]))
    else:
        emit("PASS", "References include front matter")


def check_scenario_runner_executes(failures: list[str]) -> None:
    proc = subprocess.run([sys.executable, "scripts/run-scenario-tests.py"], cwd=ROOT, text=True, capture_output=True)
    emit("PASS" if proc.returncode == 0 else "FAIL", "scenario runner executes successfully", failures if proc.returncode != 0 else None)
    if proc.returncode != 0:
        print(proc.stdout)
        print(proc.stderr)


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []
    for rel in ["SKILL.md", "AGENTS.md", "README.md", "references/index.yaml", "skills/visual-skill-registry.json", "skills/skills.manifest.yaml"]:
        check_file_exists(rel, failures)
    skill_text = read(ROOT / "SKILL.md")
    for gate in GATES:
        if gate not in skill_text:
            emit("FAIL", f"SKILL.md contains {gate}", failures)
    if len(skill_text.splitlines()) > 190:
        emit("WARN", "SKILL.md is growing beyond lightweight-router target")
    else:
        emit("PASS", "SKILL.md remains lightweight")
    check_index(failures)
    check_execution_card(failures)
    check_registry_consistency(failures)
    check_validators(failures)
    check_front_matter_and_lines(failures, warnings)
    check_scenario_runner_executes(failures)
    print()
    print(f"Summary: {len(failures)} FAIL, {len(warnings)} WARN")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
