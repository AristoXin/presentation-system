#!/usr/bin/env python3
"""Resolve references deterministically from references/index.yaml."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from evidence_lib import ROOT, VALID_ROUTES, VALID_STAGES, canonical_skill_id, load_json, load_registry, write_report


STARTUP_CORE = ["R00B", "R02", "R03", "R08"]
ROUTE_SKILLS = {
    "html_interactive": ["frontend-slides"],
    "pptx_editable": ["ppt-master"],
    "pdf_static": [],
    "screenshot_pack": [],
    "review_only": [],
    "skill_governance": [],
}


def load_index() -> dict[str, Any]:
    return load_json(ROOT / "references" / "index.yaml")


def select_references(
    *,
    mode: str,
    delivery_route: str,
    current_stage: str,
    triggers: list[str],
    named_skills: list[str],
    full_audit: bool,
) -> dict[str, Any]:
    index = load_index()
    skills, aliases = load_registry()
    max_initial = index.get("load_policy", {}).get("max_initial_references", 8)
    refs = index.get("references", [])
    ref_by_id = {ref["id"]: ref for ref in refs}
    trigger_set = set(triggers)
    named_skill_ids = [canonical_skill_id(skill, aliases) for skill in named_skills]
    trigger_set.update(named_skill_ids)
    if named_skill_ids:
        trigger_set.add("named_external_skill")
    trigger_set.add(delivery_route)
    trigger_set.add(current_stage)

    selected: list[dict[str, Any]] = []
    excluded: list[dict[str, str]] = []

    if full_audit:
        selected = refs[:]
        budget_status = {
            "max_initial_references": max_initial,
            "selected_count": len(selected),
            "within_budget": True,
            "exception": "full_audit",
        }
    else:
        for ref in refs:
            ref_id = ref["id"]
            stage_match = ref.get("stage") == current_stage
            mode_match = mode in ref.get("modes", [])
            route_match = delivery_route in ref.get("formats", [])
            trigger_match = bool(trigger_set.intersection(ref.get("triggers", [])))
            core_startup = current_stage == "startup" and ref_id in STARTUP_CORE and mode_match and route_match
            if core_startup or (stage_match and mode_match and route_match and trigger_match):
                selected.append(ref)
            else:
                excluded.append(
                    {
                        "id": ref_id,
                        "reason": f"stage={stage_match}, mode={mode_match}, route={route_match}, trigger={trigger_match}",
                    }
                )
        selected.sort(key=lambda ref: (ref.get("priority", 100), ref["id"]))
        if current_stage == "startup" and len(selected) > max_initial:
            selected = selected[:max_initial]
        budget_status = {
            "max_initial_references": max_initial,
            "selected_count": len(selected),
            "within_budget": current_stage != "startup" or len(selected) <= max_initial,
            "exception": None,
        }

    selected_ids = [ref["id"] for ref in selected]
    required_outputs: list[str] = []
    for ref in selected:
        required_outputs.extend(ref.get("owns_outputs", []))
    required_skill_ids = sorted(set(ROUTE_SKILLS.get(delivery_route, []) + named_skill_ids))
    active_gates = sorted({gate for ref in selected for gate in ref.get("gates", [])})
    blockers: list[str] = []
    if "named_external_skill" in trigger_set and not named_skill_ids:
        blockers.append("NAMED_SKILL_PARSE_BLOCKER")
    if delivery_route == "html_interactive" and current_stage in {"implementation", "post_build_qa", "qa_freeze"}:
        active_gates.extend(gate for gate in ["G7B", "G7C", "G7D"] if gate not in active_gates)

    return {
        "schema_version": 1,
        "mode": mode,
        "delivery_route": delivery_route,
        "current_stage": current_stage,
        "triggers": sorted(trigger_set),
        "named_skill_ids": named_skill_ids,
        "selected_reference_ids": selected_ids,
        "selected_paths": [ref_by_id[ref_id]["path"] for ref_id in selected_ids],
        "active_gates": active_gates,
        "required_outputs": sorted(set(required_outputs)),
        "required_skill_ids": required_skill_ids,
        "excluded_references_and_reasons": excluded,
        "reference_budget_status": budget_status,
        "blocker_codes": blockers,
        "implementation_allowed": current_stage in {"implementation", "post_build_qa", "qa_freeze"} and not blockers,
        "skill_registry_ids": sorted(skills.keys()),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", required=True)
    parser.add_argument("--delivery-route", required=True)
    parser.add_argument("--current-stage", default="startup")
    parser.add_argument("--trigger", action="append", default=[])
    parser.add_argument("--named-skill", action="append", default=[])
    parser.add_argument("--full-audit", action="store_true")
    parser.add_argument("--report")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.delivery_route not in VALID_ROUTES:
        print(f"CONFIG ERROR: invalid delivery route {args.delivery_route}", file=sys.stderr)
        return 2
    if args.current_stage not in VALID_STAGES:
        print(f"CONFIG ERROR: invalid stage {args.current_stage}", file=sys.stderr)
        return 2
    result = select_references(
        mode=args.mode,
        delivery_route=args.delivery_route,
        current_stage=args.current_stage,
        triggers=args.trigger,
        named_skills=args.named_skill,
        full_audit=args.full_audit,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    write_report(Path(args.report) if args.report else None, result)
    if not result["reference_budget_status"]["within_budget"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
