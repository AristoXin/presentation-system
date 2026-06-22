---
name: presentation-system
description: Lightweight router for presentation, deck, HTML/PPT/PDF, visual QA, multi-agent governance, online research, failure recovery, and Skill governance work. Use for audits, rule maintenance, Style Frame/Page Spec planning, production gating, QA Freeze, and anti-AI flavor design governance.
---

# presentation-system Skill

## 1. Purpose

`presentation-system` routes presentation and visual-production work through a small set of execution modes, numbered gates, reference files, and evidence requirements. It is not a complete rule encyclopedia. Detailed procedures live in `references/*.md` and are loaded only when the current task needs them.

The Skill preserves the core production system: Style Frame, Page Spec, QA Freeze, Multi-Agent Governance, Online Research, Failure Recovery, Design Standards, Anti-AI flavor / 反AI味 review, User Requirement Lock, Production Gate, work platform governance, and `headroom` for long tasks.

## 2. Use When

Use this Skill when the user asks to:

- Audit, revise, or stabilize this Skill system.
- Review historical summaries, evidence folders, or retrospective governance records against current rules.
- Create, repair, review, or freeze PPT, HTML slides, PDFs, decks, visual reports, teaching materials, client reports, roadshows, workshops, research presentations, screenshot packs, or speaker notes.
- Judge real intent, page count, delivery format, template suitability, Style Frame, Page Spec, visual quality, motion, interaction, QA, or anti-AI flavor.
- Use or verify multi-agent production, subagent review, department roles, work platform records, online research, browser/screenshot evidence, current trends, external references, or latest official docs.
- Recover from user feedback such as "丑", "AI味重", "没按流程", "没有联网", "没有调用 subagent", or "和要求不一致".

## 3. Do Not Use When

Do not use this Skill for simple file conversion, tiny copy edits, ordinary code changes, or single-command exports unless the user also asks for presentation governance, visual QA, Skill governance, production gates, online research, or multi-agent evidence.

Do not use it to generate a final visual artifact when the task is only review, planning, or Skill governance.

## 4. Execution Modes

Choose exactly one primary mode before acting. If the task changes, update the mode.

| Mode | Name | Use when | Production blocker behavior |
| --- | --- | --- | --- |
| A | Review Only | The user asks for audit, analysis, or suggestions and does not request file edits or artifacts. | Missing production tools do not block; disclose unverified areas. |
| B | Skill Governance | The user asks to modify `SKILL.md`, `AGENTS.md`, `agents/openai.yaml`, `references/`, manifests, prompts, or governance evidence. | Do not create unrelated visual artifacts. Protect core capabilities while reducing duplication. |
| C | Production | The user asks to create, repair, freeze, export, or deliver PPT/HTML/PDF/decks/pages/materials. | Required gates can block final delivery. No QA Freeze claim without evidence. |
| D | Failure Recovery | The user reports bad aesthetics, AI flavor, missing process, missing search, missing subagents, or mismatch with requirements. | Stop production first. Audit failed gates, rebuild the Current Execution Card, then repair process or Page Spec/Style Frame. |
| E | Capability Limited | A required tool, connector, subagent, browser, screenshot, search, or validation capability is unavailable. | Blocks only tasks that require real execution evidence; does not block review-only analysis. |

## 5. Core Gates

All detailed rules must reference these gate numbers instead of redefining competing "highest priority" gates.

- **G1 Intent Gate**: Identify the real purpose, audience, delivery format, template relationship, need for online research, whether this is existing-artifact repair, and whether it is only audit/advice.
- **G2 Mode Gate**: Select Mode A/B/C/D/E and apply that mode's blocker rules. Do not apply production blockers to review-only tasks.
- **G3 User Requirement Lock**: Follow the user's latest explicit requirements, corrections, forbidden assumptions, and acceptance criteria before older context.
- **G4 Reference Routing Gate**: Read `references/index.yaml`, then load only the references required for the current mode and task triggers.
- **G5 Multi-Agent Evidence Gate**: For Production, repair, QA Freeze, Style Frame, and Vx review, require real role/subagent evidence or mark the missing capability as a blocker. Review-only advice may recommend roles without blocking.
- **G6 Research Gate**: Trigger online research for latest/current information, official docs, trends, external examples, user-requested search, market/policy/pricing/legal/version-sensitive facts, or browser-source validation. Never invent sources.
- **G7 Visual QA Freeze Gate**: For visual artifacts, require screenshot/browser or equivalent visual checks, implementation review, QA record, and freeze evidence before saying final, delivered, or QA-passed.
- **G8 Failure Freeze Gate**: On user negative feedback about quality, process, research, subagents, or mismatch, stop production and audit failed gates before continuing.

## 6. Current Execution Card

For long tasks, multi-file tasks, Skill Governance, Production, Failure Recovery, or Capability Limited tasks, create or maintain a Current Execution Card using `templates/current-execution-card.md`.

The card must lock:

- Selected mode and why other modes do not apply.
- Latest user requirements and forbidden assumptions.
- Active gates G1-G8.
- Required references from `references/index.yaml`.
- Evidence requirements for research, subagents, screenshots/browser checks, QA Freeze, and blockers.
- Allowed next actions and disallowed actions.

Small Review Only tasks may use a compact inline card.

## 7. Reference Router

Before loading detailed rules, read `references/index.yaml`. Use its `read_when`, `gates`, and `required_outputs` fields to decide which reference files to load.

Rules:

- Do not read every reference by default.
- Do not copy reference details into this entry file.
- If a task asks for complete Skill audit or full Skill refactor, read all relevant core files and all references because that is the task scope.
- If `references/index.yaml` is missing or points to missing files, treat it as a Skill Governance defect and repair it before Production.

## 8. Evidence Rules

Never claim evidence that was not actually produced.

- No online research claim without source list or a clear research blocker.
- No subagent or multi-agent claim without real thread/tool/role evidence or an explicit blocker.
- No screenshot, browser validation, or visual QA claim without actual captured or inspected evidence.
- No QA Freeze, final version, delivered status, or "all checks passed" wording unless G7 evidence exists.
- No Production downgrade just because tools are missing; switch to Mode E or ask the user to change scope.

## 9. Failure Recovery

If the user says the result is ugly, AI-flavored, template-like, not according to process, missing search, missing subagents, missing review, not what they asked for, or similarly negative, enter Mode D and activate G8.

Allowed next actions:

- Freeze production.
- Build or update the Current Execution Card.
- List failed gates and missing evidence.
- Read failure-related references from `references/index.yaml`.
- Rebuild Page Spec, Style Frame, or governance rules before any new artifact production.

Not allowed:

- Direct CSS/layout patching as if the issue were local only.
- Creating a new Vx/final artifact before failure audit and required gates are restored.
- Claiming prior QA, subagent review, or research evidence retroactively.

## 10. Final Response Rules

Final responses must match the selected mode.

- Review Only: findings, assumptions, unverified areas, and suggestions.
- Skill Governance: changed files, why they changed, validation run, remaining risks, and acceptance checklist.
- Production: delivered files, evidence paths, QA/freeze status, blockers, and user-validation status.
- Failure Recovery: failed gates, frozen actions, recovery plan, and what is now allowed or blocked.
- Capability Limited: missing capabilities, affected gates, what was still completed, and what cannot be claimed.

Do not end with "final", "delivered", "QA passed", "multi-agent complete", "researched", or "browser verified" unless the required evidence exists.
