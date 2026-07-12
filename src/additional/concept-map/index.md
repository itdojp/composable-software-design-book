---
layout: book
title: "Concept Map"
description: "A reader map connecting responsibility boundaries, categorical structures, delivery controls, and the running example."
---

# Concept Map

This map shows how the book's category-theoretic vocabulary supports one engineering argument.
Start with responsibility, preserve structure across representations, make effects explicit, and require evidence before acceptance.

## The main reasoning path

1. **Set responsibility boundaries.**  
   [Chapter 01](../../chapter-chapter01/) identifies decisions, artifacts, and approvals that must remain accountable.
2. **Model stable things and allowed transformations.**  
   [Chapter 02](../../chapter-chapter02/) introduces objects, morphisms, identity, and composition as an interface vocabulary.
3. **Test whether representations agree.**  
   [Chapter 03](../../chapter-chapter03/) uses commutative diagrams to expose drift between requirements, architecture, implementation, and evidence.
4. **Preserve structure while views and systems change.**  
   [Chapters 04–07](../../chapter-chapter04/) connect translation, view changes, variation, integration, and migration to explicit preservation obligations.
5. **Separate coordination from effects.**  
   [Chapter 08](../../chapter-chapter08/) models sequential and parallel coordination, while [Chapter 09](../../chapter-chapter09/) makes tool calls and other effects reviewable.
6. **Close the loop with acceptance evidence.**  
   [Chapter 10](../../chapter-chapter10/) applies the complete chain to the policy-gated change-review example.

## Concepts, engineering questions, and evidence

| Concept cluster | Engineering question | Evidence to inspect |
| --- | --- | --- |
| Responsibility boundaries | Who may propose, approve, execute, and stop the work? | Decision rights, review plan, approval record |
| Objects and morphisms | What is stable, and which transformations are allowed? | Interface contract, transformation rule, identity and composition checks |
| Commutative diagrams | Do independent implementation paths preserve the same claim? | Cross-view trace, diagram check, mismatch report |
| Functors and natural transformations | What must survive translation or a change of view? | Mapping table, preservation invariant, version-skew check |
| Products, coproducts, pullbacks, and pushouts | How should requirements, alternatives, integrations, and migrations be composed? | Compatibility assumptions, provenance, conflict policy |
| Monoidal structure and effects | Which steps may run in parallel, and where can the outside world change? | Workflow graph, effect boundary, retry and rollback rule |
| End-to-end case study | Can the accepted implementation be traced back to the governed specification? | Specification-to-evidence trace and acceptance gate |

## How to use the map

- If the failure is about authority or approval, begin with Chapter 01 and then move to Chapters 03, 09, and 10.
- If the failure is model drift, begin with Chapters 02 and 03, then select the relevant translation or integration chapter.
- If the failure is orchestration or unsafe tool use, begin with Chapters 08 and 09, then verify the complete evidence chain in Chapter 10.
- Use [Appendix B](../../appendices/appendix-b/) for definitions and the [List of Figures and Tables](../../backmatter/list-of-figures/) for the corresponding visual references.
