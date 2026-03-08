# House Style Guide

## Scope

This guide defines the stable prose and formatting baseline for the public manuscript.
Use it after structural edits and before release-candidate publication work.

## Core prose rules

- Keep one sentence per line where practical.
- Prefer direct declarative prose over repository-instruction phrasing in reader-facing chapters.
- Use short paragraphs that carry one argument, one contrast, or one transition.
- Keep chapter openings concrete by naming the design tension before naming the formal term.
- Keep chapter endings explicit about the next design problem rather than ending on a generic recap sentence.

## Capitalization and hyphenation

- Use `AI-assisted` as the default adjective for workflows, delivery, engineering, and implementation.
- Use `AI agent` as the default noun phrase for the acting software component.
- Use `agentic` only when it is semantically better than `AI-assisted`, or when it appears in the finalized title or subtitle.
- Use `reader-facing` and `engineering-facing` with hyphens.
- Use `runtime view`, `reviewer view`, and `effect boundary` as open compounds because they are canonical glossary terms.
- Use `human review gate` and `policy gate` as open compounds in prose and glossary entries.
- Use `end-to-end` as the default compound modifier.

## Canonical artifact names

- Capitalize running-example artifact names exactly as `Change Request`, `Review Plan`, `Decision Packet`, `Approved Change`, `Policy-Evaluated Plan`, `Execution-Ready Change`, and `Acceptance Evidence` when they refer to canonical artifact classes.
- Use lowercase only when referring to a generic concept rather than the canonical artifact label.
- Keep claim IDs out of ordinary body prose unless the sentence is explicitly about traceability or review.

## Figures and tables

- Use `Figure N.M. ...` and `Table N.M. ...` captions with declarative titles.
- Follow figure captions with one short `Reader takeaway` callout sentence before the figure body.
- Keep table titles descriptive enough that a reader can recover the reason to revisit them later.
- Reuse the same terminology in captions, glossary entries, and chapter prose.

## Code, math, and identifiers

- Use code formatting for file paths, commands, environment variables, schema keys, artifact labels, and mathematical symbols.
- Use symbolic notation only when the law itself matters.
- Prefer named engineering morphisms such as `approve-or-return` when the repository artifact path is the main point.

## Source notes and references

- Keep chapter-end source notes practical and selective.
- Distinguish formal theory references from engineering and governance references when the chapter blends them.
- Use Appendix C for the master bibliography and `project-management/chapter-reference-map.md` for the editorial mapping layer.
