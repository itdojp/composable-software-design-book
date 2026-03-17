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
- Reusable variation artifact: `examples/common/policy-gated-change-review/design/variation-paths.md`
- Secondary transfer thread: Deployment approval pipeline

## Adoption Rationale

The selected example keeps the book centered on AI-assisted engineering rather than an unrelated domain.
It naturally exposes responsibility boundaries, review artifacts, commutative claims, integration concerns, and effect boundaries.
It is small enough for a minimal example and rich enough for the case-study chapter.
`Approved Change` remains the single canonical approval artifact through Chapter 10.
The emitted `approval decision record`, the broader `audit log`, and the final `acceptance evidence` remain evidence layers around that outcome rather than parallel approval artifacts.
Post-approval execution is justified by execution trace and acceptance evidence rather than by a second approval artifact.

## Secondary Transfer Thread Rationale

The recurring secondary transfer thread is the deployment approval pipeline.
It broadens the book's addressable audience toward release governance and platform-delivery readers without replacing the canonical repository workflow.
It is close enough to the running example to preserve the same bounded request, governed decision, execution boundary, and evidence pattern.
That makes it suitable for repeated short cues in the body chapters and a fuller mapping in Appendix D.

## Chapter Usage

| Chapter | Example role |
| --- | --- |
| Introduction | Motivate why the example needs compositional structure and auditability. |
| Chapter 01 | Show the human and AI responsibility boundary for proposing and approving changes. |
| Chapter 02 | Model the change request, review plan, and approved change as objects linked by morphisms. |
| Chapter 03 | Start from the minimal policy-gated approval diagram, then expand to the richer repository diagram and lightweight traceability matrix. |
| Chapter 04 | Translate the example across specification, architecture, runtime, and operational views by using the new runtime view artifact. |
| Chapter 05 | Compare reviewer view, design view, and runtime view as natural transformations between models. |
| Chapter 06 | Use the `design/variation-paths.md` artifact for combined review context, alternate review paths, and controlled variation. |
| Chapter 07 | Use `design/shared-boundary.md`, `design/replacement-plan.md`, and `verification/coherence-failure.md` for pullbacks, pushouts, and migration review. |
| Chapter 08 | Use `implementation/orchestration-diagram.md` and `implementation/synchronization-boundary.md` to explain sequential and parallel composition, fan-in, and failure isolation. |
| Chapter 09 | Use `implementation/effect-boundary.md` and `implementation/execution-trace.md` to make prompt, tool, approval, and dispatch effects explicit. |
| Chapter 10 | Reconstruct the example end to end by combining the spec, design, review, runtime, implementation, and `verification/acceptance-evidence.md` artifacts. |
