# 日本語下書きテンプレート

## 使い方

- `manuscript/ja/outline_ja.md` と 1:1 で対応させる。
- 英語正本の見出し順序を崩さない。
- 1 文 1 行で書く。
- 1 文 1 命題を基本とする。
- 主語を省略しない。
- コード識別子、ファイル名、API 名、環境変数名は英語のまま残す。

## 最小メタ情報

```yaml
chapter_id: chapter01
english_source: src/chapter-chapter01/index.md
review_owner: editorial-review
draft_status: drafting
```

## 執筆ブロック

### 章情報

- 日本語章タイトル:
- 対応英語タイトル:
- 章の目的:

### 節ブロック

- section_en:
- section_ja:
- この節で説明すること:

本文:

文 1。
文 2。

### 用語初出ブロック

- canonical_term_en:
- preferred_term_ja:
- 補足:

## 図式・数式・箇条書きの書き方

- 図式ラベルは英語正本と同じ記号を使う。
- 数式の記号名は翻訳しない。
- 箇条書きは 1 項目 1 意味にする。
- 図表キャプションの参照番号は英語正本と一致させる。

## 禁止事項

- 英語正本にない見出しを独断で追加しない。
- 英語正本の heading ID を変更しない。
- 用語ベースにない新語を無断で定着語として使わない。
- 省略主語のまま、誰が行為主体か不明な文を書かない。
