#!/usr/bin/env python3

from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CACHE_DIR = ROOT / ".cache"
CHECKER = ROOT / "scripts" / "check-publication-figure-accessibility.py"

COPY_PATHS = (
    "scripts/render-publication-figures.py",
    "scripts/check-publication-figure-accessibility.py",
    "assets/figures/publication",
    "docs/style/diagram-style.md",
    "src/chapter-chapter03/index.md",
    "src/chapter-chapter08/index.md",
    "src/chapter-chapter10/index.md",
)


def copy_fixture(destination: Path) -> None:
    for relative in COPY_PATHS:
        source = ROOT / relative
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.is_dir():
            shutil.copytree(source, target)
        else:
            shutil.copy2(source, target)


def run_checker(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["python3", str(CHECKER), "--root", str(root)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"mutation source not found in {path}: {old}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def negative_case(name: str, relative: str, old: str, new: str) -> tuple[str, bool, str]:
    with tempfile.TemporaryDirectory(prefix="figure-a11y-negative-", dir=CACHE_DIR) as temp_dir:
        fixture = Path(temp_dir)
        copy_fixture(fixture)
        replace_once(fixture / relative, old, new)
        result = run_checker(fixture)
        return name, result.returncode != 0, result.stdout or result.stderr


def main() -> int:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="figure-a11y-positive-", dir=CACHE_DIR) as temp_dir:
        fixture = Path(temp_dir)
        copy_fixture(fixture)
        positive = run_checker(fixture)
    if positive.returncode != 0:
        print(positive.stdout)
        print(positive.stderr)
        return 1

    cases = (
        (
            "missing Figure 3.2 long description",
            "src/chapter-chapter03/index.md",
            "**Long description — Figure 3.2.**",
            "**Figure notes — Figure 3.2.**",
        ),
        (
            "missing Figure 8.2 long description",
            "src/chapter-chapter08/index.md",
            "**Long description — Figure 8.2.**",
            "**Figure notes — Figure 8.2.**",
        ),
        (
            "missing Figure 10.1 long description",
            "src/chapter-chapter10/index.md",
            "**Long description — Figure 10.1.**",
            "**Figure notes — Figure 10.1.**",
        ),
        (
            "Figure 3.2 omits plan revision",
            "src/chapter-chapter03/index.md",
            "plan revision",
            "plan version",
        ),
        (
            "Figure 3.2 does not borrow required text from following prose",
            "src/chapter-chapter03/index.md",
            "same request scope, policy result",
            "same scope, policy result",
        ),
        (
            "Figure 8.2 omits broken mutable context",
            "src/chapter-chapter08/index.md",
            "mutable context",
            "runtime input",
        ),
        (
            "Figure 10.1 omits review authority",
            "src/chapter-chapter10/index.md",
            "review authority",
            "review stage",
        ),
        (
            "style guide omits distinct deliverables",
            "docs/style/diagram-style.md",
            "four distinct deliverables",
            "related deliverables",
        ),
        (
            "SVG omits role",
            "assets/figures/publication/commutative-approval-screen.svg",
            ' role="img"',
            "",
        ),
        (
            "SVG omits aria-labelledby",
            "assets/figures/publication/commutative-approval-screen.svg",
            ' aria-labelledby="commutative-approval-screen-title commutative-approval-screen-description"',
            "",
        ),
        (
            "SVG omits title",
            "assets/figures/publication/commutative-approval-screen.svg",
            '<title id="commutative-approval-screen-title">Repository-level approval paths and policy dependency</title>',
            "",
        ),
        (
            "SVG omits description",
            "assets/figures/publication/commutative-approval-screen.svg",
            '<desc id="commutative-approval-screen-description">',
            '<metadata id="commutative-approval-screen-description">',
        ),
        (
            "SVG has empty title",
            "assets/figures/publication/commutative-approval-screen.svg",
            "Repository-level approval paths and policy dependency",
            "",
        ),
        (
            "SVG has placeholder description",
            "assets/figures/publication/commutative-approval-screen.svg",
            "A change request reaches an approved change",
            "TODO placeholder",
        ),
        (
            "SVG has dangling labelledby reference",
            "assets/figures/publication/commutative-approval-screen.svg",
            "commutative-approval-screen-description",
            "missing-description",
        ),
        (
            "SVG has duplicate IDs",
            "assets/figures/publication/commutative-approval-screen.svg",
            '<rect width="100%" height="100%"',
            '<rect id="commutative-approval-screen-title" width="100%" height="100%"',
        ),
        (
            "generated SVG drifts from renderer",
            "assets/figures/publication/delivery-case-study-print.svg",
            "End-to-end governed artifact path",
            "End-to-end artifact sequence",
        ),
        (
            "renderer accessibility title is empty",
            "scripts/render-publication-figures.py",
            '"title": "Repository-level approval paths and policy dependency"',
            '"title": ""',
        ),
    )

    results = [negative_case(*case) for case in cases]
    failed = [(name, output) for name, detected, output in results if not detected]
    report = {
        "negative_detected": len(results) - len(failed),
        "negative_total": len(results),
        "positive_passed": 1,
        "positive_total": 1,
        "undetected": [name for name, _ in failed],
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    if failed:
        for name, output in failed:
            print(f"\n--- undetected mutation: {name} ---\n{output}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
