# Build Support Policy

## Scope

This document defines the supported local build paths for contributors.
Native Ruby and Bundler remain the primary authoring workflow.
Podman remains a fallback for static build verification when native tooling is unavailable.

## Supported Local Build Matrix

| Path | Support level | Intended use | Preview | Static build | Repository QA |
| --- | --- | --- | --- | --- | --- |
| Native Ruby + Bundler | Primary | Daily authoring, preview, publish checks | Supported | Supported | Supported |
| Podman container build | Fallback | Static build verification only | Not supported | Supported | Supported on the host |

## Minimum Success Criteria

### Native Ruby and Bundler

- `bundle install` completes in the repository root.
- `bundle exec jekyll serve --livereload` starts a local preview at the configured base URL.
- `bash scripts/check-native-build.sh` completes without error.
- `./scripts/check_translation_inputs.py`, `npm run qa`, and `npm run validate-deploy` complete without error.

### Podman fallback

- `bash scripts/check-podman-build.sh` completes without error and produces `_site/`.
- `./scripts/check_translation_inputs.py`, `npm run qa`, and `npm run validate-deploy` complete on the host environment.
- Podman is used for static build verification only, not as the canonical authoring preview workflow.

## Smoke Checks

- Native static build smoke check: `bash scripts/check-native-build.sh`
- Podman static build smoke check: `bash scripts/check-podman-build.sh`

## Manual Validation Procedure

1. Run the native path when Ruby and Bundler are available locally.
2. Use the Podman fallback only when the native path is unavailable in the contributor environment.
3. Run repository QA and deploy validation on the host after either static build path.
4. Record in the pull request when the fallback path was used instead of the primary path.

## Unsupported Paths

- Podman-based live preview is not a supported authoring workflow.
- Native `npm run build` without a working `bundle` executable is not a supported success path.
- Alternative container engines are not documented as supported paths in this repository.
