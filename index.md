---
layout: book
title: "Compositional Software Design for Agentic Systems"
subtitle: "A Category-Theoretic Guide to Human-AI Boundaries and Verifiable Engineering"
description: "A practical guide to governed AI-assisted software delivery using composition, diagrams, and effect boundaries that remain auditable and verifiable."
author: "ITDO Inc."
version: "First Edition"
---

# Compositional Software Design for Agentic Systems

A Category-Theoretic Guide to Human-AI Boundaries and Verifiable Engineering

A practical guide to governed AI-assisted software delivery using composition, diagrams, and effect boundaries that remain auditable and verifiable.

AI-assisted delivery is moving faster than many teams can explain who may approve a change, which design boundaries still hold, and what evidence must survive execution.
This book addresses that gap with a compositional design method for governed software delivery.
It uses category-theoretic ideas selectively so that architecture, review, orchestration, and verification remain one inspectable engineering story.

## Why This Book Now

Many teams can generate candidate changes, workflow steps, and implementation drafts more quickly than they can govern them.
That mismatch creates review debt, ambiguous ownership, and weak evidence trails.
This book is for readers who need AI-assisted engineering to stay explainable at the moment a system crosses from proposal to approval and from approval to execution.

## What Makes This Book Different

- It treats AI-assisted delivery as a design problem about boundaries, evidence, and accountability rather than a prompt-optimization problem.
- It uses category theory as a working design vocabulary for software systems rather than as a stand-alone mathematics survey.
- It builds one reusable method that connects diagrams, review gates, runtime views, traces, and acceptance evidence across a full engineering workflow.

## What You Will Learn

- Define clear responsibility boundaries between human reviewers and AI-assisted workflows.
- Model software systems with objects, morphisms, composition, and diagrams.
- Use universal constructions and effect boundaries to reason about integration, migration, and orchestration.
- Translate the formal vocabulary into an auditable end-to-end engineering workflow.

## Intended Readers

This book is written for software architects, staff engineers, technical leads, platform engineers, and AI product builders.
It assumes readers care about both formal rigor and delivery realism.
It is especially aimed at teams that need to keep approval authority, system meaning, and operational evidence aligned while AI systems participate in delivery.

## Prerequisites

Readers should be comfortable with software architecture, interface design, and technical review.
Prior exposure to category theory is helpful but not required.

## Reading Guide

Read the Preface, How to Use This Book, Who This Book Is For, the Introduction, and Chapter 01 first if you want the clearest entry into the book's promise and scope.
Read Chapters 02 through 09 in order if you want the conceptual build-up from composition and diagrams to orchestration and effect boundaries.
Read Chapter 10 after the core chapters to see the method applied as one end-to-end engineering argument.

## Quickstart

Start with the front matter and the Introduction if you want the book's main promise before any repository inspection.
Use the [minimal example](examples/minimal/policy-gated-change-review/README/) after that first pass to see the smallest reusable chain of objects, morphisms, and a diagram.
Continue with the [common running example](examples/common/policy-gated-change-review/README/) when you want to inspect the specification, design, verification, and implementation artifacts that support the chapter arguments.

## Front Matter

- [Preface](src/additional/preface/)
- [How to Use This Book](src/additional/how-to-use-this-book/)
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

- [About the Author and ITDO](src/afterword/about-the-author-and-itdo/)
- [Acknowledgments](src/afterword/acknowledgments/)

## Publication Policy

English text is the canonical source for publication.
Japanese drafts under `manuscript/ja/` are editorial inputs and are not published as-is.
They are distinct from the separately published Japanese book in `categorical-software-design-book`.

## Related Japanese Book

- `圏論によるAIエージェント時代の合成的ソフトウェア設計` (`categorical-software-design-book`) is a related but independent Japanese book.
- This English book is not a rename or replacement for that Japanese book.
- Start here if you want the English-first canonical manuscript and the current part-based composition.
- Start with the Japanese book if you want a Japanese reader-facing guide focused on software design artifacts for the AI agent era, Context Pack usage, and GitHub/CI-oriented guidance.
- Related Japanese book: [Public site](https://itdojp.github.io/categorical-software-design-book/) / [Repository](https://github.com/itdojp/categorical-software-design-book)

## License

Reader-facing book content is published under [CC BY-NC-SA 4.0](LICENSE).
Code, build files, schemas, and reusable technical assets in this repository are published under [Apache-2.0](LICENSES/Apache-2.0.txt).
Executable code snippets, shell commands, JSON fragments, YAML fragments, and other machine-readable examples embedded in the book content are treated as Apache-2.0 unless a file states otherwise.
See [LICENSE-SCOPE.md](LICENSE-SCOPE.md) for the canonical path boundary and [COMMERCIAL.md](COMMERCIAL.md) for commercial-use guidance.

---

**Author:** ITDO Inc.  
**Edition:** First Edition
**Last updated:** 2026-03-17
