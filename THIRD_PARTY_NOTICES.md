# Third-Party Notices

This repository does not currently vendor third-party source trees or bundled media packs into the tracked source tree.
Most third-party software is resolved at build time from upstream package registries or GitHub Actions.

## Build and publication dependencies

- Ruby build dependencies are declared in `Gemfile` and resolved in `Gemfile.lock`.
- The current site build uses the GitHub Pages distribution, which brings Jekyll, the `minima` theme, and related plugins under their upstream licenses.
- Node-based publication support is declared in `package.json`.
- GitHub Actions workflow dependencies are referenced from `.github/workflows/ci.yml` and `.github/workflows/pages.yml`.

## Repository assets

- Publication figures under `assets/figures/publication/` are first-party redraws for this book unless a file says otherwise.
- Repository CSS and JavaScript under `assets/css/` and `assets/js/` are first-party repository assets unless a file says otherwise.
- No separate third-party font pack, image pack, or theme source tree is currently committed under `assets/`.

## Notice handling

Third-party packages, themes, actions, fonts, and other upstream materials remain under their original licenses.
If a future subtree vendors third-party material directly into the repository, that subtree should add its own `LICENSE`, `NOTICE`, or per-file header as required by the upstream terms.

See [`LICENSE-SCOPE.md`](LICENSE-SCOPE.md) for the repository-wide boundary and [`TRADEMARKS.md`](TRADEMARKS.md) for brand exclusions.
