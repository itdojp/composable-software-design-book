---
chapter_id: chapter07
english_source: src/chapter-chapter07/index.md
review_owner: editorial-review
draft_status: drafting
---

# 引き戻しと押し出しによる統合と移行

本章は、pullback と pushout を integration と migration の repository artifact に結び付ける。
running example では `design/shared-boundary.md` と `design/replacement-plan.md` を使い、join と replacement を shared boundary ベースで説明する。

## 統合作業における共有境界

本節は、integration の前提になる canonical key、policy label、route identifier を固定する。

### Canonical keys, schemas, and policies

`Change Identity`、`Repository Scope`、`Policy Classification`、`Approval Route ID` が shared boundary を作る。
artifact 同士を join できるのは、この boundary を同じ意味で保存しているときだけである。

### Why integration fails at the boundary

integration failure は merge algorithm の前に起きる。
identifier や route label や policy vocabulary が一致しないなら、その join は constrained join ではない。

## 制約付き結合としての引き戻し

本節は、pullback を reviewer artifact と runtime artifact の constrained join として読む。

### Joining systems under shared conditions

`Decision Packet` と `Policy-Evaluated Plan` は、同じ `Change Identity`、`Repository Scope`、`Approval Route ID` を持つときだけ安全に join できる。
一部の field だけ一致しても boundary meaning が違うなら join してはいけない。

### Provenance and policy preservation

join 後も、どの policy evaluation とどの route selection がその state を作ったかを追える必要がある。
policy meaning を collapse した join は provenance が残っていても safe ではない。

## 置換と移行としての押し出し

本節は、pushout を blind swap ではなく shared interface を保った replacement として読む。

### Replacing components without losing meaning

`Legacy Route Mapper` を `Unified Review Gateway` に置き換えるときも、shared boundary を保存しなければならない。
downstream artifact が同じ boundary を消費できることが replacement の条件である。

### Controlled schema and interface migration

legacy field は schema mapping を通じて shared boundary に写される。
shadow mode と cutover criteria がない migration は reviewable ではない。

## 衝突解消とトレーサビリティ

本節は、incompatible assumption を merge ではなく explicit conflict として扱う。

### Reconciling incompatible assumptions

conflict が key、route label、policy classification、approval meaning のどこにあるかを先に決める必要がある。
`Approved Change` の意味に触れる conflict は redesign 問題である。

### Recording transformation lineage

lineage には old component、new component、compared boundary field、accepted divergence を残す。
それがないと migration 後に preserved meaning を監査できない。

## 統合と移行の判断基準

本節は、merge を続けるか redesign するかの criteria をまとめる。

### When to stop merging and redesign

stable key や policy vocabulary を共有できないなら merge を止めるべきである。
approval meaning の差分を interface rename に隠すなら redesign が必要である。

### Criteria for a safe migration plan

small shared boundary、documented schema mapping、shadow execution、lineage recording が必要である。
cutover 後も同じ approval meaning と human review obligation が残ることが条件である。
