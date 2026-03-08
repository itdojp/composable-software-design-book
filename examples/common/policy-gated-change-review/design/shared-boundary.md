---
title: "Example Design: Shared Boundary"
description: "Canonical keys, policy labels, and route identifiers for constrained joins in the running example."
---

# Example Design: Shared Boundary

This artifact defines the smallest shared boundary that the running example uses for integration work.
It keeps joins explicit before reviewer, runtime, verification, and migration artifacts are combined.

## Boundary Objects

- Change Identity
- Repository Scope
- Policy Classification
- Approval Route ID

## Boundary Mappings

- `identify-change`: Change Request -> Change Identity
- `scope-request`: Change Request -> Repository Scope
- `classify-policy`: Policy Check -> Policy Classification
- `select-route`: Review Plan -> Approval Route ID

## Boundary Rules

- An integrated artifact set is valid only when `Change Identity` and `Repository Scope` refer to the same proposed change.
- `Policy Classification` must preserve the distinction between satisfied, exception-required, and rejected outcomes.
- `Approval Route ID` must agree with `design/variation-paths.md` and the runtime route chosen for the same change.

## Pullback Reading

The reviewer-facing packet and the runtime policy state can be joined only when they agree on this shared boundary.
If either side uses a different route label or policy vocabulary, the constrained join should fail rather than silently coerce the mismatch.

## Relationship To Other Artifacts

This artifact complements `design/variation-paths.md` by naming the keys and policy labels that route variation still has to preserve.
It aligns with `runtime/runtime-view.md`, `review/reviewer-view.md`, and `verification/traceability-matrix.md` when those artifacts refer to the same change and route.
