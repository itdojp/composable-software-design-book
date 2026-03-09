---
layout: book
title: "Subject Index"
description: "Reader-facing subject index for the book's recurring concepts, artifacts, and design boundaries."
---

# Subject Index

This index is optimized for retrieval rather than for exhaustive keyword density.
Each entry names one primary chapter where the concept is first treated in full.
Later mentions should point back to that primary chapter unless the concept is materially redefined.

## Cross-reference policy

- Use the primary chapter when you want the first full explanation of a recurring concept.
- Use `See also` to move between closely related concepts that the manuscript treats separately.
- Use Appendix B when you need the canonical term definition before returning to the chapter discussion.
- In web and ebook reading, this index and the list of figures are reader-facing navigation aids.
- In print editions, the index and figure list may appear on separate pages, but the wording of the entries remains the same.

## Indexed concepts

| Term | Primary chapter | See also | Why revisit it |
| --- | --- | --- | --- |
| Acceptance Evidence | [Chapter 09](../../chapter-chapter09/) | [Chapter 10](../../chapter-chapter10/), [Appendix B](../../appendices/appendix-b/) | It closes the governed evidence story after effectful execution. |
| Approval Route ID | [Chapter 07](../../chapter-chapter07/) | `Review Route`, `shared boundary` | It keeps joins, migrations, and later evidence tied to one explicit route meaning. |
| Adapter | [Chapter 05](../../chapter-chapter05/) | `reviewer view`, `runtime view` | It explains interface reshaping without losing the design claim. |
| Approval decision record | [Chapter 01](../../chapter-chapter01/) | `Approved Change`, `Acceptance Evidence` | It preserves the review outcome without pretending to be the whole evidence bundle. |
| Approved Change | [Chapter 01](../../chapter-chapter01/) | `Approval decision record`, `Execution trace` | It is the canonical decision outcome artifact, not the full evidence bundle. |
| Audit log | [Chapter 01](../../chapter-chapter01/) | `Execution trace`, `Acceptance Evidence` | It preserves broader action history beyond the decision artifact itself. |
| Bounded delegation | [Chapter 01](../../chapter-chapter01/) | `AI agent`, `human review gate` | It defines what agents may do without inheriting approval authority. |
| Combined Review Context | [Chapter 06](../../chapter-chapter06/) | `Decision Packet`, `Review Route` | It is the smallest recoverable context for governed review. |
| Commutative diagram | [Chapter 03](../../chapter-chapter03/) | `traceability matrix`, `coherence failure` | It turns path equivalence into a reviewable consistency claim. |
| Coherence failure | [Chapter 05](../../chapter-chapter05/) | `reviewer view`, `traceability matrix` | It gives reviewers one reusable negative example when alternative views stop preserving the same claim. |
| Change Identity | [Chapter 08](../../chapter-chapter08/) | `Plan Revision`, `synchronization boundary` | It marks the stable request lineage that parallel branches and later effects must keep aligned. |
| Coproduct | [Chapter 06](../../chapter-chapter06/) | `Review Route`, `universal property` | It gives the chapter's explicit structure for route variation without hidden branch semantics. |
| Customer-support escalation workflow | [Chapter 09](../../chapter-chapter09/) | [Appendix D](../../appendices/appendix-d/), `effect boundary` | It shows how governed dispatch and emitted evidence carry over into service operations beyond repository delivery. |
| Decision Packet | [Chapter 05](../../chapter-chapter05/) | [Chapter 08](../../chapter-chapter08/), [Chapter 10](../../chapter-chapter10/) | It synchronizes scope, policy, and evidence before human judgment. |
| Deployment approval pipeline | [Chapter 10](../../chapter-chapter10/) | [Appendix D](../../appendices/appendix-d/), `Acceptance Evidence` | It is the clearest transfer of the case-study packet into release governance and post-rollout evidence. |
| Effect boundary | [Chapter 09](../../chapter-chapter09/) | `Execution trace`, `Acceptance Evidence` | It marks where pure artifact reasoning becomes operationally effectful. |
| Evidence Bundle | [Chapter 08](../../chapter-chapter08/) | `Decision Packet`, `synchronization boundary` | It captures the support set that must survive fan-in before review can proceed. |
| Execution trace | [Chapter 09](../../chapter-chapter09/) | [Chapter 10](../../chapter-chapter10/), `audit log` | It records what actually ran after approval and dispatch. |
| Execution-Ready Change | [Chapter 04](../../chapter-chapter04/) | `Approved Change`, `effect boundary` | It marks the runtime-facing state reached only after the governed approval meaning is preserved. |
| Functor | [Chapter 04](../../chapter-chapter04/) | `runtime view`, `reviewer view` | It explains structure-preserving translation across views. |
| Human review gate | [Chapter 01](../../chapter-chapter01/) | `policy gate`, `Bounded delegation` | It keeps final risk acceptance explicitly human-led. |
| Kleisli composition | [Chapter 09](../../chapter-chapter09/) | `monad`, `effect boundary` | It chains effectful steps without hiding context and evidence obligations. |
| Migration plan | [Chapter 07](../../chapter-chapter07/) | `shared boundary`, `replacement plan` | It governs replacement work without blind cutover. |
| Monad | [Chapter 09](../../chapter-chapter09/) | `Kleisli composition`, `effect boundary` | It gives the chapter's envelope for effectful operational steps. |
| Morphism | [Chapter 02](../../chapter-chapter02/) | `object`, `composition` | It names the transformation that preserves the model's structure. |
| Object | [Chapter 02](../../chapter-chapter02/) | `morphism`, `identity morphism` | It fixes the stable artifact or state boundary that later reasoning depends on. |
| Orchestration | [Chapter 08](../../chapter-chapter08/) | `synchronization boundary`, `effect boundary` | It coordinates parallel and sequential work into one governed workflow. |
| Plan Revision | [Chapter 08](../../chapter-chapter08/) | `Change Identity`, `synchronization boundary` | It keeps fan-out, retries, and later evidence attached to one current review packet instead of stale branch state. |
| Policy gate | [Chapter 01](../../chapter-chapter01/) | `human review gate`, `Policy-Evaluated Plan` | It applies rule-driven control before approval can continue. |
| Policy-Evaluated Plan | [Chapter 04](../../chapter-chapter04/) | `policy gate`, `Decision Packet` | It preserves the policy result as a first-class state rather than collapsing it into a vague approval status. |
| Product | [Chapter 06](../../chapter-chapter06/) | `Combined Review Context`, `universal property` | It gives the chapter's canonical way to recover all required review inputs from one stable boundary. |
| Pullback | [Chapter 07](../../chapter-chapter07/) | `shared boundary`, `pushout` | It explains constrained joins where artifacts must agree on one boundary. |
| Pushout | [Chapter 07](../../chapter-chapter07/) | `pullback`, `replacement plan` | It explains controlled replacement along one preserved boundary. |
| Regulated change-management review | [Chapter 07](../../chapter-chapter07/) | [Appendix D](../../appendices/appendix-d/), `shared boundary` | It shows how audit scope and approval meaning must survive the same constrained join discipline in a compliance-heavy domain. |
| Responsibility boundary | [Chapter 01](../../chapter-chapter01/) | [Introduction](../../chapter-introduction/), `effect boundary` | It is the book's main control term for explicit authority and evidence obligations. |
| Review Route | [Chapter 06](../../chapter-chapter06/) | `Combined Review Context`, `shared boundary` | It keeps review variation explicit before paths converge again. |
| Replacement plan | [Chapter 07](../../chapter-chapter07/) | `pushout`, `migration plan` | It records how legacy and new structures stay comparable during controlled replacement. |
| Reviewer view | [Chapter 05](../../chapter-chapter05/) | `runtime view`, `Decision Packet` | It is the human-facing projection of the same governed claim. |
| Runtime view | [Chapter 04](../../chapter-chapter04/) | `reviewer view`, `functor` | It translates design meaning into execution-facing state and evidence terms. |
| Route semantics | [Chapter 07](../../chapter-chapter07/) | `Review Route`, `Policy-Evaluated Plan` | It is the meaning that must stay stable when joins, migrations, or replacements claim to preserve approval logic. |
| Rollback | [Chapter 09](../../chapter-chapter09/) | `execution trace`, `Acceptance Evidence` | It is trustworthy only when the repository can reconnect the reverted action to the same approved packet and emitted trace. |
| Semantic drift | [Chapter 04](../../chapter-chapter04/) | `functor`, `coherence failure` | It names the point where a translated or refactored view stops preserving the original approval claim. |
| Schema mapping | [Chapter 07](../../chapter-chapter07/) | `replacement plan`, `shared boundary` | It is the explicit evidence that a migration preserved route, scope, and policy meaning across renamed structures. |
| Shared boundary | [Chapter 07](../../chapter-chapter07/) | `pullback`, `migration plan` | It is the minimal contract integration and replacement must preserve. |
| Shadow mode | [Chapter 07](../../chapter-chapter07/) | `replacement plan`, `transformation lineage` | It is the overlap period in which old and new route semantics are compared before cutover. |
| String diagram | [Chapter 08](../../chapter-chapter08/) | `orchestration`, `synchronization boundary` | It gives readers one compact way to inspect sequential and parallel composition without reading the whole workflow engine. |
| Synchronization boundary | [Chapter 08](../../chapter-chapter08/) | `Decision Packet`, `orchestration` | It names the fan-in contract before authority can advance. |
| Traceability matrix | [Chapter 03](../../chapter-chapter03/) | [Chapter 10](../../chapter-chapter10/), `Acceptance Evidence` | It anchors design claims to specification, verification, and implementation artifacts. |
| Transformation lineage | [Chapter 07](../../chapter-chapter07/) | `schema mapping`, `shadow execution` | It records how one integrated or replaced structure became another without losing auditability. |
| Transfer case | [Chapter 10](../../chapter-chapter10/) | [Appendix D](../../appendices/appendix-d/), `responsibility boundary` | It shows how the same compositional method moves into adjacent domains without creating a rival running example. |
| Universal property | [Chapter 06](../../chapter-chapter06/) | `product`, `coproduct` | It explains why one construction is the smallest correct reusable choice. |
| Version skew | [Chapter 05](../../chapter-chapter05/) | `reviewer view`, `runtime view` | It marks the point where parallel views or artifacts still look plausible but no longer preserve one coherent claim. |
