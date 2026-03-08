# Chapter Reference Map

This file is the editorial companion to the chapter-end `Notes and Further Reading` blocks and [Appendix C](../src/appendices/appendix-c.md).
It keeps the chapter-to-source mapping small, practical, and stable across later copyedit passes.

| Chapter | Formal theory references | Software architecture and engineering references | AI governance and evaluation references | Terminology bridge note |
| --- | --- | --- | --- | --- |
| Introduction | Fong and Spivak | *Software Architecture in Practice* | NIST AI RMF 1.0 | `compositional design` is used as an engineering method term rather than as a purely mathematical label. |
| Chapter 01 | None as primary | *Software Architecture in Practice* | NIST SSDF 1.1; NIST SP 800-218A; NIST AI RMF 1.0 | `responsibility boundary` is a reader-facing synthesis term for explicit authority and evidence boundaries. |
| Chapter 02 | Awodey; Riehl; Fong and Spivak | Domain-Driven Design | None as primary | `object` and `morphism` stay tied to stable artifacts and transformations rather than to implementation mechanics. |
| Chapter 03 | Fong and Spivak | *Software Abstractions* | NIST SSDF 1.1 | `commutative diagram` is framed as a reviewable consistency claim over repository artifacts. |
| Chapter 04 | Riehl; Fong and Spivak | *Software Architecture in Practice* | None as primary | `runtime view` is an engineering-facing translation target rather than a textbook formal term. |
| Chapter 05 | Awodey; Riehl | Domain-Driven Design | None as primary | `reviewer view` names a coherent human-facing projection of the same design claim. |
| Chapter 06 | Mac Lane; Fong and Spivak | Domain-Driven Design | None as primary | `Combined Review Context` and `Review Route` are canonical running-example names for product-like and coproduct-like structures. |
| Chapter 07 | Riehl; Mac Lane | *Software Architecture in Practice*; Domain-Driven Design | None as primary | `shared boundary` and `replacement plan` translate pullback and pushout reasoning into migration-safe repository artifacts. |
| Chapter 08 | Fong and Spivak | *Software Architecture in Practice* | ReAct | `synchronization boundary` is the operational fan-in contract, not a generic concurrency slogan. |
| Chapter 09 | Mac Lane; Awodey | None as primary | NIST AI RMF 1.0; NIST SP 800-218A; ReAct | `effect boundary` is the book's practical label for where tool calls and writes stop behaving like pure artifact moves. |
| Chapter 10 | None as primary | None as primary | NIST SSDF 1.1; NIST SP 800-218A; NIST AI RMF 1.0; NIST AI 600-1; SWE-bench | `acceptance evidence` is a running-example artifact name for the final governed evidence bundle, not a standardized industry term. |
