---
chapter_id: chapter06
english_source: src/chapter-chapter06/index.md
review_owner: editorial-review
draft_status: drafting
---

# 普遍性と積・余積

本章は、universal property を使って combined requirement と explicit variation のための最小で正しい construction を選ぶ。
running example では `Combined Review Context` を product-like な共有境界として、`Review Route` を coproduct-like な variation boundary として扱う。

## 設計基準としての普遍性

本節は、pattern に似ているかどうかではなく、repository の obligation を最小構造で支えられるかどうかで design を選ぶ。

### Why universality beats ad hoc pattern matching

ad hoc な bundle や flag は局所的には動いても、canonical boundary を与えない。
product は combined requirement の最小共有境界を問う。
coproduct は variant がどの共通境界に入るべきかを問う。

### Reading the universal condition in engineering terms

engineering 的には、universal condition は competing artifact や new route が同じ canonical construction を経由できることを要求する。
そうでなければ implicit approval boundary や hidden branch rule が残る。

## 積による複合要求の表現

本節は、scope、policy result、evidence links を一緒に扱う review boundary を product-like に読む。

### Joint constraints and shared context

`Combined Review Context` は `Requested Scope`、`Policy Result`、`Evidence Links` を同時に保持する。
reviewer view の `Decision Packet` はその presentation であり、別の source of truth ではない。

### Multi-input interfaces and synchronized state

policy result、scope、evidence が別々に更新されると approval meaning が崩れる。
product-like な共有境界を置くことで、同じ review event に属するかを repository artifact として点検できる。

## 余積による代替経路と variation

本節は、standard review と escalated review の route split を coproduct-like に読む。

### Variant handling and explicit branching

`Standard Review Path` と `Escalated Review Path` は `Review Route` に明示的に入る。
branch を boolean flag や free-form comment に隠すのではなく、named route として扱う。

### Stable extension points

新しい review route を追加しても、variant-specific logic は entry point 付近に閉じるべきである。
downstream artifact がすべて再分岐するなら stable extension point ではない。

## 普遍性から作る再利用可能な構成

本節は、一度定義した product-like boundary と coproduct-like boundary を他 artifact に再利用する。

### Decompose once and reuse many times

reviewer view、implementation workflow、traceability matrix は同じ decomposition を再利用できる。
これにより chapter-local synonym や hidden branch rule を減らせる。

### Avoiding premature specialization

joint requirement がないのに product を作ったり、意味差がないのに coproduct branch を増やしたりしてはいけない。
普遍性は最小の正しい structure を選ぶ discipline であり、過剰な formalization の口実ではない。

## 最小で正しい構成を選ぶ

本節は、product-like design と coproduct-like design を選ぶ前に確認すべき review question をまとめる。

### Questions for product-like designs

どの component が必ず一緒に必要か。
それぞれを hidden state なしに recover できるか。

### Questions for coproduct-like designs

variant の違いが obligation や risk handling の違いか。
shared boundary を保ったまま新しい variant を追加できるか。
