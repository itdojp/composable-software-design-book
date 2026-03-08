---
title: "Example Implementation: Effect Boundary"
description: "Named side-effect boundaries for the running example."
---

# Example Implementation: Effect Boundary

This artifact makes the running example's side effects explicit before they are composed into one delivery flow.
It exists so Chapter 09 can discuss effectful orchestration with named repository evidence instead of ambient tool behavior.

## Pure Core

The workflow keeps a small pure core that can be reasoned about without touching external systems.
The pure core compares scope, route rules, evidence completeness, and acceptance conditions over explicit artifacts.

### Pure Decisions

- `derive-required-checks`: Review Plan -> Required Checks
- `compare-route-rules`: Policy-Evaluated Plan -> Approval Route ID
- `check-evidence-completeness`: Decision Packet -> Review Outcome Candidate

## Effectful Steps

| Step | Effect class | External dependency | Emitted evidence |
| --- | --- | --- | --- |
| `draft-plan-with-agent` | Prompt + model invocation | LLM runtime and prompt context | Plan revision note |
| `evaluate-policy` | Tool call + repository read | Policy engine and repository metadata | Policy evaluation record |
| `collect-evidence-links` | Repository read + I/O | Diff snapshot, test outputs, linked artifacts | Evidence bundle |
| `record-review-decision` | Human approval + audit write | Reviewer action and audit store | approval decision record |
| `dispatch-execution` | External tool + state change | Execution environment | Execution report |

## Boundary Rules

- Every effectful step must name its input artifact, output artifact, and emitted evidence.
- A step that touches external state may run only after the preceding artifact boundary is complete.
- Human approval is effectful because it changes authority, not only because it writes a record.
- `dispatch-execution` is irreversible enough to require `Approved Change` plus the current synchronization boundary state.
- Escape hatches such as manual override or cached policy output must be recorded as exceptional effects rather than hidden defaults.

## Kleisli Reading

The engineering reading is that each effectful step returns one governed review context rather than a naked artifact.
A later step composes safely only when it consumes that governed context and preserves its audit obligations.
This is why the running example treats prompt context, tool output, and reviewer decisions as first-class evidence instead of incidental logging.

## Relationship To Other Artifacts

This artifact depends on `implementation/orchestration-diagram.md`, `implementation/synchronization-boundary.md`, and `verification/acceptance-evidence.md`.
It complements `implementation/execution-trace.md` by stating which effects must appear in the trace and why.
