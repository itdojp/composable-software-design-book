# Claim ID Visibility Decision

## Option Comparison

| Option | Reader readability | Review traceability | Caption clutter | Chapter portability | Long-term maintainability |
| --- | --- | --- | --- | --- | --- |
| A. Matrix only | Strong | Weak | Strong | Medium | Medium |
| B. Caption and chapter callout only | Strong | Strong | Medium | Strong | Strong |
| C. Chapter callout only | Strong | Medium | Strong | Medium | Medium |

## Decision

Adopt Option B.
Expose claim IDs only in diagram captions and chapter-level review callouts when the ID already exists in `verification/traceability-matrix.md`.
Do not place claim IDs in ordinary body paragraphs, diagram node labels, or glossary prose.

## Decision Rationale

- Option B gives readers one visible anchor near the figure without turning the chapter into an ID catalog.
- Review conversations can cite one figure-local identifier and still reach the traceability matrix quickly.
- Caption clutter stays bounded because only canonical matrix-backed claims may surface.
- Portability improves because a figure excerpt retains its claim anchor even outside the full chapter context.
- The rule is simple enough to keep stable across later chapters and future example growth.
