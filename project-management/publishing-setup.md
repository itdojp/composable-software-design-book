# Publishing Setup

## Canonical Configuration Path

The canonical Jekyll configuration file is `_config.yml` at the repository root.
There is no `docs/_config.yml` in the current setup.

## Final Metadata Values

- title: `Compositional Software Design for Agentic Systems`
- subtitle: `A Category-Theoretic Guide to Human-AI Boundaries and Verifiable Engineering`
- description: `A practical guide to designing AI-assisted software systems with composition, diagrams, and effect boundaries that remain auditable and verifiable.`
- author: `ITDO Inc.`
- url: `https://itdojp.github.io`
- baseurl: `/composable-software-design-book`
- repository: `itdojp/composable-software-design-book`

## Layout and Defaults

All published pages use the `book` layout.
The repository root page keeps explicit front matter in `index.md`.
Pages under `src/` inherit `layout: book` and `lang: en` through `_config.yml` defaults, even when chapter files already declare them explicitly.

## Local Native Preview and Build

1. Install Ruby and Bundler on the local machine.
2. Run `bundle install`.
3. Run `bundle exec jekyll serve --livereload`.
4. Open `http://127.0.0.1:4000/composable-software-design-book/`.
5. Run `bundle exec jekyll build` for a static build check.

## Container Fallback

If Ruby and Bundler are not available locally, use Podman as a fallback.

```bash
podman run --rm --userns=keep-id \
  -v "$PWD:/work" \
  -w /work \
  docker.io/library/ruby:3.3 \
  bash -lc 'bundle install && bundle exec jekyll build'
```

## Validation Commands

- `npm run validate-deploy`
- `npm run pages-status`
- `bundle exec jekyll build`

## GitHub Pages Manual Settings

1. Open `Settings` > `Pages` in the GitHub repository.
2. Set `Build and deployment` to `Deploy from a branch`.
3. Select branch `gh-pages` and folder `/ (root)`.
4. Leave `Custom domain` empty unless a later issue explicitly introduces one.
5. After the first deployment, verify `https://itdojp.github.io/composable-software-design-book/`.

## Deployment Baseline

The repository currently uses `npm run deploy` to publish `_site/` to the `gh-pages` branch.
Run `npm run validate-deploy` before deployment so metadata, baseurl, and navigation assumptions are checked first.
