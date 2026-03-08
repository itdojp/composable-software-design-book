# 日本語下書きアウトライン

## 前提

- 英語正本の構造は `project-management/toc_en.md` と `book-config.json` を参照する。
- 日本語下書きは入力専用であり、公開物として扱わない。
- 章 ID と節順序は英語正本と 1:1 で対応させる。

## Chapter ID 対応表

| chapter_id | 日本語タイトル | English title |
| --- | --- | --- |
| introduction | 序論: なぜ合成的設計が重要か | Introduction: Why Compositional Design Matters |
| chapter01 | 人間と AI の責任境界 | Human and AI Responsibility Boundaries |
| chapter02 | 対象・射・合成 | Objects, Morphisms, and Composition |
| chapter03 | 図式と可換性 | Diagrams and Commutativity |
| chapter04 | 関手とモデル変換 | Functors and Model Translation |
| chapter05 | 自然変換とビュー変換 | Natural Transformations and View Changes |
| chapter06 | 普遍性、積、余積 | Universality with Products and Coproducts |
| chapter07 | 統合と移行のための pullback / pushout | Pullbacks and Pushouts for Integration and Migration |
| chapter08 | モノイダル圏とストリング図式 | Monoidal Categories and String Diagrams |
| chapter09 | モナド、Kleisli 合成、作用境界 | Monads, Kleisli Composition, and Effect Boundaries |
| chapter10 | ケーススタディ: 仕様から AI 支援実装へ | Case Study: From Specification to AI-Assisted Implementation |

## introduction

| section_en | section_ja |
| --- | --- |
| Why AI-assisted engineering needs stronger structure | AI 支援エンジニアリングになぜ強い構造が必要か |
| Who this book is for | 本書の対象読者 |
| What the reader will gain | 読者が得るもの |
| How the book is organized | 本書の構成 |
| Conventions used throughout the book | 本書で共有する規約 |

## chapter01

| section_en | section_ja |
| --- | --- |
| Why responsibility boundaries matter | なぜ責任境界が重要か |
| Design artifacts as accountability surfaces | 設計成果物を説明責任の面として扱う |
| Allocating authority between humans and agents | 人間とエージェントの権限配分 |
| Operational control loops | 運用上の制御ループ |
| How this boundary model shapes the rest of the book | この境界モデルが後続章に与える意味 |

## chapter02

| section_en | section_ja |
| --- | --- |
| Modeling systems as objects | システムを対象として捉える |
| Morphisms as interfaces and transformations | インターフェースと変換を射として捉える |
| Composition as the core design move | 合成を設計の中心操作として捉える |
| Translating the vocabulary into engineering practice | この語彙を実務設計に接続する |
| Common modeling mistakes | よくあるモデリング上の誤り |

## chapter03

| section_en | section_ja |
| --- | --- |
| Why diagrams matter in engineering | なぜ図式が設計実務で重要か |
| Commutative diagrams as consistency tests | 可換図式を整合性検査として使う |
| Cross-view consistency | 複数ビュー間の整合性 |
| Diagram review techniques | 図式レビューの技法 |
| From diagrams to operational governance | 図式を運用ガバナンスへつなぐ |

## chapter04

| section_en | section_ja |
| --- | --- |
| Multiple abstraction levels in one system | 一つのシステムにおける複数の抽象レベル |
| Functors as structure-preserving translations | 関手を構造保存変換として捉える |
| Practical model translations | 実務でのモデル変換 |
| Lossy mappings and risk boundaries | 情報損失を伴う写像とリスク境界 |
| Heuristics for maintainable translations | 保守可能な変換の設計指針 |

## chapter05

| section_en | section_ja |
| --- | --- |
| Why alternative views must cohere | 複数ビューが整合しなければならない理由 |
| Natural transformations as controlled change of view | 自然変換を制御されたビュー変換として捉える |
| Refactoring without semantic drift | 意味をずらさないリファクタリング |
| Interface adaptation and compatibility layers | インターフェース適応と互換レイヤー |
| Review heuristics for view changes | ビュー変換レビューの観点 |

## chapter06

| section_en | section_ja |
| --- | --- |
| Universal properties as design criteria | 普遍性を設計基準として使う |
| Products for combined requirements | 複合要件に対する積 |
| Coproducts for alternatives and variation | 代替案と変種に対する余積 |
| Composition patterns built from universality | 普遍性から組み立てる設計パターン |
| Selecting the simplest correct construction | 最も単純で正しい構成を選ぶ |

## chapter07

| section_en | section_ja |
| --- | --- |
| Shared boundaries in integration work | 統合作業における共有境界 |
| Pullbacks for constrained joins | 制約付き結合に対する pullback |
| Pushouts for merger and migration | 統合・移行に対する pushout |
| Conflict resolution and traceability | 競合解消と追跡可能性 |
| Integration and migration heuristics | 統合・移行の判断指針 |

## chapter08

| section_en | section_ja |
| --- | --- |
| Sequential and parallel composition | 直列合成と並列合成 |
| Monoidal structure in systems and teams | システムとチームにおけるモノイダル構造 |
| String diagrams as reasoning tools | 推論道具としてのストリング図式 |
| Coordination patterns and failure isolation | 協調パターンと障害分離 |
| Review heuristics for composed workflows | 合成ワークフローレビューの観点 |

## chapter09

| section_en | section_ja |
| --- | --- |
| Why effects need explicit boundaries | なぜ作用には明示的な境界が必要か |
| Monads as operational envelopes | モナドを運用上の包みとして捉える |
| Kleisli composition for agent orchestration | エージェントオーケストレーションにおける Kleisli 合成 |
| Managing error, state, I/O, and external tools | エラー、状態、I/O、外部ツールの管理 |
| Effect containment in production systems | 本番システムにおける作用の封じ込め |

## chapter10

| section_en | section_ja |
| --- | --- |
| Framing the case study | ケーススタディの問題設定 |
| Building the artifact set | 成果物セットを組み立てる |
| Verification and review design | 検証計画とレビュー設計 |
| AI-assisted implementation | AI 支援実装 |
| Retrospective and extension points | 振り返りと拡張ポイント |

## Appendices

| appendix_id | 日本語タイトル | English title |
| --- | --- | --- |
| appendix-a | 記法と図式規約 | Notation and Diagram Conventions |
| appendix-b | 圏論とソフトウェア設計の用語集 | Glossary of Category-Theoretic and Engineering Terms |
| appendix-c | 参考文献と追加学習 | References and Further Study |
