---
chapter_id: chapter05
english_source: src/chapter-chapter05/index.md
review_owner: editorial-review
draft_status: drafting
---

# 自然変換とビュー変換

本章は、design view、reviewer view、runtime view の対応関係を使って、natural transformation を controlled change of view として導入する。
本章では running example に reviewer-view artifact を追加し、parallel model の整合を repository artifact で点検する。

## 複数ビューが整合しなければならない理由

本節は、同じ system を表す複数 view が drift すると parallel model ではなく parallel story になることを示す。

### Parallel models of the same system

design view は artifact structure を示す。
reviewer view は人間が判断に必要とする decision packet を示す。
runtime view は execution-time state と evidence obligation を示す。

### When disagreement between views matters

差分そのものが問題ではなく、approval meaning や policy と human judgment の分離を変えてしまう差分が問題である。
そこが変わると cosmetic difference ではなく semantic conflict になる。

## 自然変換を制御されたビュー変換として捉える

本節は、natural transformation を object 名の対応表ではなく、path 全体の整合条件として扱う。

### Components of a natural transformation

design view から reviewer view への translation と、design view から runtime view への translation を比較する。
各 object ごとの correspondence だけでなく、morphism を通った後も同じ approval meaning が保たれる必要がある。

### Naturality as a consistency condition

naturality は、source model で morphism を辿ってから view を変えても、先に view を変えてから対応する morphism を辿っても、保たれる意味が一致することを要求する。
この条件が満たされないなら、その view change は harmless refactor ではない。

## 意味ドリフトを起こさないリファクタリング

本節は、refactoring claim と behavioral equivalence claim を naturality で検査する。

### Structural refactoring

review packet の section 分割や runtime state の内部細分化は、approval boundary と evidence obligation を保つなら structural refactoring と言える。
保たれないなら単なる整理ではなく意味変更である。

### Behavioral equivalence claims

behavioral equivalence を主張するなら、human gate、policy step、traceable approval path が観測可能な意味として残っていなければならない。
どれかが落ちるなら equivalence claim は強すぎる。

## インターフェース適応と互換レイヤー

本節は、adapter と facade を複数 view を揃えるための mechanism として扱う。

### Adapters, facades, and canonical forms

reviewer view は runtime detail を隠す facade 的な役割を持つ。
runtime view は execution-time state に写す adapter 的な役割を持つ。
どちらも stable source model に anchored されていなければ compatibility theater になる。

### Managing version skew across views

一つの view だけ更新されて他が遅れると version skew が生じる。
traceability matrix と linked artifact を同じ pull request で更新しなければ、coherence claim は弱くなる。

## ビュー変換レビューの観点

本節は、view change を harmless と主張する pull request に必要な evidence を示す。

### Evidence expected in a pull request

どの source view を変え、どの invariant または claim ID を保つかを明示する必要がある。
diagram、reviewer view、runtime view、workflow、matrix のどれを同時更新したかも示す必要がある。

### Signals that a transformation is not natural

ある view だけが policy と human judgment の区別を消したり、linked artifact の label と evidence path がずれたりする場合、その transformation は natural ではない。
この判定は formal proof ではなく concrete review heuristic として使える。
