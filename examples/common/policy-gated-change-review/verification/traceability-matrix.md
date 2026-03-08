---
title: "Example Verification: Traceability Matrix"
description: "Lightweight cross-artifact traceability for the running example."
---

# Example Verification: Traceability Matrix

This lightweight matrix links the running example's core claims across specification, design, verification, and implementation.
It complements `verification/review-checks.md` rather than replacing it.

## Traceability Matrix

| Claim ID | Specification source | Design source | Verification source | Implementation source |
| --- | --- | --- | --- | --- |
| PGCR-01 | `spec/problem-statement.md#core-constraint` | `design/commutative-diagram.md` | `verification/review-checks.md` | `implementation/workflow.md#workflow-steps` |
| PGCR-02 | `spec/acceptance-criteria.md#acceptance-criteria` | `design/artifact-map.md#artifact-list` | `verification/review-checks.md` | `implementation/workflow.md#implementation-boundary` |
| PGCR-03 | `spec/acceptance-criteria.md#acceptance-criteria` | `design/commutative-diagram.md` | `verification/review-checks.md` | `implementation/workflow.md#workflow-steps` |

## Usage Notes

Use this matrix when Chapter 03 needs to connect diagram claims back to named repository artifacts.
Expose a claim ID to readers only in a figure caption or chapter-level review callout when the surrounding chapter truly needs the traceability anchor.
Keep `verification/review-checks.md` as the short review-facing checklist.
