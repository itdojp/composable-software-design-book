---
title: "Example Spec: Problem Statement"
description: "Problem framing for the running example."
---

# Example Spec: Problem Statement

The system must process repository change requests that may be partially prepared by an AI agent.
The process must remain auditable, reviewable, and reversible.

## Core Constraint

No change reaches execution without a human approval step.
Every transition must leave enough evidence for later review.

## System Boundary

The example starts when a change request enters the review flow.
The example ends when the approved change is ready for implementation execution.
