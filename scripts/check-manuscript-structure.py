#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PACKET_HEADINGS = [
    "## Learning goals",
    "## Prerequisites",
    "## Key concepts",
    "## Running example linkage",
    "## Summary",
    "## Review prompts",
    "## Notes and Further Reading",
]
MANUSCRIPT_FILES = {
    "introduction": ROOT / "src" / "chapter-introduction" / "index.md",
    "chapter01": ROOT / "src" / "chapter-chapter01" / "index.md",
    "chapter02": ROOT / "src" / "chapter-chapter02" / "index.md",
    "chapter03": ROOT / "src" / "chapter-chapter03" / "index.md",
    "chapter04": ROOT / "src" / "chapter-chapter04" / "index.md",
    "chapter05": ROOT / "src" / "chapter-chapter05" / "index.md",
    "chapter06": ROOT / "src" / "chapter-chapter06" / "index.md",
    "chapter07": ROOT / "src" / "chapter-chapter07" / "index.md",
    "chapter08": ROOT / "src" / "chapter-chapter08" / "index.md",
    "chapter09": ROOT / "src" / "chapter-chapter09" / "index.md",
    "chapter10": ROOT / "src" / "chapter-chapter10" / "index.md",
}
FIGURE_REQUIRED = {
    "introduction": 0,
    "chapter01": 1,
    "chapter02": 2,
    "chapter03": 3,
    "chapter04": 4,
    "chapter05": 5,
    "chapter06": 6,
    "chapter07": 7,
    "chapter08": 8,
    "chapter09": 9,
    "chapter10": 10,
}
CAPTION_RE = re.compile(r"^Figure (\d+)\.(\d+)\. .+\.$")


def next_nonempty(lines: list[str], start_index: int) -> tuple[int | None, str | None]:
    for index in range(start_index, len(lines)):
        if lines[index].strip():
            return index, lines[index].rstrip("\n")
    return None, None


def is_supported_figure_body(line: str | None) -> bool:
    if line is None:
        return False
    return line == "```mermaid" or line.startswith("![")


def check_packet_sections(label: str, lines: list[str], errors: list[str]) -> None:
    positions: list[int] = []

    for heading in REQUIRED_PACKET_HEADINGS:
        try:
            position = lines.index(heading)
        except ValueError:
            errors.append(f"{label}: missing required section {heading!r}")
            continue
        positions.append(position)

    if positions and positions != sorted(positions):
        errors.append(f"{label}: chapter packet sections are out of order")


def check_figures(label: str, lines: list[str], expected_major: int, errors: list[str]) -> None:
    found_minors: list[int] = []

    for index, raw_line in enumerate(lines):
        line = raw_line.strip()
        match = CAPTION_RE.match(line)
        if not match:
            continue

        major = int(match.group(1))
        minor = int(match.group(2))
        found_minors.append(minor)

        if major != expected_major:
            errors.append(f"{label}: figure major number {major} does not match expected chapter number {expected_major}")

        reference_token = f"Figure {major}.{minor}"
        previous_window = lines[max(0, index - 6) : index]
        if not any(reference_token in candidate for candidate in previous_window):
            errors.append(f"{label}: {reference_token} is not referenced in prose before the caption")

        takeaway_index, takeaway_line = next_nonempty(lines, index + 1)
        if takeaway_line is None:
            errors.append(f"{label}: {reference_token} is missing a takeaway sentence after the caption")
            continue
        if takeaway_line.startswith("#") or takeaway_line.startswith("```") or not takeaway_line.endswith("."):
            errors.append(f"{label}: {reference_token} must be followed by one takeaway sentence before the figure body")
            continue

        _, block_line = next_nonempty(lines, takeaway_index + 1)
        if not is_supported_figure_body(block_line):
            errors.append(
                f"{label}: {reference_token} must use a Mermaid block or publication image immediately after the takeaway sentence"
            )

    if not found_minors:
        errors.append(f"{label}: missing required reader-facing figure caption")
        return

    if len(found_minors) != len(set(found_minors)):
        errors.append(f"{label}: duplicate figure minor numbers detected")

    expected_minors = list(range(1, len(found_minors) + 1))
    if sorted(found_minors) != expected_minors:
        errors.append(
            f"{label}: figure minor numbers must be contiguous starting at 1, found {sorted(found_minors)!r}"
        )


def main() -> int:
    errors: list[str] = []
    checked_files: list[str] = []

    for label, path in MANUSCRIPT_FILES.items():
        checked_files.append(str(path.relative_to(ROOT)))
        if not path.exists():
            errors.append(f"{label}: missing file {path.relative_to(ROOT)}")
            continue

        lines = path.read_text(encoding="utf-8").splitlines()
        check_packet_sections(label, lines, errors)

        if label in FIGURE_REQUIRED:
            check_figures(label, lines, FIGURE_REQUIRED[label], errors)

    report = {
        "checked_files": checked_files,
        "required_packet_sections": REQUIRED_PACKET_HEADINGS,
        "figure_required_for": sorted(FIGURE_REQUIRED),
        "errors": errors,
    }

    print(json.dumps(report, indent=2, ensure_ascii=True))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
