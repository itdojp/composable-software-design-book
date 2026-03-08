#!/usr/bin/env bash

set -euo pipefail

if ! command -v bundle >/dev/null 2>&1; then
  echo "[native-build] bundle is not installed or not on PATH." >&2
  echo "[native-build] Install Ruby and Bundler for the supported native build path." >&2
  exit 1
fi

bundle exec jekyll build
