#!/usr/bin/env python3

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts/check-chapter09-monad-scope.py"
FILES = [
    Path("src/chapter-chapter09/index.md"),
    Path("src/appendices/appendix-b.md"),
    Path("src/backmatter/subject-index/index.md"),
]


def replace_text(root: Path, relative: str, old: str, new: str) -> None:
    path = root / relative
    content = path.read_text(encoding="utf-8")
    if old not in content:
        raise RuntimeError(f"fixture token not found in {relative}: {old!r}")
    path.write_text(content.replace(old, new, 1), encoding="utf-8")


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
    mutations: list[tuple[str, Callable[[Path], None]]] = [
        ("remove opening scope", lambda root: replace_text(root, "src/chapter-chapter09/index.md", "one governed-workflow engineering reading", "one general definition")),
        ("remove endofunctor", lambda root: replace_text(root, "src/chapter-chapter09/index.md", "a monad on a category `C` consists of an endofunctor `T: C -> C`", "a monad packages a computation")),
        ("remove unit", lambda root: replace_text(root, "src/chapter-chapter09/index.md", "a unit natural transformation `eta: Id_C -> T`", "a way to wrap values")),
        ("remove multiplication", lambda root: replace_text(root, "src/chapter-chapter09/index.md", "a multiplication natural transformation `mu: T composed with T -> T`", "a way to flatten values")),
        ("remove associativity", lambda root: replace_text(root, "src/chapter-chapter09/index.md", "the associativity law says", "a practical guideline says")),
        ("remove return bind equivalence", lambda root: replace_text(root, "src/chapter-chapter09/index.md", "An equivalent programming-oriented presentation uses `return` and `bind`", "A programming analogy mentions return and bind")),
        ("remove law proof boundary", lambda root: replace_text(root, "src/chapter-chapter09/index.md", "engineering test oracles for the chosen envelope, not proofs of those laws", "proofs of those laws")),
        ("turn error behavior into law", lambda root: replace_text(root, "src/chapter-chapter09/index.md", "It is not a consequence of the monad laws alone.", "It follows from the monad laws.")),
        ("remove Kleisli arrow", lambda root: replace_text(root, "src/chapter-chapter09/index.md", "a Kleisli arrow from `A` to `B` is an arrow `A -> T B`", "a Kleisli arrow chains envelopes")),
        ("make Kleisli arrow accept envelope", lambda root: replace_text(root, "src/chapter-chapter09/index.md", "A next Kleisli arrow still accepts the underlying value `B` and returns `T C`; it does not have type `T B -> T C`.", "The next step must accept that envelope and return another one.")),
        ("remove Kleisli identity", lambda root: replace_text(root, "src/chapter-chapter09/index.md", "The Kleisli identity on `A` is `eta_A`", "Kleisli composition has an identity")),
        ("remove Kleisli formula", lambda root: replace_text(root, "src/chapter-chapter09/index.md", "compose as `mu_C composed with T(g) composed with f`", "compose in sequence")),
        ("make dominant model mandatory", lambda root: replace_text(root, "src/chapter-chapter09/index.md", "not a theorem about monads and not the only valid way to represent multiple effects", "required by monads")),
        ("remove transformer alternative", lambda root: replace_text(root, "src/chapter-chapter09/index.md", "| Monad transformers or layered composite effects |", "| One combined effect |")),
        ("remove effect-handler alternative", lambda root: replace_text(root, "src/chapter-chapter09/index.md", "| Effect handlers or capability interfaces |", "| Another envelope |")),
        ("remove state-machine alternative", lambda root: replace_text(root, "src/chapter-chapter09/index.md", "| Explicit workflow state machine |", "| Another abstraction |")),
        ("restore simplified Monad glossary", lambda root: replace_text(root, "src/appendices/appendix-b.md", "**Monad.** On a category `C`, an endofunctor `T: C -> C` equipped with a unit natural transformation `eta: Id_C -> T` and a multiplication natural transformation `mu: T composed with T -> T` that satisfy the unit and associativity laws.", "**Monad.** A structure that packages effectful computation so later steps must handle its operational context explicitly.")),
        ("restore simplified Kleisli glossary", lambda root: replace_text(root, "src/appendices/appendix-b.md", "**Kleisli composition.** The Kleisli category has the same objects as the underlying category and arrows `A -> B` represented by underlying arrows `A -> T B`.", "**Kleisli composition.** The composition rule that chains effectful steps while keeping them inside one explicit effect envelope.")),
        ("remove Monad index scope", lambda root: replace_text(root, "src/backmatter/subject-index/index.md", "It has a general endofunctor-and-laws definition; the chapter's envelope is one engineering instance.", "It gives the chapter's effect envelope.")),
        ("remove Kleisli index scope", lambda root: replace_text(root, "src/backmatter/subject-index/index.md", "It composes arrows `A -> T B`; the chapter then adds governed context and evidence obligations.", "It chains governed envelopes.")),
    ]

    scratch_parent = ROOT / "qa-reports"
    scratch_parent.mkdir(parents=True, exist_ok=True)
    failures: list[str] = []
    negative_passed = 0
    positive_passed = 0
    with tempfile.TemporaryDirectory(prefix="issue93-monad-scope-", dir=scratch_parent) as temp_dir:
        temp_root = Path(temp_dir)
        baseline = temp_root / "baseline"
        copy_fixture(baseline)
        if run_checker(baseline).returncode == 0:
            positive_passed = 1
        else:
            failures.append("positive fixture failed")

        for index, (name, mutate) in enumerate(mutations, start=1):
            case_root = temp_root / f"case-{index:02d}"
            copy_fixture(case_root)
            try:
                mutate(case_root)
            except Exception as exc:
                failures.append(f"{name}: mutation failed: {exc}")
                continue
            result = run_checker(case_root)
            if result.returncode == 0:
                failures.append(f"{name}: checker accepted the mutated fixture")
            else:
                negative_passed += 1

    report = {
        "contract": "chapter09-monad-scope-regression-v1",
        "positive": {"passed": positive_passed, "total": 1},
        "negative": {"passed": negative_passed, "total": len(mutations)},
        "failures": failures,
    }
    print(json.dumps(report, indent=2, ensure_ascii=True))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
