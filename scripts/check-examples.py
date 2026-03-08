#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MINIMAL_DIR = ROOT / "examples" / "minimal" / "policy-gated-change-review"
COMMON_DIR = ROOT / "examples" / "common" / "policy-gated-change-review"
REQUIRED_COMMON_ARTIFACTS = {
    "spec/problem-statement.md",
    "spec/acceptance-criteria.md",
    "design/artifact-map.md",
    "design/commutative-diagram.md",
    "design/variation-paths.md",
    "design/shared-boundary.md",
    "design/replacement-plan.md",
    "verification/review-checks.md",
    "verification/traceability-matrix.md",
    "verification/coherence-failure.md",
    "verification/acceptance-evidence.md",
    "runtime/runtime-view.md",
    "review/reviewer-view.md",
    "implementation/workflow.md",
    "implementation/orchestration-diagram.md",
    "implementation/synchronization-boundary.md",
    "implementation/effect-boundary.md",
    "implementation/execution-trace.md",
}
REQUIRED_MARKDOWN_SECTIONS = {
    "implementation/orchestration-diagram.md": [
        "## Sequential Spine",
        "## Parallel Branches",
        "## Fan-In Rule",
    ],
    "implementation/synchronization-boundary.md": [
        "## Boundary Elements",
        "## Synchronization Rules",
        "## Failure Isolation Rules",
    ],
    "implementation/effect-boundary.md": [
        "## Pure Core",
        "## Effectful Steps",
        "## Boundary Rules",
    ],
    "implementation/execution-trace.md": [
        "## Trace Fields",
        "## Representative Trace",
        "## Trace Rules",
    ],
    "verification/acceptance-evidence.md": [
        "## Required Evidence",
        "## Acceptance Rule",
        "## Return-For-Rework Rule",
    ],
}
TRACEABILITY_REQUIRED_IDS = {
    "PGCR-01",
    "PGCR-02",
    "PGCR-03",
    "PGCR-04",
    "PGCR-05",
    "PGCR-06",
}
TRACEABILITY_REQUIRED_PATHS = {
    "implementation/synchronization-boundary.md",
    "implementation/effect-boundary.md",
    "implementation/execution-trace.md",
    "verification/acceptance-evidence.md",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []

    running_example = ROOT / "project-management" / "running-example.md"
    artifact_decision = ROOT / "project-management" / "artifact-location-decision.md"
    minimal_manifest_path = MINIMAL_DIR / "manifest.json"
    common_manifest_path = COMMON_DIR / "manifest.json"

    for path in [running_example, artifact_decision, minimal_manifest_path, common_manifest_path]:
        if not path.exists():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    minimal = load_json(minimal_manifest_path)
    common = load_json(common_manifest_path)
    book_config = load_json(ROOT / "book-config.json")
    chapter_ids = [chapter["id"] for chapter in book_config["structure"]["chapters"]]

    if minimal.get("example_id") != "policy-gated-change-review":
        errors.append("minimal example_id must be policy-gated-change-review")
    if common.get("example_id") != "policy-gated-change-review":
        errors.append("common example_id must be policy-gated-change-review")

    if minimal.get("scope") != "minimal":
        errors.append("minimal manifest scope must be minimal")
    if common.get("scope") != "common":
        errors.append("common manifest scope must be common")

    if len(minimal.get("objects", [])) < 3:
        errors.append("minimal example must declare at least three objects")
    if len(minimal.get("morphisms", [])) < 2:
        errors.append("minimal example must declare at least two morphisms")

    diagram_file = MINIMAL_DIR / minimal.get("diagram_file", "")
    if not diagram_file.exists():
        errors.append("minimal example diagram file is missing")

    common_artifacts = common.get("artifacts", [])
    artifact_paths = {artifact.get("path", "") for artifact in common_artifacts}

    phases = {artifact.get("phase") for artifact in common_artifacts}
    for phase in {"spec", "design", "verification", "implementation"}:
        if phase not in phases:
            errors.append(f"common example is missing phase: {phase}")

    missing_common_artifacts = sorted(REQUIRED_COMMON_ARTIFACTS - artifact_paths)
    for artifact_path in missing_common_artifacts:
        errors.append(f"common manifest is missing required artifact: {artifact_path}")

    for artifact in common_artifacts:
        artifact_path = COMMON_DIR / artifact["path"]
        if not artifact_path.exists():
            errors.append(f"missing common example artifact: {artifact_path.relative_to(ROOT)}")

    for relative_path, required_sections in REQUIRED_MARKDOWN_SECTIONS.items():
        path = COMMON_DIR / relative_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for section in required_sections:
            if section not in text:
                errors.append(f"{relative_path} is missing required section: {section}")

    traceability_path = COMMON_DIR / "verification" / "traceability-matrix.md"
    if traceability_path.exists():
        traceability_text = traceability_path.read_text(encoding="utf-8")
        for claim_id in TRACEABILITY_REQUIRED_IDS:
            if claim_id not in traceability_text:
                errors.append(f"traceability matrix is missing claim ID: {claim_id}")
        for required_path in TRACEABILITY_REQUIRED_PATHS:
            if required_path not in traceability_text:
                errors.append(f"traceability matrix is missing path reference: {required_path}")

    acceptance_evidence_path = COMMON_DIR / "verification" / "acceptance-evidence.md"
    if acceptance_evidence_path.exists():
        acceptance_evidence_text = acceptance_evidence_path.read_text(encoding="utf-8")
        for needle in [
            "Approved Change",
            "implementation/execution-trace.md",
            "Change Identity",
            "Plan Revision",
        ]:
            if needle not in acceptance_evidence_text:
                errors.append(f"acceptance evidence is missing required reference: {needle}")

    if common.get("chapter_coverage") != chapter_ids:
        errors.append("common example chapter_coverage must match book-config chapter IDs in order")

    readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
    index_text = (ROOT / "index.md").read_text(encoding="utf-8")
    required_links = [
        "examples/minimal/policy-gated-change-review/",
        "examples/common/policy-gated-change-review/",
    ]
    for link in required_links:
        if link not in readme_text:
            errors.append(f"README.md is missing quickstart link: {link}")
        if link not in index_text:
            errors.append(f"index.md is missing quickstart link: {link}")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
