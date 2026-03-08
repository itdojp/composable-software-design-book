# Current State Audit

## Completed foundation work

- Repository bootstrap, metadata, TOC definition, translation workflow, QA and CI, publishing setup, editorial guidance, and running example selection are complete.
- Navigation, publishing configuration, and example manifests are already wired into the repository structure.
- The current milestone moves the manuscript from skeleton chapters to publication-quality English content for the Introduction, Chapter 01, Chapter 02, Chapter 03, Chapter 04, Chapter 05, Chapter 06, and Chapter 07.
- Claim ID visibility, supported local build paths, variation artifact policy, and reusable counterexample policy are now documented as explicit repository decisions.

## Canonical source paths

| Role | Canonical source path |
| --- | --- |
| Book metadata and chapter order | `book-config.json` |
| Public landing page | `index.md` |
| Canonical English manuscript | `src/chapter-*/index.md` and `src/appendices/*.md` |
| English TOC source | `project-management/toc_en.md` |
| Chapter-to-file mapping | `project-management/chapter-map.md` |
| Running example decision | `project-management/running-example.md` |
| Supporting policy decisions | `project-management/claim-id-visibility-decision.md`, `project-management/build-support-policy.md`, `project-management/variation-artifact-decision.md`, and `project-management/non-natural-counterexample-decision.md` |
| Running example artifacts | `examples/minimal/policy-gated-change-review/` and `examples/common/policy-gated-change-review/` |
| Editorial rules | `docs/style/*.md` and `project-management/editorial-checklist.md` |
| Translation workflow and rules | `project-management/translation_workflow.md` and `project-management/translation_rules.md` |
| Editorial term base | `project-management/term-base.csv` |
| Repository term map | `TERMS.yml` |
| Translation input area | `manuscript/ja/` |
| QA and build entry points | `scripts/check_translation_inputs.py`, `scripts/qa.sh`, `scripts/check-examples.py`, `scripts/validate-github-pages.js`, and `package.json` |

## Assumptions

- English remains the publication source of truth for all reader-facing content.
- Japanese files under `manuscript/ja/` remain working inputs and do not become publish artifacts as-is.
- The running example remains `policy-gated-change-review` for Chapters 01 through 10 unless the TOC and project-management files are intentionally revised together.
- Appendix B may expand incrementally as new chapters leave skeleton state, but canonical wording should remain stable once introduced.
- Containerized Jekyll build remains an acceptable fallback when native Ruby and Bundler are unavailable in the contributor environment.

## Concrete blockers

- None for the Introduction through Chapter 07 publication milestone.

## Operational caveats

- Native Ruby and Bundler are still environment-dependent, but the supported matrix and smoke checks are now documented in `project-management/build-support-policy.md` and `CONTRIBUTING.md`.
