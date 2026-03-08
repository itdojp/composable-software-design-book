# Notation Guide

## Scope

This guide standardizes how the book writes formal notation, code notation, and pseudocode.
Use it together with `docs/style/diagram-style.md` and `docs/style/terminology.md`.

## Objects And Morphisms

- Write objects in roman text when they name software artifacts, such as `Specification`, `Interface Contract`, or `Execution Trace`.
- Write morphisms as verbs or verb phrases when the transformation matters more than the implementation detail.
- Use the same canonical English term across prose, diagrams, and glossary entries.

## Composition And Identity

- Use `g ◦ f` when the mathematical composition order matters.
- Use plain English phrases such as `compose`, `map`, or `preserve` when the prose needs to stay reader-first.
- Introduce `identity morphism` only when the stability claim matters for the argument.

## Diagram Labeling

- Keep node labels short and canonical.
- Prefer noun phrases for nodes and verb phrases for arrows.
- Reuse the same labels across diagrams when the same artifact or transformation reappears.
- Do not invent new abbreviations inside a figure unless the caption defines them.

## Code, Math, And Pseudocode

- Use inline code backticks for filenames, commands, API names, environment variables, and literal identifiers.
- Use mathematical notation only when it compresses meaning better than prose.
- Use fenced code blocks with a language tag for executable code.
- Use fenced code blocks with `text` or `pseudo` for non-executable pseudocode.

## Reader-Facing Preference

- Prefer the simplest notation that preserves the claim.
- Introduce a symbol only after the prose version of the claim is clear.
- Avoid switching between multiple notations for the same concept in one chapter.
