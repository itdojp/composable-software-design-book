---
layout: book
title: "Transfer Cases Across Domains"
appendix: appendix-d
description: "Short transfer cases that map the canonical running example into other governed engineering workflows."
---

# Appendix D. Transfer Cases Across Domains

This appendix proves that the method of the book generalizes beyond repository change review.
The running example remains canonical because it is the most detailed artifact path in the manuscript.
These transfer cases are deliberately smaller.
They broaden applicability without creating rival narratives of equal size.

## How to read the transfer cases

Each caselet maps the same compositional vocabulary into a different governed workflow.
The point is not to force every domain into identical terminology.
The point is to show which invariants, boundaries, and evidence obligations survive the domain change.

Use the mapping tables as compact translation aids.
If one domain cannot support an explicit object boundary, one stable morphism chain, one core diagram claim, one effect boundary, and one approval-evidence model, the method will expose that weakness quickly.

## Transfer case 1. Deployment approval pipeline

This caselet maps the running example into a staged production deployment workflow where release automation proposes a rollout but humans retain final release authority.

| Book concept | Deployment approval pipeline |
| --- | --- |
| Core objects | `Deployment Request`, `Release Plan`, `Approved Release`, `Execution Window` |
| Core morphisms | `derive-release-plan`, `evaluate-release-policy`, `approve-release`, `dispatch-rollout` |
| Core diagram claim | The direct approval path is valid only if policy evaluation and human release review preserve the same rollout scope and risk interpretation. |
| Effect boundary | Release write, environment mutation, rollback trigger, and external incident notification. |
| Approval and evidence model | Approval is the signed `Approved Release`, while evidence includes test reports, policy results, rollout logs, and rollback records. |
| Stable invariant | No deployment reaches execution unless rollout scope, release policy, and human approval refer to the same release revision. |

This case keeps the strongest parallel with the running example.
The main transfer is from repository review semantics to release semantics.
The compositional method still cares about bounded authority, synchronized evidence, and a reconstructable path from proposed change to operational effect.

## Transfer case 2. Customer-support escalation workflow

This caselet maps the method into a support escalation path where an AI assistant can draft triage and summaries but escalation authority remains governed by human operators.

| Book concept | Customer-support escalation workflow |
| --- | --- |
| Core objects | `Support Request`, `Escalation Packet`, `Approved Escalation`, `Action Record` |
| Core morphisms | `classify-request`, `draft-escalation-packet`, `approve-escalation`, `dispatch-action` |
| Core diagram claim | The direct escalation route is acceptable only if triage classification, evidence gathering, and human escalation judgment preserve the same case identity and severity meaning. |
| Effect boundary | Customer communication, ticket-state mutation, external paging, and incident-channel writes. |
| Approval and evidence model | Approval is the operator-approved escalation packet, while evidence includes case transcript excerpts, severity rules, routing notes, and action timestamps. |
| Stable invariant | No escalation changes customer-facing state unless the case identity, severity class, and chosen action route remain aligned. |

The useful transfer here is that the object set is not code-centric.
Even so, the method still depends on stable packet boundaries, explicit route selection, and a visible difference between delegated preparation and authorized action.

## Transfer case 3. Regulated change-management review

This caselet maps the method into a regulated compliance workflow where documentation, control evidence, and formal approval must survive audit and policy review.

| Book concept | Regulated change-management review |
| --- | --- |
| Core objects | `Regulated Change Proposal`, `Control Review Packet`, `Authorized Change`, `Compliance Evidence Bundle` |
| Core morphisms | `derive-control-review`, `evaluate-control-policy`, `approve-regulated-change`, `record-compliance-evidence` |
| Core diagram claim | The authorized path is valid only when policy interpretation, control evidence, and formal sign-off preserve the same regulatory scope and control intent. |
| Effect boundary | Control-state update, audit-log write, external filing, and remediation trigger. |
| Approval and evidence model | Approval is the signed authorization record, while evidence includes control mappings, exception records, filing references, and remediation status. |
| Stable invariant | No regulated change becomes authorized unless regulatory scope, control interpretation, and approval record remain auditable as one packet. |

This case is useful because it increases the audit burden without changing the compositional core.
The workflow still needs durable objects, reviewable morphisms, one governed packet, and explicit evidence boundaries.
What changes is the surrounding control vocabulary and the lifetime of the evidence obligations.

## What remains invariant across domains

The method generalizes because the domain nouns may change while the architectural obligations stay recognizable.
Each domain still needs stable objects, explicit transformations, one named approval boundary, one effect boundary, and evidence that can be traced back to a governing claim.
That is the invariant Chapter 10 relies on when it argues that the running example is canonical but not exclusive.
