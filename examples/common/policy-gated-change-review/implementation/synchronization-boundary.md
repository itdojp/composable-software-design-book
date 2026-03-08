---
title: "Example Implementation: Synchronization Boundary"
description: "Fan-in contract for the running example's concurrent branches."
---

# Example Implementation: Synchronization Boundary

This artifact defines the named fan-in contract that parallel branches must satisfy before review or execution may continue.
It exists so Chapter 08 can discuss coordination cost and failure isolation with one canonical boundary.

## Boundary Elements

- Change Identity
- Plan Revision
- Repository Scope
- Policy Classification
- Evidence Link Set
- Approval Route ID

## Synchronization Rules

- Policy and evidence branches must refer to the same `Change Identity` and `Plan Revision`.
- `Repository Scope` may narrow during analysis, but it may not silently widen after the `Review Plan` revision is fixed.
- `Policy Classification` and `Approval Route ID` must agree with `design/variation-paths.md` and `design/shared-boundary.md`.
- `Evidence Link Set` must contain the references that the reviewer view and acceptance criteria expect for the selected route.
- `Decision Packet` and later artifacts may not be emitted from a partial boundary.

## Failure Isolation Rules

- A missing policy result blocks synchronization and creates a named rework or manual review outcome.
- Missing evidence blocks human approval, but it does not rewrite the policy result.
- If one branch changes `Plan Revision`, every synchronized artifact derived from an older revision becomes stale.
- Retry is allowed only from the failed branch or from the synchronization point, not by bypassing the boundary.

## Engineering Reading

The synchronization boundary is the operational form of the product-like `Combined Review Context` introduced in `design/variation-paths.md`.
It is also the guard that stops parallelism from collapsing the human review gate into a race between branches.

## Relationship To Other Artifacts

This artifact complements `implementation/orchestration-diagram.md` and `implementation/workflow.md`.
It aligns with `review/reviewer-view.md` when the `Decision Packet` carries the same route, policy, and evidence meaning.
