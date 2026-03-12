# License Scope

This repository uses a path-based dual-license model.
This file defines the canonical boundary between reader-facing book content and reusable technical assets.
This file is a repository policy statement and not legal advice.

## Canonical license texts

- Root [`LICENSE`](LICENSE): `CC BY-NC-SA 4.0`
- [`LICENSES/Apache-2.0.txt`](LICENSES/Apache-2.0.txt): `Apache-2.0`

## Copyright and contributor assumption

The current repository history is administratively compatible with this licensing split because `git shortlog -sne --all` currently reports one contributor identity.
If material from additional contributors is added later, that contributor must have the right to submit the material under the path scope that applies to the target location, unless an explicit per-file notice says otherwise.

## Scope: CC BY-NC-SA 4.0

Apply `CC BY-NC-SA 4.0` to reader-facing book content and editorial metadata such as:

- `index.md`
- `src/**`
- `manuscript/ja/**`
- `assets/figures/**`
- `assets/images/**`
- `assets/diagrams/**`
- `TERMS.yml`
- `book-config.json`
- `mobile-config.json`
- `_data/navigation.json`

## Scope: Apache-2.0

Apply `Apache-2.0` to code, build, automation, site-generation, and reusable technical assets such as:

- `.codex/**`
- `.github/workflows/**`
- `_includes/**`
- `_layouts/**`
- `assets/css/**`
- `assets/js/**`
- `docs/style/**`
- `examples/**`
- `project-management/**`
- `schemas/**`
- `scripts/**`
- `shared/assets/js/**`
- `AGENTS.md`
- `CHANGELOG.md`
- `COMMERCIAL.md`
- `CONTRIBUTING.md`
- `LICENSES/**`
- `LICENSE-SCOPE.md`
- `README.md`
- `THIRD_PARTY_NOTICES.md`
- `TRADEMARKS.md`
- `Gemfile`
- `Gemfile.lock`
- `_config.yml`
- `package.json`

## Embedded code carve-out

Executable code snippets, shell commands, JSON fragments, YAML fragments, and other machine-readable examples embedded in the following content files are treated as `Apache-2.0`, unless a file says otherwise:

- `index.md`
- `src/**`
- `manuscript/ja/**`

This carve-out applies to the embedded machine-readable material itself.
The surrounding prose, figures, and editorial structure remain under the content license for the parent path.

## `_data/` review result

`_data/navigation.json` is treated as `CC BY-NC-SA 4.0`.
Its primary purpose is to carry reader-facing titles, part names, appendix names, and other textual navigation labels that appear in the public edition.

If future `_data/**` files are added for build-only flags, machine-only lookup tables, or other purely technical site-generation metadata, those files should be reviewed file by file and may be scoped to `Apache-2.0`.

## Exclusions

The following are excluded from the default content/code split unless a file says otherwise:

- `ITDO`, the book title as branding, logos, icons, and related marks
- third-party, upstream, or vendored assets that carry their own license terms
- fonts, themes, image packs, or bundled materials with separate notices
- any subtree with its own `LICENSE`, `NOTICE`, or per-file license header

See [`TRADEMARKS.md`](TRADEMARKS.md) and [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) for the operational handling of those exclusions.
