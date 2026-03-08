---
title: "Example Verification: Review Checks"
description: "Verification hooks for the running example."
---

# Example Verification: Review Checks

The running example uses a small review checklist to keep its claims testable.
It remains the concise review artifact even when the example also uses a lightweight traceability matrix.

## Verification Checks

- The artifact set is complete across specification, design, runtime, review, implementation, and verification.
- The human approval gate and the synchronization boundary are explicit.
- Parallel branches refer to the same `Change Identity` and `Plan Revision` before `Decision Packet` or `Approved Change` exists.
- Effectful steps are named separately from pure reasoning and each emits trace evidence.
- The diagram labels match the canonical terms in the prose.
- The implementation workflow references the same artifact names as the review and verification artifacts.
- The traceability matrix and acceptance evidence point each core claim back to specification, design, and implementation evidence.
