---
layout: book
title: "References and Further Study"
appendix: appendix-c
order: 14
description: "Annotated references for theory, engineering practice, and AI-assisted system design."
---

# Appendix C. References and Further Study

This appendix points readers to the sources that deepen the formal, practical, and workflow dimensions of the book.
It is intentionally selective.
Each reference is included because it extends one concrete part of the manuscript rather than because it is historically comprehensive.

## Foundational texts

This section groups the mathematical and conceptual sources that support the formal core of the book.

### Introductory category theory references

- [Steve Awodey, *Category Theory*](https://doi.org/10.1093/acprof:oso/9780198568612.001.0001) is a compact first formal text once you want a mathematically serious pass over categories, functors, natural transformations, adjunctions, and monads after Chapters 02 through 05.
- [Emily Riehl, *Category Theory in Context*](https://math.jhu.edu/~eriehl/context/) is the best follow-up when you want richer examples, stronger coverage of limits and adjunctions, and a legally hosted free PDF from the author.

### Texts on universal constructions and monoidal reasoning

- [Saunders Mac Lane, *Categories for the Working Mathematician*](https://doi.org/10.1007/978-1-4757-4721-8) remains the canonical long-term desk reference for universal constructions, adjoint functors, monoidal structure, and coherence.
- [Brendan Fong and David I. Spivak, *An Invitation to Applied Category Theory: Seven Sketches in Compositionality*](https://doi.org/10.1017/9781108668804) is the closest match to this book's goals because it connects categorical structure to databases, collaborative design, circuits, and compositional modeling.

## Engineering practice references

This section groups sources on architecture, design review, and verification-oriented software engineering.

### Architecture and interface design references

- [Len Bass, Paul Clements, and Rick Kazman, *Software Architecture in Practice*, 4th ed.](https://www.informit.com/store/software-architecture-in-practice-9780136886099) is the strongest architecture companion for readers who want to connect this book's artifact-oriented reasoning to views, quality attributes, and decision documentation.
- [Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*](https://www.informit.com/store/domain-driven-design-tackling-complexity-in-the-heart-9780321125217) is the most useful extension when you need sharper vocabulary for canonical models, bounded contexts, and interface language discipline.

### Verification, testing, and traceability references

- [Daniel Jackson, *Software Abstractions*](https://mitpressbookstore.mit.edu/book/9780262528900) is the most relevant reference here for readers who want lightweight formal methods that improve design review early rather than proof obligations late.
- [National Institute of Standards and Technology, *Secure Software Development Framework (SSDF) Version 1.1: Recommendations for Mitigating the Risk of Software Vulnerabilities*](https://doi.org/10.6028/NIST.SP.800-218) is a practical control vocabulary for traceable, reviewable, and repeatable software delivery.

## AI-assisted systems and verification references

This section groups sources on agentic systems, tool orchestration, and governance of automated work.

### Human-in-the-loop engineering references

- [Shunyu Yao et al., *ReAct: Synergizing Reasoning and Acting in Language Models*](https://arxiv.org/abs/2210.03629) is a useful comparison point when you want to contrast the book's orchestration artifacts with a widely cited agent pattern that interleaves reasoning and action.
- [National Institute of Standards and Technology, *Secure Software Development Practices for Generative AI and Dual-Use Foundation Models: An SSDF Community Profile*](https://doi.org/10.6028/NIST.SP.800-218A) is the most directly operational reference in this appendix when you need control guidance for AI model and system development inside a broader delivery lifecycle.

### Safety, auditability, and evaluation references

- [National Institute of Standards and Technology, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*](https://doi.org/10.6028/NIST.AI.100-1) is the right place to map the book's governance language onto a broader organizational risk-management framework.
- [National Institute of Standards and Technology, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*](https://doi.org/10.6028/NIST.AI.600-1) gives more concrete generative-AI risk categories, testing themes, and disclosure expectations than the base framework alone.
- [Carlos E. Jimenez et al., *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?*](https://arxiv.org/abs/2310.06770) is the most relevant evaluation reference here when you want benchmark pressure from real repository issues rather than synthetic coding prompts.

## Suggested study paths

This section gives readers multiple routes for continuing after the main text.

### Path for readers who need stronger mathematical depth

1. Read Awodey for a compact re-pass over the formal core.
2. Move to Riehl when you want richer examples and stronger practice with limits, colimits, and adjunctions.
3. Use Mac Lane as the long-term reference once you need canonical statements and proofs.
4. Return to Chapters 06 through 09 and compare your new formal vocabulary against the repository artifacts in the running example.

### Path for readers who need stronger implementation and operations depth

1. Read Software Architecture in Practice together with the running example's artifact map and workflow files.
2. Pair Domain-Driven Design with Chapters 01, 04, and 07 when refining responsibility boundaries, canonical models, and shared boundaries.
3. Use Software Abstractions and SSDF to strengthen verification and delivery controls before adding more automation.
4. Finish with AI RMF, the Generative AI Profile, ReAct, and SWE-bench so agent capabilities, control requirements, and evaluation pressure are considered together rather than in isolation.
