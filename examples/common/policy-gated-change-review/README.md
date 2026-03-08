---
title: "Running Example: Policy-Gated Change Review"
description: "The common example reused across the book."
---

# Running Example: Policy-Gated Change Review

This common example follows one repository change request from specification through implementation.
It is the canonical example reused across the book.

## Example Scope

The system accepts a change request, derives an AI-assisted review plan, fans out policy and evidence work from one bounded plan, synchronizes a reviewer packet, and requires human approval before execution.
It records execution trace entries and acceptance evidence so the same change can be reconstructed after delivery or return-for-rework.
`Approved Change` is the decision outcome artifact for that flow.
The `approval decision record`, the broader `audit log`, the `execution trace`, and the final `acceptance evidence` are emitted evidence layers around that outcome rather than parallel approval artifacts.
The artifact set is intentionally small enough to trace by hand.

## Artifact Phases

- [Specification](spec/problem-statement/)
- [Acceptance criteria](spec/acceptance-criteria/)
- [Design artifact map](design/artifact-map/)
- [Design commutative diagram](design/commutative-diagram/)
- [Design variation paths](design/variation-paths/)
- [Design shared boundary](design/shared-boundary/)
- [Design replacement plan](design/replacement-plan/)
- [Verification checks](verification/review-checks/)
- [Verification traceability matrix](verification/traceability-matrix/)
- [Verification coherence failure](verification/coherence-failure/)
- [Verification acceptance evidence](verification/acceptance-evidence/)
- [Runtime view](runtime/runtime-view/)
- [Reviewer view](review/reviewer-view/)
- [Implementation workflow](implementation/workflow/)
- [Implementation orchestration diagram](implementation/orchestration-diagram/)
- [Implementation synchronization boundary](implementation/synchronization-boundary/)
- [Implementation effect boundary](implementation/effect-boundary/)
- [Implementation execution trace](implementation/execution-trace/)

## Why This Example Was Chosen

It connects human responsibility, design artifacts, diagrams, verification evidence, and AI-assisted implementation in one flow.
That makes it suitable for reuse from Chapter 01 through Chapter 10.
`Approved Change` remains the single canonical approval artifact for the current manuscript scope.
The evidence model stays compact because approval evidence is emitted into the trace and acceptance bundle rather than expanded into a second canonical approval file.
