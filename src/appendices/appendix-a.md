---
layout: book
title: "Notation and Diagram Conventions"
appendix: appendix-a
order: 12
description: "Shared notation, diagram reading rules, and naming conventions used throughout the book."
---

# Appendix A. Notation and Diagram Conventions

This appendix provides a stable reference for the notation, diagram rules, and naming conventions used across the book.
Its purpose is not to teach category theory from scratch.
Its purpose is to keep the manuscript's diagrams, labels, and file-level references readable and stable across chapters.

## Mathematical notation used in the book

This section fixes the meaning of the mathematical symbols that appear in definitions, diagrams, and examples.

### Objects, morphisms, and composition symbols

- `A`, `B`, `C` denote objects.
  In this book an object is usually a stable artifact, interface, boundary, or workflow state rather than an arbitrary mathematical set.
- `f: A -> B` denotes a morphism from object `A` to object `B`.
  In engineering terms this is a named transformation that preserves the structure the chapter is discussing.
- `g ∘ f` denotes composition.
  Read it right to left.
  Apply `f` first and then `g`.
- `id_A` denotes the identity morphism on `A`.
  Use it when a chapter needs to state that one boundary or artifact remains unchanged under composition.

The manuscript prefers named engineering morphisms such as `approve-or-return` or `evaluate-policy` when the concrete workflow matters.
It uses symbolic notation only when the abstract law is the point being explained.

### Products, coproducts, and universal property notation

- `A × B` denotes a product-like construction.
  Read it as one combined object from which the relevant components can be projected back out.
- `A + B` or an explicitly named sum-like object denotes a coproduct-like construction.
  Read it as one explicit variation boundary with named entries from the variant cases.
- Projection maps may be written as `pi_1`, `pi_2`, or with named engineering labels such as `scope-of` and `policy-status-of`.
- Injection maps may be written as `inl`, `inr`, or with named engineering labels such as `enter-standard` and `enter-escalated`.
- Pullbacks and pushouts are introduced with named shared-boundary maps instead of dense symbolic diagrams when repository artifacts are the main concern.

When symbolic notation and repository labels both appear, the repository labels carry the reader-facing meaning.
The symbolic notation exists to clarify the law, not to replace the artifact names.

## Diagram reading conventions

This section explains how to read arrows, regions, and commutative claims without ambiguity.

### Arrow direction, labels, and path equivalence

- The direction of flow stays consistent within a chapter.
  Most workflow diagrams in this book read left to right.
- Arrow labels name transformations, not implementation trivia.
  Prefer `derive review plan` over an internal function name or tool flag.
- A path is meaningful only if each intermediate object is meaningful.
  If the intermediate node cannot be named clearly, the path is usually underspecified.
- Equivalent paths are claims, not decorations.
  If two routes are drawn as if they preserve the same result, the surrounding prose must say which invariant is being preserved.

In workflow diagrams, arrows may carry more than data flow.
They may carry review authority, synchronization obligations, route semantics, or effect boundaries.
That is why the prose always matters alongside the figure.

### When a square or larger shape is claimed to commute

- A square commutes only relative to a stated invariant.
  The book never treats commutativity as a purely visual property.
- If the diagram is illustrative rather than a proof obligation, the prose should say so explicitly.
- A broken square means one path no longer preserves the same meaning as another.
  In engineering terms this is a design defect, not just a diagram inconsistency.
- When a claim ID is shown, it must already exist in `verification/traceability-matrix.md`.
  Reader-visible claim IDs belong in figure captions and review callouts, not in diagram node labels.

For larger diagrams, read the claim locally before reading it globally.
Check each subpath and boundary first.
Then ask whether the full diagram preserves one coherent design story.

## Markdown, file, and naming conventions

This section documents the naming rules that keep manuscript files, IDs, and references stable.

### Chapter IDs, appendix IDs, and anchor stability

- Chapter IDs and appendix IDs are stable interfaces.
  Do not rewrite them casually once links, navigation, or manifests depend on them.
- Internal links should point to published destinations rather than raw source filenames when the rendered path is available.
- Canonical English manuscript files live under `src/`.
  Japanese files under `manuscript/ja/` are inputs only and do not become public output as-is.
- Running example artifact names such as `Change Request`, `Review Plan`, and `Approved Change` stay stable across prose, diagrams, and example files.

The repository treats anchor stability as a maintenance concern, not only a formatting concern.
If a heading changes, verify the downstream links and navigation assumptions in the same edit set.

### One-sentence-per-line and code identifier conventions

- Public prose uses one sentence per line where practical.
  This keeps review diffs smaller and translation workflows easier to control.
- Commands, file paths, environment variables, schema keys, and code identifiers remain in English and are formatted as code.
- Publication-grade image assets are preferred for core reader-facing figures when the figure program defines them.
- Mermaid blocks are still useful when a chapter needs a lightweight local sketch or no publication-grade redraw exists yet.
- Repository artifacts may also hold the canonical longer-form diagram or workflow description.
- Figure captions use the format `Figure N.M. Short declarative title.`
  The next line is a short `Reader takeaway` callout that teaches the reader how to read the figure.

These conventions are intentionally lightweight.
They are meant to make the book easier to maintain, review, and translate without turning every chapter into typesetting work.
