# Changelog

このプロジェクトの主要な変更点を記録します。
書式は [Keep a Changelog](https://keepachangelog.com/ja/1.1.0/) に準拠し、
バージョニングは [Semantic Versioning](https://semver.org/lang/ja/) に従います。

## [Unreleased]

## [0.4.0] - 2026-07-06

### Added

- **tombstone（Corail Tombstone）** を翻訳（1,112キー）。死亡時に墓を生成しアイテムを保護する定番Mod。
  アイテム名・説明、エンチャント・効果・特典、実績（149ペア）、ゲーム内メッセージ、コマンド、コンペンディウム（ガイド本）、設定を翻訳。`%s`/`%d`/`%%`・改行を保持し、キー一致とプレースホルダ整合を検証済み（未訳0）。
- `tools/scan_status.py`：各 Mod の日本語化状況（このパック／kubejs／Mod同梱／未翻訳）を走査して一覧表示。
- `CLAUDE.md`：ビルド・リリース手順・翻訳規約などの開発情報を集約。

### Changed

- README をユーザー向けに再構成。全 Mod を走査した「翻訳状況」（✅このパック／📦Mod同梱／🧩kubejs／❌未対応／⚪対象外）に統合。各 Mod を1行の表で個別表示。開発系の記述は `CLAUDE.md` へ移動。
- `emi`（NuclearCraft同梱のEMIタグ表示名）を対象外に分類（本パックは JEI を使い EMI 未導入で実質未使用）。

## [0.3.0] - 2026-07-06

### Added

- **immersivegeology（Immersive Geology）** を翻訳（2,120キー）。地質・鉱石加工を追加するIE系アドオン。
  鉱物名は鉱物学の日本語（軟マンガン鉱・黄銅鉱・閃ウラン鉱…）、岩石/金属はTFCと統一。
  アイテム/ブロックのテンプレート（`%s`）、機械名、実績、マニュアル、鉱脈タイプ、GUI、化学工程（ベッヒャー法・ホール・エルー法…）を翻訳。プレースホルダ整合を検証済み（未訳0）。

## [0.2.0] - 2026-07-06

### Added

- **dfc（DecoFirmaCraft）** を翻訳（3,062キー）。TFC の装飾ブロックを大量追加するMod。
  岩石・鉱石・金属・色の用語は TFC 本体の日本語に合わせ、命名規則（`低純度の花崗岩の自然銅` / `滑らかな花崗岩のハーフブロック` / `花崗岩のレンガの階段`）も TFC と統一。
  英語名が TFC の ja_jp に一致するものは直接流用（286件）、残り（2,768件）は語彙辞書で合成（未知語0）。

## [0.1.2] - 2026-07-06

### Added

- リソースパック選択画面の説明文に**バージョンを表示**。`build.py` がビルド時に git タグ（`git describe --tags`）からバージョンを自動注入し、CI ではタグ名（`--version`）を使う。ソースの `pack.mcmeta` は書き換えず zip 内の内容だけ差し替える。

## [0.1.1] - 2026-07-06

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

[Unreleased]: https://github.com/11gather11/Gravitas2-JP/compare/v0.4.0...HEAD
[0.4.0]: https://github.com/11gather11/Gravitas2-JP/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/11gather11/Gravitas2-JP/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/11gather11/Gravitas2-JP/compare/v0.1.2...v0.2.0
[0.1.2]: https://github.com/11gather11/Gravitas2-JP/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/11gather11/Gravitas2-JP/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/11gather11/Gravitas2-JP/releases/tag/v0.1.0
