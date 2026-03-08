# Variation Artifact Decision

## Option Comparison

| Option | Conceptual clarity | Reuse across chapters | Artifact sprawl risk | Explanatory value for products and coproducts | Maintenance cost |
| --- | --- | --- | --- | --- | --- |
| A. Chapter-local only | Medium | Weak | Strong | Weak | Strong |
| B. Reusable running example artifact | Strong | Strong | Medium | Strong | Medium |
| C. Appendix-style artifact only | Medium | Medium | Medium | Medium | Medium |

## Decision

Adopt Option B.
Keep one reusable variation artifact in the common running example and anchor the Chapter 06 discussion to that repository artifact.
Do not introduce a separate variation phase or a second approval artifact.

## Canonical Location And Naming

- Canonical location: `examples/common/policy-gated-change-review/design/variation-paths.md`
- Canonical artifact name: `Variation Paths`
- Intended use: Chapter 06 explanation of combined review context, alternate review routes, and later route-sensitive discussions

## Decision Rationale

- One reusable artifact gives Chapter 06 a stable repository anchor instead of a chapter-local construction.
- Keeping the artifact under `design/` avoids creating a parallel directory structure for one concept.
- The artifact is small enough to avoid example sprawl while still being reusable in later chapters.
- The naming stays concrete for software readers and still matches the products/coproducts discussion.
