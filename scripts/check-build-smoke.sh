#!/usr/bin/env bash

set -euo pipefail

if command -v bundle >/dev/null 2>&1; then
  echo "[build-smoke] Using native Ruby/Bundler build path."
  exec bash scripts/check-native-build.sh
fi

if command -v podman >/dev/null 2>&1; then
  echo "[build-smoke] Native Bundler unavailable. Falling back to Podman static build verification."
  exec bash scripts/check-podman-build.sh
fi

echo "[build-smoke] No supported static build path is available." >&2
echo "[build-smoke] Install Ruby/Bundler for the primary path or Podman for the documented fallback path." >&2
exit 1
