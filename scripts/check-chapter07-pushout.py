#!/usr/bin/env python3

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


EXPECTED_NODES = {
    "sb": "Shared Boundary",
    "lrm": "Legacy Route Mapper",
    "rm": "Replacement Mapper",
    "urg": "Unified Review Gateway",
}
EXPECTED_EDGES = [
    {"from": "sb", "to": "lrm", "label": "legacy boundary map i_L"},
    {"from": "sb", "to": "rm", "label": "replacement boundary map i_R"},
    {"from": "lrm", "to": "urg", "label": "legacy cocone q_L"},
    {"from": "rm", "to": "urg", "label": "replacement cocone q_R"},
]
CHAPTER_REQUIREMENTS = {
    "span directions": "the pushout of the span `L <- B -> R`",
    "boundary-to-legacy map": "`i_L: B -> L`",
    "boundary-to-replacement map": "`i_R: B -> R`",
    "legacy-to-gateway map": "`q_L: L -> P`",
    "replacement-to-gateway map": "`q_R: R -> P`",
    "commutativity": "`q_L ∘ i_L = q_R ∘ i_R`",
    "universal candidate": "every other candidate `Q`",
    "unique mediator": "exactly one map `u: P -> Q`",
    "mediator equations": "`u ∘ q_L = f` and `u ∘ q_R = g`",
    "pullback contrast": "the limit of a cospan `L -> B <- R`",
    "pushout contrast": "the colimit of a span `L <- B -> R`",
    "appendix cross-reference": "[Appendix B](../appendices/appendix-b/)",
    "scope classification": "a pushout-shaped design obligation, not a proof",
    "scope omissions": "without defining all objects, morphisms, or admissible equivalences",
    "scope universal-property limit": "rather than the universal property over every candidate `Q`",
}
APPENDIX_REQUIREMENTS = {
    "pullback direction": "**Pullback.** The limit of a cospan `A -> C <- B`.",
    "pullback universality": "every other object with such agreeing maps factors through it uniquely.",
    "pushout direction": "**Pushout.** The colimit of a span `A <- C -> B`.",
    "pushout universality": "every other object receiving such agreeing maps receives a unique map from the pushout.",
    "analogy boundary": "that analogy is not itself a proof of the universal property.",
}
STALE_LABELS = {"legacy fields", "mapped fields", "preserved interface"}
EXPECTED_NORMALIZED_PDF_SHA256 = "0c94bb073980c581edfea0994fa104c4e0931f9b7635ccd25102c482677b3f7f"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the Chapter 07 pushout contract.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    return parser.parse_args()


def load_figures(path: Path, errors: list[str]) -> list[dict]:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (OSError, SyntaxError) as exc:
        errors.append(f"cannot parse canonical figure source: {exc}")
        return []

    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == "FIGURES" for target in node.targets):
            try:
                value = ast.literal_eval(node.value)
            except (ValueError, SyntaxError) as exc:
                errors.append(f"FIGURES must remain a literal data structure: {exc}")
                return []
            if isinstance(value, list):
                return value
    errors.append("canonical figure source does not define FIGURES")
    return []


def edge_points(source: dict, target: dict) -> tuple[float, float, float, float]:
    source_x = source["x"] + source["w"] / 2
    source_y = source["y"] + source["h"] / 2
    target_x = target["x"] + target["w"] / 2
    target_y = target["y"] + target["h"] / 2
    if target_x >= source_x:
        start_x = source["x"] + source["w"]
        end_x = target["x"]
    else:
        start_x = source["x"]
        end_x = target["x"] + target["w"]
    return float(start_x), float(source_y), float(end_x), float(target_y)


def as_float_tuple(element: ET.Element) -> tuple[float, float, float, float]:
    return tuple(float(element.attrib[name]) for name in ("x1", "y1", "x2", "y2"))  # type: ignore[return-value]


def check_svg(path: Path, figure: dict, errors: list[str]) -> None:
    try:
        root = ET.parse(path).getroot()
    except (OSError, ET.ParseError) as exc:
        errors.append(f"{path.name}: cannot parse generated SVG: {exc}")
        return

    texts = {"".join(element.itertext()).strip() for element in root.iter() if element.tag.endswith("text")}
    required_text = set(EXPECTED_NODES.values()) | {edge["label"] for edge in EXPECTED_EDGES}
    missing_text = sorted(required_text - texts)
    if missing_text:
        errors.append(f"{path.name}: missing generated labels {missing_text!r}")
    present_stale = sorted(STALE_LABELS & texts)
    if present_stale:
        errors.append(f"{path.name}: contains stale labels {present_stale!r}")

    nodes = {node["id"]: node for node in figure["nodes"]}
    expected_lines = {
        edge_points(nodes[edge["from"]], nodes[edge["to"]]) for edge in EXPECTED_EDGES
    }
    actual_lines = {
        as_float_tuple(element) for element in root.iter() if element.tag.endswith("line")
    }
    if actual_lines != expected_lines:
        errors.append(
            f"{path.name}: rendered edge coordinates drifted; expected {sorted(expected_lines)!r}, got {sorted(actual_lines)!r}"
        )


def check_pdf(path: Path, errors: list[str]) -> None:
    try:
        data = path.read_bytes()
    except OSError as exc:
        errors.append(f"{path.name}: cannot read generated PDF: {exc}")
        return
    if not data.startswith(b"%PDF-") or len(data) < 1_000:
        errors.append(f"{path.name}: generated PDF is missing or invalid")
        return
    normalized = re.sub(
        rb"/(CreationDate|ModDate) \(D:\d{14}Z\)",
        rb"/\1 (D:00000000000000Z)",
        data,
    )
    actual_hash = hashlib.sha256(normalized).hexdigest()
    if actual_hash != EXPECTED_NORMALIZED_PDF_SHA256:
        errors.append(
            f"{path.name}: normalized content hash drifted; expected {EXPECTED_NORMALIZED_PDF_SHA256}, got {actual_hash}"
        )


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    chapter_path = root / "src/chapter-chapter07/index.md"
    appendix_path = root / "src/appendices/appendix-b.md"
    figure_list_path = root / "src/backmatter/list-of-figures/index.md"
    renderer_path = root / "scripts/render-publication-figures.py"
    asset_dir = root / "assets/figures/publication"
    errors: list[str] = []

    try:
        chapter = chapter_path.read_text(encoding="utf-8")
        appendix = appendix_path.read_text(encoding="utf-8")
        figure_list = figure_list_path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"cannot read manuscript contract: {exc}")
        chapter = ""
        appendix = ""
        figure_list = ""

    for label, token in CHAPTER_REQUIREMENTS.items():
        if token not in chapter:
            errors.append(f"chapter07: missing {label}: {token!r}")
    for label, token in APPENDIX_REQUIREMENTS.items():
        expected_count = 2 if label == "analogy boundary" else 1
        if appendix.count(token) < expected_count:
            errors.append(f"appendix-b: missing {label}: {token!r}")

    stale_chapter = "Shared Boundary <---- Replacement Mapper"
    if stale_chapter in chapter:
        errors.append("chapter07: stale reversed pushout sketch remains")

    expected_caption = "Controlled replacement forms a cocone over one shared boundary."
    if f"Figure 7.2. {expected_caption}" not in chapter:
        errors.append(f"chapter07: missing synchronized Figure 7.2 caption: {expected_caption!r}")
    if expected_caption not in figure_list:
        errors.append(f"list-of-figures: missing synchronized Figure 7.2 caption: {expected_caption!r}")

    figures = load_figures(renderer_path, errors)
    matching = [figure for figure in figures if figure.get("slug") == "replacement-gateway"]
    if len(matching) != 1:
        errors.append(f"canonical figure source must define one replacement-gateway figure, found {len(matching)}")
    else:
        figure = matching[0]
        actual_nodes = {node.get("id"): node.get("label") for node in figure.get("nodes", [])}
        if actual_nodes != EXPECTED_NODES:
            errors.append(f"canonical replacement-gateway nodes drifted: {actual_nodes!r}")
        if figure.get("edges") != EXPECTED_EDGES:
            errors.append(f"canonical replacement-gateway edges drifted: {figure.get('edges')!r}")
        for theme in ("screen", "print"):
            check_svg(asset_dir / f"replacement-gateway-{theme}.svg", figure, errors)
        check_pdf(asset_dir / "replacement-gateway-print.pdf", errors)

    report = {
        "contract": "chapter07-pushout-v1",
        "checked_files": [
            str(path.relative_to(root))
            for path in (
                chapter_path,
                appendix_path,
                figure_list_path,
                renderer_path,
                asset_dir / "replacement-gateway-screen.svg",
                asset_dir / "replacement-gateway-print.svg",
                asset_dir / "replacement-gateway-print.pdf",
            )
        ],
        "expected_edges": EXPECTED_EDGES,
        "expected_normalized_pdf_sha256": EXPECTED_NORMALIZED_PDF_SHA256,
        "errors": errors,
    }
    print(json.dumps(report, indent=2, ensure_ascii=True))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
