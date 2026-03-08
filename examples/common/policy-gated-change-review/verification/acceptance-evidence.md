---
title: "Example Verification: Acceptance Evidence"
description: "Acceptance evidence bundle for the running example."
---

# Example Verification: Acceptance Evidence

This artifact defines the minimum evidence bundle required to accept a change in the running example.
It keeps Chapter 10 grounded in repository evidence rather than retrospective narration.

## Required Evidence

| Evidence item | Why it is required |
| --- | --- |
| `spec/problem-statement.md` and `spec/acceptance-criteria.md` | Proves the accepted result still matches the stated problem and acceptance conditions. |
| `design/commutative-diagram.md` and `design/artifact-map.md` | Proves the accepted result follows the canonical artifact path. |
| `verification/review-checks.md` and `verification/traceability-matrix.md` | Proves the core claims were reviewed and can be traced across artifacts. |
| `Approved Change` | Proves human approval occurred on the named artifact boundary. |
| `implementation/execution-trace.md` | Proves effectful execution followed the governed path. |
| Execution result or return-for-rework note | Proves the workflow ended in a named operational outcome. |

## Acceptance Rule

An accepted change exists only when the evidence bundle points to one `Change Identity`, one accepted `Plan Revision`, and one `Approved Change` or named return outcome.
If those references disagree, the change is not accepted even if some individual artifacts look complete.

## Return-For-Rework Rule

A return-for-rework decision is still a governed outcome and must keep the same evidence shape.
The workflow may discard stale implementation outputs, but it may not discard the trace, policy result, or reviewer reason that caused the return.

## Claim Coverage

| Claim ID | Evidence reference | Trace step |
| --- | --- | --- |
| PGCR-02 | `design/artifact-map.md`, `verification/traceability-matrix.md` | `scope-and-bound` |
| PGCR-02 | `verification/review-checks.md`, `verification/traceability-matrix.md` | `draft-plan-with-agent` |
| PGCR-03 | `design/commutative-diagram.md`, `verification/review-checks.md` | `record-review-decision` |
| PGCR-05 | `implementation/effect-boundary.md`, `verification/review-checks.md` | `evaluate-policy` |
| PGCR-04 | `implementation/synchronization-boundary.md`, `verification/review-checks.md` | `collect-evidence-links` |
| PGCR-04 | `implementation/synchronization-boundary.md`, `verification/traceability-matrix.md` | `synchronize-for-review` |
| PGCR-01 | `Approved Change`, `verification/review-checks.md` | `record-review-decision` |
| PGCR-06 | `implementation/execution-trace.md`, `verification/acceptance-evidence.md` | `dispatch-execution` |

## Relationship To Other Artifacts

This artifact depends on `verification/review-checks.md`, `verification/traceability-matrix.md`, `implementation/effect-boundary.md`, and `implementation/execution-trace.md`.
It closes the specification-to-implementation path used in Chapter 10.
