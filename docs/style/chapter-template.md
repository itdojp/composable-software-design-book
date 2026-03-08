# Chapter Template

## Purpose

Use this template for the English canonical chapter draft.
Use it together with `docs/style/notation.md`, `docs/style/diagram-style.md`, and `docs/style/terminology.md`.

## Skeleton-Stage Compatibility

The current repository is still in the skeleton stage.
At this stage, a chapter may contain only the title, a framing paragraph, and the ordered H2/H3 map that matches the TOC.
Learning goals, prerequisites, key concepts, running example linkage, summary, and exercises become explicit sections as prose drafting advances.

## Recommended Chapter Packet

1. Title and one-sentence chapter purpose.
2. Learning goals.
3. Prerequisites.
4. Key concepts.
5. Running example linkage.
6. Main body sections that follow the TOC.
7. Summary.
8. Exercises or review prompts.

## Authoring Rules

- State the chapter purpose in one sentence immediately under the H1.
- Keep the H2 and H3 order aligned with `project-management/toc_en.md`.
- Keep one sentence per line in prose paragraphs.
- Treat the running example linkage as required once `project-management/running-example.md` exists.
- If summary or exercises are intentionally deferred, keep the decision in editorial notes rather than public placeholders.

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

## Exercises

1. Review question.
2. Design prompt.
```

## Mapping To The Current Skeleton

The present chapter skeletons already satisfy the title, framing paragraph, and ordered section map requirements.
When prose writing begins, add the chapter packet above without changing chapter IDs, source paths, or TOC order.
