#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover - dependency fallback
    Draft202012Validator = None


ROOT = Path(__file__).resolve().parents[1]
MINIMAL_DIR = ROOT / "examples" / "minimal" / "policy-gated-change-review"
COMMON_DIR = ROOT / "examples" / "common" / "policy-gated-change-review"
SCHEMA_DIR = ROOT / "schemas"
MINIMAL_SCHEMA_PATH = SCHEMA_DIR / "minimal-example-manifest.schema.json"
COMMON_SCHEMA_PATH = SCHEMA_DIR / "common-example-manifest.schema.json"
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
        "## Claim Coverage",
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


def load_json_file(path: Path, errors: list[str]) -> dict | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing required file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON in {path.relative_to(ROOT)}: {exc.msg} at line {exc.lineno} column {exc.colno}")
    return None


def format_instance_path(parts: list[object]) -> str:
    if not parts:
        return "$"
    formatted: list[str] = ["$"]
    for part in parts:
        if isinstance(part, int):
            formatted.append(f"[{part}]")
        else:
            formatted.append(f".{part}")
    return "".join(formatted)


def validate_with_subset(instance: object, schema: dict, path: list[object] | None = None) -> list[str]:
    current_path = path or []
    errors: list[str] = []
    path_label = format_instance_path(current_path)

    expected_type = schema.get("type")
    if expected_type == "object":
        if not isinstance(instance, dict):
            return [f"{path_label}: expected object"]
        required = schema.get("required", [])
        for key in required:
            if key not in instance:
                errors.append(f"{path_label}: missing required property '{key}'")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            extras = sorted(set(instance) - set(properties))
            for key in extras:
                errors.append(f"{path_label}: unexpected property '{key}'")
        for key, subschema in properties.items():
            if key in instance:
                errors.extend(validate_with_subset(instance[key], subschema, current_path + [key]))
    elif expected_type == "array":
        if not isinstance(instance, list):
            return [f"{path_label}: expected array"]
        min_items = schema.get("minItems")
        if min_items is not None and len(instance) < min_items:
            errors.append(f"{path_label}: expected at least {min_items} items")
        if schema.get("uniqueItems"):
            seen: set[str] = set()
            for index, item in enumerate(instance):
                marker = json.dumps(item, sort_keys=True)
                if marker in seen:
                    errors.append(f"{path_label}: duplicate array item at index {index}")
                seen.add(marker)
        item_schema = schema.get("items")
        if item_schema:
            for index, item in enumerate(instance):
                errors.extend(validate_with_subset(item, item_schema, current_path + [index]))
    elif expected_type == "string":
        if not isinstance(instance, str):
            return [f"{path_label}: expected string"]
        min_length = schema.get("minLength")
        if min_length is not None and len(instance) < min_length:
            errors.append(f"{path_label}: string must be at least {min_length} characters")
        pattern = schema.get("pattern")
        if pattern and not re.fullmatch(pattern, instance):
            errors.append(f"{path_label}: string does not match pattern {pattern!r}")

    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path_label}: expected constant value {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path_label}: expected one of {schema['enum']!r}")

    return errors


def validate_schema_instance(label: str, instance: dict, schema: dict, errors: list[str]) -> None:
    if Draft202012Validator is not None:
        validator = Draft202012Validator(schema)
        for error in validator.iter_errors(instance):
            location = format_instance_path(list(error.absolute_path))
            errors.append(f"{label} schema validation failed at {location}: {error.message}")
        return

    for message in validate_with_subset(instance, schema):
        errors.append(f"{label} schema validation failed at {message}")


def main() -> int:
    errors: list[str] = []

    running_example = ROOT / "project-management" / "running-example.md"
    artifact_decision = ROOT / "project-management" / "artifact-location-decision.md"
    minimal_manifest_path = MINIMAL_DIR / "manifest.json"
    common_manifest_path = COMMON_DIR / "manifest.json"
    book_config_path = ROOT / "book-config.json"

    for path in [
        running_example,
        artifact_decision,
        minimal_manifest_path,
        common_manifest_path,
        book_config_path,
        MINIMAL_SCHEMA_PATH,
        COMMON_SCHEMA_PATH,
    ]:
        if not path.exists():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")

    minimal_schema = load_json_file(MINIMAL_SCHEMA_PATH, errors) if MINIMAL_SCHEMA_PATH.exists() else None
    common_schema = load_json_file(COMMON_SCHEMA_PATH, errors) if COMMON_SCHEMA_PATH.exists() else None
    minimal = load_json_file(minimal_manifest_path, errors) if minimal_manifest_path.exists() else None
    common = load_json_file(common_manifest_path, errors) if common_manifest_path.exists() else None
    book_config = load_json_file(book_config_path, errors) if book_config_path.exists() else None

    if errors and (minimal is None or common is None or book_config is None):
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    assert minimal is not None
    assert common is not None
    assert book_config is not None

    if minimal_schema is not None:
        validate_schema_instance("minimal manifest", minimal, minimal_schema, errors)
    if common_schema is not None:
        validate_schema_instance("common manifest", common, common_schema, errors)

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
            "approval decision record",
            "implementation/execution-trace.md",
            "Change Identity",
            "Plan Revision",
            "PGCR-06",
            "dispatch-execution",
            "Execution result or return-for-rework note",
        ]:
            if needle not in acceptance_evidence_text:
                errors.append(f"acceptance evidence is missing required reference: {needle}")

    if common.get("chapter_coverage") != chapter_ids:
        errors.append("common example chapter_coverage must match book-config chapter IDs in order")

    readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
    index_text = (ROOT / "index.md").read_text(encoding="utf-8")
    readme_required_links = [
        "examples/minimal/policy-gated-change-review/README.md",
        "examples/common/policy-gated-change-review/README.md",
    ]
    index_required_links = [
        "examples/minimal/policy-gated-change-review/README/",
        "examples/common/policy-gated-change-review/README/",
    ]
    for link in readme_required_links:
        if link not in readme_text:
            errors.append(f"README.md is missing quickstart link: {link}")
    for link in index_required_links:
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
