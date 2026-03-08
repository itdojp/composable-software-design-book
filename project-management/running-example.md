# Running Example Decision

## Candidate Comparison

| Candidate | Clarity | Chapter coverage | Formal fit | Operational realism | Size control | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Policy-gated change review for AI-assisted repository work | 5 | 5 | 5 | 5 | 4 | Strong fit for responsibility boundaries, artifacts, verification, and AI-assisted implementation. |
| Access request approval workflow | 4 | 4 | 4 | 4 | 5 | Clear, but less natural for the implementation chapter. |
| Incident triage and recovery workflow | 4 | 4 | 4 | 5 | 3 | Strong operational realism, but harder to keep small. |
| API integration migration pipeline | 3 | 5 | 5 | 3 | 3 | Excellent for pullbacks and pushouts, but weaker for human review governance. |

## Adopted Example

- Running example: Policy-Gated Change Review for AI-Assisted Repository Work
- Minimal example: Policy-Gated Change Review
- Common example root: `examples/common/policy-gated-change-review/`

## Adoption Rationale

The selected example keeps the book centered on AI-assisted engineering rather than an unrelated domain.
It naturally exposes responsibility boundaries, review artifacts, commutative claims, integration concerns, and effect boundaries.
It is small enough for a minimal example and rich enough for the case-study chapter.
`Approved Change` remains the single canonical approval artifact through Chapter 10.

## Chapter Usage

| Chapter | Example role |
| --- | --- |
| Introduction | Motivate why the example needs compositional structure and auditability. |
| Chapter 01 | Show the human and AI responsibility boundary for proposing and approving changes. |
| Chapter 02 | Model the change request, review plan, and approved change as objects linked by morphisms. |
| Chapter 03 | Start from the minimal policy-gated approval diagram, then expand to the richer repository diagram and lightweight traceability matrix. |
| Chapter 04 | Translate the example across specification, architecture, and operational views. |
| Chapter 05 | Compare reviewer view, system view, and execution view as natural transformations between models. |
| Chapter 06 | Use products and coproducts for combined checks, alternate review paths, and controlled variation. |
| Chapter 07 | Reuse the example for repository migration and toolchain integration boundaries. |
| Chapter 08 | Use the example workflow to explain sequential and parallel composition in orchestration. |
| Chapter 09 | Make prompt, tool, and approval side effects explicit through effect boundaries. |
| Chapter 10 | Reconstruct the example end to end from specification to verification and implementation. |
