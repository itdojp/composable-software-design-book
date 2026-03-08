# Translation Rules

## Structural Rules

- TR-01: Japanese drafts must preserve the chapter and section order defined by `book-config.json` and `project-management/toc_en.md`.
  Check: `manuscript/ja/outline_ja.md` must list chapter IDs in the same order as `book-config.json`.
- TR-02: English canonical headings must remain stable unless the TOC source of truth is intentionally updated first.
  Check: do not rename chapter IDs, appendix IDs, or source file paths as part of translation-only work.
- TR-03: Internal links, anchor targets, and cross-reference paths must not be changed implicitly during translation.
  Check: when a link target changes, the related TOC and source files must be updated in the same change set.

## Terminology Rules

- TR-04: Code identifiers, filenames, commands, environment variables, API names, and schema keys stay in English.
  Check: Japanese prose may explain them, but the literal tokens remain unchanged.
- TR-05: Canonical English terms are defined in `project-management/term-base.csv`.
  Check: if a new term is introduced, update the term base and `TERMS.yml` before using it in public English content.
- TR-06: When a term has a preferred Japanese counterpart, use that counterpart consistently in the Japanese draft.
  Check: avoid ad hoc synonyms unless the notes column in the term base explicitly allows them.

## Math, Diagram, and Caption Rules

- TR-07: Formulas, symbols, and diagram labels stay structurally identical between Japanese draft and English canonical text.
  Check: mathematical operators, symbolic names, and diagram node labels must not be translated unless the notation appendix says otherwise.
- TR-08: Figure captions and table captions may be translated in Japanese drafts, but figure numbers, table numbers, and reference keys remain stable.
  Check: captions may change language, but identifiers and callouts must continue to resolve.

## Sentence and Style Rules

- TR-09: Use one sentence per line in both Japanese drafts and English canonical prose.
  Check: split compound reasoning into separate lines when the claim or actor changes.
- TR-10: Prefer one proposition per sentence.
  Check: if a sentence contains multiple independent claims, rewrite it as multiple lines.
- TR-11: Avoid literal translations that preserve Japanese sentence rhythm at the expense of English clarity.
  Check: normalize for international English readers instead of mapping phrases word for word.
- TR-12: Japanese drafts must restore omitted subjects when actor ambiguity would affect translation quality.
  Check: explicitly mark whether the actor is the reader, the engineer, the reviewer, the agent, or the system.

## Review Rules

- TR-13: Every translated English section must be reviewed against the current TOC, glossary, and artifact references.
  Check: reviewers confirm heading order, term usage, and referenced files before merge.
- TR-14: Translation work must not directly edit generated publish artifacts outside the canonical source files.
  Check: update `index.md`, `src/`, and project-management sources rather than editing downstream outputs.
