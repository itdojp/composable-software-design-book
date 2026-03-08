---
layout: book
title: "Objects, Morphisms, and Composition"
chapter: chapter02
order: 3
description: "Model systems, interfaces, and transformations with the core vocabulary of composition."
---

# Objects, Morphisms, and Composition

This chapter introduces the core compositional vocabulary for modeling systems, interfaces, and transformations.
It reuses the [minimal example](../../examples/minimal/policy-gated-change-review/) and the [common running example](../../examples/common/policy-gated-change-review/) so that the formal language remains tied to reviewable repository artifacts.
Use [Appendix A](../appendices/appendix-a/) for notation and [Appendix B](../appendices/appendix-b/) for canonical definitions.

## Learning goals

- Choose stable software artifacts and states that are worth modeling as objects.
- Distinguish meaningful morphisms from incidental implementation detail.
- Use composition, identity, and contract boundaries to reason about longer workflow claims.

## Prerequisites

- The responsibility-boundary framing from [Chapter 01](../chapter-chapter01/).
- Basic comfort reading repository artifacts and workflow diagrams.

## Key concepts

- `object`
- `morphism`
- `composition`
- `identity morphism`

## Running example linkage

- Inspect the [minimal diagram](../../examples/minimal/policy-gated-change-review/diagram/) for the smallest object-and-morphism set that still carries the approval claim.
- Use the [artifact map](../../examples/common/policy-gated-change-review/design/artifact-map/) to compare abstract object choice with concrete repository artifacts.

## Modeling systems as objects

This chapter does not begin by treating every file, function, or event as an object.
It begins by asking which units stay stable enough to support review, reuse, and traceable change.

### Choosing the right units of design

An object in this book is a stable unit of design, not simply anything that exists in the system.
The unit is worth modeling as an object when it has a recognizable boundary, a durable role, and a review consequence if it changes incorrectly.

In the running example, `Change Request`, `Review Plan`, and `Approved Change` satisfy those conditions.
Each one is a durable artifact class with a specific role in the workflow.
Each one can be inspected independently.
Each one can also fail in a different way.

This is why the chapter does not start with prompts, model weights, or individual shell commands.
Those details may matter later, especially when effect boundaries become explicit.
At this stage, they are usually implementation detail rather than the stable unit the reviewer needs.

The right object choice is therefore driven by boundaries and invariants.
If a unit carries a distinct contract, can survive a handoff, and supports a separate review question, it is a strong candidate for object status.
If it exists only as a transient implementation convenience, it usually should not anchor the model.

### Objects as stable interfaces and states

Software objects in a compositional model can represent either stable interfaces or stable states.
The difference matters less than the fact that the unit remains identifiable across transformations.
The `Change Request` is a stateful artifact that captures intent, scope, and constraints.
The `Review Plan` is a reviewable interface between request interpretation and approval.
The `Approved Change` is the state reached after the required gate conditions hold.

This view prevents a common modeling error.
Teams often talk about "the workflow" as if it were one object.
That collapse hides the fact that the workflow crosses multiple boundaries with different obligations.
A single blob cannot explain where a request becomes reviewable, where policy is checked, or where human judgment enters.

Object choice therefore stabilizes the later argument.
If the reader cannot tell what counts as the same object before and after a step, it becomes impossible to state whether a transformation preserved meaning.
That is why object selection is the first modeling decision, not an afterthought.

## Morphisms as interfaces and transformations

Once the objects are chosen, the next question is how one valid state or artifact becomes another.
The answer is not every implementation step.
It is the transformation that preserves the structure the model cares about.

### Behavior-preserving change

A morphism is a named transformation between objects.
In software design, that name should capture the meaningful change rather than the incidental mechanism.
`draft-review-plan` is a better morphism name than "run model with prompt template 7" because the former states the transformation the reviewer actually cares about.

The morphism claim becomes stronger when the preserved behavior is explicit.
In the running example, `draft-review-plan` should preserve the relevant scope and constraints of the `Change Request`.
`human-approval` should preserve the judgment that the plan is acceptable under the stated policy and acceptance criteria.

This is why morphisms are design claims before they are implementation claims.
A script, API call, or agent interaction may realize the morphism, but it is not identical to the morphism.
If the implementation changes while the preserved artifact relationship stays the same, the morphism is stable.
If the implementation silently drops a constraint, the morphism claim has failed even if the code still runs.

The [minimal diagram](../../examples/minimal/policy-gated-change-review/diagram/) makes this concrete.
It names both the stepwise path and the direct path.
The direct edge `policy-gated-approval` only makes sense if the composed steps preserve the same meaning as the shorter claim.

### Partial functions, total functions, and contracts

Many software transformations are not defined for every conceivable input.
That does not make them useless.
It means the team must be honest about the domain on which the transformation is intended to work.

A total function is defined for every input in its stated domain.
A partial function is defined only when additional preconditions hold.
In practice, many workflow steps that teams informally describe as universal are partial once their real constraints are stated.

`draft-review-plan` may be total over well-formed `Change Request` artifacts that include scope, constraints, and acceptance criteria.
It is not total over arbitrary text pasted into an issue tracker.
`human-approval` is also partial if the plan may be rejected, escalated, or returned for revision rather than approved directly.

Interface contracts make this manageable.
They state what a valid source object must contain and what a successful target object must guarantee.
When the contract is missing, a workflow appears smoother than it really is.
When the contract is explicit, the team can decide whether to narrow the domain, add a pre-validation step, or model alternative outcomes more explicitly in later chapters.

## Composition as the core design move

The real power of the vocabulary appears when the team composes several trustworthy steps into one larger claim.
Composition is the move that lets a local artifact transformation become a system-level argument.

### Associativity and modular reasoning

If one morphism takes `Change Request` to `Review Plan`, and another takes `Review Plan` to `Approved Change`, then the two can compose into a path from request to approved change.
In notation, `human-approval ◦ draft-review-plan` states that the second step is applied after the first.
The notation matters here because order is part of the design claim.

The running example uses a direct edge called `policy-gated-approval`.
That edge is not a shortcut for convenience only.
It is a claim that the composed path preserves the same meaning the workflow wants the direct path to denote.

Associativity makes this useful in larger systems.
If the workflow later inserts request normalization or policy evidence generation before approval, the team can regroup the composed path without changing its meaning as long as the interfaces still align.
That is what allows modular reasoning.
Different engineers can review adjacent parts of the path without losing the whole-system claim.

This is not abstract bookkeeping.
It affects how repositories are reviewed.
A team can validate one morphism against one contract, then compose the approved steps into a larger workflow argument.
Without associativity, every longer path would have to be re-argued from scratch.

### Identity morphisms and boundary stability

An identity morphism leaves an object unchanged under composition.
In software terms, it represents a step that preserves the object's modeled meaning exactly.
This matters because workflows often contain pass-through steps that should not alter the artifact they carry.

For example, a repository service may reformat metadata, reindex a request, or move an artifact between storage locations.
If those steps preserve the modeled `Change Request` exactly, they behave like identity morphisms with respect to this chapter's design model.
If they alter scope, constraints, or reviewer obligations, they are not identities and should not be treated as harmless plumbing.

Identity morphisms therefore test boundary stability.
A stable boundary allows a no-op pass-through without changing the artifact's design meaning.
An unstable boundary forces every transport or serialization step to become a semantic risk.
That instability is expensive because it expands the number of places where the team must re-check invariants.

## Translating the vocabulary into engineering practice

The formal vocabulary earns its place only when it improves design and review decisions.
This section translates objects, morphisms, and composition into the day-to-day work of services, repositories, and review checkpoints.

### Service interactions and data transformations

The same object and morphism language works outside the running example because most software systems already rely on stable boundaries.
An API request can be modeled as an object when its schema and guarantees matter.
A schema translation can be modeled as a morphism when the preserved fields and constraints are explicit.
A deployment manifest can be an object when later steps depend on its contract rather than on one tool's internal representation.

The running example keeps the discussion grounded.
The [problem statement](../../examples/common/policy-gated-change-review/spec/problem-statement/) provides the source boundary.
The [artifact map](../../examples/common/policy-gated-change-review/design/artifact-map/) shows the durable units that matter across phases.
The [design diagram](../../examples/common/policy-gated-change-review/design/commutative-diagram/) then states the composition claim that later chapters will test more rigorously.

This vocabulary helps teams separate model from mechanism.
An AI agent, a service call, and a script may all realize the same morphism if they preserve the same contract.
The tool choice still matters operationally, but it should not be confused with the design relation being claimed.

### Composition in review checklists

Compositional reasoning can be turned into a practical review checklist.
Before trusting a workflow path, ask the following questions.

- What is the source object, and what is the target object?
- Which invariant or contract must the morphism preserve?
- Is the transformation total on its stated domain, or does it depend on hidden preconditions?
- What evidence artifact shows that the transformation actually preserved the claimed structure?
- If multiple steps are composed, who owns the approval for the composed path as a whole?

These questions are useful in pull requests, design reviews, and workflow approvals because they expose hidden assumptions early.
They also prepare the reader for Chapter 03, where diagrams make these path claims easier to inspect.

## Common modeling mistakes

Most failed models are not wrong because the team lacks formal vocabulary.
They fail because the model hides boundaries, smuggles in implementation detail, or assigns too much meaning to one overloaded node.

### Overloading one object with multiple concerns

One common mistake is to treat one object as if it carried several unrelated responsibilities.
In the running example, calling the whole approval workflow one object would erase the difference between request intent, reviewable plan, and approved outcome.
It would also hide where distinct actors gain or lose authority.

A similar problem appears when the `Review Plan` is treated as both the proposal artifact and the complete record of approval.
Those roles may overlap in a small example, but they are not conceptually identical.
When one object carries too many concerns, later chapters cannot state clean morphisms or clean commutative claims.

The corrective move is simple.
Split the model where the review question changes.
If a reviewer would ask a different question about one part of the state than another, the model probably needs separate objects.

### Mistaking implementation detail for structure

The opposite mistake is to model transient implementation choices as if they were the stable structure.
Prompt phrasing, one temporary file path, or one internal API name may matter operationally, but they are often not the object or morphism the design argument depends on.

This matters especially in AI-assisted systems because implementations change quickly.
If the model is built from volatile detail, every prompt revision appears to invalidate the entire design.
If the model is built from stable contracts and preserved transformations, the team can change tools without rewriting the conceptual map.

The test is whether the design claim survives a tool substitution.
If one agent platform is replaced with another and the preserved artifact path remains the same, the object and morphism model was probably well chosen.
If the model collapses immediately, it was describing mechanism rather than structure.

## Summary

- Objects should name stable artifacts or states that support separate review questions.
- Morphisms should name preserved transformations rather than transient implementation detail.
- Composition is the core move that turns local artifact checks into a whole-workflow claim.

## Review prompts

1. Which unit in your current workflow is stable enough to model as an object, and which one only looks stable because of tool habit.
2. Which transformation in your process is really partial even though the team talks about it as if it were total.
3. Which composed path in your repository deserves one explicit invariant before it grows further.
