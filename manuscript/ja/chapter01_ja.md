---
chapter_id: chapter01
english_source: src/chapter-chapter01/index.md
review_owner: editorial-review
draft_status: drafting
---

# 人間と AI の責任境界

本章は、AI 支援開発で誰が何を決め、どの artifact と evidence を残し、どこで rollback と escalation を要求するかを定義する。
本章では running example の `Change Request`、`Review Plan`、`Approved Change` を責任境界の中心 artifact として扱う。

## なぜ責任境界が重要か

本節は、責任境界を process の後付けではなく、設計構造そのものとして扱う理由を示す。

### Hidden delegation and diffused ownership

AI 支援ワークフローでは、委任が prompt や automation の内部に隠れやすい。
最終 diff だけを見ても、誰が提案し、誰が条件を満たしたと判断し、誰が承認したかは分からない。

### Auditability as a design objective

監査可能性は後から log を足せばよい性質ではない。
problem statement、acceptance criteria、verification checks、review decision を最初から artifact として残す必要がある。

## Design artifacts as accountability surfaces

本節は、責任境界を enforce する面として設計成果物を扱う。

### Specifications, interfaces, and verification plans

`Change Request` は要求の範囲と制約を定義する。
`Review Plan` は agent が何をしてよく、何を人間に戻すべきかを定義する。
verification plan は workflow が自分の主張をどう検査するかを定義する。

### Decision logs and review records

永続化すべきなのは会話の全文ではなく、境界を越えた理由を説明する最小記録である。
audit log と execution trace は重要だが、それだけでは設計上の正当性は示せない。

## 人間とエージェントの権限配分

本節は、AI に委任できる作業と、人間が保持すべき判断を分ける。

### Delegation, approval, and escalation

agent は `Review Plan` の下書きや file-level change の提案はできるが、acceptance criteria の変更や `Approved Change` の承認はできない。
policy 結果が曖昧な場合、artifact が不足している場合、不可逆な effect を伴う場合は escalation が必要である。

### Unsafe automation patterns

提案と承認を同じ automation に持たせることは危険である。
`policy gate` と `human review gate` を一つの曖昧な承認状態に畳み込むことも危険である。

## 運用上の制御ループ

本節は、承認後の monitoring、rollback、incident response を責任境界の延長として扱う。

### Monitoring, rollback, and incident response

`Approved Change` は責任の終点ではなく、より高い信頼で execution を開始する起点である。
そのため execution trace、rollback 条件、incident routing を事前に結び付けておく必要がある。

### Feedback from operations to design

運用で見つかった曖昧さは prompt tuning だけで直すべきではない。
`Change Request`、`Review Plan`、verification plan の構造に戻して修正する必要がある。

## この境界モデルが後続章に与える意味

本節は、本章の責任境界モデルが後続の形式章の問いを準備することを示す。

### Questions to carry into the formal chapters

どの artifact を object とみなし、どの変換を morphism とみなすかという問いは、責任境界の設計から自然に現れる。
どの path が同じ意味を保つかという問いが、diagram と commutativity の章につながる。

### Criteria for a trustworthy workflow

信頼できる workflow には、explicit artifact path、分離された `policy gate` と `human review gate`、bounded delegation、verification evidence、rollback 可能性が必要である。
これらが欠ける場合、後続の形式技法を使っても曖昧な workflow 自体は救えない。
