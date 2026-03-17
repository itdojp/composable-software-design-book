# Figure Program

## Purpose

This document defines the publication-grade figure system for the manuscript.
Compact Mermaid figures may still appear where a lightweight inline sketch is enough.
The main reader-facing argument figures use the publication assets under `assets/figures/publication/` for screen and print reuse.

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
| Introduction governed path | Figure 0.1 | `src/chapter-introduction/index.md` | `introduction-governed-path-*` |
| Responsibility boundaries | Figure 1.1 | `src/chapter-chapter01/index.md` | `responsibility-boundaries-*` |
| Minimal object composition baseline | Figure 2.1 | `src/chapter-chapter02/index.md` | `object-composition-*` |
| Minimal approval commutativity | Figure 3.1 | `src/chapter-chapter03/index.md` | `minimal-approval-commutativity-*` |
| Commutative approval claim | Figure 3.2 | `examples/common/policy-gated-change-review/design/commutative-diagram.md` | `commutative-approval-*` |
| Design-to-runtime translation | Figure 4.1 | `src/chapter-chapter04/index.md` | `design-runtime-translation-*` |
| Reviewer-facing naturality | Figure 5.1 | `src/chapter-chapter05/index.md` | `reviewer-naturality-*` |
| Product-like review context | Figure 6.1 | `src/chapter-chapter06/index.md` | `review-context-product-*` |
| Variation paths | Figure 6.2 | `examples/common/policy-gated-change-review/design/variation-paths.md` | `variation-paths-*` |
| Shared-boundary join | Figure 7.1 | `src/chapter-chapter07/index.md` | `shared-boundary-join-*` |
| Replacement gateway | Figure 7.2 | `src/chapter-chapter07/index.md` | `replacement-gateway-*` |
| Orchestration fan-out | Figure 8.1 | `examples/common/policy-gated-change-review/implementation/orchestration-diagram.md` | `orchestration-diagram-*` |
| String-diagram fan-in contrast | Figure 8.2 | `src/chapter-chapter08/index.md` | `string-diagram-fan-in-*` |
| Synchronization boundary | Chapter 08 table and prose | `examples/common/policy-gated-change-review/implementation/synchronization-boundary.md` | `synchronization-boundary-*` |
| Effect boundary | Figure 9.1 | `examples/common/policy-gated-change-review/implementation/effect-boundary.md` | `effect-boundary-*` |
| Pure core and effectful shell | Figure 9.2 | `src/chapter-chapter09/index.md` | `pure-core-effectful-shell-*` |
| Case-study delivery path | Figure 10.1 | `src/chapter-chapter10/index.md` | `delivery-case-study-*` |

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
