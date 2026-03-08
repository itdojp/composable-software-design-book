# Figure Program

## Purpose

This document defines the publication-grade figure system for the manuscript.
The repository-native Mermaid diagrams remain the chapter-local explanatory source, while the publication assets under `assets/figures/publication/` provide the polished screen and print variants.

## Visual system

| Element | Screen treatment | Print treatment | Meaning |
| --- | --- | --- | --- |
| Object or state | Slate outline with pale blue fill | Dark gray outline with light gray fill | Stable artifact, interface, or workflow state |
| Decision or governed state | Blue outline with pale blue-gray fill | Black outline with medium gray fill | A boundary that changes authority or governance state |
| Evidence artifact | Green outline with pale green fill | Dark gray outline with very light gray fill | Trace, evidence, or verification support |
| Boundary box | Dashed outline | Dashed outline | Shared boundary, synchronization contract, or integration seam |
| Effect zone | Warm neutral background band | Light gray background band | Steps that cross a side-effect boundary |
| Arrow label | Inline text above the edge | Inline text above the edge | Named transformation or relation |

## Core figure inventory

| Figure family | Canonical manuscript anchor | Source artifact | Publication assets |
| --- | --- | --- | --- |
| Commutative approval claim | Figure 3.2 | `examples/common/policy-gated-change-review/design/commutative-diagram.md` | `commutative-approval-*` |
| Variation paths | Figure 6.2 | `examples/common/policy-gated-change-review/design/variation-paths.md` | `variation-paths-*` |
| Orchestration fan-out | Figure 8.1 | `examples/common/policy-gated-change-review/implementation/orchestration-diagram.md` | `orchestration-diagram-*` |
| Synchronization boundary | Chapter 08 table and prose | `examples/common/policy-gated-change-review/implementation/synchronization-boundary.md` | `synchronization-boundary-*` |
| Effect boundary | Figure 9.1 | `examples/common/policy-gated-change-review/implementation/effect-boundary.md` | `effect-boundary-*` |

## Asset policy

- `*-screen.svg` is the ebook-safe and web-safe asset.
- `*-print.svg` is the grayscale-safe vector asset.
- `*-print.pdf` is the print-distribution fallback asset generated from the same canonical drawing spec.
- Do not hand-edit generated assets.
- Regenerate assets by running `npm run figures:render` or `python3 scripts/render-publication-figures.py`.

## Caption policy

- Keep the chapter caption as the primary reader-facing claim.
- Use the publication asset filename only in figure lists or editorial notes.
- When a figure is tied to a repository artifact, name that artifact in the list-of-figures backmatter rather than in every chapter caption.
