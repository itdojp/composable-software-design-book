# Non-Natural Counterexample Decision

## Option Comparison

| Option | Reuse across chapters | Reader overhead before Chapter 07 | Running example consistency | Maintenance cost |
| --- | --- | --- | --- | --- |
| Prose-only | Weak | Strong | Medium | Strong |
| Reusable artifact | Strong | Medium | Strong | Medium |
| Appendix-only reusable artifact | Medium | Medium | Weak | Medium |

## Decision

Adopt the reusable artifact option.
Keep one lightweight repository-level counterexample in the common running example so later chapters can point to the same failed claim.
Do not multiply negative artifacts unless a later chapter needs a distinct failure mode.

## Canonical Location

The canonical location is `examples/common/policy-gated-change-review/verification/coherence-failure.md`.

## Decision Rationale

- One reusable artifact is enough to stabilize the negative case without changing the book's main example.
- The verification area is the least disruptive home because the artifact is used to challenge review claims, not to replace the main design.
- The artifact reuses the existing variation-path structure instead of inventing a second negative example family.
- Later chapters can cite one stable failure case for broken commutativity, non-natural view changes, and unsafe migration claims.
