# Artifact Location Decision

## Options Considered

| Option | Decision | Reason |
| --- | --- | --- |
| `docs/spec` and `docs/examples` | Rejected | `docs/` would blur source assets with publish-oriented material. |
| `artifacts/` plus `examples/` | Rejected | Splits one example across multiple roots and makes quickstart navigation harder. |
| `examples/` with nested `minimal/` and `common/` | Adopted | Keeps all example assets under one canonical source root while preserving a clean minimal/common split. |

## Canonical Location

The canonical location for example assets is `examples/`.
The minimal example lives under `examples/minimal/`.
The common running example lives under `examples/common/`.

## Common Example Substructure

The common example uses the following phase-oriented subdirectories.

- `spec/`
- `design/`
- `review/`
- `runtime/`
- `verification/`
- `implementation/`

The reusable variation artifact introduced for Chapter 06 lives at `design/variation-paths.md`.
It stays under `design/` rather than creating a dedicated top-level variation phase.

## Decision Rationale

This layout keeps the example source tree discoverable from the repository root.
It avoids mixing source assets with publish configuration or project-management notes.
It also makes it easy to attach validation hooks to one root without scattering path rules across the repository.
Keeping the variation artifact under `design/` preserves this structure while still giving Chapter 06 one canonical reusable location.
