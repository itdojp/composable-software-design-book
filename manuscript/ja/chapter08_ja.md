---
chapter_id: chapter08
english_source: src/chapter-chapter08/index.md
review_owner: editorial-review
draft_status: drafting
---

# モノイダル圏とストリング図式

本章は、直列合成と並列合成を repository workflow の artifact と responsibility flow に結び付ける。
running example では `implementation/orchestration-diagram.md` と `implementation/synchronization-boundary.md` を使い、fan-out、fan-in、failure isolation を canonical artifact で説明する。

## 直列合成と並列合成

本節は、順序付き obligation と独立に進められる branch を区別する。

### Time, order, and concurrency in workflows

`Change Request`、`Review Plan`、`Decision Packet`、`Approved Change` は mandatory spine を作る。
policy evaluation と evidence collection は同じ `Review Plan` revision に対してだけ並列化できる。

### When independence can be exploited

branch が独立していると言えるのは、scope、route、policy meaning を hidden state で共有していないときだけである。
速い branch が `Approved Change` の代わりになる設計は independence ではなく authority leak である。

## システムとチームにおけるモノイダル構造

本節は、parallel composition を scheduler の都合ではなく shared context を保つ設計構造として読む。

### Parallelizable work and shared resources

policy branch と evidence branch は並列に動いても、同じ `Change Identity`、`Repository Scope`、`Plan Revision` を保つ必要がある。
repository metadata や reviewer attention は shared resource であり、ここが drift すると composition の意味が崩れる。

### Coordination costs and synchronization points

coordination cost は fan-in で表面化する。
`Decision Packet` は `Policy Classification`、`Evidence Link Set`、`Approval Route ID` が同期境界を満たしたときだけ作られる。

## 推論道具としてのストリング図式

本節は、wire を artifact と preserved context、box を transformation として読む。

### Reading flows of data, control, and responsibility

wire は data だけでなく control authority や review obligation も運ぶ。
`approve-or-return` だけが `Approved Change` を作れることを図式で固定すると、preparation と authorization を混同しにくくなる。

### Exposing hidden coupling in workflows

mutable prompt context や unlabeled retry cache は hidden coupling の典型である。
string diagram は missing wire を可視化するので、parallel だと思っていた branch が実際には共有状態に依存していると分かる。

## 協調パターンと障害分離

本節は、pipeline、fan-out、fan-in、fallback path を reviewable な boundary として扱う。

### Pipelines, fan-out, and fan-in

workflow の spine は approval meaning を保ち、parallel branch は preparatory work に限定される。
新しい branch を足すなら既存の同期境界に join するか、新しい boundary を明示する必要がある。

### Recovery boundaries and fallback paths

policy failure は implicit pass ではなく manual review か rework に落とすべきである。
evidence failure は policy result を書き換えず、sync を止めて stale packet の生成を防ぐべきである。

## 合成ワークフローレビューの観点

本節は、並列 workflow を review するときの structural question をまとめる。

### What to inspect in orchestration diagrams

どの artifact が fan-out を許可するか。
どの morphism だけが `Approved Change` を作れるか。
同期境界を構成する field は何か。

### How to detect brittle coordination designs

shared mutable context、unlabeled summary step、partial success からの execution dispatch は brittle signal である。
Chapter 09 では、その branch が持つ effect を explicit boundary として固定し、prompt、tool call、approval write、dispatch の risk を整理する。
