---
chapter_id: chapter09
english_source: src/chapter-chapter09/index.md
review_owner: editorial-review
draft_status: drafting
---

# モナド、クライスリ合成、効果境界

本章は、AI-assisted workflow の side effect を repository artifact として見える形にする。
running example では `implementation/effect-boundary.md`、`implementation/execution-trace.md`、`verification/acceptance-evidence.md` を使い、effectful step を pure core から分離する。

## なぜ効果には明示的な境界が必要か

本節は、tool call、prompt、approval write、execution dispatch を design commitment として扱う。

### Side effects as design commitments

effect は implementation detail ではなく authority と evidence の変化点である。
どの dependency に触れ、どの evidence を出すかを named step にしないと review できない。

### The cost of hidden operational behavior

hidden prompt context や silent cache fallback は同じ artifact から違う outcome を作り得る。
それでは traceability も rollback も信頼できない。

## モナドを運用上の包みとして捉える

本節は、effectful computation を value と operational context の組として扱う。

### Pure core and effectful shell

scope comparison や evidence completeness check は pure core に寄せられる。
LLM invocation、policy engine call、review decision record、execution dispatch は effectful shell に残る。

### Reading unit and bind in engineering terms

unit は pure artifact を governed context に入れる操作である。
bind はその context を保ったまま次の effectful step へ渡し、failure でも evidence obligation を失わないようにする。

## エージェントオーケストレーションにおけるクライスリ合成

本節は、effect envelope を返す step 同士を chain する見方を使う。

### Tool calls, prompts, and execution context

agent runtime、policy engine、reviewer action、execution environment は異なる effect source である。
それぞれが prompt context、tool output、authority change を持つので、裸の function composition では十分でない。

### Chaining effectful steps safely

policy timeout は naked error ではなく retry や manual review を含む governed outcome で返すべきである。
evidence collection failure も sync boundary に渡せる named state にしておくと later step が推測に頼らずに済む。

## エラー、状態、I/O、外部ツールの管理

本節は、複数の effect class を一つの review story にまとめる。

### Choosing the dominant effect model

running example では dominated effect model を governed review state に置く。
error、state、I/O はすべて reviewability と approval semantics の下で解釈される。

### Composing multiple effects without confusion

prompt context、tool result、approval record、dispatch result を同じ envelope の evidence field に置くと reader-facing な story が安定する。
effect ごとに別の暗黙規約を持ち込むと workflow は読めなくなる。

## 本番システムにおける効果の封じ込め

本節は、escape hatch、rollback、audit を governed artifact として残す。

### Reviewable escape hatches

manual override や cached policy usage は invisible default にしてはいけない。
deviation を authorized event として trace に残す必要がある。

### Operational limits, rollback, and audit

retry は failed branch か sync point に限定し、irreversible step は `Approved Change` の後にしか置かない。
Chapter 10 では acceptance evidence を使って、specification から implementation までの full path を再構成する。
