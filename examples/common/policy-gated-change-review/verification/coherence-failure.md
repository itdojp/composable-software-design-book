---
title: "Example Verification: Coherence Failure"
description: "Reusable counterexample where route variation breaks the claimed approval meaning."
---

# Example Verification: Coherence Failure

This artifact records one reusable failure case for the running example.
It exists so later chapters can cite one concrete negative example instead of restating the same broken claim in chapter-local prose.

## Failure Scenario

An escalated review route omits the current `Policy Result` from the reviewer-facing packet.
The runtime path still allows an execution-ready transition after a policy exception is manually waived.

## Broken Correspondences

- The reviewer view no longer preserves the distinction between policy evaluation and human judgment.
- The product-like `Combined Review Context` no longer exposes all three required components for approval.
- The coproduct-like `Review Route` still converges on `Approved Change`, but it reaches that state without the original approval meaning.

## Review Consequence

This route change is not natural with respect to the design, reviewer, and runtime views.
It should be reviewed as a coherence failure rather than a presentation-only refactor.

## Reuse Notes

Use this artifact when later chapters need one repository-level counterexample for broken commutativity, unstable shared boundaries, or unsafe replacement claims.
Do not introduce another negative artifact unless a later chapter needs a distinct failure mode that this artifact cannot express.
