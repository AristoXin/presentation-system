#!/usr/bin/env python3
"""Validate route-specific visual production evidence."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from evidence_lib import IssueLog, load_json, non_empty, path_from_ref, resolve_evidence_dir, sha256_file, write_report

PHASES = {"pre-code", "post-build", "qa-freeze"}
BASE_REQUIRED = {
    "html_interactive": {
        "pre-code": [
            "design-synthesis.json",
            "page-manifest.json",
            "motion-opportunities.json",
            "anti-template-review.json",
            "html-experience.json",
            "editorial-approval.json",
            "pre-code-freeze.json",
        ],
        "post-build": ["browser-qa.json"],
        "qa-freeze": ["qa-freeze.json"],
    },
    "pptx_editable": {
        "pre-code": ["page-manifest.json", "design-synthesis.json", "editorial-approval.json", "pre-code-freeze.json"],
        "post-build": ["browser-qa.json"],
        "qa-freeze": ["qa-freeze.json"],
    },
    "pdf_static": {
        "pre-code": ["page-manifest.json", "design-synthesis.json", "editorial-approval.json", "pre-code-freeze.json"],
        "post-build": ["browser-qa.json"],
        "qa-freeze": ["qa-freeze.json"],
    },
    "screenshot_pack": {
        "pre-code": ["page-manifest.json", "design-synthesis.json", "editorial-approval.json"],
        "post-build": ["browser-qa.json"],
        "qa-freeze": ["qa-freeze.json"],
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("target_dir", nargs="?", default=".")
    parser.add_argument("--run-id")
    parser.add_argument("--phase", choices=sorted(PHASES), default="post-build")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--report")
    return parser.parse_args()


def require_json(evidence_dir: Path, run_id: str, filename: str, log: IssueLog) -> dict[str, Any] | None:
    path = evidence_dir / filename
    if not path.exists() or path.stat().st_size == 0:
        log.fail("EVIDENCE_FILE_MISSING", f"{filename} is missing or empty.")
        return None
    data = load_json(path, log)
    if data.get("run_id") != run_id:
        log.fail("RUN_ID_MISMATCH", f"{filename} run_id does not match run.json.")
    if any(str(data).find(token) >= 0 for token in ["<placeholder>", "TBD", "TODO"]):
        log.fail("TEMPLATE_PLACEHOLDER_PRESENT", f"{filename} still contains placeholder text.")
    return data


def validate_design(data: dict[str, Any] | None, log: IssueLog) -> None:
    if not data:
        return
    for field in ["visual_thesis", "narrative_spine", "page_families", "inputs", "reviewer_evidence_ref"]:
        if not non_empty(data.get(field)):
            log.fail("DESIGN_SYNTHESIS_FIELD_MISSING", f"design-synthesis.json lacks {field}.")
    inputs = data.get("inputs", {})
    for field in ["content", "ui", "aesthetic", "motion", "interaction", "qa"]:
        if not non_empty(inputs.get(field)):
            log.fail("DESIGN_INPUT_MISSING", f"design synthesis lacks {field} input.")
    for conflict in data.get("conflicts", []):
        if not non_empty(conflict.get("resolution")):
            log.fail("DESIGN_CONFLICT_UNRESOLVED", "Design conflict lacks resolution.")
    if data.get("approval_status") != "approved":
        log.fail("DESIGN_NOT_APPROVED", "design-synthesis.json approval_status must be approved.")


def pages_from_manifest(data: dict[str, Any] | None, log: IssueLog) -> list[dict[str, Any]]:
    if not data:
        return []
    pages = data.get("pages", [])
    if not isinstance(pages, list) or not pages:
        log.fail("PAGE_MANIFEST_EMPTY", "page-manifest.json has no pages.")
        return []
    required = ["page_id", "order", "role", "family", "core_message", "visual_anchor", "source_asset_ids", "motion_class"]
    for page in pages:
        for field in required:
            if field not in page:
                log.fail("PAGE_FIELD_MISSING", f"{page.get('page_id', '<unknown>')} lacks {field}.")
        if page.get("motion_class") == "intentionally-static" and not non_empty(page.get("static_justification")):
            log.fail("STATIC_JUSTIFICATION_MISSING", f"{page.get('page_id')} is intentionally-static without justification.")
        if page.get("motion_class") == "motion-required" and not non_empty(page.get("required_states")):
            log.fail("REQUIRED_STATES_MISSING", f"{page.get('page_id')} is motion-required without required_states.")
    return pages


def validate_motion(data: dict[str, Any] | None, pages: list[dict[str, Any]], log: IssueLog) -> None:
    if not data:
        return
    entries = data.get("pages", [])
    by_id = {entry.get("page_id"): entry for entry in entries}
    manifest_ids = {page.get("page_id") for page in pages}
    if set(by_id) != manifest_ids:
        log.fail("MOTION_PAGE_COVERAGE_MISMATCH", "motion-opportunities.json must cover exactly the page manifest pages.")
    classes = []
    required_fields = ["purpose", "trigger", "idle_state", "reveal_states", "completed_state", "back_or_replay", "reduced_motion", "export_state"]
    for page_id, entry in by_id.items():
        motion_class = entry.get("motion_class")
        classes.append(motion_class)
        if motion_class not in {"motion-required", "motion-optional", "intentionally-static"}:
            log.fail("INVALID_MOTION_CLASS", f"{page_id} has invalid motion_class {motion_class}.")
        if motion_class == "motion-required":
            for field in required_fields:
                if not non_empty(entry.get(field)):
                    log.fail("MOTION_REQUIRED_FIELD_MISSING", f"{page_id} lacks {field}.")
        if motion_class == "intentionally-static":
            if not non_empty(entry.get("static_justification")):
                log.fail("STATIC_JUSTIFICATION_MISSING", f"{page_id} lacks static_justification.")
            if not (non_empty(entry.get("simultaneous_reading_reason")) or non_empty(entry.get("equivalent_reason"))):
                log.fail("STATIC_READING_REASON_MISSING", f"{page_id} lacks simultaneous reading reason.")
    if len(set(classes)) == 1 and len(classes) > 1:
        log.warn("UNIFORM_MOTION_CLASS", "All pages use the same motion class; this requires a waiver for QA Freeze.")


def validate_anti_template(data: dict[str, Any] | None, pages: list[dict[str, Any]], log: IssueLog) -> None:
    if not data or not pages:
        return
    families = [page.get("family") for page in pages]
    counts = Counter(families)
    if len(counts) == 1 and len(families) > 1:
        waivers = data.get("waivers", [])
        if not waivers:
            log.warn("SINGLE_PAGE_FAMILY", "All pages use one family without a waiver.")
    for idx in range(2, len(families)):
        if families[idx] == families[idx - 1] == families[idx - 2]:
            if not data.get("waivers"):
                log.warn("REPEATED_PAGE_FAMILY", "Three consecutive pages use the same family without waiver.")
            break
    if not non_empty(data.get("family_distribution")):
        log.fail("ANTI_TEMPLATE_DISTRIBUTION_MISSING", "anti-template-review.json lacks family_distribution.")


def validate_html_experience(data: dict[str, Any] | None, log: IssueLog) -> None:
    if not data:
        return
    checks = ["navigation_state", "page_state", "reveal_state", "replay_back", "keyboard", "wheel", "touch_pointer", "reduced_motion", "export_print_stable_state"]
    for field in checks:
        if not non_empty(data.get(field)):
            log.fail("HTML_EXPERIENCE_FIELD_MISSING", f"html-experience.json lacks {field}.")


def validate_editorial(data: dict[str, Any] | None, target: Path, evidence_dir: Path, log: IssueLog) -> None:
    if not data:
        return
    records = data.get("approvals", [])
    if not records:
        log.fail("EDITORIAL_APPROVAL_EMPTY", "editorial-approval.json has no approvals.")
        return
    for record in records:
        for field in ["department", "decision", "comments", "approved_at", "reviewed_artifact_path", "reviewed_artifact_sha256"]:
            if not non_empty(record.get(field)):
                log.fail("EDITORIAL_FIELD_MISSING", f"editorial approval lacks {field}.")
        if record.get("author_agent_id") and record.get("author_agent_id") == record.get("deputy_editor_agent_id"):
            log.fail("EDITORIAL_SELF_REVIEW", "author_agent_id equals deputy_editor_agent_id.")
        if not (record.get("tool_call_id") or record.get("thread_id") or record.get("execution_ref")):
            log.fail("EDITORIAL_EXECUTION_REF_MISSING", "editorial approval lacks real execution reference.")
        artifact = path_from_ref(target, evidence_dir, record.get("reviewed_artifact_path"))
        if artifact and artifact.exists() and record.get("reviewed_artifact_sha256") != sha256_file(artifact):
            log.fail("EDITORIAL_ARTIFACT_HASH_MISMATCH", f"{artifact} hash mismatch.")


def html_markers(path: Path) -> dict[str, dict[str, str]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    markers: dict[str, dict[str, str]] = {}
    for match in re.finditer(r"<[^>]+data-page-id=[\"']([^\"']+)[\"'][^>]*>", text, re.I):
        tag = match.group(0)
        page_id = match.group(1)
        markers[page_id] = {
            "family": _attr(tag, "data-family"),
            "motion_class": _attr(tag, "data-motion-class"),
            "state": _attr(tag, "data-state"),
        }
    return markers


def _attr(tag: str, name: str) -> str:
    match = re.search(name + r"=[\"']([^\"']+)[\"']", tag, re.I)
    return match.group(1) if match else ""


def validate_html_dom(target: Path, evidence_dir: Path, html_exp: dict[str, Any] | None, pages: list[dict[str, Any]], phase: str, strict: bool, log: IssueLog) -> None:
    if not html_exp or phase == "pre-code":
        return
    artifact = path_from_ref(target, evidence_dir, html_exp.get("artifact_path"))
    if artifact is None or not artifact.exists():
        log.fail("HTML_ARTIFACT_MISSING", "html-experience.json artifact_path is missing.")
        return
    markers = html_markers(artifact)
    if not markers:
        log.fail("HTML_MACHINE_MARKERS_MISSING", "HTML lacks data-page-id markers.")
        return
    for page in pages:
        marker = markers.get(page["page_id"])
        if not marker:
            log.fail("HTML_PAGE_MARKER_MISSING", f"HTML lacks marker for {page['page_id']}.")
            continue
        if marker.get("family") != page.get("family"):
            log.fail("HTML_PAGE_FAMILY_MISMATCH", f"{page['page_id']} data-family does not match manifest.")
        if marker.get("motion_class") != page.get("motion_class"):
            log.fail("HTML_MOTION_CLASS_MISMATCH", f"{page['page_id']} data-motion-class does not match manifest.")
        if strict and page.get("motion_class") == "motion-required" and not non_empty(marker.get("state")):
            log.fail("HTML_STATE_MISSING", f"{page['page_id']} motion-required marker lacks state.")
    text = artifact.read_text(encoding="utf-8", errors="ignore")
    if strict:
        for code, pattern, message in [
            ("REDUCED_MOTION_MISSING", r"prefers-reduced-motion", "HTML lacks reduced-motion handling."),
            ("EXPORT_PRINT_STABLE_MISSING", r"@media\s+print|data-export|export-mode", "HTML lacks export/print stable state."),
            ("KEYBOARD_INPUT_MISSING", r"keydown", "HTML lacks keyboard input handling."),
        ]:
            if not re.search(pattern, text, re.I):
                log.fail(code, message)
        if re.search(r"nextSlide|prevSlide", text) and not re.search(r"data-state|setAttribute\(['\"]data-state", text):
            log.fail("NEXT_PREV_ONLY_HTML", "HTML appears to expose next/prev without page-level state.")


def validate_browser_qa(data: dict[str, Any] | None, target: Path, evidence_dir: Path, strict: bool, log: IssueLog) -> None:
    if not data:
        return
    screenshots = data.get("screenshots", [])
    if strict and not screenshots:
        log.fail("BROWSER_QA_SCREENSHOT_MISSING", "QA Freeze requires screenshot/browser evidence.")
    for shot in screenshots:
        path = path_from_ref(target, evidence_dir, shot.get("path"))
        if path is None or not path.exists() or path.stat().st_size == 0:
            log.fail("BROWSER_QA_SCREENSHOT_INVALID", f"Screenshot is missing or empty: {shot.get('path')}")


def validate_qa_freeze(data: dict[str, Any] | None, strict: bool, log: IssueLog) -> None:
    if not data:
        return
    unresolved = data.get("unresolved_blockers", [])
    unapproved_warns = data.get("unapproved_warnings", [])
    if unresolved:
        log.fail("QA_FREEZE_UNRESOLVED_BLOCKERS", "qa-freeze.json contains unresolved blockers.")
    if strict and unapproved_warns:
        log.fail("QA_FREEZE_UNAPPROVED_WARNINGS", "strict QA Freeze cannot pass with unapproved warnings.")
    if data.get("decision") != "approved":
        log.fail("QA_FREEZE_NOT_APPROVED", "qa-freeze.json decision must be approved.")


def main() -> int:
    args = parse_args()
    target = Path(args.target_dir).resolve()
    log = IssueLog()
    try:
        evidence_dir, run = resolve_evidence_dir(target, args.run_id)
    except Exception as exc:
        print(f"CONFIG ERROR: {exc}", file=sys.stderr)
        return 2
    route = run.get("delivery_route")
    run_id = run.get("run_id")
    if route in {"review_only", "skill_governance"}:
        log.pass_("VISUAL_EVIDENCE_NOT_REQUIRED", f"{route} does not require visual production evidence.")
        write_report(Path(args.report) if args.report else None, {"issues": [i.to_dict() for i in log.issues], "summary": log.summary()})
        return 0
    if route not in BASE_REQUIRED:
        print(f"CONFIG ERROR: unsupported delivery_route {route}", file=sys.stderr)
        return 2

    required = list(BASE_REQUIRED[route]["pre-code"])
    if args.phase in {"post-build", "qa-freeze"}:
        required.extend(BASE_REQUIRED[route].get("post-build", []))
    if args.phase == "qa-freeze":
        required.extend(BASE_REQUIRED[route].get("qa-freeze", []))
    data = {filename: require_json(evidence_dir, run_id, filename, log) for filename in required}

    design = data.get("design-synthesis.json")
    manifest = data.get("page-manifest.json")
    motion = data.get("motion-opportunities.json")
    anti = data.get("anti-template-review.json")
    html_exp = data.get("html-experience.json")
    editorial = data.get("editorial-approval.json")
    browser = data.get("browser-qa.json")
    qa = data.get("qa-freeze.json")

    validate_design(design, log)
    pages = pages_from_manifest(manifest, log)
    if route == "html_interactive":
        validate_motion(motion, pages, log)
        validate_html_experience(html_exp, log)
        validate_html_dom(target, evidence_dir, html_exp, pages, args.phase, args.strict or args.phase == "qa-freeze", log)
    validate_anti_template(anti, pages, log)
    validate_editorial(editorial, target, evidence_dir, log)
    if args.phase in {"post-build", "qa-freeze"}:
        validate_browser_qa(browser, target, evidence_dir, args.strict or args.phase == "qa-freeze", log)
    if args.phase == "qa-freeze":
        validate_qa_freeze(qa, args.strict, log)

    if args.phase == "qa-freeze" and args.strict and log.warnings:
        log.fail("QA_FREEZE_WARNINGS_PRESENT", "strict QA Freeze cannot pass with unapproved validator warnings.")

    report = {
        "run_id": run_id,
        "delivery_route": route,
        "phase": args.phase,
        "strict": args.strict,
        "issues": [issue.to_dict() for issue in log.issues],
        "summary": log.summary(),
    }
    write_report(Path(args.report) if args.report else None, report)
    print()
    print(f"Summary: {len(log.failures)} FAIL, {len(log.warnings)} WARN")
    return 1 if log.failures else 0


if __name__ == "__main__":
    sys.exit(main())
