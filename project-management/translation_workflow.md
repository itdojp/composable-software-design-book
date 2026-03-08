# Translation Workflow

## Source Hierarchy

English content in `index.md` and `src/` is the authoritative source for publication.
Japanese material under `manuscript/ja/` is input only and must never be published as the final source.
The English TOC and chapter metadata are defined by `project-management/toc_en.md` and `book-config.json`.
Terminology is governed by `project-management/term-base.csv` and `TERMS.yml`.

## Roles and Responsibilities

The draft author prepares the Japanese outline and chapter draft.
The translator or editor updates the English canonical source files.
The reviewer checks structural alignment, terminology, references, and technical accuracy.
The release owner runs repository checks before build or publish operations.

## Workflow Steps

1. Confirm that `project-management/toc_en.md` and `book-config.json` are current.
2. Sync `project-management/term-base.csv` and `TERMS.yml` before new terminology appears in running text.
3. Update `manuscript/ja/outline_ja.md` so the Japanese outline stays 1:1 with the English chapter and section structure.
4. Draft Japanese prose in `manuscript/ja/` by using `manuscript/ja/jp-draft-template.md`.
5. Translate and editorially adapt the content into the English canonical files in `src/` and `index.md`.
6. Review the English update for structure, terminology, links, formulas, and artifact references.
7. Run `scripts/check_translation_inputs.py` and resolve every reported failure.
8. Only after the checks pass, continue to build or publish steps.

## Glossary Update Timing

Update the glossary before a new canonical English term is introduced.
Update the glossary when a Japanese draft introduces a domain-specific nuance that affects translation choices.
Update the glossary when a preferred English term changes, even if the Japanese wording stays stable.

## Pre-Build and Pre-Publish Checks

- English canonical files have been updated, and Japanese draft files remain outside the public source set.
- `project-management/term-base.csv` and `TERMS.yml` agree on all shared canonical terms.
- `manuscript/ja/outline_ja.md` matches the current chapter ID order in `book-config.json`.
- Public-facing content files do not contain Japanese text.
- No placeholder tokens such as `TODO`, `TBD`, or `REPLACE_ME` remain in tracked manuscript and workflow files.

## Review Record Expectations

Each translation batch should state the touched English source files.
Each translation batch should state whether the glossary changed.
Each translation batch should identify the reviewer responsible for terminology and structural integrity.
