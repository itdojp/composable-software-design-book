# Release Candidate: v0.1.0-rc1

## Scope

- English canonical manuscript for the Introduction, Chapters 01 through 10, and Appendices A through C.
- Running example artifacts from specification through acceptance evidence.
- Native Ruby/Bundler primary build path with repository QA and GitHub Pages validation.

## Release Criteria

- `npm run build:native` passes on a contributor host with native Ruby and Bundler.
- `npm run qa` passes, including manuscript-structure checks and example trace collation.
- `npm run validate-deploy` passes.
- `npm run pages-status` confirms that `_site` exists after the build.
- Public-facing files contain no placeholder tokens.
- Chapters 03 through 10 contain reader-facing figures with numbered captions and explicit prose references.

## Included Material

- Responsibility-boundary framing, compositional foundations, translation, naturality, universality, integration, orchestration, effects, and case-study chapters.
- Appendix A notation and diagram conventions.
- Appendix B glossary and canonical terminology mapping.
- Appendix C annotated references and study paths.
- Running example artifacts for specification, design, runtime, review, implementation, and verification.

## Known Non-Blocking Caveats

- Native Ruby/Bundler remains environment-dependent, even though it is the canonical build path.
- The running-example validators check schema, section, and field-level consistency, but they do not prove semantic equivalence of every artifact path.
- Release review still depends on editorial judgment for prose quality, figure clarity, and chapter-to-chapter pacing.

## Verification Commands

- `npm run build:native`
- `npm run qa`
- `npm run validate-deploy`
- `npm run pages-status`

## Release Decision

This repository is ready for `v0.1.0-rc1` stabilization review once the release commit reruns the verification commands above without local uncommitted changes.
