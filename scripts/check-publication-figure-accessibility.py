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
    "introduction-governed-path": {
        "path": "src/chapter-introduction/index.md",
        "number": "0.1",
        "caption": "Figure 0.1. Compositional design keeps authority attached to artifacts instead of to opaque automation.",
        "alt_required": ("publication redraw", "governed path from request to evidence"),
        "required": (
            "change request",
            "review plan",
            "decision packet",
            "human approval",
            "approved change",
            "execution-ready change",
            "acceptance evidence",
            "opaque automation",
        ),
    },
    "responsibility-boundaries": {
        "path": "src/chapter-chapter01/index.md",
        "number": "1.1",
        "caption": "Figure 1.1. Responsibility boundaries separate decision artifacts from emitted evidence.",
        "alt_required": ("publication redraw", "responsibility boundaries", "decision artifacts and evidence"),
        "required": (
            "change request",
            "review plan",
            "decision packet",
            "approved change",
            "approval decision record",
            "execution trace",
            "acceptance evidence",
            "approval authority",
        ),
    },
    "object-composition": {
        "path": "src/chapter-chapter02/index.md",
        "number": "2.1",
        "caption": "Figure 2.1. The running example becomes a model only when stable artifacts and named transformations are explicit.",
        "alt_required": ("publication redraw", "object-and-morphism chain"),
        "required": (
            "change request",
            "review plan",
            "approved change",
            "draft review plan",
            "human approval",
            "policy-gated approval",
            "durable boundaries",
            "composition",
        ),
    },
    "minimal-approval-commutativity": {
        "path": "src/chapter-chapter03/index.md",
        "number": "3.1",
        "caption": "Figure 3.1. Minimal approval commutativity claim.",
        "alt_required": ("publication redraw", "minimal approval commutativity claim"),
        "required": (
            "change request",
            "approved change",
            "draft review plan",
            "human approval",
            "minimal commutative claim",
            "same approval meaning",
            "does not commute",
            "invalid",
        ),
    },
    "commutative-approval": {
        "path": "src/chapter-chapter03/index.md",
        "number": "3.2",
        "caption": "Figure 3.2. Repository-level approval claim with explicit policy dependency (`PGCR-01`).",
        "alt_required": ("publication redraw", "repository-level approval claim"),
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
    "design-runtime-translation": {
        "path": "src/chapter-chapter04/index.md",
        "number": "4.1",
        "caption": "Figure 4.1. Design-to-runtime translation keeps the approval path intact.",
        "alt_required": ("publication redraw", "design-to-runtime translation chain"),
        "required": (
            "design view",
            "runtime view",
            "change request",
            "approved change",
            "pending request",
            "execution-ready change",
            "translation arrows",
            "human approval boundary",
        ),
    },
    "reviewer-naturality": {
        "path": "src/chapter-chapter05/index.md",
        "number": "5.1",
        "caption": "Figure 5.1. Reviewer-facing naturality square for one approval move.",
        "alt_required": ("publication redraw", "reviewer-facing naturality square"),
        "required": (
            "review plan",
            "approved change",
            "human approval",
            "decision packet",
            "approve-or-return",
            "review outcome",
            "square commutes",
            "same approval meaning",
        ),
    },
    "review-context-product": {
        "path": "src/chapter-chapter06/index.md",
        "number": "6.1",
        "caption": "Figure 6.1. Product-like review context keeps all three approval inputs recoverable.",
        "alt_required": ("publication redraw", "product-like review context"),
        "required": (
            "combined review context",
            "requested scope",
            "policy result",
            "evidence links",
            "three labeled projections",
            "opaque summary",
            "recoverability",
            "separately inspectable",
        ),
    },
    "variation-paths": {
        "path": "src/chapter-chapter06/index.md",
        "number": "6.2",
        "caption": "Figure 6.2. Explicit review routes converge on one approval meaning.",
        "alt_required": ("publication redraw", "explicit review routes", "one approval meaning"),
        "required": (
            "combined review context",
            "standard review route",
            "escalated review route",
            "approved change",
            "standard controls",
            "escalated controls",
            "request identity",
            "one comparable approval meaning",
        ),
    },
    "shared-boundary-join": {
        "path": "src/chapter-chapter07/index.md",
        "number": "7.1",
        "caption": "Figure 7.1. Constrained joins remain valid only through one preserved shared boundary.",
        "alt_required": ("publication redraw", "shared-boundary join"),
        "required": (
            "reviewer view",
            "policy-evaluated plan",
            "shared boundary",
            "decision packet",
            "constrained join",
            "route, scope, and policy meaning",
            "match",
            "trustworthy review meaning",
        ),
    },
    "replacement-gateway": {
        "path": "src/chapter-chapter07/index.md",
        "number": "7.2",
        "caption": "Figure 7.2. Controlled replacement forms a cocone over one shared boundary.",
        "alt_required": ("publication redraw", "shared boundary", "unified gateway"),
        "required": (
            "shared boundary",
            "legacy route mapper",
            "replacement mapper",
            "unified review gateway",
            "`i_l`",
            "`i_r`",
            "`q_l`",
            "`q_r`",
            "two composites",
            "agree",
        ),
    },
    "orchestration-diagram": {
        "path": "src/chapter-chapter08/index.md",
        "number": "8.1",
        "caption": "Figure 8.1. Running example fan-out and synchronization boundary.",
        "alt_required": ("publication redraw", "governed fan-out and synchronization"),
        "required": (
            "review plan",
            "policy-evaluated plan",
            "evidence bundle",
            "decision packet",
            "synchronize for review",
            "approve-or-return",
            "approved change",
            "cannot advance authority independently",
        ),
    },
    "string-diagram-fan-in": {
        "path": "src/chapter-chapter08/index.md",
        "number": "8.2",
        "caption": "Figure 8.2. String-diagram reading distinguishes lawful fan-in from broken summary merges.",
        "alt_required": ("publication redraw", "lawful and broken fan-in"),
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
    "effect-boundary": {
        "path": "src/chapter-chapter09/index.md",
        "number": "9.1",
        "caption": "Figure 9.1. Governed effect chain for the running example.",
        "alt_required": ("publication redraw", "governed effect chain"),
        "required": (
            "review plan",
            "tool call",
            "decision packet",
            "approval write",
            "effect boundary",
            "execution dispatch",
            "execution trace",
            "acceptance evidence",
            "authority changes",
        ),
    },
    "pure-core-effectful-shell": {
        "path": "src/chapter-chapter09/index.md",
        "number": "9.2",
        "caption": "Figure 9.2. Pure checks stay inside the core while governed effects remain in the shell.",
        "alt_required": ("publication redraw", "pure core and effectful shell"),
        "required": (
            "pure core",
            "review plan",
            "scope and route checks",
            "evidence completeness",
            "governed envelope",
            "effectful shell",
            "approval write",
            "dispatch action",
            "trace and evidence",
        ),
    },
    "delivery-case-study": {
        "path": "src/chapter-chapter10/index.md",
        "number": "10.1",
        "caption": "Figure 10.1. End-to-end artifact path for the case study.",
        "alt_required": ("publication redraw", "end-to-end case-study path"),
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


def image_match(text: str, asset_slug: str) -> re.Match[str] | None:
    image_pattern = re.compile(
        rf"^!\[(?P<alt>[^\n]*)\]\([^\n)]*{re.escape(asset_slug)}-screen\.svg\)\s*$",
        re.MULTILINE,
    )
    return image_pattern.search(text)


def long_description_block(text: str, number: str, match: re.Match[str]) -> str | None:
    if match is None:
        return None
    tail = text[match.end() :]
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
        match = image_match(text, slug)
        if match is None:
            errors.append(f"Figure {contract['number']} is missing its publication SVG image")
            continue
        alt_text = normalize(match.group("alt"))
        if not 30 <= len(alt_text) <= 180:
            errors.append(
                f"Figure {contract['number']} alt text must be concise and descriptive: {len(alt_text)} characters"
            )
        if PLACEHOLDER_PATTERN.search(alt_text) or alt_text.lower() in {"diagram", "figure", "image"}:
            errors.append(f"Figure {contract['number']} alt text is generic or contains placeholder text")
        for phrase in contract["alt_required"]:
            if phrase.lower() not in alt_text.lower():
                errors.append(f"Figure {contract['number']} alt text is missing: {phrase}")

        caption = contract["caption"]
        if text.count(caption) != 1 or text.find(caption) > match.start():
            errors.append(f"Figure {contract['number']} must have its canonical claim-bearing caption before the image")

        block = long_description_block(text, contract["number"], match)
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


def validate_pdf(path: Path, figure: dict, errors: list[str]) -> None:
    try:
        data = path.read_bytes()
    except OSError as exc:
        errors.append(f"{path.name}: cannot read generated PDF: {exc}")
        return
    if not data.startswith(b"%PDF-") or len(data) < 1_000:
        errors.append(f"{path.name}: generated PDF is missing or invalid")
        return

    edge_signature = ";".join(
        f"{edge['from']}>{edge['to']}:{edge['label']}" for edge in figure["edges"]
    )
    metadata_view = data.replace(b"\x00", b"").replace(b"\xfe\xff", b"")
    required_metadata = {
        f"/Title ({figure['slug']}-print)".encode(): "title",
        f"/Subject (figure-contract:{figure['slug']}:{edge_signature})".encode(): "edge contract",
        b"/Creator (render-publication-figures.py)": "generator",
        b"/Count 1": "single page",
        f"/Width {figure['width']}".encode(): "canvas width",
        f"/Height {figure['height']}".encode(): "canvas height",
    }
    for token, label in required_metadata.items():
        if token not in metadata_view:
            errors.append(f"{path.name}: missing generated PDF {label} marker")


def validate_assets(root: Path, renderer: ModuleType, errors: list[str]) -> tuple[int, int]:
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

    expected_pdf_names = {f"{slug}-print.pdf" for slug in slugs}
    actual_pdf_names = {path.name for path in asset_dir.glob("*.pdf")}
    if actual_pdf_names != expected_pdf_names:
        errors.append(
            "publication PDF inventory differs from renderer: "
            f"missing={sorted(expected_pdf_names - actual_pdf_names)}, extra={sorted(actual_pdf_names - expected_pdf_names)}"
        )

    checked_svg = 0
    checked_pdf = 0
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
            checked_svg += 1
        pdf_path = asset_dir / f"{figure['slug']}-print.pdf"
        if pdf_path.is_file():
            validate_pdf(pdf_path, figure, errors)
            checked_pdf += 1
    return checked_svg, checked_pdf


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    errors: list[str] = []
    long_descriptions = validate_long_descriptions(root, errors)
    validate_style_guide(root, errors)
    svg_assets = 0
    pdf_assets = 0
    try:
        renderer = load_renderer(root)
        svg_assets, pdf_assets = validate_assets(root, renderer, errors)
    except Exception as exc:  # noqa: BLE001 - emit a stable QA report
        errors.append(f"renderer validation failed: {exc}")

    report = {
        "critical_long_descriptions": long_descriptions,
        "publication_svg_assets": svg_assets,
        "publication_pdf_assets": pdf_assets,
        "errors": errors,
        "status": "ok" if not errors else "failed",
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
