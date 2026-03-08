---
layout: book
title: "Glossary of Category-Theoretic and Engineering Terms"
appendix: appendix-b
order: 13
description: "Definitions and cross-references for the canonical terms used in the book."
---

# Appendix B. Glossary of Category-Theoretic and Engineering Terms

This appendix centralizes the canonical vocabulary used across category theory, software design, and AI-assisted workflows.

## Category-theoretic terms

This section groups the core formal terms that appear in the explanatory chapters.
The definitions stay brief because each term is expanded in the chapter where it does real design work.

### Objects, morphisms, and commutativity

**Object.** A stable unit in a design model, such as a software artifact, interface, or system state that can participate in named transformations.
See [Chapter 02](../chapter-chapter02/).

**Morphism.** A named transformation between objects that preserves the structure the model cares about.
See [Chapter 02](../chapter-chapter02/).

**Composition.** The act of connecting compatible morphisms into one longer path whose engineering meaning can still be reviewed as a whole.
See [Chapter 02](../chapter-chapter02/).

**Identity morphism.** A morphism that leaves an object unchanged under composition.
See [Chapter 02](../chapter-chapter02/).

**Associativity.** The law that compatible compositions keep the same meaning even when their grouping changes.
See [Chapter 02](../chapter-chapter02/).

**Commutative diagram.** A diagram in which different paths are claimed to preserve the same result or meaning.
See [Chapter 03](../chapter-chapter03/).

**Traceability matrix.** A table that links requirements, design choices, verification checks, and implementation evidence across related artifacts.
See [Chapter 03](../chapter-chapter03/) and [Chapter 10](../chapter-chapter10/).

### Functors, natural transformations, and universal constructions

**Functor.** A structure-preserving translation between categories or design views.
See [Chapter 04](../chapter-chapter04/).

**Runtime view.** A representation of the system as observed during execution, including operational states, transitions, and evidence obligations.
See [Chapter 04](../chapter-chapter04/).

**Semantic drift.** A mismatch in which a translated artifact no longer preserves the intended meaning of its source view.
See [Chapter 04](../chapter-chapter04/).

**Natural transformation.** A coherent change between functorial views of the same design space.
See [Chapter 05](../chapter-chapter05/).

**Naturality.** The consistency condition that says a change of view preserves meaning across corresponding paths, not only across isolated labels.
See [Chapter 05](../chapter-chapter05/).

**Universal property.** A definition that characterizes a construction by the unique way other structures map to or from it.
See [Chapter 06](../chapter-chapter06/).

**Product.** A construction that combines required components into one canonical object from which each component can be recovered.
See [Chapter 06](../chapter-chapter06/).

**Coproduct.** A construction that makes alternatives explicit by giving each variant a named entry into one shared boundary.
See [Chapter 06](../chapter-chapter06/).

**Pullback.** A construction that joins structures only where they agree on a stated shared boundary or constraint.
See [Chapter 07](../chapter-chapter07/).

**Pushout.** A construction that merges or replaces structures along a shared boundary while preserving the meaning that boundary carries.
See [Chapter 07](../chapter-chapter07/).

**Monoidal category.** A category equipped with a parallel composition operator and a unit object so sequential and parallel structure can be reasoned about together.
See [Chapter 08](../chapter-chapter08/).

**String diagram.** A diagrammatic notation in which wires represent preserved context or artifacts and boxes represent composed steps.
See [Chapter 08](../chapter-chapter08/).

**Monad.** A structure that packages effectful computation so later steps must handle its operational context explicitly.
See [Chapter 09](../chapter-chapter09/).

**Kleisli composition.** The composition rule that chains effectful steps while keeping them inside one explicit effect envelope.
See [Chapter 09](../chapter-chapter09/).

## Software design terms

This section stabilizes the engineering vocabulary that connects the formal model to implementation work.
These terms are reader-facing because the book uses them to move from diagrams to repository artifacts and review consequences.

### Interface contracts, artifacts, and verification evidence

**Compositional design.** A design approach that treats systems as explicit artifacts and transformations whose combined behavior can be reviewed as a composed path.
See [Introduction](../chapter-introduction/).

**Design artifact.** A durable document, model, or file that explains, constrains, reviews, or governs a system change.
See [Chapter 01](../chapter-chapter01/).

**Interface contract.** A precise statement of inputs, outputs, guarantees, and obligations at a system or workflow boundary.
See [Chapter 01](../chapter-chapter01/) and [Chapter 02](../chapter-chapter02/).

**Partial function.** A transformation that is defined only for inputs that satisfy stated preconditions or domain restrictions.
See [Chapter 02](../chapter-chapter02/).

**Total function.** A transformation that is defined for every input in its stated domain.
See [Chapter 02](../chapter-chapter02/).

**Verification plan.** A documented method for checking that the workflow's claims and constraints continue to hold.
See [Chapter 01](../chapter-chapter01/).

**Responsibility boundary.** A documented boundary that assigns decision rights, required evidence, and escalation rules across humans, agents, and automation.
See [Chapter 01](../chapter-chapter01/).

**Reviewer view.** A reviewer-facing representation that preserves decision-relevant meaning while hiding operational detail that does not affect judgment.
See [Chapter 05](../chapter-chapter05/).

**Adapter.** A component or representation that reshapes one interface into another compatible form.
See [Chapter 05](../chapter-chapter05/).

**Facade.** A simplified boundary that hides internal complexity behind a smaller external view.
See [Chapter 05](../chapter-chapter05/).

**Version skew.** A state in which linked views or artifacts are updated at different times and temporarily disagree about the same system claim.
See [Chapter 05](../chapter-chapter05/).

**Coherence failure.** A mismatch in which supposedly corresponding paths or views no longer preserve the same design meaning.
See [Chapter 05](../chapter-chapter05/) and [Chapter 07](../chapter-chapter07/).

**Shared boundary.** The canonical set of keys, schemas, or policy labels that multiple artifacts must preserve before they can be safely joined or replaced.
See [Chapter 07](../chapter-chapter07/).

### Integration boundaries, migrations, and orchestration

**Provenance.** The recorded origin and transformation history of an artifact, field, or decision used during integration or migration.
See [Chapter 07](../chapter-chapter07/).

**Schema mapping.** A defined correspondence between old and new data or interface fields used during controlled migration.
See [Chapter 07](../chapter-chapter07/).

**Migration plan.** A staged plan for replacing or restructuring a system while preserving required invariants and rollback options.
See [Chapter 07](../chapter-chapter07/).

**Operational workflow.** A sequence of runtime or human activities that moves an artifact set from one reviewed state to the next.
See [Chapter 01](../chapter-chapter01/) and [Chapter 10](../chapter-chapter10/).

**Rollback.** A controlled return to a previously safe state after an implementation or operational step violates an expected invariant.
See [Chapter 01](../chapter-chapter01/) and [Chapter 09](../chapter-chapter09/).

**Orchestration.** The coordination of multiple effectful steps, tools, or agents into one workflow.
See [Chapter 08](../chapter-chapter08/) and [Chapter 09](../chapter-chapter09/).

**Synchronization boundary.** A named fan-in contract that concurrent branches must satisfy before a workflow may continue.
See [Chapter 08](../chapter-chapter08/) and [Chapter 10](../chapter-chapter10/).

## AI agent and workflow terms

This section defines the operational vocabulary for human-AI collaboration and tool-mediated delivery.
The terms are anchored in the running example so that later formal chapters stay connected to concrete software work.

### Delegation, escalation, and review authority

**AI agent.** A software actor that plans or acts using model-driven reasoning and tool use within a stated boundary.
See [Introduction](../chapter-introduction/).

**Bounded delegation.** A delegation pattern that limits agent authority by explicit scope, policy, and escalation conditions.
See [Chapter 01](../chapter-chapter01/).

**Policy gate.** A rule-driven checkpoint that blocks progress until stated policy conditions hold.
See [Chapter 01](../chapter-chapter01/) and the [running example](../../examples/common/policy-gated-change-review/).

**Human review gate.** A mandatory human approval step before a higher-risk action or workflow transition may continue.
See [Chapter 01](../chapter-chapter01/).

**Change Request.** The artifact that states the requested outcome, scope, and constraints before delegated work begins.
See [Chapter 01](../chapter-chapter01/) and the [running example](../../examples/common/policy-gated-change-review/).

**Review Plan.** The artifact that scopes delegated work, names required checks, and records what still requires human judgment.
See [Chapter 01](../chapter-chapter01/) and the [running example](../../examples/common/policy-gated-change-review/).

**Approved Change.** The artifact state reached after required policy checks and human approval are both satisfied.
See [Chapter 01](../chapter-chapter01/) and the [running example](../../examples/common/policy-gated-change-review/).

### Effect boundaries, tool calls, and execution traces

**Effect boundary.** A boundary that makes side effects explicit and reviewable before they are composed into a larger workflow.
See [Chapter 09](../chapter-chapter09/).

**Tool call.** An invocation of an external capability by an agent or orchestrator.
See [Chapter 09](../chapter-chapter09/).

**Execution trace.** A recorded sequence of steps, inputs, outputs, and decisions that occurred during execution.
See [Chapter 09](../chapter-chapter09/) and [Chapter 10](../chapter-chapter10/).

**Audit log.** A durable record of actions, decisions, and changes kept for later inspection.
See [Chapter 01](../chapter-chapter01/) and [Chapter 09](../chapter-chapter09/).

**Prompt context.** The task state, instructions, and references supplied to a model call at invocation time.
See [Chapter 09](../chapter-chapter09/).

**Acceptance evidence.** The bundle of approved artifacts, checks, traces, and review outcomes used to justify acceptance of a change.
See [Chapter 10](../chapter-chapter10/).

## Translation and usage notes

This section records terminology decisions that matter for cross-language drafting and editorial consistency.
The book keeps canonical English wording stable across prose, diagrams, glossary entries, and running example artifacts.

### Canonical English terms and acceptable Japanese counterparts

Use the English glossary term as the publication source of truth.
Use `project-management/term-base.csv` and `TERMS.yml` to keep Japanese drafting choices aligned with that source.
When a reader-facing term appears in a diagram or workflow file, reuse the same wording instead of inventing chapter-local synonyms.

### Terms that must remain untranslated in running text

Commands, file paths, environment variables, schema keys, and code identifiers remain in English.
The running example artifact labels `Change Request`, `Review Plan`, and `Approved Change` stay stable across diagrams and supporting files.
Chapter IDs, appendix IDs, and internal links are treated as stable interfaces rather than prose that may be rewritten freely.
