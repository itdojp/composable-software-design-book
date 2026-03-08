---
title: "Example Design: Artifact Map"
description: "Artifact locations for the running example."
---

# Example Design: Artifact Map

This artifact map defines the canonical files that support the running example.

## Artifact List

- `spec/problem-statement.md`
- `spec/acceptance-criteria.md`
- `design/commutative-diagram.md`
- `design/variation-paths.md`
- `design/shared-boundary.md`
- `design/replacement-plan.md`
- `verification/review-checks.md`
- `verification/traceability-matrix.md`
- `verification/coherence-failure.md`
- `verification/acceptance-evidence.md`
- `runtime/runtime-view.md`
- `review/reviewer-view.md`
- `implementation/workflow.md`
- `implementation/orchestration-diagram.md`
- `implementation/synchronization-boundary.md`
- `implementation/effect-boundary.md`
- `implementation/execution-trace.md`

## Design Intent

The map keeps the example small enough to audit manually.
It also mirrors the specification to implementation path used in Chapter 10.
`Approved Change` remains the single canonical approval artifact for this example, so no separate approval-record file is introduced at this stage.
`Approved Change` records the decision outcome only.
It is not the execution-evidence artifact for the workflow.
Execution evidence belongs in `implementation/execution-trace.md` and `verification/acceptance-evidence.md`.
The `approval decision record` is emitted evidence attached to the `record-review-decision` step rather than a second canonical artifact.
`runtime/runtime-view.md` is the lightweight runtime proxy introduced for Chapter 04 model translation work.
`review/reviewer-view.md` is the reviewer-facing projection introduced for Chapter 05 view-change work.
`design/variation-paths.md` is the design artifact introduced for Chapter 06 combination and variation work.
`design/shared-boundary.md` and `design/replacement-plan.md` are the integration and migration artifacts introduced for Chapter 07.
`verification/coherence-failure.md` is the reusable negative artifact introduced after Chapter 06 to keep later failure discussions anchored to one canonical example.
`implementation/orchestration-diagram.md` and `implementation/synchronization-boundary.md` are the coordination artifacts introduced for Chapter 08.
`implementation/effect-boundary.md` and `implementation/execution-trace.md` are the effect and audit artifacts introduced for Chapter 09.
`verification/acceptance-evidence.md` is the end-to-end evidence artifact introduced for Chapter 10.
