---
title: "Example Implementation: Execution Trace"
description: "Minimum execution trace schema for the running example."
---

# Example Implementation: Execution Trace

This artifact records the minimum execution trace that the running example expects after planning, review, and dispatch.
It exists so Chapters 09 and 10 can discuss auditability with one canonical trace shape.

## Trace Fields

- Trace ID
- Change Identity
- Plan Revision
- Step ID
- Effect Class
- Input Artifact
- Output Artifact
- Actor Or Tool
- Timestamp
- Evidence Link

## Representative Trace

| Step ID | Input artifact | Effect class | Output artifact | Actor or tool | Evidence link |
| --- | --- | --- | --- | --- | --- |
| `scope-and-bound` | Change Request | Pure classification | Review Plan | Review orchestrator | Plan revision note |
| `draft-plan-with-agent` | Review Plan inputs | Prompt + model invocation | Review Plan | AI agent runtime | Plan revision note |
| `evaluate-policy` | Review Plan | Tool call + repository read | Policy-Evaluated Plan | Policy engine | Policy evaluation record |
| `collect-evidence-links` | Review Plan | Repository read + I/O | Evidence Bundle | Evidence collector | Evidence bundle |
| `synchronize-for-review` | Policy-Evaluated Plan + Evidence Bundle | Synchronization | Decision Packet | Review orchestrator | Synchronization boundary check |
| `record-review-decision` | Decision Packet | Human approval + audit write | Approved Change | Assigned reviewer | Approval decision record |
| `dispatch-execution` | Approved Change | External tool + state change | Executable Change Set | Implementation executor | Execution report |

## Trace Rules

- Successful and return-for-rework paths use the same trace fields so later review can compare them directly.
- Every synchronized path must keep one `Change Identity` and one `Plan Revision` until a rework decision creates a new revision.
- Retry creates a new trace entry instead of mutating a previous one in place.
- Acceptance evidence must reference the trace entries that justify approval and dispatch.

## Relationship To Other Artifacts

This trace refines `implementation/workflow.md` and `implementation/effect-boundary.md`.
It aligns with `verification/acceptance-evidence.md` when the evidence bundle points back to the same `Approved Change` or named rework outcome.
