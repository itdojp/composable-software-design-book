# Compositional Software Design for Agentic Systems

## A Category-Theoretic Guide to Human-AI Boundaries and Verifiable Engineering

A practical guide to designing AI-assisted software systems with composition, diagrams, and effect boundaries that remain auditable and verifiable.

## Scope

This repository contains the English canonical manuscript and the supporting project management assets.
Japanese drafts under `manuscript/ja/` are working inputs and are not published.
Contributor workflow and local build guidance are documented in [`CONTRIBUTING.md`](CONTRIBUTING.md).

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
