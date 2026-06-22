# AGENTS.md

## 1. Role

You are the implementation agent for this repository. Treat `presentation-system` as a lightweight entry router plus reference-based execution system.

## 2. Source of Truth

- `SKILL.md` defines the entry protocol, modes, G1-G8, and evidence rules.
- `references/index.yaml` defines reference routing by mode, trigger, gate, and required output.
- `references/*.md` define detailed procedures for production, design, QA, multi-agent work, online research, failure recovery, and Skill governance.
- `templates/*.md` define evidence formats such as the Current Execution Card.
- `scripts/validate-skill-structure.py` checks structural drift.
- `tests/scenarios.yaml` lists regression scenarios for mode and gate behavior.

## 3. Required Startup

Before modifying behavior, read:

- `SKILL.md`
- `references/index.yaml`
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

Production, repair, Style Frame, Vx review, and QA Freeze tasks usually require real multi-agent/subagent, browser/screenshot, and QA evidence. Review Only tasks may disclose missing evidence without blocking analysis.

## 6. Blocker Handling

For Production tasks, missing required tools can block final delivery:

- Missing subagent capability affects G5.
- Missing online search or official-source access affects G6.
- Missing browser/screenshot capability affects G7.
- User dissatisfaction or process failure activates G8.

For Review Only or suggestion tasks, missing tools should be disclosed as unverified scope, not treated as a blocker.

## 7. Commit Discipline

When editing this repository:

- Preserve core concepts: presentation-system, Style Frame, Page Spec, QA Freeze, Multi-Agent Governance, Online Research, Failure Recovery, Design Standards, Anti-AI flavor / 反AI味, User Requirement Lock, Production Gate, work platform, and `headroom`.
- Reduce duplication rather than adding another hard-gate block.
- Update `references/index.yaml` when adding or repurposing references.
- Run `python3 scripts/validate-skill-structure.py` when available.
- Summarize changed files, validation results, blockers, and remaining risk.

`allow_implicit_invocation` is intentionally `true` in `agents/openai.yaml` because this Skill should auto-trigger for presentation, deck, HTML/PPT/PDF, visual QA, online research, failure recovery, and Skill governance tasks. It should not trigger for simple exports or tiny unrelated edits.
