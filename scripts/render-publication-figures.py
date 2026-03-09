#!/usr/bin/env python3

from __future__ import annotations

import html
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "figures" / "publication"


THEMES = {
    "screen": {
        "background": "#fbfcfe",
        "text": "#172033",
        "arrow": "#43516d",
        "object_fill": "#edf4ff",
        "object_stroke": "#5f7db4",
        "decision_fill": "#dde8ff",
        "decision_stroke": "#2f5cb4",
        "evidence_fill": "#edf8f1",
        "evidence_stroke": "#4e8a64",
        "boundary_fill": "#f6f8fc",
        "boundary_stroke": "#75829b",
        "effect_fill": "#fff3dc",
        "effect_stroke": "#b8872f",
    },
    "print": {
        "background": "#ffffff",
        "text": "#111111",
        "arrow": "#333333",
        "object_fill": "#f0f0f0",
        "object_stroke": "#3f3f3f",
        "decision_fill": "#d9d9d9",
        "decision_stroke": "#111111",
        "evidence_fill": "#fafafa",
        "evidence_stroke": "#5a5a5a",
        "boundary_fill": "#ffffff",
        "boundary_stroke": "#6b6b6b",
        "effect_fill": "#efefef",
        "effect_stroke": "#6f6f6f",
    },
}


FIGURES = [
    {
        "slug": "commutative-approval",
        "width": 1080,
        "height": 520,
        "zones": [],
        "nodes": [
            {"id": "cr", "label": "Change Request", "x": 80, "y": 90, "w": 190, "h": 64, "kind": "object"},
            {"id": "rp", "label": "Review Plan", "x": 420, "y": 90, "w": 180, "h": 64, "kind": "object"},
            {"id": "pc", "label": "Policy Check", "x": 420, "y": 280, "w": 180, "h": 64, "kind": "decision"},
            {"id": "ac", "label": "Approved Change", "x": 780, "y": 185, "w": 210, "h": 64, "kind": "decision"},
        ],
        "edges": [
            {"from": "cr", "to": "rp", "label": "derive review plan"},
            {"from": "rp", "to": "ac", "label": "human approval"},
            {"from": "cr", "to": "pc", "label": "policy check"},
            {"from": "pc", "to": "rp", "label": "satisfied"},
            {"from": "cr", "to": "ac", "label": "policy-gated approval path", "bend": 140},
        ],
    },
    {
        "slug": "design-runtime-translation",
        "width": 1320,
        "height": 640,
        "zones": [
            {"x": 60, "y": 80, "w": 520, "h": 460, "label": "Design view", "kind": "boundary"},
            {"x": 740, "y": 80, "w": 520, "h": 460, "label": "Runtime view", "kind": "boundary"},
        ],
        "nodes": [
            {"id": "cr", "label": "Change Request", "x": 110, "y": 130, "w": 190, "h": 64, "kind": "object"},
            {"id": "pc", "label": "Policy Check", "x": 350, "y": 130, "w": 180, "h": 64, "kind": "decision"},
            {"id": "rp", "label": "Review Plan", "x": 350, "y": 280, "w": 180, "h": 64, "kind": "object"},
            {"id": "ac", "label": "Approved Change", "x": 350, "y": 430, "w": 210, "h": 64, "kind": "decision"},
            {"id": "pr", "label": "Pending Request", "x": 790, "y": 130, "w": 190, "h": 64, "kind": "object"},
            {"id": "pl", "label": "Planned Review", "x": 1030, "y": 130, "w": 190, "h": 64, "kind": "object"},
            {"id": "pep", "label": "Policy-Evaluated Plan", "x": 1030, "y": 280, "w": 220, "h": 64, "kind": "decision"},
            {"id": "erc", "label": "Execution-Ready Change", "x": 1030, "y": 430, "w": 220, "h": 64, "kind": "decision"},
        ],
        "edges": [
            {"from": "cr", "to": "pc", "label": "policy check"},
            {"from": "pc", "to": "rp", "label": "satisfied"},
            {"from": "rp", "to": "ac", "label": "human approval"},
            {"from": "pr", "to": "pl", "label": "classify request"},
            {"from": "pl", "to": "pep", "label": "evaluate policy"},
            {"from": "pep", "to": "erc", "label": "request approval"},
            {"from": "cr", "to": "pr", "label": "translate"},
            {"from": "rp", "to": "pl", "label": "translate"},
            {"from": "pc", "to": "pep", "label": "translate"},
            {"from": "ac", "to": "erc", "label": "translate"},
        ],
    },
    {
        "slug": "reviewer-naturality",
        "width": 1080,
        "height": 520,
        "zones": [],
        "nodes": [
            {"id": "rp", "label": "Review Plan", "x": 100, "y": 100, "w": 190, "h": 64, "kind": "object"},
            {"id": "ac", "label": "Approved Change", "x": 770, "y": 100, "w": 210, "h": 64, "kind": "decision"},
            {"id": "dp", "label": "Decision Packet", "x": 100, "y": 300, "w": 210, "h": 64, "kind": "decision"},
            {"id": "ro", "label": "Review Outcome", "x": 770, "y": 300, "w": 210, "h": 64, "kind": "decision"},
        ],
        "edges": [
            {"from": "rp", "to": "ac", "label": "human approval"},
            {"from": "rp", "to": "dp", "label": "package for review"},
            {"from": "dp", "to": "ro", "label": "approve or return"},
            {"from": "ac", "to": "ro", "label": "project review outcome"},
        ],
    },
    {
        "slug": "review-context-product",
        "width": 1080,
        "height": 520,
        "zones": [],
        "nodes": [
            {"id": "crc", "label": "Combined Review Context", "x": 90, "y": 205, "w": 260, "h": 64, "kind": "object"},
            {"id": "rs", "label": "Requested Scope", "x": 700, "y": 90, "w": 210, "h": 64, "kind": "object"},
            {"id": "pr", "label": "Policy Result", "x": 700, "y": 215, "w": 200, "h": 64, "kind": "decision"},
            {"id": "el", "label": "Evidence Links", "x": 700, "y": 340, "w": 210, "h": 64, "kind": "evidence"},
        ],
        "edges": [
            {"from": "crc", "to": "rs", "label": "scope of"},
            {"from": "crc", "to": "pr", "label": "policy status of"},
            {"from": "crc", "to": "el", "label": "evidence links of"},
        ],
    },
    {
        "slug": "variation-paths",
        "width": 1080,
        "height": 520,
        "zones": [],
        "nodes": [
            {"id": "crc", "label": "Combined Review Context", "x": 70, "y": 180, "w": 250, "h": 64, "kind": "object"},
            {"id": "std", "label": "Standard Review Route", "x": 430, "y": 90, "w": 240, "h": 64, "kind": "object"},
            {"id": "esc", "label": "Escalated Review Route", "x": 430, "y": 280, "w": 240, "h": 64, "kind": "object"},
            {"id": "ac", "label": "Approved Change", "x": 800, "y": 180, "w": 210, "h": 64, "kind": "decision"},
        ],
        "edges": [
            {"from": "crc", "to": "std", "label": "enter standard route"},
            {"from": "crc", "to": "esc", "label": "enter escalated route"},
            {"from": "std", "to": "ac", "label": "approve with standard controls"},
            {"from": "esc", "to": "ac", "label": "approve with escalated controls"},
        ],
    },
    {
        "slug": "shared-boundary-join",
        "width": 1160,
        "height": 560,
        "zones": [
            {"x": 430, "y": 160, "w": 250, "h": 180, "label": "Shared boundary", "kind": "boundary"},
        ],
        "nodes": [
            {"id": "rv", "label": "Reviewer View", "x": 80, "y": 130, "w": 190, "h": 64, "kind": "object"},
            {"id": "pep", "label": "Policy-Evaluated Plan", "x": 80, "y": 330, "w": 230, "h": 64, "kind": "decision"},
            {"id": "sb", "label": "Shared Boundary", "x": 455, "y": 220, "w": 200, "h": 64, "kind": "object"},
            {"id": "dp", "label": "Decision Packet", "x": 840, "y": 220, "w": 210, "h": 64, "kind": "decision"},
        ],
        "edges": [
            {"from": "rv", "to": "sb", "label": "project boundary"},
            {"from": "pep", "to": "sb", "label": "project boundary"},
            {"from": "sb", "to": "dp", "label": "permit constrained join"},
        ],
    },
    {
        "slug": "replacement-gateway",
        "width": 1160,
        "height": 560,
        "zones": [
            {"x": 420, "y": 170, "w": 250, "h": 180, "label": "Shared boundary", "kind": "boundary"},
        ],
        "nodes": [
            {"id": "lrm", "label": "Legacy Route Mapper", "x": 70, "y": 110, "w": 230, "h": 64, "kind": "object"},
            {"id": "rm", "label": "Replacement Mapper", "x": 70, "y": 350, "w": 230, "h": 64, "kind": "object"},
            {"id": "sb", "label": "Shared Boundary", "x": 445, "y": 230, "w": 200, "h": 64, "kind": "object"},
            {"id": "urg", "label": "Unified Review Gateway", "x": 840, "y": 230, "w": 240, "h": 64, "kind": "decision"},
        ],
        "edges": [
            {"from": "lrm", "to": "sb", "label": "legacy fields"},
            {"from": "rm", "to": "sb", "label": "mapped fields"},
            {"from": "sb", "to": "urg", "label": "preserved interface"},
        ],
    },
    {
        "slug": "orchestration-diagram",
        "width": 1160,
        "height": 560,
        "zones": [],
        "nodes": [
            {"id": "rp", "label": "Review Plan", "x": 70, "y": 220, "w": 190, "h": 64, "kind": "object"},
            {"id": "pep", "label": "Policy-Evaluated Plan", "x": 420, "y": 110, "w": 250, "h": 64, "kind": "decision"},
            {"id": "eb", "label": "Evidence Bundle", "x": 420, "y": 320, "w": 220, "h": 64, "kind": "evidence"},
            {"id": "dp", "label": "Decision Packet", "x": 800, "y": 220, "w": 200, "h": 64, "kind": "decision"},
            {"id": "ac", "label": "Approved Change", "x": 800, "y": 420, "w": 210, "h": 64, "kind": "decision"},
        ],
        "edges": [
            {"from": "rp", "to": "pep", "label": "evaluate policy"},
            {"from": "rp", "to": "eb", "label": "collect evidence links"},
            {"from": "pep", "to": "dp", "label": "synchronize for review"},
            {"from": "eb", "to": "dp", "label": "synchronize for review"},
            {"from": "dp", "to": "ac", "label": "approve or return"},
        ],
    },
    {
        "slug": "synchronization-boundary",
        "width": 1160,
        "height": 560,
        "zones": [
            {"x": 350, "y": 110, "w": 680, "h": 300, "label": "Synchronization boundary", "kind": "boundary"},
        ],
        "nodes": [
            {"id": "pr", "label": "Plan Revision", "x": 70, "y": 110, "w": 180, "h": 64, "kind": "object"},
            {"id": "pc", "label": "Policy Classification", "x": 70, "y": 240, "w": 210, "h": 64, "kind": "decision"},
            {"id": "el", "label": "Evidence Links", "x": 70, "y": 370, "w": 180, "h": 64, "kind": "evidence"},
            {"id": "dp", "label": "Decision Packet", "x": 760, "y": 235, "w": 220, "h": 64, "kind": "decision"},
        ],
        "edges": [
            {"from": "pr", "to": "dp", "label": "same change identity"},
            {"from": "pc", "to": "dp", "label": "same route semantics"},
            {"from": "el", "to": "dp", "label": "same evidence set"},
        ],
    },
    {
        "slug": "effect-boundary",
        "width": 1180,
        "height": 600,
        "zones": [
            {"x": 420, "y": 80, "w": 680, "h": 420, "label": "Effect boundary", "kind": "effect"},
        ],
        "nodes": [
            {"id": "rp", "label": "Review Plan", "x": 70, "y": 120, "w": 190, "h": 64, "kind": "object"},
            {"id": "dp", "label": "Decision Packet", "x": 70, "y": 320, "w": 200, "h": 64, "kind": "decision"},
            {"id": "tc", "label": "Tool Call", "x": 520, "y": 110, "w": 160, "h": 64, "kind": "effect"},
            {"id": "aw", "label": "Approval Write", "x": 760, "y": 110, "w": 180, "h": 64, "kind": "decision"},
            {"id": "ed", "label": "Execution Dispatch", "x": 760, "y": 290, "w": 200, "h": 64, "kind": "effect"},
            {"id": "tr", "label": "Execution Trace", "x": 520, "y": 400, "w": 180, "h": 64, "kind": "evidence"},
            {"id": "ae", "label": "Acceptance Evidence", "x": 840, "y": 400, "w": 220, "h": 64, "kind": "evidence"},
        ],
        "edges": [
            {"from": "rp", "to": "tc", "label": "prepare bounded inputs"},
            {"from": "dp", "to": "aw", "label": "record approved outcome"},
            {"from": "aw", "to": "ed", "label": "authorize dispatch"},
            {"from": "ed", "to": "tr", "label": "emit trace"},
            {"from": "aw", "to": "ae", "label": "emit decision evidence"},
            {"from": "tr", "to": "ae", "label": "assemble acceptance claim"},
        ],
    },
    {
        "slug": "delivery-case-study",
        "width": 1320,
        "height": 360,
        "zones": [],
        "nodes": [
            {"id": "ps", "label": "Problem Statement", "x": 40, "y": 140, "w": 190, "h": 64, "kind": "object"},
            {"id": "acr", "label": "Acceptance Criteria", "x": 250, "y": 140, "w": 190, "h": 64, "kind": "object"},
            {"id": "das", "label": "Design Artifact Set", "x": 460, "y": 140, "w": 210, "h": 64, "kind": "object"},
            {"id": "dp", "label": "Decision Packet", "x": 700, "y": 140, "w": 200, "h": 64, "kind": "decision"},
            {"id": "ac", "label": "Approved Change", "x": 920, "y": 140, "w": 210, "h": 64, "kind": "decision"},
            {"id": "et", "label": "Execution Trace", "x": 1140, "y": 70, "w": 170, "h": 64, "kind": "evidence"},
            {"id": "ae", "label": "Acceptance Evidence", "x": 1140, "y": 220, "w": 180, "h": 64, "kind": "evidence"},
        ],
        "edges": [
            {"from": "ps", "to": "acr", "label": "fix scope"},
            {"from": "acr", "to": "das", "label": "realize design"},
            {"from": "das", "to": "dp", "label": "assemble review"},
            {"from": "dp", "to": "ac", "label": "approve or return"},
            {"from": "ac", "to": "et", "label": "dispatch and observe"},
            {"from": "et", "to": "ae", "label": "assemble evidence"},
            {"from": "ac", "to": "ae", "label": "record approved outcome"},
        ],
    },
    {
        "slug": "introduction-governed-path",
        "width": 1260,
        "height": 360,
        "zones": [],
        "nodes": [
            {"id": "cr", "label": "Change Request", "x": 60, "y": 140, "w": 190, "h": 64, "kind": "object"},
            {"id": "rp", "label": "Review Plan", "x": 300, "y": 140, "w": 180, "h": 64, "kind": "object"},
            {"id": "dp", "label": "Decision Packet", "x": 540, "y": 140, "w": 210, "h": 64, "kind": "decision"},
            {"id": "ac", "label": "Approved Change", "x": 800, "y": 60, "w": 210, "h": 64, "kind": "decision"},
            {"id": "erc", "label": "Execution-Ready Change", "x": 800, "y": 220, "w": 240, "h": 64, "kind": "decision"},
            {"id": "ae", "label": "Acceptance Evidence", "x": 1080, "y": 140, "w": 190, "h": 64, "kind": "evidence"},
        ],
        "edges": [
            {"from": "cr", "to": "rp", "label": "draft bounded proposal"},
            {"from": "rp", "to": "dp", "label": "synchronize evidence"},
            {"from": "dp", "to": "ac", "label": "human approval"},
            {"from": "ac", "to": "erc", "label": "dispatch governed execution"},
            {"from": "erc", "to": "ae", "label": "emit trace and evidence"},
        ],
    },
    {
        "slug": "responsibility-boundaries",
        "width": 1380,
        "height": 520,
        "zones": [],
        "nodes": [
            {"id": "cr", "label": "Change Request", "x": 60, "y": 210, "w": 190, "h": 64, "kind": "object"},
            {"id": "rp", "label": "Review Plan", "x": 330, "y": 210, "w": 180, "h": 64, "kind": "object"},
            {"id": "dp", "label": "Decision Packet", "x": 600, "y": 210, "w": 210, "h": 64, "kind": "decision"},
            {"id": "ac", "label": "Approved Change", "x": 1140, "y": 110, "w": 210, "h": 64, "kind": "decision"},
            {"id": "adr", "label": "Approval Decision Record", "x": 1140, "y": 210, "w": 220, "h": 64, "kind": "evidence"},
            {"id": "et", "label": "Execution Trace", "x": 1140, "y": 310, "w": 190, "h": 64, "kind": "evidence"},
            {"id": "ae", "label": "Acceptance Evidence", "x": 1140, "y": 410, "w": 210, "h": 64, "kind": "evidence"},
        ],
        "edges": [
            {"from": "cr", "to": "rp", "label": "draft review plan"},
            {"from": "rp", "to": "dp", "label": "synchronize for review"},
            {"from": "dp", "to": "ac", "label": "approve or return"},
            {"from": "dp", "to": "adr", "label": "emit decision evidence"},
            {"from": "ac", "to": "et", "label": "dispatch and observe"},
            {"from": "et", "to": "ae", "label": "assemble acceptance claim"},
        ],
    },
    {
        "slug": "object-composition",
        "width": 1080,
        "height": 520,
        "zones": [],
        "nodes": [
            {"id": "cr", "label": "Change Request", "x": 70, "y": 180, "w": 190, "h": 64, "kind": "object"},
            {"id": "rp", "label": "Review Plan", "x": 430, "y": 90, "w": 180, "h": 64, "kind": "object"},
            {"id": "ac", "label": "Approved Change", "x": 780, "y": 250, "w": 210, "h": 64, "kind": "decision"},
        ],
        "edges": [
            {"from": "cr", "to": "rp", "label": "draft review plan"},
            {"from": "rp", "to": "ac", "label": "human approval"},
            {"from": "cr", "to": "ac", "label": "policy-gated approval", "bend": 160},
        ],
    },
]


def node_theme(kind: str, theme: dict[str, str]) -> tuple[str, str]:
    if kind == "decision":
        return theme["decision_fill"], theme["decision_stroke"]
    if kind == "evidence":
        return theme["evidence_fill"], theme["evidence_stroke"]
    if kind == "effect":
        return theme["effect_fill"], theme["effect_stroke"]
    return theme["object_fill"], theme["object_stroke"]


def node_lookup(nodes: list[dict]) -> dict[str, dict]:
    return {node["id"]: node for node in nodes}


def center(node: dict) -> tuple[float, float]:
    return node["x"] + node["w"] / 2, node["y"] + node["h"] / 2


def edge_points(a: dict, b: dict) -> tuple[float, float, float, float]:
    ax, ay = center(a)
    bx, by = center(b)
    if bx >= ax:
        start_x = a["x"] + a["w"]
        end_x = b["x"]
    else:
        start_x = a["x"]
        end_x = b["x"] + b["w"]
    start_y = ay
    end_y = by
    return start_x, start_y, end_x, end_y


def svg_text(x: float, y: float, text: str, size: int = 22, weight: str = "400") -> str:
    return (
        f'<text x="{x}" y="{y}" fill="currentColor" '
        f'font-family="Helvetica, Arial, sans-serif" font-size="{size}" '
        f'font-weight="{weight}" text-anchor="middle">{html.escape(text)}</text>'
    )


def render_svg(fig: dict, theme_name: str) -> str:
    theme = THEMES[theme_name]
    nodes = node_lookup(fig["nodes"])
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{fig["width"]}" height="{fig["height"]}" viewBox="0 0 {fig["width"]} {fig["height"]}">',
        f'<rect width="100%" height="100%" fill="{theme["background"]}"/>',
        "<defs>",
        f'<marker id="arrow-{theme_name}" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto">',
        f'<path d="M0,0 L12,6 L0,12 z" fill="{theme["arrow"]}"/>',
        "</marker>",
        "</defs>",
        f'<g style="color:{theme["text"]}">',
    ]

    for zone in fig["zones"]:
        stroke = theme["boundary_stroke"] if zone["kind"] == "boundary" else theme["effect_stroke"]
        fill = theme["boundary_fill"] if zone["kind"] == "boundary" else theme["effect_fill"]
        dash = ' stroke-dasharray="12 8"' if zone["kind"] == "boundary" else ""
        parts.append(
            f'<rect x="{zone["x"]}" y="{zone["y"]}" width="{zone["w"]}" height="{zone["h"]}" '
            f'rx="20" ry="20" fill="{fill}" fill-opacity="0.55" stroke="{stroke}" stroke-width="3"{dash}/>'
        )
        parts.append(svg_text(zone["x"] + zone["w"] / 2, zone["y"] - 12, zone["label"], 24, "600"))

    for edge in fig["edges"]:
        start_x, start_y, end_x, end_y = edge_points(nodes[edge["from"]], nodes[edge["to"]])
        label_x = (start_x + end_x) / 2
        label_y = (start_y + end_y) / 2 - 14
        if edge.get("bend"):
            bend = edge["bend"]
            parts.append(
                f'<path d="M {start_x} {start_y} Q {label_x} {start_y + bend} {end_x} {end_y}" '
                f'fill="none" stroke="{theme["arrow"]}" stroke-width="4" marker-end="url(#arrow-{theme_name})"/>'
            )
            label_y = start_y + bend / 2 - 10
        else:
            parts.append(
                f'<line x1="{start_x}" y1="{start_y}" x2="{end_x}" y2="{end_y}" '
                f'stroke="{theme["arrow"]}" stroke-width="4" marker-end="url(#arrow-{theme_name})"/>'
            )
        parts.append(svg_text(label_x, label_y, edge["label"], 20, "500"))

    for node in fig["nodes"]:
        fill, stroke = node_theme(node["kind"], theme)
        parts.append(
            f'<rect x="{node["x"]}" y="{node["y"]}" width="{node["w"]}" height="{node["h"]}" '
            f'rx="18" ry="18" fill="{fill}" stroke="{stroke}" stroke-width="3"/>'
        )
        parts.append(svg_text(node["x"] + node["w"] / 2, node["y"] + node["h"] / 2 + 7, node["label"], 22, "600"))

    parts.append("</g></svg>")
    return "\n".join(parts)


def render_pdf(fig: dict) -> Image.Image:
    theme = THEMES["print"]
    image = Image.new("RGB", (fig["width"], fig["height"]), theme["background"])
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    bold = ImageFont.load_default()
    nodes = node_lookup(fig["nodes"])

    for zone in fig["zones"]:
        stroke = theme["boundary_stroke"] if zone["kind"] == "boundary" else theme["effect_stroke"]
        fill = theme["boundary_fill"] if zone["kind"] == "boundary" else theme["effect_fill"]
        draw.rounded_rectangle(
            [zone["x"], zone["y"], zone["x"] + zone["w"], zone["y"] + zone["h"]],
            radius=18,
            outline=stroke,
            fill=fill,
            width=3,
        )
        draw.text((zone["x"] + 10, zone["y"] - 26), zone["label"], fill=theme["text"], font=bold)

    for edge in fig["edges"]:
        start_x, start_y, end_x, end_y = edge_points(nodes[edge["from"]], nodes[edge["to"]])
        draw.line((start_x, start_y, end_x, end_y), fill=theme["arrow"], width=3)
        draw.polygon(
            [(end_x, end_y), (end_x - 12, end_y - 6), (end_x - 12, end_y + 6)],
            fill=theme["arrow"],
        )
        label_x = (start_x + end_x) / 2
        label_y = (start_y + end_y) / 2 - 18
        if edge.get("bend"):
            label_y = start_y + edge["bend"] / 2 - 10
        draw.text((label_x - 50, label_y), edge["label"], fill=theme["text"], font=font)

    for node in fig["nodes"]:
        fill, stroke = node_theme(node["kind"], theme)
        draw.rounded_rectangle(
            [node["x"], node["y"], node["x"] + node["w"], node["y"] + node["h"]],
            radius=18,
            outline=stroke,
            fill=fill,
            width=3,
        )
        draw.text((node["x"] + 16, node["y"] + 24), node["label"], fill=theme["text"], font=bold)

    return image


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for fig in FIGURES:
        for theme_name in ("screen", "print"):
            svg_path = OUT_DIR / f"{fig['slug']}-{theme_name}.svg"
            svg_path.write_text(render_svg(fig, theme_name), encoding="utf-8")

        pdf_path = OUT_DIR / f"{fig['slug']}-print.pdf"
        render_pdf(fig).save(pdf_path, "PDF", resolution=144.0)


if __name__ == "__main__":
    main()
