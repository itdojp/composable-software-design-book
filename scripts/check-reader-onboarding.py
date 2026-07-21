#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


DEFAULT_ROOT = Path(__file__).resolve().parents[1]

ONBOARDING_HEADINGS = (
    "## Start Here",
    "## What You Will Be Able to Produce",
    "## Fit and Limits",
    "## Choose a Reading Path",
    "## Why This Book Now",
    "## What Makes This Book Different",
    "## Front Matter",
)

TOP_REQUIREMENTS = {
    "audience": "software architects, staff engineers, technical leads, platform engineers, and AI product builders",
    "prerequisite": "prior exposure to category theory is helpful but not required",
    "book-first sequence": "before inspecting repository artifacts",
    "how-to-use link": "[How to Use This Book](src/additional/how-to-use-this-book/)",
    "reader-fit link": "[Who This Book Is For](src/additional/who-this-book-is-for/)",
    "introduction link": "[Introduction](src/chapter-introduction/)",
    "first chapter link": "[Chapter 01](src/chapter-chapter01/)",
    "responsibility outcome": "A responsibility-boundary map",
    "diagram outcome": "A set of named objects, transformations, and diagrams",
    "decision outcome": "A synchronized decision packet",
    "evidence outcome": "An effect boundary, execution trace, and acceptance-evidence path",
    "applicability": "Use this method when AI-assisted work crosses an approval or execution boundary",
    "non-applicability": "The method is not a prompt-optimization guide, a product comparison, or a substitute",
    "ordinary alternative": "Do not force a categorical abstraction",
    "full path": "**Full method:**",
    "governance path": "**Governance path:**",
    "architecture path": "**Architecture path:**",
    "delivery path": "**Delivery path:**",
    "minimal example": "[minimal example](examples/minimal/policy-gated-change-review/README/)",
    "common example": "[common running example](examples/common/policy-gated-change-review/README/)",
    "related-reader route": "[Categorical Software Design Book](https://itdojp.github.io/categorical-software-design-book/)",
}

FORBIDDEN_TOP_TEXT = (
    "Phase 5 Practical-Connection Review Gate",
    "## Publication Policy",
    "English text is the canonical source for publication",
    "manuscript/ja/",
    "GitHub Copilot",
    "unresolved review threads",
    "maintainer-only",
)

SECTION_REQUIREMENTS = {
    "## Start Here": (
        TOP_REQUIREMENTS["audience"],
        TOP_REQUIREMENTS["prerequisite"],
        TOP_REQUIREMENTS["book-first sequence"],
        TOP_REQUIREMENTS["how-to-use link"],
        TOP_REQUIREMENTS["reader-fit link"],
        TOP_REQUIREMENTS["introduction link"],
        TOP_REQUIREMENTS["first chapter link"],
    ),
    "## What You Will Be Able to Produce": (
        TOP_REQUIREMENTS["responsibility outcome"],
        TOP_REQUIREMENTS["diagram outcome"],
        TOP_REQUIREMENTS["decision outcome"],
        TOP_REQUIREMENTS["evidence outcome"],
    ),
    "## Fit and Limits": (
        TOP_REQUIREMENTS["applicability"],
        TOP_REQUIREMENTS["non-applicability"],
        TOP_REQUIREMENTS["ordinary alternative"],
    ),
    "## Choose a Reading Path": (
        TOP_REQUIREMENTS["full path"],
        TOP_REQUIREMENTS["governance path"],
        TOP_REQUIREMENTS["architecture path"],
        TOP_REQUIREMENTS["delivery path"],
        TOP_REQUIREMENTS["minimal example"],
        TOP_REQUIREMENTS["common example"],
    ),
}

HOW_TO_REQUIREMENTS = (
    "the book carries the primary reading experience",
    "## Read it front to back if you are adopting the full method",
    "## Start with the governance path if your urgent problem is authority and review",
    "## Start with the architecture path if your urgent problem is model integrity",
    "## Start with the delivery path if your urgent problem is orchestration",
    "Do not reverse the dependency.",
)

EDITORIAL_REQUIREMENTS = (
    "## Phase 5 Practical-Connection Review Gate",
    "maintainer-only editorial gate",
    "rather than placing it in the public landing-page onboarding flow",
    "preserved structure or invariant",
    "non-applicability condition",
)

PUBLISHING_REQUIREMENTS = (
    "## Canonical Source and Related-Book Boundary",
    "English text in this repository is the canonical publication source",
    "Japanese drafts under `manuscript/ja/` are editorial inputs",
    "related but independent Japanese reader-facing book",
    "not a rename, replacement, or translation chain",
    "public landing page should expose only the reader-relevant route",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate reader-first public landing-page onboarding.")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT, help="Repository root to validate.")
    return parser.parse_args()


def read(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"cannot read {path}: {exc}")
        return ""


def validate_top(text: str, errors: list[str]) -> None:
    heading_positions: list[int] = []
    for heading in ONBOARDING_HEADINGS:
        if text.count(heading) != 1:
            errors.append(f"public top must contain exactly one heading: {heading}")
            continue
        heading_positions.append(text.index(heading))
    if len(heading_positions) == len(ONBOARDING_HEADINGS) and heading_positions != sorted(heading_positions):
        errors.append("public top reader-onboarding headings are out of order")

    body_headings = re.findall(r"^#{1,2} .+$", text, re.MULTILINE)
    if len(body_headings) < 2 or body_headings[1] != "## Start Here":
        errors.append("Start Here must be the first H2 after the book title")

    for label, token in TOP_REQUIREMENTS.items():
        if token not in text:
            errors.append(f"public top is missing {label}: {token}")
    for token in FORBIDDEN_TOP_TEXT:
        if token in text:
            errors.append(f"public top exposes maintainer/editorial process text: {token}")

    for heading, tokens in SECTION_REQUIREMENTS.items():
        start = text.find(heading)
        if start < 0:
            continue
        following = text[start + len(heading) :]
        next_heading = re.search(r"^## ", following, re.MULTILINE)
        section = following[: next_heading.start()] if next_heading else following
        for token in tokens:
            if token not in section:
                errors.append(f"{heading} is missing reader-onboarding content: {token}")

    front_matter = text.split("---", 2)[1] if text.startswith("---") and text.count("---") >= 2 else ""
    required_metadata = {
        'title: "Compositional Software Design for Agentic Systems"',
        'subtitle: "A Category-Theoretic Guide to Human-AI Boundaries and Verifiable Engineering"',
        'description: "A practical guide to governed AI-assisted software delivery using composition, diagrams, and effect boundaries that remain auditable and verifiable."',
        'layout: book',
    }
    for token in required_metadata:
        if token not in front_matter:
            errors.append(f"public top front matter drifted: {token}")


def validate_tokens(name: str, text: str, tokens: tuple[str, ...], errors: list[str]) -> None:
    for token in tokens:
        if token not in text:
            errors.append(f"{name} is missing contract text: {token}")


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    errors: list[str] = []
    paths = {
        "public top": root / "index.md",
        "How to Use": root / "src" / "additional" / "how-to-use-this-book" / "index.md",
        "editorial checklist": root / "project-management" / "editorial-checklist.md",
        "publishing setup": root / "project-management" / "publishing-setup.md",
    }
    content = {name: read(path, errors) for name, path in paths.items()}
    validate_top(content["public top"], errors)
    validate_tokens("How to Use", content["How to Use"], HOW_TO_REQUIREMENTS, errors)
    validate_tokens("editorial checklist", content["editorial checklist"], EDITORIAL_REQUIREMENTS, errors)
    validate_tokens("publishing setup", content["publishing setup"], PUBLISHING_REQUIREMENTS, errors)

    report = {
        "checked_files": [str(path.relative_to(root)) for path in paths.values()],
        "onboarding_headings": list(ONBOARDING_HEADINGS),
        "top_requirements": len(TOP_REQUIREMENTS),
        "forbidden_process_terms": len(FORBIDDEN_TOP_TEXT),
        "errors": errors,
        "status": "ok" if not errors else "failed",
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
