---
chapter_id: chapter03
english_source: src/chapter-chapter03/index.md
review_owner: editorial-review
draft_status: drafting
---

# 図式と可換性

本章は、diagram を装飾ではなく compact design argument として扱い、複数 path が同じ意味を保つかを repository artifact に結び付けて検査する。
本章では minimal diagram、common running example の richer diagram、traceability matrix を一体で使う。

## なぜ図式が設計実務で重要か

本節は、diagram が prose よりも path 比較と invariant の保持を明確に表せる理由を説明する。

### Diagrams as compact design arguments

diagram は workflow の順序説明ではなく、複数 path の関係を一度に見せる設計主張である。
`draft-review-plan` と `human-approval` の合成が `policy-gated-approval` を正当化するかという問いは、diagram にすると review question になる。

### When prose is not enough

prose だけでは、どの path 比較が核心で、どの invariant が失われたかが見えにくい。
richer repository diagram は `Policy Check` を独立させることで、approval claim の条件をより明確にする。

## 可換図式を整合性検査として使う

本節は、commutativity を artifact 間の preserved meaning を検査する条件として扱う。

### Equivalent paths and preserved meaning

diagram が可換であるとは、複数の path が同じ見た目を持つことではなく、同じ設計意味を保つことである。
traceability matrix は、その主張を problem statement、design、verification、implementation に結び付ける。

### Broken squares as design defects

policy が request scope を変えたのに `Review Plan` が更新されない場合、diagram の主張は壊れる。
この broken square は単なる documentation error ではなく、semantic drift を示す設計欠陥である。

## 複数ビュー間の整合性

本節は、requirements、design、workflow、repository-level artifact を diagram でつなぐ。

### Requirements, architecture, and runtime views

problem statement、acceptance criteria、design diagram、implementation workflow は、一つの coherent story を保つ必要がある。
diagram は、その story が view をまたいでも崩れていないかを確認する中間表現になる。

### Mapping code-level artifacts back to design

diagram の node と arrow は、対応する file や verification artifact へ辿れなければ保守できない。
artifact map、review checks、traceability matrix を併用することで、その写像を小さく保てる。

## 図式レビューの技法

本節は、diagram review を repeatable practice として扱う。

### Minimal diagrams for design reviews

最初は one invariant、one review question に絞った最小 diagram から始めるべきである。
node が stable artifact か、arrow が meaningful transformation か、adjacent prose に invariant が書かれているかを確認する。

### Counterexamples and edge cases

diagram は、曖昧な policy outcome、stale review plan、approval bypass のような counterexample で試す必要がある。
反例で壊れるなら、diagram か artifact set のどちらかが不足している。

## 図式を運用ガバナンスへつなぐ

本節は、diagram を approval、audit、change management に結び付ける。

### Using diagrams in approvals and audits

approval では、diagram だけでなく review checks と traceability matrix を併せて主張を審査する必要がある。
audit でも、何が実行されたかだけでなく、どの commutative claim を repository が主張していたかを確認するべきである。

### Keeping diagrams synchronized with change

workflow、specification、verification artifact が変わるなら、diagram も同じ pull request で更新する必要がある。
diagram を first-class design artifact として version 管理しないと、trust している path equivalence claim が実態とずれる。
