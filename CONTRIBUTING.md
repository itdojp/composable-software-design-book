# Contributing

## Source of Truth

English content in `index.md` and `src/` is the publication source of truth.
Japanese files under `manuscript/ja/` are working inputs and must not be published as-is.
Canonical terminology is governed by `project-management/term-base.csv` and `TERMS.yml`.

## Recommended Local Workflow

Install Ruby and Bundler locally for the primary preview and build path.
Run `bundle install` before the first local preview or build.
Use `bundle exec jekyll serve --livereload` for local preview.
Use `bash scripts/check-native-build.sh` or `npm run build:native` for the primary static build smoke check.
Use `npm run build:smoke` only as a convenience wrapper that prefers the native path and falls back to Podman when native Bundler is unavailable.

## Supported Build Matrix

| Path | Support level | Supported tasks | Primary commands |
| --- | --- | --- | --- |
| Native Ruby + Bundler | Primary | preview, static build, repository QA | `bundle exec jekyll serve --livereload`, `npm run build:native`, `npm run qa`, `npm run validate-deploy` |
| Podman container build | Fallback | static build verification, repository QA on the host | `npm run build:podman`, `npm run qa`, `npm run validate-deploy` |

GitHub Actions runs a separate native Ruby/Bundler build job so the canonical primary path stays under continuous verification even when some contributors use the local Podman fallback.

## Container Fallback

If native Ruby or Bundler is unavailable, use Podman as the documented fallback.
Run `bash scripts/check-podman-build.sh` or `npm run build:podman`.
Treat the container command as the fallback for build verification, not as the canonical authoring workflow.
Podman live preview is not a supported authoring path in the current repository policy.

## Required Checks

Run `./scripts/check_translation_inputs.py` after updating canonical English content or Japanese working drafts.
Run `npm run qa` as the default repository gate.
Use `npm run qa:examples:deep` when you need to inspect the generated trace collation report directly under `qa-reports/examples/`.
Run `npm run build:native` when native Ruby/Bundler is available, or `npm run build:podman` when using the documented fallback.
Run `npm run validate-deploy` before publish-related changes are merged.
The supported build matrix and smoke-check policy are documented in `project-management/build-support-policy.md`.

## Running Example Notes

`Approved Change` remains the single canonical approval artifact through Chapter 10.
`verification/review-checks.md` remains the concise review artifact.
`verification/traceability-matrix.md` carries the lightweight cross-artifact mapping introduced for the Chapter 03 path.
