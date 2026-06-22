# presentation-system

`presentation-system` is a lightweight Skill router for presentation governance, visual production, Skill audits, and evidence-based QA.

## Skill Architecture

presentation-system uses a lightweight entry router plus reference-based execution model.

- `SKILL.md`: entry protocol, execution modes, G1-G8, and evidence rules.
- `references/index.yaml`: routing table for detailed references.
- `references/*.md`: detailed procedures for production, design, QA, multi-agent work, online research, failure recovery, and Skill governance.
- `templates/*.md`: evidence templates, including the Current Execution Card.
- `scripts/validate-skill-structure.py`: structural validation.
- `tests/scenarios.yaml`: regression scenarios for mode and gate behavior.
- `skills/skills.manifest.yaml`: conditional/recommended tool declarations, including `last30days-skill` for recent community and trend research.

The entry file does not carry all detailed rules. It selects the mode, activates the relevant gates, and routes the agent to the smallest necessary reference set.

Complex tasks must establish or maintain a Current Execution Card. This is required for long tasks, multi-file tasks, Skill Governance, Production, Failure Recovery, and Capability Limited work.

Review Only and Production tasks have different blocker rules. Missing production tools do not block read-only analysis, but they do block claims that require real evidence.

Do not fabricate online research, screenshot/browser, subagent, multi-agent, QA Freeze, or final-delivery evidence.

`allow_implicit_invocation` is `true` because this Skill should auto-trigger for presentation, deck, HTML/PPT/PDF, visual QA, online research, failure recovery, and Skill governance tasks. It should not trigger for simple exports or tiny unrelated edits.
