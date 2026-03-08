---
chapter_id: chapter02
english_source: src/chapter-chapter02/index.md
review_owner: editorial-review
draft_status: drafting
---

# 対象・射・合成

本章は、AI 支援時代のソフトウェア設計を記述するために、object、morphism、composition を repository artifact と workflow に結び付けて導入する。
本章では running example の `Change Request`、`Review Plan`、`Approved Change` を継続して使う。

## システムを対象として捉える

本節は、何を object として固定するとレビュー、再利用、追跡可能性にとって有益かを定める。

### Choosing the right units of design

object は単に存在するものではなく、境界、役割、review consequence を持つ安定した設計単位である。
running example では `Change Request`、`Review Plan`、`Approved Change` がその条件を満たす。

### Objects as stable interfaces and states

object は安定した interface を表すこともあれば、安定した state を表すこともある。
重要なのは、変換の前後で同じ設計単位として識別できることである。

## インターフェースと変換を射として捉える

本節は、どの変換を morphism と見なすべきかを定義する。

### Behavior-preserving change

morphism は object 間の名前付き変換であり、実装手段ではなく保持すべき意味を表す。
`draft-review-plan` は prompt 実装ではなく、要求の制約と範囲を `Review Plan` に保つ変換として読むべきである。

### Partial functions, total functions, and contracts

多くの workflow step は、実際には任意入力に対して定義されていない。
そのため team は total function と partial function を区別し、interface contract で有効 domain を明示する必要がある。

## 合成を設計の中心操作として捉える

本節は、複数の妥当な step を一つの設計主張にまとめるために composition が必要であることを示す。

### Associativity and modular reasoning

`human-approval ◦ draft-review-plan` は、`Change Request` から `Approved Change` への合成 path を与える。
associativity により、途中 step を追加しても interface が整合する限り全体の意味を保ったまま再分割できる。

### Identity morphisms and boundary stability

identity morphism は object の意味を変えない pass-through を表す。
transport や serialization が意味を変えないなら identity 的に扱えるが、制約や責務を変えるならそうではない。

## この語彙を実務設計に接続する

本節は、object、morphism、composition を service interaction、data transformation、review checklist に接続する。

### Service interactions and data transformations

API request、schema translation、deployment manifest も、境界と contract が安定していれば object や morphism として扱える。
重要なのは tool 名ではなく、どの artifact relation を保つかである。

### Composition in review checklists

review では source object、target object、preserved invariant、hidden precondition、evidence artifact を確認する必要がある。
合成 path 全体を誰が承認するかも review point として明示する必要がある。

## よくあるモデリング上の誤り

本節は、合成的推論を弱める典型的な誤りを整理する。

### Overloading one object with multiple concerns

approval workflow 全体を一つの object とみなすと、request、plan、approval の責務差分が消える。
review question が変わる場所では object を分けるべきである。

### Mistaking implementation detail for structure

prompt phrasing や一時 file path のような揮発的 detail を stable structure と取り違えるのは危険である。
tool を置き換えても保たれる contract と transformation を object と morphism の中心に置くべきである。
