# Changelog

## [Unreleased]

### Added

- Phase 5 practical-connection review gates in `README.md` and the public landing page.
- Editorial checks for theory-to-practice mapping, evidence boundaries, non-applicability conditions, and the related-book responsibility boundary.
- Pull request template items for related issues, GitHub Copilot review, unresolved thread checks, and repository validation evidence.

### Changed

- Appendix D now states how transfer cases should record preserved structure, drift detection, and the limits of a compositional analogy.

## [0.1.0-rc1] - 2026-03-08

### Added

- Full English canonical manuscript for the Introduction, Chapters 01 through 10, and Appendices A through C.
- Reader-facing Mermaid figures for Chapters 03 through 10, aligned with the running example and figure-caption policy.
- Release-candidate note in `project-management/release-v0.1.0-rc1.md`.
- `scripts/check-manuscript-structure.py` for chapter packet and figure-structure validation.

### Changed

- Standardized public links to the minimal and common running example landing pages on the published `README/` paths.
- Tightened the Chapter 04 and Chapter 05 formal bridges so path mappings and view-change claims stay internally consistent.
- Strengthened example QA so `effect-boundary.md`, `execution-trace.md`, and `acceptance-evidence.md` are checked for field-level agreement.
- Clarified the evidence terminology around the emitted `approval decision record` and the execution result path.

### Verification

- `npm run build:native`
- `npm run qa`
- `npm run validate-deploy`
- `npm run pages-status`
