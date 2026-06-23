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
- `evidence/<run_id>/*.json`: runtime evidence consumed by validators.

The entry file does not carry all detailed rules. It selects the mode, activates the relevant gates, and routes the agent to the smallest necessary reference set.

Complex tasks must establish or maintain a Current Execution Card. This is required for long tasks, multi-file tasks, Skill Governance, Production, Failure Recovery, and Capability Limited work.

Review Only and Production tasks have different blocker rules. Missing production tools do not block read-only analysis, but they do block claims that require real evidence.

Do not fabricate online research, screenshot/browser, subagent, multi-agent, QA Freeze, or final-delivery evidence.

Markdown templates are worksheets. They do not pass validators until converted
into the current run's JSON evidence files.

`allow_implicit_invocation` is `true` because this Skill should auto-trigger for presentation, deck, HTML/PPT/PDF, visual QA, online research, failure recovery, and Skill governance tasks. It should not trigger for simple exports or tiny unrelated edits.

## Companion Skill Installation

Users who download `presentation-system` may not have every companion Skill installed locally. Codex must help them verify and install missing Skills before claiming related capabilities.

Run:

```bash
bash skills/verify-skills.sh
```

This writes `skills/runtime-lock.json` for the current machine. The file is
ignored by git and must be regenerated or verified for each production run
before a Skill can be marked `called`.

To install public GitHub-backed companion Skills known to this repository, run:

```bash
bash skills/install-skills.sh --install-missing
```

Currently this installer can directly install `last30days-skill` from `mvanhorn/last30days-skill`. Account-bound, private, local, connector, MCP, or API-key-backed capabilities still require explicit user consent and setup. If a required Skill cannot be installed or enabled, record it as `manual_equivalent`, `not_applicable`, or `blocked` in the Skill Invocation Ledger; do not claim it was called.

## Visual Production Architecture

presentation-system uses a pre-code visual production model.

Core chain:

1. Intent and mode detection
2. Reference routing
3. External Skill availability scan
4. External Skill invocation and absorption
5. Source material intake
6. Design synthesis
7. Motion opportunity mapping
8. Anti-template review
9. HTML experience contract
10. Editorial approval
11. Pre-code visual freeze
12. Formal implementation
13. Post-implementation visual QA
14. QA Freeze

No visual implementation should start before the pre-code visual freeze.

## Runtime Evidence

A production run should write JSON evidence under:

```text
evidence/<run_id>/
  run.json
  current-execution-card.json
  reference-route.json
  skill-invocations.json
  skill-absorption.json
  source-material-intake.json
  design-synthesis.json
  page-manifest.json
  motion-opportunities.json
  anti-template-review.json
  html-experience.json
  editorial-approval.json
  pre-code-freeze.json
  browser-qa.json
  qa-freeze.json
```

Resolve references deterministically:

```bash
python3 scripts/resolve-reference-route.py \
  --mode production \
  --delivery-route html_interactive \
  --current-stage startup
```

Run validation:

```bash
python3 scripts/validate-skill-structure.py
python3 scripts/run-scenario-tests.py
python3 scripts/validate-skill-invocation.py <target_dir> --run-id <run_id>
python3 scripts/validate-visual-production.py <target_dir> --run-id <run_id> --phase qa-freeze --strict
bash skills/verify-skills.sh
```

Automated checks verify routing and evidence structure. They cannot prove
absolute aesthetic quality by themselves; final aesthetic approval still needs
real reviewer/subagent capability and screenshot or equivalent visual evidence.
