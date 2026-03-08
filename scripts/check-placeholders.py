#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOKENS = [
    "TBD",
    "TODO",
    "REPLACE_ME",
    "Working Title",
]
TOKEN_RE = re.compile("|".join(re.escape(token) for token in TOKENS))


def collect_public_files() -> list[Path]:
    files = [
        ROOT / "README.md",
        ROOT / "index.md",
        ROOT / "book-config.json",
        ROOT / "_config.yml",
        ROOT / "_data" / "navigation.json",
    ]
    files.extend(sorted((ROOT / "src").glob("chapter-*/index.md")))
    files.extend(sorted((ROOT / "src" / "appendices").glob("*.md")))
    files.extend(sorted((ROOT / "src" / "additional").glob("**/*.md")))
    files.extend(sorted((ROOT / "src" / "parts").glob("**/*.md")))
    files.extend(sorted((ROOT / "src" / "afterword").glob("**/*.md")))
    files.extend(sorted((ROOT / "src" / "backmatter").glob("**/*.md")))
    return [path for path in files if path.exists()]


def find_issues(path: Path) -> list[dict[str, object]]:
    issues: list[dict[str, object]] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    for line_number, line in enumerate(lines, start=1):
        for match in TOKEN_RE.finditer(line):
            issues.append(
                {
                    "file": str(path.relative_to(ROOT)),
                    "line": line_number,
                    "column": match.start() + 1,
                    "token": match.group(0),
                    "snippet": line.strip(),
                }
            )
    return issues


def main() -> int:
    issues: list[dict[str, object]] = []
    for path in collect_public_files():
        issues.extend(find_issues(path))

    report = {
        "summary": {
            "filesChecked": len(collect_public_files()),
            "issues": len(issues),
        },
        "issues": issues,
    }

    print(json.dumps(report, ensure_ascii=False, indent=2))

    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
