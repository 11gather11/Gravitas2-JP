# CLAUDE.md — 開発ガイド

このリポジトリは **All The Mods - Gravitas²**（[AllTheMods/Gravitas2](https://github.com/AllTheMods/Gravitas2)、MC 1.20.1 Forge）の非公式日本語翻訳リソースパックです。このファイルはメンテナ・AIアシスタント向けの開発情報をまとめます（ユーザー向けの導入・翻訳状況は [README.md](README.md)）。

## リポジトリ構成

```
Gravitas2-JP/
├─ pack/                          リソースパックのソース（これを zip 化する）
│  ├─ pack.mcmeta                 pack_format 15（説明文はビルド時にバージョン注入）
│  ├─ pack.png                    アイコン（64x64）
│  └─ assets/<ns>/lang/ja_jp.json 各Modの翻訳。Patchouli本は assets/<ns>/patchouli_books/...
├─ build.py                       pack/ を zip 化＋全JSON検証＋インスタンスへ配置
├─ tools/scan_status.py           各Modの日本語化状況を走査
├─ CHANGELOG.md                   Keep a Changelog 形式
├─ CLAUDE.md / README.md / LICENSE
├─ .gitattributes                 テキスト=LF（CRLF の \r 化け防止）
└─ .github/workflows/             ci.yml（検証）/ release.yml（タグで自動リリース）
```

## ビルド

```bash
python build.py            # dist/Gravitas2-JP.zip を生成し、インスタンスの resourcepacks へも配置
python build.py --no-copy  # dist/ に出力するだけ（CI で使用）
```

- ビルド時に `pack/` 内の全 `*.json` と `pack.mcmeta` の妥当性を検証（不正なら中断）。
- pack.mcmeta の `description` 1行目に `§8<version>` を注入（ソースは書き換えず zip 内のみ差し替え）。バージョンは `--version` 引数 → `git describe --tags` → `dev` の順で決定。
- 配置先はインスタンスの `resourcepacks/` フォルダ。環境に合わせて `build.py` 冒頭の `INSTANCE_RESOURCEPACKS` を変更する（例: `F:\Games\Minecraft\CurseForge\Instances\All The Mods - Gravitas\resourcepacks`）。
- **ゲーム起動中は有効なパックの zip がロックされ、インスタンスへのコピーが失敗する**。その場合はゲームを閉じてから再ビルドする。

## バージョニングとリリース

- [Semantic Versioning](https://semver.org/lang/ja/)（`vMAJOR.MINOR.PATCH`）を git タグで管理。新規Mod追加は MINOR、修正は PATCH。
- 手順：
  1. `pack/assets/<ns>/lang/ja_jp.json` を追加・編集
  2. `CHANGELOG.md` の `[Unreleased]` を更新（リリース時は該当バージョンに確定＋リンク追記）
  3. コミット & push（CI が全JSONを検証）
  4. リリース：`git tag vX.Y.Z && git push origin vX.Y.Z` → Actions が zip をビルドして GitHub Release を自動作成
- コミットの `user.email` は GitHub の noreply（`160300516+11gather11@users.noreply.github.com`）に設定済み。gh CLI は認証済み。

## 翻訳の方針・規約

- **キーは変更せず値のみ翻訳**。以下は必ず保持：
  - カラーコード `&x` / `§x`、書式プレースホルダ `%s` `%d` `%1$s`、改行（JSON上は `\n`）、URL
  - Patchouli 書式 `$(p)` `$(l:...)` `$(li)` `$()` など。リンク先ID（`$(l:peripherals/chat_box)`）は英語のまま、可視テキストのみ訳す
- **固有名詞（Mod名など）は原則そのまま**。
- **用語は TerraFirmaCraft 本体の日本語に合わせる**（岩石・鉱石・金属・色）。TFC の ja_jp は Mod jar とパック側 `kubejs/assets/tfc/lang/ja_jp.json` にある。
- **鉱物名は鉱物学の正式名称**（例：Pyrolusite→軟マンガン鉱、Chalcopyrite→黄銅鉱）。
- 専門用語（電圧ティア・化学工程など）は分かりやすさ優先で意訳可。
- 翻訳後は **キー一致**（en_us と ja_jp のキー集合が一致）と **プレースホルダ整合**（`%s` 等の個数一致）を検証する。

### 合成生成（大量の規則的な名前）

装飾・鉱石ブロックなど名前が規則的な Mod は、語彙辞書で合成生成すると効率的かつ表記揺れが無い。

- **mcw_tfc_aio**：「木材/色/素材 × 家具」を辞書で合成（全2014ブロック）。
- **dfc（DecoFirmaCraft）**：TFC と同じ命名規則を再現。名詞は「の」で連結（`花崗岩のレンガの階段`）、形容詞は直付け（`滑らかな花崗岩`）、グレードは `低純度の`。英語名が TFC の ja_jp に一致すれば直接流用。
- **immersivegeology**：block の多くは `.prospected`（値＝鉱石名）でユニーク値に集約。value→ja 辞書を全キーに適用。`%s` テンプレートはプレースホルダを保持したまま訳す。
- 生成器は必ず **未知トークン0** を確認してから採用する。

## 翻訳状況の確認

```bash
python tools/scan_status.py "<インスタンスのパス>"
```

各Modを走査し `done_RP`（このパック）/ `done_kubejs` / `done_jar`（Mod同梱）/ `TODO`（未翻訳）に分類。README の「翻訳状況」もこの走査結果に基づく。

## 既知の制約

- **Patchouli 本の表紙紹介文（`book.json` の `landing_text`）はリソースパックで翻訳できない**。`book.json` はデータパック（`data/<ns>/patchouli_books/...`）側にあり、`assets/` の上書きは無視される。データパックでの上書きは可能だが本パックでは非対応（本文ページ・UIは翻訳済み）。
