---
chapter_id: introduction
english_source: src/chapter-introduction/index.md
review_owner: editorial-review
draft_status: drafting
---

# 序論: なぜ合成的設計が重要か

本章は、AI 支援ソフトウェア開発において、合成的設計がガバナンスと説明責任のための実務的な道具になることを示す。
本章では `Change Request`、`Review Plan`、`Approved Change` を使う running example を導入する。

## AI 支援エンジニアリングになぜ強い構造が必要か

本節は、AI 支援ワークフローで構造が弱いまま自動化を進めると、責任と意味保存の確認が難しくなることを示す。

### Hidden complexity in agentic workflows

AI エージェントは単独で働くのではなく、prompt context、tool call、policy check、human review をまたいで動作する。
各段階が元の要求の意味を保つとは限らないため、artifact の列を明示しないと責任が拡散する。

### Why composition is a governance tool

合成は数理上の操作であるだけでなく、複数段階の変換が同じ意味を保つかを検査する統治の道具でもある。
`draft-review-plan` と `human-approval` の連結が `policy-gated-approval` を正当化するという見方が、本書全体の出発点になる。

## Who this book is for

本節は、どのような読者がこの本を必要とし、どの前提知識で読めるかを整理する。

### Primary readers and use cases

主な読者は software architect、staff engineer、technical lead、platform engineer、AI product builder である。
engineering manager や review owner も、AI に委任できる範囲と人間が保持すべき判断を設計するために対象に含まれる。

### What prior knowledge is assumed

読者は software architecture、interface contract、technical review、repository workflow に慣れていることを前提とする。
category theory の専門知識は不要だが、不変条件と境界を丁寧に追う姿勢は必要である。

## What the reader will gain

本節は、本書が残したい実務上の成果を定義する。

### Design vocabulary and review patterns

読者は object、morphism、composition、diagram、effect boundary を、設計成果物とレビュー論点に結び付けて使えるようになる。
抽象語彙は、artifact、invariant、verification consequence を明示するための実務語として使う。

### A reusable workflow for AI-assisted delivery

読者は、problem statement、acceptance criteria、artifact map、verification plan、implementation workflow をつなぐ最小構成を得る。
その構成は、AI 支援開発を速くするだけでなく、監査可能で可逆な形に保つための骨格になる。

## How the book is organized

本節は、責任境界から形式語彙、そしてケーススタディへ進む構成意図を説明する。

### From foundations to case study

序論と Chapter 01 が責任境界と成果物の必要性を定義する。
Chapter 02 以降が object、morphism、diagram、translation、effect boundary を段階的に導入し、Chapter 10 で end-to-end に戻る。

### Suggested reading paths

多くの読者は Chapter 03 までは順に読み、その後は関心に応じて進むのがよい。
AI governance を先に掴みたい読者は Introduction、Chapter 01、Chapter 03、Chapter 09、Chapter 10 を優先するとよい。

## Conventions used throughout the book

本節は、記法、用語、cross-reference を安定させるための編集規約を示す。

### Notation and diagram rules

node には安定した artifact 名を置き、arrow には変換や判断を表す動詞句を置く。
図式は装飾ではなく、どの invariant を読者に確認させるかが明確でなければならない。

### Terminology, IDs, and cross-references

英語正本が公開用の source of truth であり、日本語下書きは入力専用である。
`Change Request`、`Review Plan`、`Approved Change`、`policy gate` などの canonical term は chapter 間でぶらさない。
