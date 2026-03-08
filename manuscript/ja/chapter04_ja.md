---
chapter_id: chapter04
english_source: src/chapter-chapter04/index.md
review_owner: editorial-review
draft_status: drafting
---

# 関手とモデル変換

本章は、specification、design、runtime、implementation の各 view を、構造を保ちながら写す translation discipline として functor を導入する。
本章では running example に runtime view artifact を追加し、model translation を repository artifact に結び付ける。

## 一つのシステムにおける複数の抽象レベル

本節は、一つの system に複数 view が必要である理由と、その view が同じ system を保っていなければならない理由を示す。

### Domain, architecture, and runtime categories

specification view は何が常に真であるべきかを定義する。
design view はその制約をどの artifact path と control point で実現するかを定義する。
runtime view は execution-time state と transition で同じ意味を保てているかを定義する。

### What must remain invariant

human approval の必須性、policy check と human review の分離、request meaning の traceability、verification evidence の連結は view をまたいでも保たれる必要がある。
これらを落とす translation は、単なる表現変換ではなく設計変更になる。

## 関手を構造保存変換として捉える

本節は、functor を object と morphism の対応付けだけでなく、composition を保つ translation rule として扱う。

### Objects and morphisms under translation

specification の approval obligation は design の control path に写り、design の path は runtime の state transition に写る。
名前は変わっても、対応する役割と制約が保たれていなければならない。

### Preserving composition across views

object 対応だけでは不十分であり、composed path も対応しなければならない。
design で `policy check` と `human approval` が分かれているなら、runtime でもその順序と意味が保たれる必要がある。

## 実務でのモデル変換

本節は、running example を specification から design、design から runtime と operations へ移す。

### From specification to architecture

problem statement と acceptance criteria は、architecture が守るべき constraint を与える。
design diagram と artifact map は、その constraint を repository 上の object、edge、file に翻訳する。

### From architecture to operational workflow

runtime view は design の approval claim を execution-time state と transition に写す。
implementation workflow は、その runtime 構造を実際の作業順に展開する operational procedure である。

## 情報損失を伴う写像とリスク境界

本節は、semantic drift と deliberate approximation を区別する。

### Detecting semantic drift

runtime view が human approval を明示しなくなったり、workflow が diagram にない bypass path を持つと semantic drift が起きる。
これは documentation lag ではなく translation defect として扱うべきである。

### Documenting deliberate approximation

全ての detail を target view に持ち込む必要はないが、何を落としても invariant が保たれるかは明示する必要がある。
source view、omit した detail、なお保たれる invariant を書かなければ、安全な簡略化か欠落かを判定できない。

## 保守可能な変換の設計指針

本節は、長期に保守できる translation を選ぶための基準を示す。

### Choosing stable source models

prompt transcript や一時的な implementation detail ではなく、problem statement、acceptance criteria、design diagram のような stable constraint から translation を始めるべきである。
安定した source model があると、later view の change を比較しやすくなる。

### Designing translation interfaces for change

view 間の handoff は stable label、claim ID、artifact reference を持つ interface として設計するべきである。
runtime view を変えるなら workflow と traceability matrix も同じ change set で見直すべきである。
