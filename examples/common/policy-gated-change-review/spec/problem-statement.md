---
title: "Example Spec: Problem Statement"
description: "Problem framing for the running example."
---

# Example Spec: Problem Statement

The system must process repository change requests that may be partially prepared by an AI agent.
The process must remain auditable, reviewable, and reversible.

## Core Constraint

No change reaches execution without a human approval step.
Parallel branches may prepare policy and evidence in advance, but they may not bypass the human review gate.
Every effectful transition must leave enough trace and evidence for later review.

## System Boundary

The example starts when a change request enters the review flow.
The example ends when the approved change is executed or returned for rework with preserved evidence.

## Explicit Non-Goals

- Autonomous approval without a named human review decision.
- Opaque tool chaining that cannot be reconstructed from repository artifacts.
- General-purpose multi-repository release orchestration beyond the bounded change-review flow.
