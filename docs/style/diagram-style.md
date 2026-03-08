# Diagram Style Guide

## Scope

This guide standardizes the visual and editorial rules for commutative diagrams, string diagrams, and architecture diagrams.
Use it together with `docs/style/notation.md`.

## Shared Rules

- Every diagram must answer one review question or support one explicit claim.
- Every diagram must use canonical labels from the glossary and term base.
- Every diagram must be referenced in the surrounding prose before the reader encounters it.
- Every diagram caption must state why the diagram exists, not just what it contains.

## Commutative Diagrams

- Use commutative diagrams when multiple paths are claimed to preserve the same meaning.
- Label arrows with transformation names rather than implementation detail.
- State the preserved invariant in the prose directly before or after the figure.
- If the diagram is only illustrative and not a proof obligation, say so explicitly.

## String Diagrams

- Use string diagrams for sequential and parallel composition, orchestration, or workflow reasoning.
- Keep the direction of flow consistent within a chapter.
- Make concurrency and synchronization points visually explicit.
- Name recovery or fallback edges when failure handling matters.

## Architecture Diagrams

- Use architecture diagrams for bounded contexts, interfaces, external systems, and operational boundaries.
- Show the stable interfaces and contracts, not every runtime detail.
- Reuse the same artifact names that appear in the text and running example.
- Avoid diagram labels that duplicate whole sentences.

## Figure Captions

- Use the format `Figure N.M. Short declarative title.` for numbered figures.
- Follow the title sentence with one short sentence that states the intended reader takeaway.
- If a diagram supports an invariant, name the invariant in the caption or adjacent prose.
- Claim IDs may appear only when they already exist in `verification/traceability-matrix.md`.
- Reader-visible claim IDs belong in figure captions and chapter-level review callouts, not in ordinary body paragraphs or diagram node labels.

## Invariant Mapping

- When a diagram encodes an invariant, restate that invariant in prose.
- Link the invariant to the related artifact, review checkpoint, or verification evidence.
- Keep the invariant wording stable across chapters unless the scope changes intentionally.
