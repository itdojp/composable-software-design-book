# Current State Audit

## Completed foundation work

- Repository bootstrap, metadata, TOC definition, translation workflow, QA and CI, publishing setup, editorial guidance, and running example selection are complete.
- Navigation, publishing configuration, and example manifests are already wired into the repository structure.
- The current manuscript now contains publication-quality English content for the Introduction, Chapter 01, Chapter 02, Chapter 03, Chapter 04, Chapter 05, Chapter 06, Chapter 07, Chapter 08, Chapter 09, Chapter 10, Appendix A, and Appendix C.
- Claim ID visibility, supported local build paths, variation artifact policy, and reusable counterexample policy are now documented as explicit repository decisions.
- The repository now has a full first-draft publication path from specification through AI-assisted implementation, including orchestration, effect, execution-trace, and acceptance-evidence artifacts.
- Core chapters now read locally before they read repository-first: each chapter carries a reader-facing figure or recap exhibit, a takeaway callout, and chapter-local explanation of the main artifact dependency.
- Chapter openings and handoffs now vary by local tension and payoff rather than repeating one repository-instruction template.
- All drafted chapters now include the reader-facing chapter packet sections required for the first publication milestone: learning goals, prerequisites, key concepts, running example linkage, summary, and review prompts.
- The theory chapters now include compact formal bridge blocks so the categorical title of each chapter pays off in reader-visible structure tied to the running example.
- The book package now includes front matter, part openers, afterword, and reader-facing backmatter so the manuscript reads as a book rather than as a repository outline.
- Appendix D now provides three transfer caselets that show how the method carries into deployment approval, support escalation, and regulated change-management domains.
- The late body chapters now thread transfer caselets directly into the main narrative so the method's portability is visible before the reader reaches Appendix D.
- The manuscript now includes chapter-end notes and further reading blocks, a chapter-to-reference map, and an Appendix C chapter guide so source guidance is chapter-aware rather than appendix-only.
- A publication-grade figure program now covers the Introduction and all ten core chapters, with generated screen and print assets under `assets/figures/publication/`.
- The repository now has a stable house style guide and editorial decision log for capitalization, hyphenation, figure caption policy, and recurring chapter-level prose decisions.
- The subject index and list-of-figures backmatter now include edition-stable cross-reference policy for web, ebook, and print reuse.
- Transfer caselets and Appendix D exhibits are now recoverable from backmatter rather than only from chapter-by-chapter reading.
- The glossary, editorial term base, and Japanese support map now cover the stable late-chapter running-example vocabulary and the clarified approval-evidence model.
- Appendix A now provides a stable notation, figure-caption, and naming reference for the manuscript.
- Appendix C now provides an annotated follow-on reading set for category theory, software architecture, lightweight formal methods, AI governance, and agent evaluation.
- The repository now has an explicit `v0.1.0-rc1` release-candidate note and changelog entry for stabilization review.
- CI now runs repository QA and a separate native Ruby/Bundler build job, so the canonical primary build path remains under continuous verification.
- GitHub Pages publication now uses a dedicated GitHub Actions workflow that builds from the repository root and deploys the generated `_site/` artifact.
- Example QA now includes manifest schema validation, generated trace collation, and section-level checks for the Chapter 08 through Chapter 10 artifacts.
- Core QA now includes a repository-local manuscript structure check for chapter packets and reader-facing figure captions in Chapters 03 through 10.
- The pre-Chapter-03 decision bundle is fully absorbed into the current Chapter 03 manuscript, contributor workflow, and running-example artifact set, so no stage-specific blocker remains.

## Canonical source paths

| Role | Canonical source path |
| --- | --- |
| Book metadata and chapter order | `book-config.json` |
| Public landing page | `index.md` |
| Canonical English manuscript | `src/additional/**/index.md`, `src/parts/**/index.md`, `src/chapter-*/index.md`, `src/appendices/*.md`, `src/backmatter/**/index.md`, and `src/afterword/**/index.md` |
| English TOC source | `project-management/toc_en.md` |
| Chapter-to-file mapping | `project-management/chapter-map.md` |
| Chapter-to-reference mapping | `project-management/chapter-reference-map.md` |
| Running example decision | `project-management/running-example.md` |
| Supporting policy decisions | `project-management/claim-id-visibility-decision.md`, `project-management/build-support-policy.md`, `project-management/variation-artifact-decision.md`, and `project-management/non-natural-counterexample-decision.md` |
| Figure inventory and asset policy | `project-management/figure-program.md` and `assets/figures/publication/` |
| Release notes and history | `project-management/release-v0.1.0-rc1.md` and `CHANGELOG.md` |
| Running example artifacts | `examples/minimal/policy-gated-change-review/` and `examples/common/policy-gated-change-review/` |
| Editorial rules | `docs/style/*.md`, `project-management/editorial-checklist.md`, and `project-management/editorial-style-decision-log.md` |
| Translation workflow and rules | `project-management/translation_workflow.md` and `project-management/translation_rules.md` |
| Editorial term base | `project-management/term-base.csv` |
| Repository term map | `TERMS.yml` |
| JSON schemas for structured QA input | `schemas/*.schema.json` |
| Translation input area | `manuscript/ja/` |
| QA and build entry points | `scripts/check_translation_inputs.py`, `scripts/qa.sh`, `scripts/check-manuscript-structure.py`, `scripts/check-examples.py`, `scripts/collate-example-traces.py`, `scripts/render-publication-figures.py`, `scripts/validate-github-pages.js`, and `package.json` |
| GitHub Pages deployment workflow | `.github/workflows/pages.yml` |

## Assumptions

- English remains the publication source of truth for all reader-facing content.
- Japanese files under `manuscript/ja/` remain working inputs and do not become publish artifacts as-is.
- The running example remains `policy-gated-change-review` for Chapters 01 through 10 unless the TOC and project-management files are intentionally revised together.
- Appendix B may expand incrementally as later revisions introduce genuinely new canonical terms, but established wording should remain stable once introduced.
- Containerized Jekyll build remains an acceptable fallback when native Ruby and Bundler are unavailable in the contributor environment.

## Concrete blockers

- None for the current `v0.1.0-rc1` stabilization milestone.

## Operational caveats

- Native Ruby and Bundler are still environment-dependent, but the supported matrix and smoke checks are now documented in `project-management/build-support-policy.md` and `CONTRIBUTING.md`.
