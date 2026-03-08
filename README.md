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
- `npm run qa`
- `npm run build`
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

## QA

Run `npm run qa:core` before opening a pull request.
This command fetches the current `book-formatter` QA tooling into `.cache/book-formatter`, runs the core checks, and writes reports to `qa-reports/core/`.
Use `npm run qa` as the default local gate when no example-specific checks are required yet.

## Preview And Publish

Install Ruby and Bundler, then run `bundle install`.
Use `bundle exec jekyll serve --livereload` for local preview and `bundle exec jekyll build` for a static build check.
Run `npm run validate-deploy` before publishing.
Repository-level publishing setup is documented in `project-management/publishing-setup.md`.
If native Ruby or Bundler is unavailable, use the Podman fallback described in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Running Example Quickstart

Start with the [minimal example](examples/minimal/policy-gated-change-review/) to see one object-morphism-diagram chain.
Then move to the [common running example](examples/common/policy-gated-change-review/) to follow the full specification-to-implementation artifact path.

## English-first authoring policy

- English is the authoritative source for publication.
- Japanese drafts under `manuscript/ja/` are input only.
- Update shared terminology in `TERMS.yml` when canonical wording changes.
