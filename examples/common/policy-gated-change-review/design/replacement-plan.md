---
title: "Example Design: Replacement Plan"
description: "Controlled replacement of a route-selection component in the running example."
---

# Example Design: Replacement Plan

This artifact defines a controlled replacement of one route-selection component without changing approval meaning.
It exists so Chapter 07 can discuss pushouts as migration structures rather than as ad hoc cutovers.

## Components

- Legacy Route Mapper
- Replacement Mapper
- Review Boundary Contract
- Unified Review Gateway

The Replacement Mapper is the candidate new route-selection implementation.
The Unified Review Gateway is the downstream facade that receives both legacy and replacement mappings after they agree on the Review Boundary Contract.

## Shared Interface

- Inputs: Change Identity, Repository Scope, Policy Classification
- Outputs: Approval Route ID, policy provenance, migration note

## Schema Mapping

- `legacy_change_key` -> Change Identity
- `legacy_scope_bucket` -> Repository Scope
- `legacy_policy_status` -> Policy Classification
- `legacy_route_hint` -> Approval Route ID

## Migration Steps

1. Run the Legacy Route Mapper and Replacement Mapper in shadow mode on the same change set.
2. Compare `Approval Route ID` and policy provenance under the shared interface.
3. Map both outputs into the Unified Review Gateway only when their composites from the Review Boundary Contract agree.
4. Cut over only when the replacement path preserves the same approval meaning and route obligations.
5. Keep transformation lineage for every divergence found during the overlap period.

## Pushout Reading

The Review Boundary Contract maps into both the Legacy Route Mapper and Replacement Mapper, and both map into the Unified Review Gateway.
The migration therefore uses the gateway as a pushout-shaped cocone over the common-source span rather than performing a blind swap.
The replacement is acceptable only if downstream artifacts can continue to consume the same boundary while the old component is retired.

## Failure Conditions

- The new gateway collapses `Standard Review Path` and `Escalated Review Path` into one opaque status.
- The new gateway emits route labels that the reviewer and runtime views cannot compare.
- The migration loses the provenance needed to explain why one route decision replaced another.

## Relationship To Other Artifacts

This artifact depends on `design/shared-boundary.md` and `design/variation-paths.md`.
It complements `verification/coherence-failure.md` by showing the controlled replacement path that avoids the failure case.
