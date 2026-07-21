#!/usr/bin/env python3

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CACHE_DIR = ROOT / ".cache"
CHECKER = ROOT / "scripts" / "check-reader-onboarding.py"
FILES = (
    "index.md",
    "src/additional/how-to-use-this-book/index.md",
    "project-management/editorial-checklist.md",
    "project-management/publishing-setup.md",
)


def copy_fixture(destination: Path) -> None:
    for relative in FILES:
        source = ROOT / relative
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def run_checker(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CHECKER), "--root", str(root)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def replace_once(root: Path, relative: str, old: str, new: str) -> None:
    path = root / relative
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"mutation source not found in {relative}: {old}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def main() -> int:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    mutations = (
        ("remove Start Here", "index.md", "## Start Here", "## Reader Notes"),
        ("remove target audience", "index.md", "software architects, staff engineers, technical leads, platform engineers, and AI product builders", "software teams"),
        ("make category theory required", "index.md", "prior exposure to category theory is helpful but not required", "prior exposure to category theory is required"),
        ("remove book-first sequence", "index.md", "before inspecting repository artifacts", "while inspecting repository artifacts"),
        ("remove How to Use route", "index.md", "[How to Use This Book](src/additional/how-to-use-this-book/)", "How to Use This Book"),
        ("remove first chapter route", "index.md", "[Chapter 01](src/chapter-chapter01/)", "Chapter 01"),
        ("remove responsibility outcome", "index.md", "A responsibility-boundary map", "A general overview"),
        ("remove decision outcome", "index.md", "A synchronized decision packet", "A review document"),
        ("remove applicability", "index.md", "Use this method when AI-assisted work crosses an approval or execution boundary", "This method is broadly useful"),
        ("remove non-applicability", "index.md", "The method is not a prompt-optimization guide, a product comparison, or a substitute", "The method complements"),
        ("remove ordinary alternative", "index.md", "Do not force a categorical abstraction", "Prefer a categorical abstraction"),
        ("remove governance path", "index.md", "**Governance path:**", "**Selected chapters:**"),
        ("remove delivery path", "index.md", "**Delivery path:**", "**Operational chapters:**"),
        ("remove minimal example", "index.md", "[minimal example](examples/minimal/policy-gated-change-review/README/)", "minimal example"),
        ("expose Phase 5 on top", "index.md", "## Front Matter", "## Phase 5 Practical-Connection Review Gate\n\nInternal review text.\n\n## Front Matter"),
        ("expose publication policy on top", "index.md", "## Related Reading", "## Publication Policy\n\nEnglish text is the canonical source for publication.\n\n## Related Reading"),
        ("drift top metadata", "index.md", 'layout: book', 'layout: default'),
        ("remove How to Use book-first contract", "src/additional/how-to-use-this-book/index.md", "the book carries the primary reading experience", "the repository carries the primary reading experience"),
        ("remove maintainer-only relocation", "project-management/editorial-checklist.md", "maintainer-only editorial gate", "editorial gate"),
        ("remove non-applicability editorial check", "project-management/editorial-checklist.md", "non-applicability condition", "application condition"),
        ("remove canonical source relocation", "project-management/publishing-setup.md", "English text in this repository is the canonical publication source", "English text is a publication source"),
        ("collapse related-book boundary", "project-management/publishing-setup.md", "related but independent Japanese reader-facing book", "Japanese edition"),
        ("remove reader-only public route", "project-management/publishing-setup.md", "public landing page should expose only the reader-relevant route", "public landing page should expose the repository workflow"),
    )

    failures: list[str] = []
    passed_negative = 0
    with tempfile.TemporaryDirectory(prefix="reader-onboarding-", dir=CACHE_DIR) as temp_dir:
        temp_root = Path(temp_dir)
        baseline = temp_root / "baseline"
        copy_fixture(baseline)
        positive = run_checker(baseline)
        if positive.returncode != 0:
            failures.append(f"positive fixture failed: {positive.stdout}{positive.stderr}")

        for index, (name, relative, old, new) in enumerate(mutations, start=1):
            fixture = temp_root / f"case-{index:02d}"
            copy_fixture(fixture)
            try:
                replace_once(fixture, relative, old, new)
            except Exception as exc:
                failures.append(f"{name}: mutation failed: {exc}")
                continue
            result = run_checker(fixture)
            if result.returncode == 0:
                failures.append(f"{name}: checker accepted the mutated fixture")
            else:
                passed_negative += 1

    report = {
        "positive_passed": 0 if failures and failures[0].startswith("positive fixture") else 1,
        "positive_total": 1,
        "negative_detected": passed_negative,
        "negative_total": len(mutations),
        "failures": failures,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
