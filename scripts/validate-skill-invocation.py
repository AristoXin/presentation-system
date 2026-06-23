#!/usr/bin/env python3
"""Validate external Skill invocation evidence from structured JSON."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

from evidence_lib import (
    IssueLog,
    canonical_skill_id,
    formal_artifacts,
    has_field_path,
    load_json,
    load_registry,
    non_empty,
    path_from_ref,
    resolve_evidence_dir,
    sha256_file,
    write_report,
)

VALID_STATES = {"called", "manual_equivalent", "not_applicable", "blocked"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("target_dir", nargs="?", default=".")
    parser.add_argument("--run-id")
    parser.add_argument("--report")
    return parser.parse_args()


def required_skills(run: dict[str, Any], route: dict[str, Any], aliases: dict[str, str]) -> list[str]:
    raw = []
    raw.extend(run.get("required_skill_ids", []))
    raw.extend(route.get("required_skill_ids", []))
    raw.extend(run.get("named_skill_ids", []))
    return sorted({canonical_skill_id(str(skill), aliases) for skill in raw})


def load_runtime_lock(target: Path, evidence_dir: Path, run: dict[str, Any], invocations: dict[str, Any], log: IssueLog) -> dict[str, Any] | None:
    ref = invocations.get("runtime_lock_ref") or run.get("runtime_lock_ref") or "skills/runtime-lock.json"
    lock_path = path_from_ref(target, evidence_dir, ref)
    if lock_path is None or not lock_path.exists():
        log.fail("RUNTIME_LOCK_MISSING", f"Runtime lock is required for called Skills: {ref}")
        return None
    try:
        lock = load_json(lock_path, log)
    except Exception:
        return None
    if not lock.get("skills"):
        log.fail("RUNTIME_LOCK_EMPTY", "Runtime lock contains no skill entries.")
        return None
    log.pass_("RUNTIME_LOCK_FOUND", str(lock_path))
    return lock


def runtime_entry(lock: dict[str, Any] | None, skill_id: str) -> dict[str, Any] | None:
    if not lock:
        return None
    for entry in lock.get("skills", []):
        if entry.get("canonical_skill_id") == skill_id:
            return entry
    return None


def validate_absorption(
    target: Path,
    evidence_dir: Path,
    skill_id: str,
    absorbed_into: list[Any],
    absorption: dict[str, Any],
    log: IssueLog,
) -> None:
    rows = [row for row in absorption.get("absorptions", []) if row.get("skill_id") == skill_id]
    if not rows:
        log.fail("SKILL_ABSORPTION_MISSING", f"{skill_id} has no structured absorption row.")
        return
    for row in rows:
        downstream = path_from_ref(target, evidence_dir, row.get("downstream_file"))
        if downstream is None or not downstream.exists() or downstream.stat().st_size == 0:
            log.fail("ABSORPTION_DOWNSTREAM_MISSING", f"{skill_id} downstream file is missing or empty.")
            continue
        data = None
        if downstream.suffix == ".json":
            try:
                data = load_json(downstream)
            except Exception:
                data = None
        field_paths = row.get("field_paths", [])
        if not field_paths:
            log.fail("ABSORPTION_FIELD_PATH_MISSING", f"{skill_id} absorption lacks field_paths.")
        elif data is not None:
            missing = [field for field in field_paths if not has_field_path(data, field)]
            if missing:
                log.fail("ABSORPTION_FIELD_PATH_INVALID", f"{skill_id} missing downstream fields: {missing}")
        if not (row.get("page_ids") or row.get("page_families")):
            log.fail("ABSORPTION_PAGE_MAPPING_MISSING", f"{skill_id} absorption lacks page or page-family mapping.")
        if not row.get("qa_checks"):
            log.fail("ABSORPTION_QA_MISSING", f"{skill_id} absorption lacks QA checks.")
    if not absorbed_into:
        log.fail("ABSORBED_INTO_MISSING", f"{skill_id} invocation lacks absorbed_into references.")


def validate_called(
    target: Path,
    evidence_dir: Path,
    entry: dict[str, Any],
    runtime: dict[str, Any] | None,
    absorption: dict[str, Any],
    log: IssueLog,
) -> None:
    skill_id = entry["skill_id"]
    lock_entry = runtime_entry(runtime, skill_id)
    if not lock_entry:
        log.fail("RUNTIME_LOCK_ENTRY_MISSING", f"{skill_id} has called state but no runtime lock entry.")
    elif lock_entry.get("availability") != "resolved":
        log.fail("RUNTIME_SKILL_UNRESOLVED", f"{skill_id} runtime lock entry is not resolved.")
    else:
        resolved = Path(str(lock_entry.get("resolved_path")))
        skill_md = resolved / "SKILL.md"
        if not resolved.exists() or not skill_md.exists():
            log.fail("RUNTIME_SKILL_PATH_INVALID", f"{skill_id} resolved path or SKILL.md is missing.")
        elif lock_entry.get("skill_md_sha256") and lock_entry["skill_md_sha256"] != sha256_file(skill_md):
            log.fail("RUNTIME_SKILL_HASH_MISMATCH", f"{skill_id} SKILL.md sha256 does not match runtime lock.")
        else:
            log.pass_("RUNTIME_SKILL_RESOLVED", skill_id)

    for field in ["invocation_method", "evidence_ref"]:
        if not non_empty(entry.get(field)):
            log.fail("INVOCATION_FIELD_MISSING", f"{skill_id} called entry lacks {field}.")
    if not (entry.get("tool_call_id") or entry.get("thread_id") or entry.get("session_evidence")):
        log.fail("REAL_INVOCATION_REFERENCE_MISSING", f"{skill_id} called entry lacks tool/thread/session evidence.")

    output_files = entry.get("output_files", [])
    if not output_files:
        log.fail("OUTPUT_FILES_MISSING", f"{skill_id} called entry has no output_files.")
    for output in output_files:
        output_path = path_from_ref(target, evidence_dir, output.get("path"))
        if output_path is None or not output_path.exists() or output_path.stat().st_size == 0:
            log.fail("OUTPUT_FILE_INVALID", f"{skill_id} output is missing or empty: {output.get('path')}")
            continue
        expected = output.get("sha256") or entry.get("output_sha256")
        if expected and sha256_file(output_path) != expected:
            log.fail("OUTPUT_HASH_MISMATCH", f"{skill_id} output hash mismatch: {output.get('path')}")
    validate_absorption(target, evidence_dir, skill_id, entry.get("absorbed_into", []), absorption, log)


def validate_manual(target: Path, evidence_dir: Path, run: dict[str, Any], entry: dict[str, Any], log: IssueLog) -> None:
    skill_id = entry["skill_id"]
    if run.get("user_requires_real_skill_invocation"):
        log.fail("MANUAL_EQUIVALENT_NOT_ALLOWED", f"{skill_id} is manual_equivalent but user requires real invocation.")
    record_path = path_from_ref(target, evidence_dir, entry.get("manual_equivalent_ref"))
    if record_path is None or not record_path.exists():
        log.fail("MANUAL_EQUIVALENT_RECORD_MISSING", f"{skill_id} lacks a manual-equivalent record.")
        return
    record = load_json(record_path, log)
    for field in ["unavailable_reason", "limitations", "approval", "approved_by"]:
        if not non_empty(record.get(field)):
            log.fail("MANUAL_EQUIVALENT_FIELD_MISSING", f"{skill_id} manual record lacks {field}.")


def validate_last30days(entry: dict[str, Any], log: IssueLog) -> None:
    if entry.get("skill_id") != "last30days-search" or entry.get("state") != "called":
        return
    for field in ["queries", "sources", "source_dates", "retrieved_at", "adopt_reject", "source_to_design_translation"]:
        if not non_empty(entry.get(field)):
            log.fail("LAST30DAYS_FIELD_MISSING", f"last30days-search lacks {field}.")


def main() -> int:
    args = parse_args()
    target = Path(args.target_dir).resolve()
    log = IssueLog()
    try:
        evidence_dir, run = resolve_evidence_dir(target, args.run_id)
    except Exception as exc:
        print(f"CONFIG ERROR: {exc}", file=sys.stderr)
        return 2

    if run.get("run_id") != (args.run_id or run.get("run_id")):
        print("CONFIG ERROR: --run-id does not match run.json", file=sys.stderr)
        return 2
    skills, aliases = load_registry()
    try:
        route = load_json(evidence_dir / "reference-route.json") if (evidence_dir / "reference-route.json").exists() else {}
        invocations = load_json(evidence_dir / "skill-invocations.json", log)
        absorption = load_json(evidence_dir / "skill-absorption.json", log)
    except Exception:
        return 2

    if invocations.get("run_id") != run["run_id"] or absorption.get("run_id") != run["run_id"]:
        log.fail("RUN_ID_MISMATCH", "Skill evidence run_id does not match run.json.")

    required = required_skills(run, route, aliases)
    entries = invocations.get("invocations", [])
    if not isinstance(entries, list) or not entries:
        log.fail("INVOCATION_LEDGER_EMPTY", "skill-invocations.json contains no invocation entries.")
    canonical_entries: dict[str, dict[str, Any]] = {}
    for entry in entries:
        skill_id = canonical_skill_id(str(entry.get("skill_id", "")), aliases)
        entry["skill_id"] = skill_id
        if skill_id not in skills:
            log.fail("UNKNOWN_SKILL_ID", f"{skill_id} is not in canonical registry.")
            continue
        if skill_id in canonical_entries:
            log.fail("DUPLICATE_SKILL_ENTRY", f"{skill_id} appears more than once.")
        canonical_entries[skill_id] = entry
        if entry.get("state") not in VALID_STATES:
            log.fail("INVALID_SKILL_STATE", f"{skill_id} has invalid state {entry.get('state')!r}.")

    for skill_id in required:
        if skill_id not in canonical_entries:
            log.fail("REQUIRED_SKILL_UNRESOLVED", f"{skill_id} is required but missing from invocation ledger.")

    runtime = load_runtime_lock(target, evidence_dir, run, invocations, log) if any(entry.get("state") == "called" for entry in entries) else None
    artifacts = formal_artifacts(target)
    for entry in canonical_entries.values():
        state = entry.get("state")
        if state == "called":
            validate_called(target, evidence_dir, entry, runtime, absorption, log)
            validate_last30days(entry, log)
        elif state == "manual_equivalent":
            validate_manual(target, evidence_dir, run, entry, log)
        elif state == "not_applicable":
            reason = entry.get("reason")
            if not non_empty(reason) or str(reason).strip().lower() in {"not needed", "n/a", "不需要"}:
                log.fail("NOT_APPLICABLE_REASON_WEAK", f"{entry['skill_id']} lacks a task-specific not_applicable reason.")
        elif state == "blocked" and artifacts:
            log.fail("BLOCKED_WITH_FORMAL_ARTIFACT", f"{entry['skill_id']} is blocked but formal artifact(s) exist.")

    report = {
        "run_id": run.get("run_id"),
        "target": str(target),
        "evidence_dir": str(evidence_dir),
        "required_skill_ids": required,
        "issues": [issue.to_dict() for issue in log.issues],
        "summary": log.summary(),
    }
    write_report(Path(args.report) if args.report else None, report)
    print()
    print(f"Summary: {len(log.failures)} FAIL, {len(log.warnings)} WARN")
    return 1 if log.failures else 0


if __name__ == "__main__":
    sys.exit(main())
