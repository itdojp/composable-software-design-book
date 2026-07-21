#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


CHAPTER_REQUIREMENTS = {
    "opening scope": "one governed-workflow engineering reading",
    "scope boundary": "describe this book's design choice rather than a requirement imposed by category theory",
    "general endofunctor": "a monad on a category `C` consists of an endofunctor `T: C -> C`",
    "unit natural transformation": "a unit natural transformation `eta: Id_C -> T`",
    "multiplication natural transformation": "a multiplication natural transformation `mu: T composed with T -> T`",
    "unit laws": "The unit laws say",
    "associativity law": "the associativity law says",
    "return bind equivalence": "An equivalent programming-oriented presentation uses `return` and `bind`",
    "envelope is an interpretation": "one concrete engineering interpretation of `T`",
    "left identity": "`return a >>= f` is equivalent to `f a`",
    "right identity": "`m >>= return` is equivalent to `m`",
    "bind associativity": "`(m >>= f) >>= g` is equivalent to `m >>= (lambda x: f x >>= g)`",
    "law proof boundary": "engineering test oracles for the chosen envelope, not proofs of those laws",
    "error audit scope": "It is not a consequence of the monad laws alone.",
    "Kleisli arrow": "a Kleisli arrow from `A` to `B` is an arrow `A -> T B`",
    "Kleisli objects": "The Kleisli category has the same objects as the underlying category.",
    "Kleisli versus bind": "A next Kleisli arrow still accepts the underlying value `B` and returns `T C`; it does not have type `T B -> T C`.",
    "bind threading": "Bind or Kleisli composition threads the existing `T B` through that arrow and flattens the result into `T C`.",
    "Kleisli identity": "The Kleisli identity on `A` is `eta_A`",
    "Kleisli composition": "compose as `mu_C composed with T(g) composed with f`",
    "selected M": "this book's chosen instance of `T`",
    "dominant model choice": "not a theorem about monads and not the only valid way to represent multiple effects",
    "transformer alternative": "| Monad transformers or layered composite effects |",
    "effect alternatives": "| Effect handlers or capability interfaces |",
    "state machine alternative": "| Explicit workflow state machine |",
    "selection criterion": "failure, authority, and audit requirements rather than a claim that category theory mandates one dominant envelope",
}

APPENDIX_REQUIREMENTS = {
    "general monad": "**Monad.** On a category `C`, an endofunctor `T: C -> C` equipped with a unit natural transformation `eta: Id_C -> T` and a multiplication natural transformation `mu: T composed with T -> T`",
    "monad laws": "`return` and `bind` with left identity, right identity, and associativity",
    "monad analogy boundary": "one engineering interpretation of this structure, not the general definition",
    "general Kleisli": "arrows `A -> B` represented by underlying arrows `A -> T B`",
    "Kleisli result": "Arrows `A -> T B` and `B -> T C` compose into an arrow `A -> T C`",
    "Kleisli laws": "identities supplied by the unit and associativity supplied by the monad laws",
    "context boundary": "an additional property of the selected `T`, not part of the definition alone",
}

INDEX_REQUIREMENTS = {
    "Monad index scope": "It has a general endofunctor-and-laws definition; the chapter's envelope is one engineering instance.",
    "Kleisli index scope": "It composes arrows `A -> T B`; the chapter then adds governed context and evidence obligations.",
}

PROHIBITED_SIMPLIFICATIONS = {
    "old Monad glossary definition": "**Monad.** A structure that packages effectful computation so later steps must handle its operational context explicitly.",
    "old Kleisli glossary definition": "**Kleisli composition.** The composition rule that chains effectful steps while keeping them inside one explicit effect envelope.",
    "monad equals envelope": "monad is an operational envelope by definition",
    "single model is required": "monads require one dominant effect model",
    "Kleisli arrow accepts envelope": "The next step must accept that envelope and return another one.",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Chapter 09 monad scope boundaries.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    return parser.parse_args()


def require_tokens(label: str, content: str, requirements: dict[str, str], errors: list[str]) -> None:
    for name, token in requirements.items():
        if token not in content:
            errors.append(f"{label}: missing {name}: {token!r}")


def main() -> int:
    root = parse_args().root.resolve()
    paths = {
        "chapter09": root / "src/chapter-chapter09/index.md",
        "appendix-b": root / "src/appendices/appendix-b.md",
        "subject-index": root / "src/backmatter/subject-index/index.md",
    }
    errors: list[str] = []
    content: dict[str, str] = {}
    for label, path in paths.items():
        try:
            content[label] = path.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"{label}: cannot read {path.relative_to(root)}: {exc}")
            content[label] = ""

    require_tokens("chapter09", content["chapter09"], CHAPTER_REQUIREMENTS, errors)
    require_tokens("appendix-b", content["appendix-b"], APPENDIX_REQUIREMENTS, errors)
    require_tokens("subject-index", content["subject-index"], INDEX_REQUIREMENTS, errors)

    combined = "\n".join(content.values()).lower()
    for name, token in PROHIBITED_SIMPLIFICATIONS.items():
        if token.lower() in combined:
            errors.append(f"scope: prohibited {name}: {token!r}")

    report = {
        "contract": "chapter09-monad-scope-v1",
        "checked_files": [str(path.relative_to(root)) for path in paths.values()],
        "requirements": {
            "chapter": len(CHAPTER_REQUIREMENTS),
            "appendix": len(APPENDIX_REQUIREMENTS),
            "subject_index": len(INDEX_REQUIREMENTS),
        },
        "errors": errors,
    }
    print(json.dumps(report, indent=2, ensure_ascii=True))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
