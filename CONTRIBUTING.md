# Contributing

## Source of Truth

English content in `index.md` and `src/` is the publication source of truth.
Japanese files under `manuscript/ja/` are working inputs and must not be published as-is.
Canonical terminology is governed by `project-management/term-base.csv` and `TERMS.yml`.

## Recommended Local Workflow

Install Ruby and Bundler locally for the primary preview and build path.
Run `bundle install` before the first local preview or build.
Use `bundle exec jekyll serve --livereload` for local preview.
Use `bundle exec jekyll build` for the primary static build check.

## Container Fallback

If native Ruby or Bundler is unavailable, use Podman as the documented fallback.
Run `podman run --rm --userns=keep-id -v "$PWD:/work" -w /work docker.io/library/ruby:3.3 bash -lc 'bundle install && bundle exec jekyll build'`.
Treat the container command as the fallback for build verification, not as the canonical authoring workflow.

## Required Checks

Run `./scripts/check_translation_inputs.py` after updating canonical English content or Japanese working drafts.
Run `npm run qa` as the default repository gate.
Run `npm run validate-deploy` before publish-related changes are merged.

## Running Example Notes

`Approved Change` remains the single canonical approval artifact through Chapter 10.
`verification/review-checks.md` remains the concise review artifact.
`verification/traceability-matrix.md` carries the lightweight cross-artifact mapping introduced for the Chapter 03 path.
