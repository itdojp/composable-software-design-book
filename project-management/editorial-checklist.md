# Editorial Checklist

## Reference Set

- Chapter template: `docs/style/chapter-template.md`
- House style guide: `docs/style/house-style.md`
- Notation guide: `docs/style/notation.md`
- Diagram guide: `docs/style/diagram-style.md`
- Terminology guide: `docs/style/terminology.md`
- Editorial style decision log: `project-management/editorial-style-decision-log.md`
- Term base: `project-management/term-base.csv`
- English TOC: `project-management/toc_en.md`

## Structural Checks

- The chapter ID, title, and source file path match `book-config.json` and `project-management/chapter-map.md`.
- The H2 and H3 order matches the English TOC.
- Heading stability is preserved unless a TOC update intentionally changes it first.
- Internal links point to published destinations rather than source markdown filenames.

## Editorial Checks

- The opening paragraph states the chapter purpose clearly.
- Reader-facing prose is English-reader-first rather than translation-shaped.
- One sentence per line is preserved in prose sections.
- Placeholder tokens such as `TODO`, `TBD`, `REPLACE_ME`, and `Working Title` are absent from public-facing files.

## Notation And Diagram Checks

- Formal notation follows `docs/style/notation.md`.
- Diagram captions and invariants follow `docs/style/diagram-style.md`.
- Numbered figures use one `Reader takeaway` callout line between caption and figure body.
- Claim IDs, when used, appear only in matrix-backed captions or chapter-level review callouts.
- Code, math, and pseudocode are visually distinct and tagged consistently.

## Terminology Checks

- Canonical terms follow `docs/style/terminology.md`.
- New terms update `project-management/term-base.csv` and `TERMS.yml` in the same change set.
- Glossary wording, figure labels, and prose wording do not drift apart.

## Content Progress Checks

- Learning goals, prerequisites, key concepts, running example linkage, summary, and review prompts are present in drafted public chapters unless an explicit editorial exception is recorded.
- Notes and Further Reading are present in drafted public chapters.
- Running example linkage uses the canonical `policy-gated-change-review` example and points readers to the relevant artifact or example landing page.
- QA and translation validation scripts still pass after the edit set.
