---
layout: book
title: "Compositional Software Design for Agentic Systems"
subtitle: "A Category-Theoretic Guide to Human-AI Boundaries and Verifiable Engineering"
description: "A practical guide to governed AI-assisted software delivery using composition, diagrams, and effect boundaries that remain auditable and verifiable."
author: "ITDO Inc."
version: "First Edition"
last_updated: "2026-05-23"
---

# Compositional Software Design for Agentic Systems

A Category-Theoretic Guide to Human-AI Boundaries and Verifiable Engineering

A practical guide to governed AI-assisted software delivery using composition, diagrams, and effect boundaries that remain auditable and verifiable.

AI-assisted delivery is moving faster than many teams can explain who may approve a change, which design boundaries still hold, and what evidence must survive execution.
This book addresses that gap with a compositional design method for governed software delivery.
It uses category-theoretic ideas selectively so that architecture, review, orchestration, and verification remain one inspectable engineering story.

## Start Here

This book is for software architects, staff engineers, technical leads, platform engineers, and AI product builders who need AI-assisted delivery to remain reviewable when work crosses from proposal to approval and from approval to execution.
You should be comfortable with software architecture, interface design, and technical review; prior exposure to category theory is helpful but not required.
Begin with [How to Use This Book](src/additional/how-to-use-this-book/), [Who This Book Is For](src/additional/who-this-book-is-for/), the [Introduction](src/chapter-introduction/), and [Chapter 01](src/chapter-chapter01/) before inspecting repository artifacts.

## What You Will Be Able to Produce

- A responsibility-boundary map that separates delegated drafting, policy evaluation, human approval, execution, and evidence.
- A set of named objects, transformations, and diagrams that makes preservation claims reviewable across design and runtime views.
- A synchronized decision packet that keeps request scope, policy results, evidence, and approval authority distinguishable.
- An effect boundary, execution trace, and acceptance-evidence path that connects an approved change to its operational outcome.

## Fit and Limits

Use this method when AI-assisted work crosses an approval or execution boundary, when multiple views must preserve one design meaning, or when a team must reconstruct why an automated action was allowed.
The method is not a prompt-optimization guide, a product comparison, or a substitute for domain-specific legal, security, safety, or architecture review.
Do not force a categorical abstraction onto a local problem when an ordinary interface contract, checklist, or test communicates the obligation more clearly.

## Choose a Reading Path

- **Full method:** read the [Preface](src/additional/preface/), [How to Use This Book](src/additional/how-to-use-this-book/), [Concept Map](src/additional/concept-map/), [Introduction](src/chapter-introduction/), and Chapters 01 through 10 in order.
- **Governance path:** read the [Introduction](src/chapter-introduction/), [Chapter 01](src/chapter-chapter01/), [Chapter 03](src/chapter-chapter03/), [Chapter 09](src/chapter-chapter09/), and [Chapter 10](src/chapter-chapter10/).
- **Architecture path:** read the [Introduction](src/chapter-introduction/), Chapters [01](src/chapter-chapter01/), [02](src/chapter-chapter02/), and [03](src/chapter-chapter03/), followed by Chapters [04](src/chapter-chapter04/) through [07](src/chapter-chapter07/).
- **Delivery path:** read the [Introduction](src/chapter-introduction/), [Chapter 01](src/chapter-chapter01/), [Chapter 08](src/chapter-chapter08/), [Chapter 09](src/chapter-chapter09/), and [Chapter 10](src/chapter-chapter10/).

After the prose establishes the method, use the [minimal example](examples/minimal/policy-gated-change-review/README/) to inspect its smallest artifact chain and the [common running example](examples/common/policy-gated-change-review/README/) to trace the full specification, design, review, implementation, and evidence path.

## Why This Book Now

Many teams can generate candidate changes, workflow steps, and implementation drafts more quickly than they can govern them.
That mismatch creates review debt, ambiguous ownership, and weak evidence trails.
This book addresses that gap at the points where a system changes approval authority or causes an operational effect.

## What Makes This Book Different

- It treats AI-assisted delivery as a design problem about boundaries, evidence, and accountability rather than a prompt-optimization problem.
- It uses category theory as a working design vocabulary for software systems rather than as a stand-alone mathematics survey.
- It connects diagrams, review boundaries, runtime views, traces, and acceptance evidence as one reusable engineering method.

## Front Matter

- [Preface](src/additional/preface/)
- [How to Use This Book](src/additional/how-to-use-this-book/)
- [Concept Map](src/additional/concept-map/)
- [Who This Book Is For](src/additional/who-this-book-is-for/)

## Introduction

- [Introduction: Why Compositional Design Matters](src/chapter-introduction/)

## Part I. Foundations and Responsibility Boundaries

- [Part I Opener. Foundations and Responsibility Boundaries](src/parts/part-i/)
- [Chapter 01. Human and AI Responsibility Boundaries](src/chapter-chapter01/)
- [Chapter 02. Objects, Morphisms, and Composition](src/chapter-chapter02/)
- [Chapter 03. Diagrams and Commutativity](src/chapter-chapter03/)

## Part II. Structure-Preserving Translation and Integration

- [Part II Opener. Structure-Preserving Translation and Integration](src/parts/part-ii/)
- [Chapter 04. Functors and Model Translation](src/chapter-chapter04/)
- [Chapter 05. Natural Transformations and View Changes](src/chapter-chapter05/)
- [Chapter 06. Universality with Products and Coproducts](src/chapter-chapter06/)
- [Chapter 07. Pullbacks and Pushouts for Integration and Migration](src/chapter-chapter07/)

## Part III. Coordination, Effects, and Delivery

- [Part III Opener. Coordination, Effects, and Delivery](src/parts/part-iii/)
- [Chapter 08. Monoidal Categories and String Diagrams](src/chapter-chapter08/)
- [Chapter 09. Monads, Kleisli Composition, and Effect Boundaries](src/chapter-chapter09/)
- [Chapter 10. Case Study: From Specification to AI-Assisted Implementation](src/chapter-chapter10/)

## Appendices

- [Appendix A. Notation and Diagram Conventions](src/appendices/appendix-a/)
- [Appendix B. Glossary of Category-Theoretic and Engineering Terms](src/appendices/appendix-b/)
- [Appendix C. References and Further Study](src/appendices/appendix-c/)
- [Appendix D. Transfer Cases Across Domains](src/appendices/appendix-d/)

## Backmatter

- [Subject Index](src/backmatter/subject-index/)
- [List of Figures and Tables](src/backmatter/list-of-figures/)

## Afterword

- [Publisher Note and ITDO](src/afterword/about-the-author-and-itdo/)
- [Acknowledgments](src/afterword/acknowledgments/)

## Related Reading

For a Japanese reader-facing treatment centered on design artifacts, Context Pack use, and GitHub/CI workflows, see the independent [Categorical Software Design Book](https://itdojp.github.io/categorical-software-design-book/).

## License

Reader-facing book content is published under [CC BY-NC-SA 4.0](LICENSE).
Code, build files, schemas, and reusable technical assets in this repository are published under [Apache-2.0](LICENSES/Apache-2.0.txt).
Executable code snippets, shell commands, JSON fragments, YAML fragments, and other machine-readable examples embedded in the book content are treated as Apache-2.0 unless a file states otherwise.
See [LICENSE-SCOPE.md](LICENSE-SCOPE.md) for the canonical path boundary and [COMMERCIAL.md](COMMERCIAL.md) for commercial-use guidance.

---

**Author:** ITDO Inc.  
**Edition:** First Edition
**Last updated:** {{ page.last_updated }}
