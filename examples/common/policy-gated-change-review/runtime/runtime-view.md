---
title: "Example Runtime: Runtime View"
description: "Runtime-level representation of the running example."
---

# Example Runtime: Runtime View

This runtime view translates the running example into execution-time states, control points, and evidence obligations.
It keeps the approval claim visible while making the operational handoffs explicit.

## Runtime Objects

- Pending Request
- Planned Review
- Policy-Evaluated Plan
- Execution-Ready Change

## Runtime Transitions

- `classify-request`: Pending Request -> Planned Review
- `evaluate-policy`: Planned Review -> Policy-Evaluated Plan
- `request-human-approval`: Policy-Evaluated Plan -> Execution-Ready Change

## Operational Invariants

- No `Execution-Ready Change` exists without both a satisfied policy result and human approval.
- Every runtime transition can be traced back to the canonical specification, design, and verification artifacts.

## Relationship To Other Views

This runtime view refines `design/commutative-diagram.md` and `implementation/workflow.md`.
It preserves the same approval meaning while expressing it in execution-time terms.
