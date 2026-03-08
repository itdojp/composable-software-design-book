---
chapter_id: chapter10
english_source: src/chapter-chapter10/index.md
review_owner: editorial-review
draft_status: drafting
---

# ケーススタディ: 仕様から AI 支援実装へ

本章は、running example を specification、design、verification、implementation の一続きの artifact path として読み直す。
目的は、これまでの formal term が repository delivery workflow にどう効くかを end-to-end で示すことである。

## ケーススタディの問題設定

本節は、problem statement、system boundary、success condition を確認する。

### Problem statement and system boundary

例は AI が一部を準備する repository change request を、監査可能で reviewable かつ reversible な形で処理する。
workflow は pre-execution approval で終わらず、execution か return-for-rework までを system boundary に含める。

### Success criteria and non-goals

success は artifact completion、explicit synchronization boundary、execution trace、acceptance evidence で定義される。
autonomous approval や opaque tool chaining は non-goal であり、scope を意図的に狭く保つ。

## 成果物セットを組み立てる

本節は、specification、design artifact、diagram、traceability をどう重ねるかをまとめる。

### Specification, architecture, and interface contracts

`spec/problem-statement.md` と `spec/acceptance-criteria.md` が problem と success を固定する。
`design/artifact-map.md`、`design/commutative-diagram.md`、`design/variation-paths.md`、`design/shared-boundary.md`、`design/replacement-plan.md` が translation、variation、integration の contract を作る。

### Diagram set and traceability matrix

runtime view、reviewer view、orchestration diagram、effect boundary は同じ approval meaning を別の operational angle から見せる。
traceability matrix は各 claim が spec、design、verification、implementation のどこにあるかを短い表で接続する。

## 検証計画とレビュー設計

本節は、review checklist、negative artifact、acceptance evidence を一つの verification design としてまとめる。

### Test strategy and acceptance evidence

`verification/review-checks.md` は短い checklist を提供し、`verification/coherence-failure.md` は failure case を固定する。
`verification/acceptance-evidence.md` は accepted outcome を支える最小 evidence bundle を定義する。

### Human checkpoints in an AI-assisted loop

AI は plan drafting や evidence preparation を支援できるが、approval authority は持たない。
normal approval、manual handling、return-for-rework はすべて human checkpoint であり、同じ artifact identity を保つ必要がある。

## AI 支援実装

本節は、bounded delegation、parallel branch、failure handling を implementation artifact に接続する。

### Delegating bounded tasks to agents

agent に渡すのは「変更を処理せよ」ではなく、bounded `Review Plan` を作る、evidence を集める、という限定された transformation である。
これにより orchestration diagram と sync boundary の review question を維持できる。

### Reviewing outputs, failures, and rework

policy timeout、missing evidence、new plan revision は all-or-nothing 失敗ではなく governed rework outcome として扱う。
execution trace と effect boundary があることで、何を retry し、何を discard し、何を preserved evidence として残すかを説明できる。

## 振り返りと拡張ポイント

本節は、method が validated したことと、今後 tooling を強くしたい部分を切り分ける。

### What the case study validates

formal vocabulary は artifact quality、review discipline、operational evidence を改善するときに実務価値を持つ。
小さな example でも specification から implementation まで同じ approval meaning を保てることが確認できる。

### Where the method needs stronger tooling

synchronization boundary validator、claim ID の図式反映、execution trace の自動集約はまだ lightweight artifact 依存である。
ただし canonical interface は整ったので、次段階ではこの path を自動化しても意味の境界を壊しにくい。
