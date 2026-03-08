---
title: "Minimal Example: Policy-Gated Change Review"
description: "A minimal object-morphism-diagram example for the book."
---

# Minimal Example: Policy-Gated Change Review

This minimal example introduces the smallest useful slice of the running example.
It can be read in a few minutes and gives the reader one object-level chain, one composed morphism, and one diagram.

## Objects

- Change Request
- Review Plan
- Approved Change

## Morphisms

- `draft-review-plan`: Change Request -> Review Plan
- `human-approval`: Review Plan -> Approved Change
- `policy-gated-approval`: Change Request -> Approved Change

## Why This Example Matters

The first two morphisms compose into a single policy-gated approval path.
That small chain is enough to discuss composition, diagram reading, responsibility boundaries, and effect containment.

## Diagram

See [the minimal diagram](diagram/) for the commutative reading of the example.
