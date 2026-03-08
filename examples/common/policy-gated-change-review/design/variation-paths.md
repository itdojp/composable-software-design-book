---
title: "Example Design: Variation Paths"
description: "Product-like combination and coproduct-like review routes for the running example."
---

# Example Design: Variation Paths

This artifact makes the running example's combination and variation rules explicit.
It supports Chapter 06 without introducing a second canonical approval artifact.

## Product-Like Review Context

The workflow needs several independently meaningful inputs at the same time before human approval can complete.
The product-like object is `Combined Review Context`.
It is the smallest shared context that preserves the information required for review.

### Component Objects

- Requested Scope
- Policy Result
- Evidence Links

### Canonical Projections

- `scope-of`: Combined Review Context -> Requested Scope
- `policy-status-of`: Combined Review Context -> Policy Result
- `evidence-links-of`: Combined Review Context -> Evidence Links

### Engineering Reading

The [reviewer view](../review/reviewer-view.md) renders this context as a `Decision Packet`.
The construction stays product-like only while each downstream check can recover the same three components without hidden global state.

## Coproduct-Like Review Routes

The workflow supports more than one explicit review route before approval completion.
The coproduct-like object is `Review Route`.
It makes route selection explicit while keeping `Approved Change` as the single canonical approval artifact.

### Variant Objects

- Standard Review Path
- Escalated Review Path

### Canonical Entries

- `enter-standard`: Standard Review Path -> Review Route
- `enter-escalated`: Escalated Review Path -> Review Route

### Routing Rules

- Standard Review Path applies when the change stays within the default repository boundary and policy status is satisfied without exceptions.
- Escalated Review Path applies when protected files, elevated operational risk, or policy exceptions require added scrutiny.
- Both routes still require explicit human approval before `Approved Change` exists.

## Relationship To Other Artifacts

This artifact complements `commutative-diagram.md` by separating combination from variation.
It aligns with `review/reviewer-view.md`, `runtime/runtime-view.md`, and `implementation/workflow.md` when those artifacts preserve the same route boundary and approval meaning.
