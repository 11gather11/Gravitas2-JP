# Changelog

このプロジェクトの主要な変更点を記録します。
書式は [Keep a Changelog](https://keepachangelog.com/ja/1.1.0/) に準拠し、
バージョニングは [Semantic Versioning](https://semver.org/lang/ja/) に従います。

## [Unreleased]

### Removed

- Advanced Peripherals ガイド本の**表紙紹介文（landing_text）**はリソースパックでは翻訳できないため（Patchouli の `book.json` はデータパック `data/` 側にあり、`assets/` の上書きは無視される）、無効だった `assets/advancedperipherals/patchouli_books/manual/book.json` を削除。表紙の1文のみ英語のまま（本文ページ・UIは日本語）。

### Fixed

- `pack.mcmeta` の description に生の改行が含まれ不正なJSONだった問題を修正（リソースパック一覧で説明が「□」に化ける不具合）。
- 改行コードによる文字化けを防ぐため `.gitattributes` を追加し、テキストを LF に正規化。
- `build.py` の検証対象に `pack.mcmeta` を追加（CIで同種の不正JSONを検出できるように）。

## [0.1.0] - 2026-07-06

### Added

- 初版リリース。
- **gravitas**：FTB Quests のクエスト全32章を翻訳（1,775キー）。
- **Integrated Dynamics スイート**（本体 / Tunnels / Crafting / Terminals）：
  ガイド本・アイテム名・GUI・オペレーター・アスペクト・実績を翻訳（計2,523キー）。
- **mcw_tfc_aio**：Macaw's 家具（TFC統合版）を翻訳（2,033キー）。
- **advancedperipherals**：アイテム名・ツールチップ・Patchouli ガイド本を翻訳（88キー＋本26ファイル）。
- **patchouli**：本ビューアのUI（全Patchouli本共通）を翻訳（90キー）。
- `build.py`（ビルド＋JSON検証）、`README.md`、`LICENSE`（CC BY-NC-SA 4.0）、CI/自動リリース。

[Unreleased]: https://github.com/11gather11/Gravitas2-JP/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/11gather11/Gravitas2-JP/releases/tag/v0.1.0
