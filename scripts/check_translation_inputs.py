#!/usr/bin/env python3

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
JAPANESE_RE = re.compile(r"[ぁ-んァ-ン一-龠々ー]")
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|REPLACE_ME)\b")
REQUIRED_TERM_CATEGORIES = {
    "category-theory",
    "software-design",
    "ai-agents",
    "formal-methods",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_terms_yml(path: Path) -> dict[str, str]:
    text = read_text(path)
    lines = text.splitlines()
    mapping: dict[str, str] = {}
    current_ja: str | None = None

    for raw_line in lines:
        if raw_line.startswith("  ") and raw_line.endswith(":") and not raw_line.strip().startswith("en:"):
            current_ja = raw_line.strip()[:-1]
            continue
        if current_ja and raw_line.strip().startswith("en:"):
            mapping[current_ja] = raw_line.split(":", 1)[1].strip()
            current_ja = None

    return mapping


def parse_term_base(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        expected = [
            "term_en",
            "term_ja",
            "category",
            "canonical_definition_en",
            "notes",
        ]
        if reader.fieldnames != expected:
            raise ValueError(f"unexpected CSV header: {reader.fieldnames}")
        return list(reader)


def parse_outline_chapter_ids(path: Path, valid_ids: set[str]) -> list[str]:
    ids: list[str] = []
    for line in read_text(path).splitlines():
        match = re.match(r"^\|\s*([a-z0-9-]+)\s*\|", line)
        if not match:
            continue
        candidate = match.group(1)
        if candidate in valid_ids:
            ids.append(candidate)
    return ids


def collect_public_facing_files() -> list[Path]:
    files = [
        ROOT / "README.md",
        ROOT / "index.md",
        ROOT / "book-config.json",
        ROOT / "_data" / "navigation.json",
    ]
    files.extend(sorted((ROOT / "src").glob("chapter-*/index.md")))
    files.extend(sorted((ROOT / "src" / "appendices").glob("*.md")))
    files.extend(sorted((ROOT / "src" / "additional").glob("**/*.md")))
    files.extend(sorted((ROOT / "src" / "parts").glob("**/*.md")))
    files.extend(sorted((ROOT / "src" / "afterword").glob("**/*.md")))
    files.extend(sorted((ROOT / "src" / "backmatter").glob("**/*.md")))
    return files


def collect_placeholder_targets() -> list[Path]:
    targets = collect_public_facing_files()
    targets.extend(
        [
            ROOT / "manuscript" / "ja" / "outline_ja.md",
            ROOT / "manuscript" / "ja" / "jp-draft-template.md",
            ROOT / "project-management" / "title-decision.md",
            ROOT / "project-management" / "toc_en.md",
            ROOT / "project-management" / "chapter-map.md",
            ROOT / "project-management" / "term-base.csv",
        ]
    )
    return sorted(dict.fromkeys(targets))


def main() -> int:
    errors: list[str] = []

    required_files = [
        ROOT / "project-management" / "translation_workflow.md",
        ROOT / "project-management" / "translation_rules.md",
        ROOT / "project-management" / "term-base.csv",
        ROOT / "manuscript" / "ja" / "outline_ja.md",
        ROOT / "manuscript" / "ja" / "jp-draft-template.md",
    ]
    for path in required_files:
        if not path.exists():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")

    cfg_path = ROOT / "book-config.json"
    if not cfg_path.exists():
        errors.append("missing required file: book-config.json")
        config = {}
    else:
        config = json.loads(read_text(cfg_path))

    chapter_ids = [chapter["id"] for chapter in config.get("structure", {}).get("chapters", [])]
    chapter_id_set = set(chapter_ids)

    outline_path = ROOT / "manuscript" / "ja" / "outline_ja.md"
    if outline_path.exists() and chapter_ids:
        outline_ids = parse_outline_chapter_ids(outline_path, chapter_id_set)
        if outline_ids != chapter_ids:
            errors.append(
                "outline_ja.md chapter IDs do not match book-config.json order: "
                f"expected {chapter_ids}, got {outline_ids}"
            )

    terms_path = ROOT / "TERMS.yml"
    term_base_path = ROOT / "project-management" / "term-base.csv"
    if terms_path.exists() and term_base_path.exists():
        try:
            terms_yml = parse_terms_yml(terms_path)
            term_rows = parse_term_base(term_base_path)
        except Exception as exc:  # pragma: no cover - CLI error aggregation
            errors.append(str(exc))
            term_rows = []
            terms_yml = {}

        if len(term_rows) < 40:
            errors.append(f"term-base.csv must contain at least 40 rows, found {len(term_rows)}")

        categories = {row["category"].strip() for row in term_rows if row["category"].strip()}
        missing_categories = sorted(REQUIRED_TERM_CATEGORIES - categories)
        if missing_categories:
            errors.append(f"term-base.csv is missing required categories: {', '.join(missing_categories)}")

        csv_lookup = {(row["term_ja"].strip(), row["term_en"].strip()) for row in term_rows}
        for term_ja, term_en in terms_yml.items():
            if (term_ja, term_en) not in csv_lookup:
                errors.append(
                    "TERMS.yml entry missing from term-base.csv: "
                    f"{term_ja} -> {term_en}"
                )

    for path in collect_public_facing_files():
        text = read_text(path)
        if JAPANESE_RE.search(text):
            errors.append(f"Japanese text found in public-facing file: {path.relative_to(ROOT)}")

    for path in collect_placeholder_targets():
        text = read_text(path)
        if PLACEHOLDER_RE.search(text):
            errors.append(f"placeholder token found in file: {path.relative_to(ROOT)}")

    if errors:
        print("FAIL")
        for item in errors:
            print(f"- {item}")
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
