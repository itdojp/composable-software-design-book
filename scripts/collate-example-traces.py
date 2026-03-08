#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMMON_DIR = ROOT / "examples" / "common" / "policy-gated-change-review"
DEFAULT_REPORT_DIR = ROOT / "qa-reports" / "examples"
TRACEABILITY_PATH = COMMON_DIR / "verification" / "traceability-matrix.md"
ACCEPTANCE_EVIDENCE_PATH = COMMON_DIR / "verification" / "acceptance-evidence.md"
EXECUTION_TRACE_PATH = COMMON_DIR / "implementation" / "execution-trace.md"
EFFECT_BOUNDARY_PATH = COMMON_DIR / "implementation" / "effect-boundary.md"
COMMON_MANIFEST_PATH = COMMON_DIR / "manifest.json"
KNOWN_SYMBOLIC_REFS = {
    "Approved Change",
    "approval decision record",
    "Execution result or return-for-rework note",
    "Change Identity",
    "Plan Revision",
    "Plan revision note",
    "Policy evaluation record",
    "Evidence bundle",
    "Synchronization boundary check",
    "Execution report",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_json(path: Path) -> dict:
    return json.loads(read_text(path))


def slugify_heading(text: str) -> str:
    slug = text.strip().lower()
    slug = re.sub(r"`([^`]*)`", r"\1", slug)
    slug = re.sub(r"[^a-z0-9 _-]", "", slug)
    slug = slug.replace(" ", "-")
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug


def collect_heading_slugs(path: Path) -> set[str]:
    slugs: set[str] = set()
    for line in read_text(path).splitlines():
        if not line.startswith("#"):
            continue
        heading = line.lstrip("#").strip()
        if heading:
            slugs.add(slugify_heading(heading))
    return slugs


def normalize_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")


def parse_markdown_table(text: str, heading: str) -> list[dict[str, str]]:
    lines = text.splitlines()
    start_index: int | None = None

    for index, line in enumerate(lines):
        if line.strip() == heading:
            start_index = index + 1
            break

    if start_index is None:
        raise ValueError(f"missing heading: {heading}")

    while start_index < len(lines) and not lines[start_index].strip():
        start_index += 1

    table_lines: list[str] = []
    while start_index < len(lines) and lines[start_index].lstrip().startswith("|"):
        table_lines.append(lines[start_index])
        start_index += 1

    if len(table_lines) < 2:
        raise ValueError(f"missing markdown table under heading: {heading}")

    header_cells = [cell.strip() for cell in table_lines[0].strip().strip("|").split("|")]
    normalized_headers = [normalize_key(cell) for cell in header_cells]
    rows: list[dict[str, str]] = []

    for line in table_lines[2:]:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != len(normalized_headers):
            raise ValueError(f"table row shape mismatch under heading: {heading}")
        rows.append(dict(zip(normalized_headers, cells)))

    return rows


def parse_bullet_section(text: str, heading: str) -> list[str]:
    lines = text.splitlines()
    start_index: int | None = None

    for index, line in enumerate(lines):
        if line.strip() == heading:
            start_index = index + 1
            break

    if start_index is None:
        raise ValueError(f"missing heading: {heading}")

    bullets: list[str] = []
    while start_index < len(lines):
        line = lines[start_index]
        if line.startswith("#"):
            break
        stripped = line.strip()
        if stripped.startswith("- "):
            bullets.append(stripped[2:].strip())
        start_index += 1

    if not bullets:
        raise ValueError(f"missing bullet list under heading: {heading}")

    return bullets


def extract_code_refs(text: str) -> list[str]:
    return re.findall(r"`([^`]+)`", text)


def resolve_ref(ref: str, manifest_paths: set[str], heading_cache: dict[Path, set[str]]) -> dict[str, object]:
    if ".md" not in ref:
        return {
            "kind": "symbolic",
            "ref": ref,
            "exists": ref in KNOWN_SYMBOLIC_REFS,
            "declared_in_manifest": ref in KNOWN_SYMBOLIC_REFS,
        }

    relative_path, anchor = (ref.split("#", 1) + [None])[:2]
    target_path = COMMON_DIR / relative_path
    path_exists = target_path.exists()

    anchor_exists = True
    if anchor:
        if target_path not in heading_cache and path_exists:
            heading_cache[target_path] = collect_heading_slugs(target_path)
        anchor_exists = path_exists and anchor in heading_cache.get(target_path, set())

    return {
        "kind": "path",
        "ref": ref,
        "path": relative_path,
        "anchor": anchor,
        "exists": path_exists,
        "anchor_exists": anchor_exists,
        "declared_in_manifest": relative_path in manifest_paths,
    }


def build_summary_markdown(report: dict) -> str:
    consistency = report["consistency"]
    lines = [
        "# Example Trace Collation Summary",
        "",
        f"- Claims collated: {len(report['traceability']['claims'])}",
        f"- Trace steps collated: {len(report['execution_trace']['steps'])}",
        f"- Required evidence rows: {len(report['acceptance_evidence']['required_evidence'])}",
        f"- Claim coverage rows: {len(report['acceptance_evidence']['claim_coverage'])}",
        f"- Effectful steps collated: {len(report['effect_boundary']['steps'])}",
        "",
        "## Consistency",
        "",
        f"- Missing claim coverage: {len(consistency['missing_claim_coverage'])}",
        f"- Missing artifact reference: {len(consistency['missing_artifact_reference'])}",
        f"- Dangling references: {len(consistency['dangling_references'])}",
        f"- Unexpected unmapped trace items: {len(consistency['unexpected_unmapped_trace_items'])}",
        f"- Missing required evidence refs: {len(consistency['missing_required_evidence_reference'])}",
        f"- Missing effect trace steps: {len(consistency['missing_effect_trace_step'])}",
        f"- Effect class mismatches: {len(consistency['effect_class_mismatch'])}",
        f"- Evidence link mismatches: {len(consistency['effect_evidence_mismatch'])}",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--report-dir",
        default=str(DEFAULT_REPORT_DIR),
        help="Directory for generated collation reports.",
    )
    args = parser.parse_args()

    errors: list[str] = []
    for path in [TRACEABILITY_PATH, ACCEPTANCE_EVIDENCE_PATH, EXECUTION_TRACE_PATH, EFFECT_BOUNDARY_PATH, COMMON_MANIFEST_PATH]:
        if not path.exists():
            errors.append(f"missing required artifact: {path.relative_to(ROOT)}")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    manifest = read_json(COMMON_MANIFEST_PATH)
    manifest_paths = {artifact["path"] for artifact in manifest.get("artifacts", [])}
    heading_cache: dict[Path, set[str]] = {}

    traceability_text = read_text(TRACEABILITY_PATH)
    acceptance_text = read_text(ACCEPTANCE_EVIDENCE_PATH)
    execution_text = read_text(EXECUTION_TRACE_PATH)
    effect_boundary_text = read_text(EFFECT_BOUNDARY_PATH)

    try:
        traceability_rows = parse_markdown_table(traceability_text, "## Traceability Matrix")
        required_evidence_rows = parse_markdown_table(acceptance_text, "## Required Evidence")
        claim_coverage_rows = parse_markdown_table(acceptance_text, "## Claim Coverage")
        trace_fields = parse_bullet_section(execution_text, "## Trace Fields")
        execution_rows = parse_markdown_table(execution_text, "## Representative Trace")
        effect_rows = parse_markdown_table(effect_boundary_text, "## Effectful Steps")
    except ValueError as exc:
        print("FAIL")
        print(f"- {exc}")
        return 1

    trace_step_ids = {row["step_id"].strip("`") for row in execution_rows}
    execution_rows_by_step = {row["step_id"].strip("`"): row for row in execution_rows}
    known_symbolic_refs = set(KNOWN_SYMBOLIC_REFS)
    for row in execution_rows:
        known_symbolic_refs.add(row["input_artifact"])
        known_symbolic_refs.add(row["output_artifact"])
        known_symbolic_refs.add(row["evidence_link"])
    KNOWN_SYMBOLIC_REFS.update(known_symbolic_refs)

    resolved_refs: list[dict[str, object]] = []
    claims: list[dict[str, object]] = []
    for row in traceability_rows:
        claim_id = row["claim_id"]
        sources = {
            "specification": row["specification_source"],
            "design": row["design_source"],
            "verification": row["verification_source"],
            "implementation": row["implementation_source"],
        }
        resolved = {kind: resolve_ref(ref.strip("`"), manifest_paths, heading_cache) for kind, ref in sources.items()}
        resolved_refs.extend(resolved.values())
        claims.append(
            {
                "claim_id": claim_id,
                "sources": sources,
                "resolved_sources": resolved,
            }
        )

    required_evidence: list[dict[str, object]] = []
    for row in required_evidence_rows:
        refs = [resolve_ref(ref, manifest_paths, heading_cache) for ref in extract_code_refs(row["evidence_item"])]
        resolved_refs.extend(refs)
        required_evidence.append(
            {
                "evidence_item": row["evidence_item"],
                "why_it_is_required": row["why_it_is_required"],
                "references": refs,
            }
        )

    effect_steps: list[dict[str, object]] = []
    for row in effect_rows:
        effect_steps.append(
            {
                "step": row["step"].strip("`"),
                "effect_class": row["effect_class"],
                "external_dependency": row["external_dependency"],
                "emitted_evidence": row["emitted_evidence"],
            }
        )

    claim_coverage: list[dict[str, object]] = []
    for row in claim_coverage_rows:
        refs = [resolve_ref(ref, manifest_paths, heading_cache) for ref in extract_code_refs(row["evidence_reference"])]
        resolved_refs.extend(refs)
        trace_step = row["trace_step"].strip("`")
        claim_coverage.append(
            {
                "claim_id": row["claim_id"],
                "evidence_reference": row["evidence_reference"],
                "resolved_references": refs,
                "trace_step": trace_step,
                "trace_step_exists": trace_step in trace_step_ids,
            }
        )

    missing_claim_coverage = sorted(
        {claim["claim_id"] for claim in claims} - {row["claim_id"] for row in claim_coverage}
    )

    missing_artifact_reference = sorted(
        {
            resolved["ref"]
            for resolved in resolved_refs
            if resolved["kind"] == "path" and resolved["exists"] and not resolved["declared_in_manifest"]
        }
    )

    dangling_references = sorted(
        {
            resolved["ref"]
            for resolved in resolved_refs
            if (resolved["kind"] == "path" and (not resolved["exists"] or not resolved.get("anchor_exists", True)))
            or (resolved["kind"] == "symbolic" and not resolved["exists"])
        }
        | {
            row["trace_step"]
            for row in claim_coverage
            if not row["trace_step_exists"]
        }
    )

    covered_trace_steps = {row["trace_step"] for row in claim_coverage}
    unexpected_unmapped_trace_items = sorted(trace_step_ids - covered_trace_steps)
    missing_required_evidence_reference = sorted(
        row["evidence_item"] for row in required_evidence if not row["references"]
    )

    missing_effect_trace_step: list[str] = []
    effect_class_mismatch: list[str] = []
    effect_evidence_mismatch: list[str] = []
    for row in effect_steps:
        trace_row = execution_rows_by_step.get(row["step"])
        if trace_row is None:
            missing_effect_trace_step.append(row["step"])
            continue
        if trace_row["effect_class"] != row["effect_class"]:
            effect_class_mismatch.append(
                f"{row['step']}: effect-boundary={row['effect_class']} trace={trace_row['effect_class']}"
            )
        if trace_row["evidence_link"] != row["emitted_evidence"]:
            effect_evidence_mismatch.append(
                f"{row['step']}: effect-boundary={row['emitted_evidence']} trace={trace_row['evidence_link']}"
            )

    report = {
        "example_id": manifest["example_id"],
        "generated_from": {
            "traceability_matrix": str(TRACEABILITY_PATH.relative_to(ROOT)),
            "acceptance_evidence": str(ACCEPTANCE_EVIDENCE_PATH.relative_to(ROOT)),
            "execution_trace": str(EXECUTION_TRACE_PATH.relative_to(ROOT)),
            "effect_boundary": str(EFFECT_BOUNDARY_PATH.relative_to(ROOT)),
        },
        "traceability": {
            "claims": claims,
        },
        "acceptance_evidence": {
            "required_evidence": required_evidence,
            "claim_coverage": claim_coverage,
        },
        "execution_trace": {
            "fields": trace_fields,
            "steps": execution_rows,
        },
        "effect_boundary": {
            "steps": effect_steps,
        },
        "consistency": {
            "missing_claim_coverage": missing_claim_coverage,
            "missing_artifact_reference": missing_artifact_reference,
            "dangling_references": dangling_references,
            "unexpected_unmapped_trace_items": unexpected_unmapped_trace_items,
            "missing_required_evidence_reference": missing_required_evidence_reference,
            "missing_effect_trace_step": missing_effect_trace_step,
            "effect_class_mismatch": effect_class_mismatch,
            "effect_evidence_mismatch": effect_evidence_mismatch,
        },
    }

    report_dir = Path(args.report_dir)
    if not report_dir.is_absolute():
        report_dir = ROOT / report_dir
    report_dir.mkdir(parents=True, exist_ok=True)
    json_path = report_dir / "trace-collation.json"
    markdown_path = report_dir / "trace-collation.md"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    markdown_path.write_text(build_summary_markdown(report), encoding="utf-8")

    if (
        missing_claim_coverage
        or missing_artifact_reference
        or dangling_references
        or unexpected_unmapped_trace_items
        or missing_required_evidence_reference
        or missing_effect_trace_step
        or effect_class_mismatch
        or effect_evidence_mismatch
    ):
        print("FAIL")
        for category, values in report["consistency"].items():
            if not values:
                continue
            print(f"- {category}: {', '.join(values)}")
        return 1

    print("PASS")
    print(f"- wrote {json_path.relative_to(ROOT)}")
    print(f"- wrote {markdown_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
