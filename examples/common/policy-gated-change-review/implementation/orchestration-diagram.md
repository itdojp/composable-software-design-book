---
title: "Example Implementation: Orchestration Diagram"
description: "Sequential and parallel composition for the running example."
---

# Example Implementation: Orchestration Diagram

This artifact makes the running example's sequential and parallel composition explicit.
It exists so Chapters 08 through 10 can discuss orchestration with canonical repository artifacts instead of chapter-local pseudo workflows.

## Sequential Spine

The workflow has one mandatory spine that every change follows.
The spine preserves the approval meaning introduced in earlier chapters.

- Change Request
- Review Plan
- Decision Packet
- Approved Change
- Executable Change Set

## Sequential Morphisms

- `scope-and-bound`: Change Request -> Review Plan
- `synchronize-for-review`: Review Plan -> Decision Packet
- `approve-or-return`: Decision Packet -> Approved Change
- `dispatch-execution`: Approved Change -> Executable Change Set

## Parallel Branches

Two branches may run in parallel once one `Review Plan` revision exists.

| Branch | Purpose | Output artifact |
| --- | --- | --- |
| Policy branch | Evaluate repository policy, risk class, and required route. | Policy-Evaluated Plan |
| Evidence branch | Collect diff summaries, referenced checks, and evidence links. | Evidence Bundle |

The branches are allowed to run concurrently because neither branch may create `Approved Change` on its own.
They are still bound to the same `Change Identity` and `Plan Revision`.

## Fan-In Rule

The fan-in point is the `Decision Packet`.
`Decision Packet` may exist only when the outputs of the policy branch and the evidence branch satisfy the [synchronization boundary](synchronization-boundary.md).
This keeps reviewer input explicit instead of letting one faster branch stand in for the other.

## Failure And Fallback Paths

- Policy evaluation failure routes the workflow to manual review or rework, and it never degrades into an implicit pass.
- Evidence collection failure blocks fan-in until the missing evidence is supplied or the change is returned for rework.
- A new `Plan Revision` invalidates stale branch outputs and requires the fan-out to run again.

## Relationship To Other Artifacts

This artifact refines `implementation/workflow.md` by making sequential and parallel composition visible.
It aligns with `review/reviewer-view.md`, `runtime/runtime-view.md`, and `verification/traceability-matrix.md` when those artifacts preserve the same approval semantics.
