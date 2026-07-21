#!/usr/bin/env python3

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from types import ModuleType


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
SVG_NAMESPACE = "http://www.w3.org/2000/svg"
PLACEHOLDER_PATTERN = re.compile(r"\b(?:TODO|TBD|FIXME|placeholder|lorem ipsum)\b", re.IGNORECASE)

CRITICAL_FIGURES = {
    "commutative-approval": {
        "path": "src/chapter-chapter03/index.md",
        "number": "3.2",
        "required": (
            "change request",
            "review plan",
            "approved change",
            "policy check",
            "human approval",
            "commutes only",
            "request scope",
            "plan revision",
        ),
    },
    "string-diagram-fan-in": {
        "path": "src/chapter-chapter08/index.md",
        "number": "8.2",
        "required": (
            "lawful side",
            "policy and evidence branches",
            "change identity",
            "plan revision",
            "synchronized packet",
            "broken side",
            "mutable context",
            "unlabeled summary",
            "trustworthy approval meaning",
        ),
    },
    "delivery-case-study": {
        "path": "src/chapter-chapter10/index.md",
        "number": "10.1",
        "required": (
            "problem statement",
            "acceptance criteria",
            "design artifact set",
            "decision packet",
            "approved change",
            "execution trace",
            "acceptance evidence",
            "review authority",
        ),
    },
}

STYLE_REQUIREMENTS = (
    "## Complex Image Accessibility",
    "caption concise",
    "Markdown alt text",
    "**Long description — Figure N.M.**",
    'role="img"',
    "aria-labelledby",
    "accessible name",
    "detailed equivalent text",
    "missing, empty, placeholder, duplicate, or dangling metadata",
    "four distinct deliverables",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate publication figure accessibility contracts.")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT, help="Repository root to validate.")
    return parser.parse_args()


def normalize(value: str | None) -> str:
    return " ".join((value or "").split())


def load_renderer(root: Path) -> ModuleType:
    path = root / "scripts" / "render-publication-figures.py"
    spec = importlib.util.spec_from_file_location("publication_figure_renderer", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load renderer: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def long_description_block(text: str, number: str, asset_slug: str) -> str | None:
    image_pattern = re.compile(
        rf"^!\[[^\n]+\]\([^\n)]*{re.escape(asset_slug)}-screen\.svg\)\s*$",
        re.MULTILINE,
    )
    image_match = image_pattern.search(text)
    if image_match is None:
        return None
    tail = text[image_match.end() :]
    next_heading = re.search(r"^#{2,6}\s", tail, re.MULTILINE)
    section = tail[: next_heading.start()] if next_heading else tail
    label = f"**Long description — Figure {number}.**"
    label_offset = section.find(label)
    if label_offset < 0:
        return None
    following = section[label_offset + len(label) :].lstrip("\n")
    block = following.split("\n\n", 1)[0].strip()
    return block or None


def validate_long_descriptions(root: Path, errors: list[str]) -> int:
    checked = 0
    for slug, contract in CRITICAL_FIGURES.items():
        path = root / contract["path"]
        if not path.is_file():
            errors.append(f"missing chapter source for Figure {contract['number']}: {path}")
            continue
        text = path.read_text(encoding="utf-8")
        block = long_description_block(text, contract["number"], slug)
        if block is None:
            errors.append(
                f"Figure {contract['number']} must have an adjacent Long description block after {slug}-screen.svg"
            )
            continue
        normalized = normalize(block).lower()
        if len(normalized) < 240:
            errors.append(f"Figure {contract['number']} long description is too short: {len(normalized)} characters")
        if PLACEHOLDER_PATTERN.search(normalized):
            errors.append(f"Figure {contract['number']} long description contains placeholder text")
        for phrase in contract["required"]:
            if phrase.lower() not in normalized:
                errors.append(f"Figure {contract['number']} long description is missing: {phrase}")
        checked += 1
    return checked


def validate_style_guide(root: Path, errors: list[str]) -> None:
    path = root / "docs" / "style" / "diagram-style.md"
    if not path.is_file():
        errors.append(f"missing diagram style guide: {path}")
        return
    text = path.read_text(encoding="utf-8")
    for token in STYLE_REQUIREMENTS:
        if token not in text:
            errors.append(f"diagram style guide is missing contract text: {token}")


def validate_svg(
    path: Path,
    expected: str,
    expected_title: str,
    expected_description: str,
    errors: list[str],
) -> None:
    actual = path.read_text(encoding="utf-8")
    if actual != expected:
        errors.append(f"generated SVG is out of sync with renderer: {path.name}")
    try:
        root = ET.fromstring(actual)
    except ET.ParseError as exc:
        errors.append(f"invalid SVG XML in {path.name}: {exc}")
        return

    if root.get("role") != "img":
        errors.append(f"{path.name} must set role=img")
    labelled_by = (root.get("aria-labelledby") or "").split()
    if len(labelled_by) != 2 or len(set(labelled_by)) != 2:
        errors.append(f"{path.name} must reference one unique title and desc from aria-labelledby")

    title = root.find(f"{{{SVG_NAMESPACE}}}title")
    description = root.find(f"{{{SVG_NAMESPACE}}}desc")
    title_text = normalize(title.text if title is not None else None)
    description_text = normalize(description.text if description is not None else None)
    title_id = title.get("id") if title is not None else None
    description_id = description.get("id") if description is not None else None

    if not title_text:
        errors.append(f"{path.name} must have a non-empty title")
    if not description_text:
        errors.append(f"{path.name} must have a non-empty desc")
    if title_text != expected_title:
        errors.append(f"{path.name} title differs from the renderer accessibility specification")
    if description_text != expected_description:
        errors.append(f"{path.name} desc differs from the renderer accessibility specification")
    if len(description_text) < 80:
        errors.append(f"{path.name} desc is too short: {len(description_text)} characters")
    if title_text == description_text:
        errors.append(f"{path.name} title and desc must have distinct roles")
    if PLACEHOLDER_PATTERN.search(f"{title_text} {description_text}"):
        errors.append(f"{path.name} contains placeholder accessibility metadata")
    if labelled_by != [title_id, description_id]:
        errors.append(f"{path.name} aria-labelledby does not match its title/desc IDs in order")

    all_ids = [element.get("id") for element in root.iter() if element.get("id")]
    if len(all_ids) != len(set(all_ids)):
        errors.append(f"{path.name} contains duplicate IDs")
    missing_ids = [reference for reference in labelled_by if reference not in all_ids]
    if missing_ids:
        errors.append(f"{path.name} aria-labelledby has dangling references: {', '.join(missing_ids)}")


def validate_assets(root: Path, renderer: ModuleType, errors: list[str]) -> int:
    figures = renderer.FIGURES
    metadata = renderer.ACCESSIBILITY
    slugs = [figure["slug"] for figure in figures]
    if len(slugs) != len(set(slugs)):
        errors.append("renderer FIGURES contains duplicate slugs")
    if set(metadata) != set(slugs):
        missing = sorted(set(slugs) - set(metadata))
        extra = sorted(set(metadata) - set(slugs))
        errors.append(f"renderer accessibility coverage mismatch: missing={missing}, extra={extra}")

    asset_dir = root / "assets" / "figures" / "publication"
    expected_names = {f"{slug}-{theme}.svg" for slug in slugs for theme in ("screen", "print")}
    actual_names = {path.name for path in asset_dir.glob("*.svg")}
    if actual_names != expected_names:
        errors.append(
            "publication SVG inventory differs from renderer: "
            f"missing={sorted(expected_names - actual_names)}, extra={sorted(actual_names - expected_names)}"
        )

    checked = 0
    for figure in figures:
        try:
            expected_title, expected_description = renderer.accessibility_metadata(figure)
        except Exception as exc:  # noqa: BLE001 - report a closed contract, not a traceback
            errors.append(f"could not derive accessibility metadata for {figure['slug']}: {exc}")
            continue
        for theme in ("screen", "print"):
            path = asset_dir / f"{figure['slug']}-{theme}.svg"
            if not path.is_file():
                continue
            expected = renderer.render_svg(figure, theme)
            validate_svg(path, expected, expected_title, expected_description, errors)
            checked += 1
    return checked


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    errors: list[str] = []
    long_descriptions = validate_long_descriptions(root, errors)
    validate_style_guide(root, errors)
    svg_assets = 0
    try:
        renderer = load_renderer(root)
        svg_assets = validate_assets(root, renderer, errors)
    except Exception as exc:  # noqa: BLE001 - emit a stable QA report
        errors.append(f"renderer validation failed: {exc}")

    report = {
        "critical_long_descriptions": long_descriptions,
        "publication_svg_assets": svg_assets,
        "errors": errors,
        "status": "ok" if not errors else "failed",
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
