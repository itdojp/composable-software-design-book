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
- In print workflows, the same entries can be split into separate index and figure-list pages without changing the canonical wording below.

## Indexed concepts

| Term | Primary chapter | See also | Why revisit it |
| --- | --- | --- | --- |
| Acceptance Evidence | [Chapter 09](../../chapter-chapter09/) | [Chapter 10](../../chapter-chapter10/), [Appendix B](../../appendices/appendix-b/) | It closes the governed evidence story after effectful execution. |
| Adapter | [Chapter 05](../../chapter-chapter05/) | `reviewer view`, `runtime view` | It explains interface reshaping without losing the design claim. |
| Approved Change | [Chapter 01](../../chapter-chapter01/) | `Approval decision record`, `Execution trace` | It is the canonical decision outcome artifact, not the full evidence bundle. |
| Audit log | [Chapter 01](../../chapter-chapter01/) | `Execution trace`, `Acceptance Evidence` | It preserves broader action history beyond the decision artifact itself. |
| Bounded delegation | [Chapter 01](../../chapter-chapter01/) | `AI agent`, `human review gate` | It defines what agents may do without inheriting approval authority. |
| Combined Review Context | [Chapter 06](../../chapter-chapter06/) | `Decision Packet`, `Review Route` | It is the smallest recoverable context for governed review. |
| Commutative diagram | [Chapter 03](../../chapter-chapter03/) | `traceability matrix`, `coherence failure` | It turns path equivalence into a reviewable consistency claim. |
| Decision Packet | [Chapter 05](../../chapter-chapter05/) | [Chapter 08](../../chapter-chapter08/), [Chapter 10](../../chapter-chapter10/) | It synchronizes scope, policy, and evidence before human judgment. |
| Effect boundary | [Chapter 09](../../chapter-chapter09/) | `Execution trace`, `Acceptance Evidence` | It marks where pure artifact reasoning becomes operationally effectful. |
| Execution trace | [Chapter 09](../../chapter-chapter09/) | [Chapter 10](../../chapter-chapter10/), `audit log` | It records what actually ran after approval and dispatch. |
| Functor | [Chapter 04](../../chapter-chapter04/) | `runtime view`, `reviewer view` | It explains structure-preserving translation across views. |
| Human review gate | [Chapter 01](../../chapter-chapter01/) | `policy gate`, `Bounded delegation` | It keeps final risk acceptance explicitly human-led. |
| Kleisli composition | [Chapter 09](../../chapter-chapter09/) | `monad`, `effect boundary` | It chains effectful steps without hiding context and evidence obligations. |
| Migration plan | [Chapter 07](../../chapter-chapter07/) | `shared boundary`, `replacement plan` | It governs replacement work without blind cutover. |
| Monad | [Chapter 09](../../chapter-chapter09/) | `Kleisli composition`, `effect boundary` | It gives the chapter's envelope for effectful operational steps. |
| Morphism | [Chapter 02](../../chapter-chapter02/) | `object`, `composition` | It names the transformation that preserves the model's structure. |
| Object | [Chapter 02](../../chapter-chapter02/) | `morphism`, `identity morphism` | It fixes the stable artifact or state boundary that later reasoning depends on. |
| Orchestration | [Chapter 08](../../chapter-chapter08/) | `synchronization boundary`, `effect boundary` | It coordinates parallel and sequential work into one governed workflow. |
| Policy gate | [Chapter 01](../../chapter-chapter01/) | `human review gate`, `Policy-Evaluated Plan` | It applies rule-driven control before approval can continue. |
| Pullback | [Chapter 07](../../chapter-chapter07/) | `shared boundary`, `pushout` | It explains constrained joins where artifacts must agree on one boundary. |
| Pushout | [Chapter 07](../../chapter-chapter07/) | `pullback`, `replacement plan` | It explains controlled replacement along one preserved boundary. |
| Responsibility boundary | [Chapter 01](../../chapter-chapter01/) | [Introduction](../../chapter-introduction/), `effect boundary` | It is the book's main control term for explicit authority and evidence obligations. |
| Review Route | [Chapter 06](../../chapter-chapter06/) | `Combined Review Context`, `shared boundary` | It keeps review variation explicit before paths converge again. |
| Reviewer view | [Chapter 05](../../chapter-chapter05/) | `runtime view`, `Decision Packet` | It is the human-facing projection of the same governed claim. |
| Runtime view | [Chapter 04](../../chapter-chapter04/) | `reviewer view`, `functor` | It translates design meaning into execution-facing state and evidence terms. |
| Shared boundary | [Chapter 07](../../chapter-chapter07/) | `pullback`, `migration plan` | It is the minimal contract integration and replacement must preserve. |
| Synchronization boundary | [Chapter 08](../../chapter-chapter08/) | `Decision Packet`, `orchestration` | It names the fan-in contract before authority can advance. |
| Traceability matrix | [Chapter 03](../../chapter-chapter03/) | [Chapter 10](../../chapter-chapter10/), `Acceptance Evidence` | It anchors design claims to specification, verification, and implementation artifacts. |
| Universal property | [Chapter 06](../../chapter-chapter06/) | `product`, `coproduct` | It explains why one construction is the smallest correct reusable choice. |
