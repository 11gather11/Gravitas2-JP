# Gravitas2-JP

[All The Mods - Gravitas²](https://github.com/AllTheMods/Gravitas2) （ATMTeam製の Minecraft 1.20.1 Forge モッドパック）の**非公式日本語翻訳リソースパック**。

クエストや各Modのアイテム名・ガイドブックなどを日本語化します。ゲームの言語設定が日本語（`ja_jp`）のとき自動で適用されます。

## 翻訳状況

| 対象 | 内容 | キー数 |
|------|------|-------:|
| `gravitas` | FTB Quests のクエスト（全32章） | 1,775 |
| `integrateddynamics` | 本体：本・アイテム名・オペレーター・アスペクト・実績 | 1,753 |
| `integratedtunnels` | アイテム/液体/エネルギー転送 | 486 |
| `integratedcrafting` | 自動クラフト | 109 |
| `integratedterminals` | ストレージ端末 | 175 |
| `mcw_tfc_aio` | Macaw's 家具（TFC統合版） | 2,033 |
| `dfc` | DecoFirmaCraft（TFC装飾ブロック大量追加） | 3,062 |
| `advancedperipherals` | アイテム名・ツールチップ・ガイドブック（Patchouli） | 88 + 本26ファイル |
| `patchouli` | 本ビューアのUI（Categories / Chapters など、全Patchouli本共通） | 90 |

※ Create / GregTech CEu / TerraFirmaCraft 本体は、パック側（kubejs）で日本語が提供されています。

## ディレクトリ構成

```
Gravitas2-JP/
├─ pack/                 リソースパックのソース
│  ├─ pack.mcmeta
│  └─ assets/<mod>/lang/ja_jp.json …
├─ build.py              pack/ を zip 化してビルド
├─ README.md
└─ .gitignore            dist/ と *.zip は追跡しない
```

## ビルド方法

```bash
python build.py            # dist/Gravitas2-JP.zip を生成し、インスタンスの resourcepacks へも配置
python build.py --no-copy  # dist/ に出力するだけ
```

ビルド時に全 `ja_jp.json` の JSON 妥当性を検証します。インスタンスの配置先は `build.py` 冒頭の `INSTANCE_RESOURCEPACKS` を環境に合わせて変更してください。

## 導入方法

1. `build.py` でビルド（またはリリースの zip を入手）
2. できた `Gravitas2-JP.zip` を Minecraft インスタンスの `resourcepacks/` に入れる
3. ゲーム内 `設定 → リソースパック` で有効化
4. ゲームの言語を「日本語」にする
   - アイテム名などは **F3+T**（リソースリロード）で反映
   - Patchouli の本は **ゲーム再起動**で反映

## 翻訳方針

- キーは変更せず値のみ翻訳。書式コード（`&`/`§` カラー、`$(...)` Patchouli書式）、`%s`/`%d`、改行、URL は保持。
- Mod名などの固有名詞は原則そのまま。
- 専門用語（GregTech の電圧ティア、化学工程など）は分かりやすさを優先して意訳した箇所あり。
- 翻訳は AI（Claude）による作成。誤訳・表記ゆれの指摘歓迎。

## バージョニングとリリース

- [Semantic Versioning](https://semver.org/lang/ja/)（`vMAJOR.MINOR.PATCH`）を git タグで管理します。
- 変更点は [CHANGELOG.md](CHANGELOG.md)（[Keep a Changelog](https://keepachangelog.com/ja/1.1.0/) 形式）に記録します。
- **リリース手順**：`CHANGELOG.md` を更新してコミット後、タグを push すると GitHub Actions が zip をビルドして Release を自動作成します。

  ```bash
  git tag v0.1.0
  git push origin v0.1.0
  ```

- **CI**：`main` への push / PR ごとに、全 `ja_jp.json` と Patchouli 本 JSON の妥当性を検証します（`.github/workflows/`）。

## ライセンス

- 本リポジトリの**翻訳物**は [Creative Commons 表示 - 非営利 - 継承 4.0 国際 (CC BY-NC-SA 4.0)](LICENSE) の下で提供されます。
- ただし、**原文**（クエスト・各Modのテキスト）の著作権は各権利者（ATMTeam および各Mod作者）に帰属します。本リポジトリはその翻訳（二次的著作物）です。
- 再配布・改変の際は、CC BY-NC-SA 4.0 の条件に加え、元パック [AllTheMods/Gravitas2](https://github.com/AllTheMods/Gravitas2) および各Modのライセンスにも従ってください。
- 非公式の有志翻訳であり、ATMTeam 公式とは関係ありません。
