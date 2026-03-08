---
title: "Example Implementation: Workflow"
description: "Implementation-oriented workflow for the running example."
---

# Example Implementation: Workflow

This workflow shows how the running example crosses from specification into controlled implementation work.

## Workflow Steps

1. Receive the change request and classify the requested scope.
2. Ask the AI agent to draft a bounded review plan.
3. Run policy evaluation and evidence collection in parallel against the same plan revision.
4. Synchronize those branch outputs into one reviewer-facing `Decision Packet`.
5. Route the packet to the standard or escalated human review path according to the recorded risk boundary.
6. Execute implementation only after the approved artifact set is complete and the effect boundary permits dispatch.
7. Record execution trace entries and acceptance evidence for the executed or returned change.

## Implementation Boundary

The AI agent may propose a review plan, but it cannot approve the change.
The workflow therefore preserves a clear human responsibility boundary.
Escalation changes the route to review, but it does not remove the mandatory human approval step.
Parallelism is allowed only between named branches that still synchronize before `Decision Packet`, `Approved Change`, or execution dispatch exists.
Effectful steps remain explicit through `implementation/effect-boundary.md` and `implementation/execution-trace.md`.
