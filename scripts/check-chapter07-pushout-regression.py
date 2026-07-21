#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts/check-chapter07-pushout.py"
FILES = [
    Path("src/chapter-chapter07/index.md"),
    Path("src/appendices/appendix-b.md"),
    Path("src/backmatter/list-of-figures/index.md"),
    Path("examples/common/policy-gated-change-review/design/replacement-plan.md"),
    Path("scripts/render-publication-figures.py"),
    Path("assets/figures/publication/replacement-gateway-screen.svg"),
    Path("assets/figures/publication/replacement-gateway-print.svg"),
    Path("assets/figures/publication/replacement-gateway-print.pdf"),
]


def replace_text(root: Path, relative: str, old: str, new: str) -> None:
    path = root / relative
    content = path.read_text(encoding="utf-8")
    if old not in content:
        raise RuntimeError(f"fixture token not found in {relative}: {old!r}")
    path.write_text(content.replace(old, new, 1), encoding="utf-8")


def replace_regex(root: Path, relative: str, pattern: str, replacement: str) -> None:
    path = root / relative
    content = path.read_text(encoding="utf-8")
    updated, count = re.subn(pattern, replacement, content, count=1)
    if count != 1:
        raise RuntimeError(
            f"fixture pattern matched {count} times in {relative}: {pattern!r}"
        )
    path.write_text(updated, encoding="utf-8")


def reverse_figure_edge(root: Path, source: str, target: str) -> None:
    replace_regex(
        root,
        "scripts/render-publication-figures.py",
        rf'\{{"from"\s*:\s*"{re.escape(source)}"\s*,\s*"to"\s*:\s*"{re.escape(target)}"',
        f'{{"from": "{target}", "to": "{source}"',
    )


def copy_fixture(destination: Path) -> None:
    for relative in FILES:
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / relative, target)


def run_checker(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CHECKER), "--root", str(root)],
        check=False,
        capture_output=True,
        text=True,
    )


def main() -> int:
    scratch_parent = ROOT / "qa-reports"
    scratch_parent.mkdir(parents=True, exist_ok=True)
    failures: list[str] = []
    passed_negative = 0

    mutations: list[tuple[str, Callable[[Path], None]]] = [
        (
            "reverse boundary-to-legacy edge",
            lambda root: reverse_figure_edge(root, "sb", "lrm"),
        ),
        (
            "reverse boundary-to-replacement edge",
            lambda root: reverse_figure_edge(root, "sb", "rm"),
        ),
        (
            "reverse legacy cocone edge",
            lambda root: reverse_figure_edge(root, "lrm", "urg"),
        ),
        (
            "reverse replacement cocone edge",
            lambda root: reverse_figure_edge(root, "rm", "urg"),
        ),
        (
            "remove commutativity equation",
            lambda root: replace_text(root, "src/chapter-chapter07/index.md", "`q_L ∘ i_L = q_R ∘ i_R`", "`q_L and q_R should agree`"),
        ),
        (
            "remove universal candidate",
            lambda root: replace_text(root, "src/chapter-chapter07/index.md", "every other candidate `Q`", "another candidate"),
        ),
        (
            "remove unique mediator",
            lambda root: replace_text(root, "src/chapter-chapter07/index.md", "exactly one map `u: P -> Q`", "a map from the gateway"),
        ),
        (
            "remove mediator equations",
            lambda root: replace_text(root, "src/chapter-chapter07/index.md", "`u ∘ q_L = f` and `u ∘ q_R = g`", "the expected triangles commute"),
        ),
        (
            "reverse chapter span",
            lambda root: replace_text(root, "src/chapter-chapter07/index.md", "the pushout of the span `L <- B -> R`", "the pushout of `L -> B <- R`"),
        ),
        (
            "remove pullback contrast",
            lambda root: replace_text(root, "src/chapter-chapter07/index.md", "the limit of a cospan `L -> B <- R`", "a compatible join"),
        ),
        (
            "remove scope classification",
            lambda root: replace_text(root, "src/chapter-chapter07/index.md", "a pushout-shaped design obligation, not a proof", "a pushout proof"),
        ),
        (
            "remove appendix link",
            lambda root: replace_text(root, "src/chapter-chapter07/index.md", "[Appendix B](../appendices/appendix-b/)", "Appendix B"),
        ),
        (
            "reverse appendix pushout",
            lambda root: replace_text(root, "src/appendices/appendix-b.md", "**Pushout.** The colimit of a span `A <- C -> B`.", "**Pushout.** The colimit of a cospan `A -> C <- B`."),
        ),
        (
            "reverse appendix pullback",
            lambda root: replace_text(root, "src/appendices/appendix-b.md", "**Pullback.** The limit of a cospan `A -> C <- B`.", "**Pullback.** The limit of a span `A <- C -> B`."),
        ),
        (
            "drift list-of-figures caption",
            lambda root: replace_text(root, "src/backmatter/list-of-figures/index.md", "Controlled replacement forms a cocone over one shared boundary.", "Controlled replacement stays anchored to one shared boundary."),
        ),
        (
            "drift Chapter 07 caption",
            lambda root: replace_text(root, "src/chapter-chapter07/index.md", "Figure 7.2. Controlled replacement forms a cocone over one shared boundary.", "Figure 7.2. Controlled replacement stays anchored to one shared boundary."),
        ),
        (
            "remove replacement component",
            lambda root: replace_text(root, "examples/common/policy-gated-change-review/design/replacement-plan.md", "- Replacement Mapper\n", ""),
        ),
        (
            "remove canonical gateway agreement",
            lambda root: replace_text(root, "examples/common/policy-gated-change-review/design/replacement-plan.md", "Map both outputs into the Unified Review Gateway only when their composites from the Review Boundary Contract agree.", "Compare both outputs before cutover."),
        ),
        (
            "remove replacement span arrow",
            lambda root: replace_text(root, "examples/common/policy-gated-change-review/design/replacement-plan.md", "`i_R`: Change Identity -> Change Identity", "Replacement fields remain canonical"),
        ),
        (
            "conflate comparison adapter with span arrows",
            lambda root: replace_text(root, "src/chapter-chapter07/index.md", "This comparison adapter runs from implementation-native fields back to the boundary and is not one of the formal span arrows `B -> L` and `B -> R`.", "This schema mapping defines the pushout span."),
        ),
        (
            "stale generated SVG label",
            lambda root: replace_text(root, "assets/figures/publication/replacement-gateway-screen.svg", "legacy boundary map i_L", "legacy fields"),
        ),
        (
            "stale but valid generated PDF",
            lambda root: (root / "assets/figures/publication/replacement-gateway-print.pdf").write_bytes(
                (ROOT / "assets/figures/publication/shared-boundary-join-print.pdf").read_bytes()
            ),
        ),
        (
            "invalid generated PDF",
            lambda root: (root / "assets/figures/publication/replacement-gateway-print.pdf").write_bytes(b"not a PDF"),
        ),
    ]

    with tempfile.TemporaryDirectory(prefix="issue92-pushout-", dir=scratch_parent) as temp_dir:
        temp_root = Path(temp_dir)
        baseline = temp_root / "baseline"
        copy_fixture(baseline)
        positive = run_checker(baseline)
        if positive.returncode != 0:
            failures.append(f"positive fixture failed: {positive.stdout}{positive.stderr}")

        for index, (name, mutate) in enumerate(mutations, start=1):
            case_root = temp_root / f"case-{index:02d}"
            copy_fixture(case_root)
            try:
                mutate(case_root)
            except Exception as exc:  # fixture construction failure must fail the regression suite
                failures.append(f"{name}: mutation failed: {exc}")
                continue
            result = run_checker(case_root)
            if result.returncode == 0:
                failures.append(f"{name}: checker accepted the mutated fixture")
            else:
                passed_negative += 1

    report = {
        "contract": "chapter07-pushout-regression-v1",
        "positive": {"passed": 0 if failures and failures[0].startswith("positive fixture") else 1, "total": 1},
        "negative": {"passed": passed_negative, "total": len(mutations)},
        "failures": failures,
    }
    print(json.dumps(report, indent=2, ensure_ascii=True))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
