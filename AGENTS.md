# AGENTS.md

## 1. Role

You are the implementation agent for this repository. Treat `presentation-system` as a lightweight entry router plus reference-based execution system.

## 2. Source of Truth

- `SKILL.md` defines the entry protocol, modes, G1-G8, and evidence rules.
- `references/index.yaml` defines reference routing by mode, trigger, gate, and required output.
- `references/*.md` define detailed procedures for production, design, QA, multi-agent work, online research, failure recovery, and Skill governance.
- `templates/*.md` define evidence formats such as the Current Execution Card.
- `evidence/<run_id>/*.json` is the machine-validated runtime evidence model.
- `scripts/validate-skill-structure.py` checks structural drift.
- `tests/scenarios.yaml` lists regression scenarios for mode and gate behavior.

## 3. Required Startup

Before modifying behavior, read:

- `SKILL.md`
- `references/index.yaml`
- `scripts/resolve-reference-route.py` output for the current mode, stage, route, triggers, and named Skills
- Files directly relevant to the user's selected mode and task

Do not read every reference by default. Full reference reads are appropriate only when the user asks for complete Skill audit/refactor or when the Current Execution Card requires them.

## 4. Mode Handling

Use the modes from `SKILL.md`:

- Mode A: Review Only
- Mode B: Skill Governance
- Mode C: Production
- Mode D: Failure Recovery
- Mode E: Capability Limited

For Skill Governance, modify only Skill-system files unless the user explicitly requests otherwise. For Production, follow the routed references and active gates before creating or changing final artifacts.

## 5. Evidence Handling

Never claim research, subagent work, screenshots, browser checks, QA Freeze, final delivery, or all-checks-passed status unless there is actual evidence.

Use the current `run_id` for all machine evidence. Do not use copied Markdown
templates, final summaries, or placeholder records as validator evidence.
External Skill `called` records must reference the current `skills/runtime-lock.json`.

Production, repair, Style Frame, Vx review, and QA Freeze tasks usually require real multi-agent/subagent, browser/screenshot, and QA evidence. Review Only tasks may disclose missing evidence without blocking analysis.

## 6. Blocker Handling

For Production tasks, missing required tools can block final delivery:

- Missing subagent capability affects G5.
- Missing online search or official-source access affects G6.
- Missing browser/screenshot capability affects G7.
- User dissatisfaction or process failure activates G8.

QA Freeze must run `scripts/validate-visual-production.py <target> --run-id <id> --phase qa-freeze --strict` or be reported as unverified.

For Review Only or suggestion tasks, missing tools should be disclosed as unverified scope, not treated as a blocker.

## 7. Commit Discipline

When editing this repository:

- Preserve core concepts: presentation-system, Style Frame, Page Spec, QA Freeze, Multi-Agent Governance, Online Research, Failure Recovery, Design Standards, Anti-AI flavor / 反AI味, User Requirement Lock, Production Gate, work platform, and `headroom`.
- Reduce duplication rather than adding another hard-gate block.
- Update `references/index.yaml` when adding or repurposing references.
- Run `python3 scripts/validate-skill-structure.py` when available.
- Run `python3 scripts/run-scenario-tests.py` after routing, validator, fixture, or scenario changes.
- Summarize changed files, validation results, blockers, and remaining risk.

`allow_implicit_invocation` is intentionally `true` in `agents/openai.yaml` because this Skill should auto-trigger for presentation, deck, HTML/PPT/PDF, visual QA, online research, failure recovery, and Skill governance tasks. It should not trigger for simple exports or tiny unrelated edits.

## 8. Pre-Code Visual Production Rule

For any visual Production task, Codex must not start by creating or editing final HTML/CSS/JS/PPT/PDF files.

Before implementation, Codex must create or update Skill Availability Scan, Skill Invocation Ledger, Skill Absorption Matrix, Source Material Intake and Adaptation Contract, Design Synthesis Contract, Motion Opportunity Map, Anti-Template Review, HTML Experience Contract when HTML is involved, Editorial Design Board, and Pre-Code Visual Freeze.

If these records are missing, Codex must stop with `PRE_CODE_VISUAL_BLOCKER`. Do not replace these artifacts with a checklist in the final response. Do not claim UI/aesthetic/motion integration unless the Design Synthesis Contract exists. Do not claim motion design unless the Motion Opportunity Map exists. Do not claim HTML is interactive or non-static unless the HTML Experience Contract exists. Do not start implementation and then write these records afterward.

## 9. External Skill Invocation Rule

Codex must not silently replace named external Skills with its own implementation.

Before writing final visual artifacts, Codex must create or update Skill Availability Scan, Skill Invocation Ledger, Skill Absorption Matrix, Manual Equivalent Record when applicable, and Skill Capability Blocker when required.

If `design-dna`, `PPT DNA`, `guizang`, `StyleKit`, `Taste`, `frontend-slides`, `html-ppt`, `huashu`, `ppt-master`, `humanize-ppt`, or `last30days` is required by the user, reference router, or delivery route, it must be resolved before implementation. Do not claim a named Skill was used or absorbed unless the ledger and absorption matrix exist.

## 10. Editorial Approval Rule

For visual Production, department collaboration is not a final-response claim.

Codex must create or update Editorial Design Board, Department Draft Records, Deputy Editor Consensus Record, Editor-in-Chief Approval Record, and Formal Production Handoff.

Only after these records approve the non-final reference draft may Codex start formal implementation. If records are missing, stop with `EDITORIAL_APPROVAL_BLOCKER`.
