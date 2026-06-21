# Skill Revision Summary - V6.2 Governance Hardening

Date: 2026-06-20

## User-Reported Failures Addressed

- No real subagent creation and no enforceable deputy-editor/chief-editor review chain.
- Review degraded into main-agent self-check after the first pass.
- Tool or subagent unavailability could be silently treated as a downgrade.
- Language-content and UI responsibilities were blurred, causing term/acronym components such as STAR to be laid out incorrectly.
- Table-like content could use inconsistent alignment and arbitrary short-sentence wrapping.
- Decorative line color systems were not explicitly banned.
- Motion design had no department, script, review gate, or clear restraint/diversity principle.
- When the user requested a file/version without specifying format, the default format was ambiguous.
- Current mainstream aesthetic research could be skipped, letting old templates masquerade as design judgment.

## Governance Changes

- Added a deputy-chief-editor gate before chief-editor review.
- Required parallel initial review from language content, brand/aesthetic, layout/UI, motion design, interaction/delivery, and QA-risk departments.
- Required all applicable deputy editors to agree before deputy-chief review, then chief-editor review.
- Required every post-fix review to return to the same deputy-editor subagent.
- Added a new department-creation gate: new departments require an application, deputy-chief pre-review, chief-editor approval, and an independent subagent.
- Replaced automatic downgrade language with a hard pause plus chief-editor and user approval.

## Design And QA Changes

- Added `17-motion-design-standards.md` for motion department scope, motion script requirements, intensity rules, vetoes, and QA checks.
- Added acronym/term component rules in `04-design-standards.md`, including the STAR-style first-letter/full-word binding problem.
- Added table-like alignment rules and a ban on arbitrary breaking of complete short judgment phrases.
- Added line/color semantic rules to reject decorative multi-color divider systems.
- Added old-version rejection gate in `11-aesthetic-anti-ai.md`.
- Added a mainstream aesthetic trend research card before Style Frame when the user asks for current/mainstream/latest aesthetics.
- Added motion evidence and blocker evidence requirements in `10-version-evidence.md`.

## Files Updated

- `SKILL.md`
- `AGENTS.md`
- `agents/openai.yaml`
- `references/00-system-overview.md`
- `references/01-team-roles.md`
- `references/02-workflow.md`
- `references/03-delivery-routing.md`
- `references/04-design-standards.md`
- `references/06-interaction-standards.md`
- `references/07-qa-checklist.md`
- `references/08-skill-governance.md`
- `references/10-version-evidence.md`
- `references/11-aesthetic-anti-ai.md`
- `references/16-multi-agent-governance.md`
- `references/17-motion-design-standards.md`
- `skills/verify-skills.sh`

## Remaining Enforcement Standard

Any future HTML/PPT/PDF production using this skill must create a real collaboration record before production. If subagents, tools, or a necessary department cannot be created or used, production pauses until the chief editor and the user explicitly approve the reduced scope.
