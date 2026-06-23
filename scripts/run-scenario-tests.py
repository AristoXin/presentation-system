#!/usr/bin/env python3
"""Executable regression tests for routing and validator fixtures."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PY = sys.executable


def run_json(cmd: list[str]) -> tuple[int, dict[str, Any], str]:
    proc = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError:
        payload = {}
    return proc.returncode, payload, proc.stdout + proc.stderr


def run_code(cmd: list[str]) -> tuple[int, str]:
    proc = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    return proc.returncode, proc.stdout + proc.stderr


def assert_true(condition: bool, message: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {message}")
    else:
        print(f"FAIL: {message}")
        failures.append(message)


def load_scenarios() -> list[dict[str, Any]]:
    path = ROOT / "tests" / "scenarios.yaml"
    return json.loads(path.read_text(encoding="utf-8")).get("scenarios", [])


def check_scenarios(failures: list[str]) -> None:
    for scenario in load_scenarios():
        context = scenario["context"]
        expected = scenario["expected"]
        cmd = [
            PY,
            "scripts/resolve-reference-route.py",
            "--mode",
            context["mode"],
            "--delivery-route",
            context["delivery_route"],
            "--current-stage",
            context["stage"],
        ]
        for trigger in context.get("triggers", []):
            cmd.extend(["--trigger", trigger])
        for skill in context.get("named_skills", []):
            cmd.extend(["--named-skill", skill])
        if context.get("full_audit"):
            cmd.append("--full-audit")
        code, payload, output = run_json(cmd)
        assert_true(code == 0, f"{scenario['id']} resolver exits 0", failures)
        if code != 0:
            print(output)
            continue
        selected = payload.get("selected_reference_ids", [])
        expected_refs = expected.get("reference_ids", [])
        assert_true(all(ref in selected for ref in expected_refs), f"{scenario['id']} selected references include expected IDs", failures)
        expected_skills = sorted(expected.get("required_skill_ids", []))
        assert_true(sorted(payload.get("required_skill_ids", [])) == expected_skills, f"{scenario['id']} required skills match", failures)
        assert_true(set(expected.get("active_gates", [])).issubset(set(payload.get("active_gates", []))), f"{scenario['id']} active gates include expected gates", failures)
        assert_true(payload.get("implementation_allowed") == expected.get("implementation_allowed"), f"{scenario['id']} implementation_allowed matches", failures)
        assert_true(payload.get("blocker_codes", []) == expected.get("blocker_codes", []), f"{scenario['id']} blockers match", failures)
        budget = payload.get("reference_budget_status", {})
        if context.get("stage") == "startup" and not context.get("full_audit"):
            assert_true(budget.get("selected_count", 99) <= expected.get("max_initial_references", 8), f"{scenario['id']} startup budget respected", failures)
        if context.get("full_audit"):
            assert_true(budget.get("exception") == expected.get("budget_exception"), f"{scenario['id']} full_audit exception recorded", failures)


def check_fixture_command(name: str, cmd: list[str], expected_code: int, failures: list[str]) -> None:
    code, output = run_code(cmd)
    ok = code == expected_code
    assert_true(ok, f"{name} exits {expected_code}", failures)
    if not ok:
        print(output)


def check_duplicate_owner_fixture(failures: list[str]) -> None:
    fixture = ROOT / "tests" / "fixtures" / "duplicate-output-owner" / "index.json"
    data = json.loads(fixture.read_text(encoding="utf-8"))
    duplicate = [name for name, owners in data.get("outputs", {}).items() if isinstance(owners, list) and len(owners) > 1]
    assert_true("DesignSynthesisContract" in duplicate, "duplicate-output-owner fixture is detected as duplicate", failures)


def check_fixtures(failures: list[str]) -> None:
    fixtures = ROOT / "tests" / "fixtures"
    visual = "scripts/validate-visual-production.py"
    invocation = "scripts/validate-skill-invocation.py"
    check_fixture_command("valid-interactive-html", [PY, visual, str(fixtures / "valid-interactive-html"), "--run-id", "valid-html", "--phase", "qa-freeze", "--strict"], 0, failures)
    check_fixture_command("intentionally-static-valid", [PY, visual, str(fixtures / "intentionally-static-valid"), "--run-id", "static-valid", "--phase", "pre-code"], 0, failures)
    check_fixture_command("pptx-without-html-contract", [PY, visual, str(fixtures / "pptx-without-html-contract"), "--run-id", "pptx-route", "--phase", "pre-code"], 0, failures)
    check_fixture_command("blank-evidence-html", [PY, visual, str(fixtures / "blank-evidence-html"), "--run-id", "blank-html", "--phase", "pre-code"], 1, failures)
    check_fixture_command("static-next-prev-html", [PY, visual, str(fixtures / "static-next-prev-html"), "--run-id", "next-prev", "--phase", "qa-freeze", "--strict"], 1, failures)
    check_fixture_command("motion-required-without-state", [PY, visual, str(fixtures / "motion-required-without-state"), "--run-id", "motion-missing", "--phase", "pre-code"], 1, failures)
    check_fixture_command("skill-not-applicable-valid", [PY, invocation, str(fixtures / "skill-not-applicable-valid"), "--run-id", "skill-na"], 0, failures)
    check_fixture_command("blocked-skill-with-artifact", [PY, invocation, str(fixtures / "blocked-skill-with-artifact"), "--run-id", "blocked-artifact"], 1, failures)
    check_fixture_command("manual-equivalent-real-call-required", [PY, invocation, str(fixtures / "manual-equivalent-real-call-required"), "--run-id", "manual-real-required"], 1, failures)
    check_fixture_command("runtime-lock-missing", [PY, invocation, str(fixtures / "runtime-lock-missing"), "--run-id", "runtime-missing"], 1, failures)
    check_duplicate_owner_fixture(failures)


def main() -> int:
    failures: list[str] = []
    check_scenarios(failures)
    check_fixtures(failures)
    print()
    print(f"Summary: {len(failures)} FAIL")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
