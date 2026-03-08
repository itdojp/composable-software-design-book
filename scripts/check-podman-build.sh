#!/usr/bin/env bash

set -euo pipefail

if ! command -v podman >/dev/null 2>&1; then
  echo "[podman-build] podman is not installed or not on PATH." >&2
  echo "[podman-build] Install Podman for the documented fallback build path." >&2
  exit 1
fi

podman run --rm --userns=keep-id \
  -v "$PWD:/work" \
  -w /work \
  "${PODMAN_RUBY_IMAGE:-docker.io/library/ruby:3.3}" \
  bash -lc 'bundle install && bundle exec jekyll build'
