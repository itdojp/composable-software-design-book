---
title: "Example Implementation: Workflow"
description: "Implementation-oriented workflow for the running example."
---

# Example Implementation: Workflow

This workflow shows how the running example crosses from specification into controlled implementation work.

## Workflow Steps

1. Receive the change request and classify the requested scope.
2. Ask the AI agent to draft a bounded review plan.
3. Run policy checks against the plan and the requested change.
4. Route the plan to a human reviewer for approval or rejection.
5. Execute implementation only after the approved artifact set is complete.

## Implementation Boundary

The AI agent may propose a review plan, but it cannot approve the change.
The workflow therefore preserves a clear human responsibility boundary.
