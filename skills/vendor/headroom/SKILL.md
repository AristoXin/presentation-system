---
name: headroom
description: Context headroom and long-task continuity skill for presentation-system. Use when a task spans many files, many rounds, long logs, screenshot packs, exports, multiple subagents, or risks losing track of decisions. Produces compact state summaries, read/edit indexes, decision logs, risk lists, and handoff packets. Do not use for normal small edits.
---

# Headroom

Use this skill only when the toolchain/context副主编 or 总编 decides the task needs context compression. Do not call it automatically for every task.

## When To Use

Use Headroom when one or more are true:

- More than 8 source or reference files are involved.
- The task spans multiple turns, subagents, or production rounds.
- Logs, screenshots, QA records, exports, or version evidence are growing large.
- A handoff, resume, or context compaction is likely.
- The team needs a stable state packet before total editor review, QA freeze, or user验收.

Do not use Headroom for short one-file edits, simple QA comments, or ordinary final summaries.

## Outputs

Create or update a compact state packet in the current version evidence folder:

```text
versions/<version>/evidence/headroom-state.md
```

If no version exists yet, write to:

```text
versions/_working/evidence/headroom-state.md
```

## State Packet Template

```markdown
# Headroom State

## Current Objective

## Current Version

## Read Files

| File | Why Read | Key Takeaway |
| :--- | :--- | :--- |

## Edited Files

| File | Change | Reason | Needs Follow-up |
| :--- | :--- | :--- | :--- |

## Decisions

| Decision | Owner | Evidence | Status |
| :--- | :--- | :--- | :--- |

## Open Risks

| Risk | Owner | Next Check |
| :--- | :--- | :--- |

## Subagent State

| Agent | Role | Task | Status | Output |
| :--- | :--- | :--- | :--- | :--- |

## QA / Evidence State

| Evidence | Path | Status |
| :--- | :--- | :--- |

## Next Actions

1.
2.
3.
```

## Rules

1. Keep the packet short enough to reread quickly.
2. Prefer file paths and concrete decisions over prose.
3. Do not replace the full source of truth. The packet points back to files, screenshots, QA records, and subagent outputs.
4. Record uncertainty explicitly; do not hide missing evidence.
5. Update the packet after major edits, after subagent results, before QA freeze, and before user验收.
