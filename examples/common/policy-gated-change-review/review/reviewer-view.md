---
title: "Example Review: Reviewer View"
description: "Reviewer-facing representation of the running example."
---

# Example Review: Reviewer View

This reviewer view presents the running example as a decision packet for a human reviewer.
It suppresses operational detail that the reviewer does not need while preserving the approval meaning that the design and runtime views must still respect.

## Reviewer Objects

- Review Intake
- Decision Packet
- Review Outcome

## Reviewer Morphisms

- `summarize-for-review`: Review Intake -> Decision Packet
- `compare-policy-and-scope`: Decision Packet -> Decision Packet
- `approve-or-return`: Decision Packet -> Review Outcome

## Reviewer Invariants

- The reviewer can see the requested scope, policy status, and required evidence before deciding.
- The reviewer view preserves the distinction between policy evaluation and human judgment.
- A positive `Review Outcome` must correspond to the canonical `Approved Change` state.

## Relationship To Other Views

This reviewer view projects `design/commutative-diagram.md` into a human decision perspective.
It aligns with `runtime/runtime-view.md` by preserving the same approval meaning under different labels and omitted detail.
