---
title: "Example Design: Replacement Plan"
description: "Controlled replacement of a route-selection component in the running example."
---

# Example Design: Replacement Plan

This artifact defines a controlled replacement of one route-selection component without changing approval meaning.
It exists so Chapter 07 can discuss pushouts as migration structures rather than as ad hoc cutovers.

## Components

- Legacy Route Mapper
- Review Boundary Contract
- Unified Review Gateway

## Shared Interface

- Inputs: Change Identity, Repository Scope, Policy Classification
- Outputs: Approval Route ID, policy provenance, migration note

## Schema Mapping

- `legacy_change_key` -> Change Identity
- `legacy_scope_bucket` -> Repository Scope
- `legacy_policy_status` -> Policy Classification
- `legacy_route_hint` -> Approval Route ID

## Migration Steps

1. Run the Legacy Route Mapper and Unified Review Gateway in shadow mode on the same change set.
2. Compare `Approval Route ID` and policy provenance under the shared interface.
3. Cut over only when the new gateway preserves the same approval meaning and route obligations.
4. Keep transformation lineage for every divergence found during the overlap period.

## Pushout Reading

The migration merges the legacy and replacement components along the shared review boundary rather than through a blind swap.
The replacement is acceptable only if downstream artifacts can continue to consume the same boundary while the old component is retired.

## Failure Conditions

- The new gateway collapses `Standard Review Path` and `Escalated Review Path` into one opaque status.
- The new gateway emits route labels that the reviewer and runtime views cannot compare.
- The migration loses the provenance needed to explain why one route decision replaced another.

## Relationship To Other Artifacts

This artifact depends on `design/shared-boundary.md` and `design/variation-paths.md`.
It complements `verification/coherence-failure.md` by showing the controlled replacement path that avoids the failure case.
