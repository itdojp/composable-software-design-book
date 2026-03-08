# Chapter Template

## Purpose

Use this template for the English canonical chapter draft.
Use it together with `docs/style/notation.md`, `docs/style/diagram-style.md`, and `docs/style/terminology.md`.

## Current Draft State

The repository is now in a full first-draft state.
Drafted public chapters are expected to include the complete chapter packet rather than only a title, framing paragraph, and TOC-aligned section map.
Deferral of packet sections should be treated as an editorial exception and recorded outside public-facing manuscript prose.

## Recommended Chapter Packet

1. Title and one-sentence chapter purpose.
2. Learning goals.
3. Prerequisites.
4. Key concepts.
5. Running example linkage.
6. Main body sections that follow the TOC.
7. Summary.
8. Review prompts.

## Authoring Rules

- State the chapter purpose in one sentence immediately under the H1.
- Keep the H2 and H3 order aligned with `project-management/toc_en.md`.
- Keep one sentence per line in prose paragraphs.
- Treat the running example linkage as required in drafted public chapters.
- Treat summary and review prompts as expected public sections unless an explicit editorial exception is recorded.
- If a packet section is intentionally deferred, keep the decision in editorial notes rather than public placeholders.

## Drafting Template

```md
# Chapter Title

One-sentence chapter purpose.

## Learning goals

- Goal 1.
- Goal 2.
- Goal 3.

## Prerequisites

- Assumed concept or skill 1.
- Assumed concept or skill 2.

## Key concepts

- Canonical term 1.
- Canonical term 2.
- Canonical term 3.

## Running example linkage

- Example role in this chapter.
- Artifact or section that the reader should inspect.

## Section Title

Section purpose sentence.

### Subsection Title

Subsection purpose sentence.

## Summary

Short recap of the chapter claims and their design implications.

## Review prompts

1. Review question.
2. Design prompt.
```

## Applying The Template In Revision

The current manuscript already uses the chapter packet in drafted public chapters.
Use the template above when revising a chapter, backfilling a weaker section, or drafting a new canonical chapter file.
Do so without changing chapter IDs, source paths, or TOC order.
