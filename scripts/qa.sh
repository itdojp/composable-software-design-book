#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-core}"

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CACHE_DIR="${ROOT}/.cache"
BOOK_FORMATTER_DIR="${CACHE_DIR}/book-formatter"
BOOK_FORMATTER_REPO="${BOOK_FORMATTER_REPO:-https://github.com/itdojp/book-formatter.git}"
BOOK_FORMATTER_REF="${BOOK_FORMATTER_REF:-main}"
REPORT_ROOT="${ROOT}/qa-reports"
REPORT_DIR="${REPORT_ROOT}/${MODE}"

PUBLIC_MD_IGNORE=(
  "node_modules/**"
  "**/node_modules/**"
  ".cache/**"
  "qa-reports/**"
  "manuscript/**"
  "project-management/**"
  "shared/**"
  "templates/**"
  "tests/**"
)

log() {
  printf '[qa] %s\n' "$*"
}

ensure_book_formatter() {
  mkdir -p "${CACHE_DIR}"

  if [[ ! -d "${BOOK_FORMATTER_DIR}/.git" ]]; then
    log "Cloning book-formatter into ${BOOK_FORMATTER_DIR}"
    git clone --depth 1 --branch "${BOOK_FORMATTER_REF}" "${BOOK_FORMATTER_REPO}" "${BOOK_FORMATTER_DIR}"
  else
    log "Updating book-formatter cache"
    git -C "${BOOK_FORMATTER_DIR}" fetch --depth 1 origin "${BOOK_FORMATTER_REF}"
    git -C "${BOOK_FORMATTER_DIR}" checkout --detach FETCH_HEAD
  fi

  if [[ ! -d "${BOOK_FORMATTER_DIR}/node_modules" ]]; then
    log "Installing book-formatter dependencies"
    (cd "${BOOK_FORMATTER_DIR}" && npm ci)
  fi
}

join_ignore_args() {
  local -a out=()
  local pattern
  for pattern in "${PUBLIC_MD_IGNORE[@]}"; do
    out+=("--ignore" "$pattern")
  done
  printf '%s\0' "${out[@]}"
}

run_node_check() {
  local name="$1"
  shift
  log "Running ${name}"
  (cd "${BOOK_FORMATTER_DIR}" && "$@")
}

run_core() {
  mkdir -p "${REPORT_DIR}"
  ensure_book_formatter

  log "Preparing report directory ${REPORT_DIR}"

  run_node_check \
    validate-config \
    npm start -- validate-config --config "${ROOT}/book-config.json" \
    > "${REPORT_DIR}/validate-config.log" 2>&1

  mapfile -d '' IGNORE_ARGS < <(join_ignore_args)

  run_node_check \
    check-links \
    node scripts/check-links.js "${ROOT}" \
    --pattern "**/*.md" \
    "${IGNORE_ARGS[@]}" \
    --output "${REPORT_DIR}/check-links.json" \
    > "${REPORT_DIR}/check-links.log" 2>&1

  run_node_check \
    check-unicode \
    node scripts/check-unicode.js "${ROOT}" \
    --pattern "**/*.md" \
    "${IGNORE_ARGS[@]}" \
    --output "${REPORT_DIR}/check-unicode.json" \
    --fail-on error \
    > "${REPORT_DIR}/check-unicode.log" 2>&1

  run_node_check \
    check-layout-risk \
    node scripts/check-layout-risk.js "${ROOT}" \
    --pattern "**/*.md" \
    "${IGNORE_ARGS[@]}" \
    --output "${REPORT_DIR}/check-layout-risk.json" \
    --fail-on none \
    > "${REPORT_DIR}/check-layout-risk.log" 2>&1

  run_node_check \
    check-markdown-structure \
    node scripts/check-markdown-structure.js "${ROOT}" \
    --pattern "**/*.md" \
    "${IGNORE_ARGS[@]}" \
    --output "${REPORT_DIR}/check-markdown-structure.json" \
    --fail-on error \
    > "${REPORT_DIR}/check-markdown-structure.log" 2>&1

  run_node_check \
    check-textlint \
    node scripts/check-textlint.js "${ROOT}" \
    --pattern "**/*.md" \
    "${IGNORE_ARGS[@]}" \
    --output "${REPORT_DIR}/check-textlint.json" \
    --fail-on none \
    > "${REPORT_DIR}/check-textlint.log" 2>&1

  log "Running placeholder check"
  python3 "${ROOT}/scripts/check-placeholders.py" > "${REPORT_DIR}/check-placeholders.json"

  log "Running manuscript structure check"
  python3 "${ROOT}/scripts/check-manuscript-structure.py" > "${REPORT_DIR}/check-manuscript-structure.json"

  cat > "${REPORT_DIR}/summary.txt" <<EOF
QA mode: ${MODE}
Repository root: ${ROOT}
book-formatter ref: ${BOOK_FORMATTER_REF}
Reports:
- validate-config.log
- check-links.json
- check-unicode.json
- check-layout-risk.json
- check-markdown-structure.json
- check-textlint.json
- check-placeholders.json
- check-manuscript-structure.json
EOF

  log "Core QA completed"
}

case "${MODE}" in
  core)
    run_core
    ;;
  all)
    run_core
    ;;
  *)
    echo "Unsupported QA mode: ${MODE}" >&2
    exit 2
    ;;
esac
