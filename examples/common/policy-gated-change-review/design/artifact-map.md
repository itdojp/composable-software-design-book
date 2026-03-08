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
- `verification/review-checks.md`
- `verification/traceability-matrix.md`
- `verification/coherence-failure.md`
- `runtime/runtime-view.md`
- `review/reviewer-view.md`
- `implementation/workflow.md`

## Design Intent

The map keeps the example small enough to audit manually.
It also mirrors the specification to implementation path used in Chapter 10.
`Approved Change` remains the single canonical approval artifact for this example, so no separate approval-record file is introduced at this stage.
`runtime/runtime-view.md` is the lightweight runtime proxy introduced for Chapter 04 model translation work.
`review/reviewer-view.md` is the reviewer-facing projection introduced for Chapter 05 view-change work.
`design/variation-paths.md` is the design artifact introduced for Chapter 06 combination and variation work.
`verification/coherence-failure.md` is the reusable negative artifact introduced after Chapter 06 to keep later failure discussions anchored to one canonical example.
