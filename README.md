# Compositional Software Design for Agentic Systems

## A Category-Theoretic Guide to Human-AI Boundaries and Verifiable Engineering

A practical guide to designing AI-assisted software systems with composition, diagrams, and effect boundaries that remain auditable and verifiable.

## Scope

This repository contains the English canonical manuscript and the supporting project management assets.
Japanese drafts under `manuscript/ja/` are working inputs and are not published.
Those internal drafts are distinct from the separately published Japanese book in `categorical-software-design-book`.
Contributor workflow and local build guidance are documented in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Relationship to the related Japanese book

- This repository is an independent English book.
- The related Japanese book is `圏論によるAIエージェント時代の合成的ソフトウェア設計` (`categorical-software-design-book`).
- The two books share themes and some terminology, but they are not legacy/current versions and are not simple translations of each other.
- Start with this repository if you want the English-first canonical manuscript and the current composition centered on compositional design for agentic systems.
- Start with the Japanese book if you want a Japanese reader-facing book focused on design artifacts for the AI agent era, Context Pack usage, and GitHub/CI-oriented guidance.
- Related Japanese book:
  - Public site: https://itdojp.github.io/categorical-software-design-book/
  - Repository: https://github.com/itdojp/categorical-software-design-book

## Licensing

Reader-facing book content is licensed under [`CC BY-NC-SA 4.0`](LICENSE).
Code, build files, schemas, site-generation assets, and reusable technical examples are licensed under [`Apache-2.0`](LICENSES/Apache-2.0.txt).
The canonical boundary, embedded-code carve-out, `_data/` review result, commercial guidance, trademark handling, and third-party notices are documented in [`LICENSE-SCOPE.md`](LICENSE-SCOPE.md), [`COMMERCIAL.md`](COMMERCIAL.md), [`TRADEMARKS.md`](TRADEMARKS.md), and [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).
## Repository Structure

- English canonical manuscript: `index.md` and `src/`
- Japanese draft area: `manuscript/ja/`
- Translation term base: `TERMS.yml`
- Codex repository instructions: `AGENTS.md`

## Commands

- `npm run qa:core`
- `npm run qa:examples`
- `npm run qa:examples:deep`
- `npm run qa`
- `npm run figures:render`
- `npm run build`
- `npm run build:native`
- `npm run build:podman`
- `npm run build:smoke`
- `npm run serve`
- `npm run validate-deploy`
- `npm run pages-status`

## Translation Workflow

- English workflow guide: `project-management/translation_workflow.md`
- Translation rules: `project-management/translation_rules.md`
- Canonical term base: `project-management/term-base.csv`

## Project Management Status

- Current state audit: [`project-management/current-state-audit.md`](project-management/current-state-audit.md)
- Next open questions: [`project-management/next-open-questions.md`](project-management/next-open-questions.md)
- Release candidate note: [`project-management/release-v0.1.0-rc1.md`](project-management/release-v0.1.0-rc1.md)
- Changelog: [`CHANGELOG.md`](CHANGELOG.md)
- Chapter-to-reference map: [`project-management/chapter-reference-map.md`](project-management/chapter-reference-map.md)
- Figure program: [`project-management/figure-program.md`](project-management/figure-program.md)

## Editorial And Style

- House style: `docs/style/house-style.md`
- Chapter template: `docs/style/chapter-template.md`
- Diagram style: `docs/style/diagram-style.md`
- Terminology guide: `docs/style/terminology.md`
- Editorial checklist: `project-management/editorial-checklist.md`

## QA

Run `npm run qa:core` before opening a pull request.
This command fetches the current `book-formatter` QA tooling into `.cache/book-formatter`, runs the core checks, and writes reports to `qa-reports/core/`.
It also runs the repository-local manuscript structure check for chapter packets and reader-facing figure coverage.
Run `npm run qa:examples` to execute manifest schema validation, lightweight example checks, and generated trace collation for the running example.
The generated example reports are written to `qa-reports/examples/`.
Use `npm run qa` as the default local gate.
Run `npm run figures:render` when the publication-grade redraws under `assets/figures/publication/` need to be regenerated from the canonical figure definitions.

## Preview And Publish

Install Ruby and Bundler, then run `bundle install`.
Use `bundle exec jekyll serve --livereload` for local preview and `npm run build:native` for the primary static build smoke check.
Use `npm run build:smoke` as a local convenience wrapper that prefers the native path and falls back to Podman only when native Bundler is unavailable.
Run `npm run validate-deploy` before publishing.
GitHub Pages publication is handled by the [`Deploy GitHub Pages` workflow](.github/workflows/pages.yml), which builds from the repository root and deploys `_site/` through GitHub Actions.
Repository-level publishing setup is documented in `project-management/publishing-setup.md`.
If native Ruby or Bundler is unavailable, use `npm run build:podman` as the documented fallback described in [`CONTRIBUTING.md`](CONTRIBUTING.md).
The support boundary for native and Podman paths is documented in `project-management/build-support-policy.md`.
GitHub Actions continuously verifies the canonical primary path through a separate native Ruby/Bundler build job, so fallback usage on a local host does not redefine the repository's primary build policy.

## Running Example Quickstart

Start with the [minimal example](examples/minimal/policy-gated-change-review/README.md) to see one object-morphism-diagram chain.
Then move to the [common running example](examples/common/policy-gated-change-review/README.md) to follow the full specification-to-implementation artifact path.

## English-first authoring policy

- English is the authoritative source for publication.
- Japanese drafts under `manuscript/ja/` are input only.
- Update shared terminology in `TERMS.yml` when canonical wording changes.
