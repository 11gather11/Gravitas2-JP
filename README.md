# Gravitas2-JP

[All The Mods - Gravitas²](https://github.com/AllTheMods/Gravitas2)（ATMTeam製の Minecraft 1.20.1 Forge モッドパック）の**非公式日本語翻訳リソースパック**。

クエストや各Modのアイテム名・ガイドブックなどを日本語化します。ゲームの言語設定が日本語（`ja_jp`）のとき自動で適用されます。

## 導入方法

1. [Releases](https://github.com/11gather11/Gravitas2-JP/releases) から最新の `Gravitas2-JP-vX.Y.Z.zip` をダウンロード
2. Minecraft インスタンスの `resourcepacks/` フォルダに入れる
3. ゲーム内 `設定 → リソースパック` で有効化
4. ゲームの言語を「日本語」にする
   - アイテム名などは **F3+T**（リソースリロード）で反映
   - Patchouli の本は **ゲーム再起動**で反映

## 翻訳状況

このモッドパックの Mod を走査した結果です（`en_us` を持つ名前空間 218 個）。日本語化の状態は次の通り。数値は英語キー数の目安です。

- ✅ **このパックで翻訳**：9／📦 **Mod同梱で対応済み**：70／🧩 **パック側 kubejs で対応済み**：3／❌ **未対応（翻訳候補）**：98（ほかにライブラリ等 38 は対象外）

### ✅ このパックで翻訳

| 名前空間 | 内容 | キー数 |
|------|------|-------:|
| `dfc` | DecoFirmaCraft（TFC装飾ブロック大量追加） | 3,062 |
| `immersivegeology` | Immersive Geology（地質・鉱石加工） | 2,120 |
| `mcw_tfc_aio` | Macaw's 家具（TFC統合版） | 2,033 |
| `integrateddynamics` | Integrated Dynamics 本体（本・アイテム・オペレーター・アスペクト・実績） | 1,754 |
| `integratedtunnels` | Integrated Tunnels（転送） | 487 |
| `integratedterminals` | Integrated Terminals（ストレージ端末） | 176 |
| `integratedcrafting` | Integrated Crafting（自動クラフト） | 110 |
| `patchouli` | Patchouli 本ビューアUI（全Patchouli本共通） | 90 |
| `advancedperipherals` | Advanced Peripherals（アイテム・Patchouli本） | 88 |
| **合計** | 10名前空間 ＋ Patchouli本26ファイル | **9,920** |

### 📦 元から日本語対応（Mod同梱・kubejs）

多くの Mod は自前で `ja_jp` を同梱しており、そのまま日本語表示されます。パック側 kubejs でも一部提供されています。

<details><summary>🧩 パック側 kubejs（3）</summary>

`tfc`(8,481) / `gtceu`(5,921) / `create`(3,646)

</details>

<details><summary>📦 Mod 同梱（70）</summary>

`nuclearcraft`(2,851) / `immersiveengineering`(1,405) / `iceandfire`(1,322) / `railways`(1,293) / `railcraft`(1,025) / `apotheosis`(1,014) / `firmalife`(1,013) / `ae2`(999) / `everycomp`(962) / `createbigcannons`(744) / `powergrid`(663) / `sgjourney`(661) / `xaerominimap`(611) / `enderio`(553) / `inventoryprofilesnext`(519) / `recruits`(519) / `createdeco`(418) / `alltheores`(333) / `farmersdelight`(323) / `create_connected`(307) / `createdieselgenerators`(286) / `allthemodium`(282) / `jade`(280) / `sophisticatedcore`(276) / `createaddition`(255) / `computercraft`(233) / `sophisticatedbackpacks`(228) / `voicechat`(228) / `waystones`(199) / `enchdesc`(183) / `gcyr`(183) / `expatternprovider`(172) / `advanced_ae`(167) / `repurposed_structures`(161) / `modernfix`(137) / `storagedrawers`(133) / `jei`(132) / `nochatreports`(129) / `immersive_aircraft`(123) / `petrolpark`(81) / `xaerobetterpvp`(77) / `comforts`(77) / `iris`(72) / `copycats`(67) / `chalk`(64) / `simpleradio`(55) / `trackwork`(55) / `valkyrienskies`(55) / `projectred_core`(54) / `lootr`(51) / `cloth-config2`(49) / `curios`(48) / `immersive_machinery`(40) / `tfcagedalcohol`(38) / `bellsandwhistles`(38) / `sodiumdynamiclights`(34) / `bookshelf`(32) / `enderchests`(28) / `allthetweaks`(26) / `minecraft`(21) / `ae2ct`(19) / `waterflasks`(17) / `tfcgroomer`(16) / `astikorcarts`(15) / `controlling`(12) / `moonlight`(9) / `aeinfinitybooster`(3) / `pccard`(1) / `searchables`(1) / `endertanks`(0)

</details>

### ❌ 未対応（翻訳候補）

プレイに関わる主な未翻訳 Mod（キー数の多い順）。

<details><summary>翻訳候補（98）</summary>

`emi`(2,129) / `tombstone`(1,112) / `scguns`(971) / `tfcastikorcarts`(928) / `ftbquests`(572) / `vintage`(481) / `tfc_ie_addon`(461) / `vs_clockwork`(458) / `thoriumreactors`(369) / `framedblocks`(346) / `ftbchunks`(282) / `xaeroworldmap`(272) / `beneath`(268) / `sfm`(255) / `firmaciv`(239) / `potionsmaster`(237) / `integrateddynamicscompat`(214) / `tfcgenviewer`(177) / `projectred_fabrication`(174) / `bits_n_bobs`(174) / `projectred_illumination`(162) / `hostilenetworks`(160) / `create_new_age`(158) / `attributeslib`(130) / `gregitas_core`(129) / `fluxnetworks`(123) / `alekiships`(120) / `workers`(114) / `buildinggadgets2`(111) / `megacells`(108) / `simpleplanes`(108) / `ftblibrary`(99) / `smallships`(95) / `laserio`(90) / `ftbteams`(89) / `sfcr`(88) / `create_tweaked_controllers`(85) / `mininggadgets`(85) / `projectred_transmission`(71) / `precisionprospecting`(70) / `petrolsparts`(69) / `tfc_textile`(69) / `freecam`(65) / `tfships`(63) / `tfccaffeinated`(61) / `extremesoundmuffler`(56) / `survivorsdelight`(56) / `deathpunishment`(53) / `tfclunchbox`(49) / `betterp2p`(47) / `ezvcsurvival`(44) / `advancedtfctech`(43) / `zume`(42) / `tfceureka`(41) / `vs_eureka`(40) / `fallingtrees`(40) / `tfcthermaldeposits`(39) / `tfcambiental`(38) / `tfcchannelcasting`(38) / `jadeaddons`(36) / `projectred_integration`(35) / `ae2wtlib`(35) / `siegemachines`(34) / `createmoredrillheads`(34) / `workerstfc`(33) / `blazemap`(32) / `cccbridge`(32) / `trashcans`(32) / `drivebywire`(29) / `create_factory_logistics`(27) / `woodencog`(27) / `ae2netanalyser`(24) / `wirelessredstone`(24) / `merequester`(23) / `tfcseedsoftime`(23) / `wirelesschargers`(23) / `createhorsepower`(21) / `cartography`(15) / `ae2things`(12) / `integratedterminalscompat`(12) / `jade_vs`(10) / `coldsgrappler`(8) / `survivorsabilities`(7) / `castirongrill`(6) / `hangglider`(5) / `create_hp_ts`(5) / `createimmersiveunnecessaryshaft`(5) / `eyesoficeandfire`(5) / `tfc_support_indicator`(5) / `tfcea`(5) / `findme`(4) / `tfccanes`(4) / `easynametags`(3) / `headlight`(3) / `showcaseitem`(2) / `auroras`(1) / `justenoughprofessions`(1) / `waves`(1)

</details>

<details><summary>対象外：ライブラリ・軽量化・API・設定など（38）</summary>

`distanthorizons`(466) / `chloride`(154) / `sodium`(65) / `configured`(62) / `titanium`(48) / `creativecore`(44) / `cyclopscore`(42) / `itemfilters`(41) / `configuration`(40) / `guideme`(36) / `balm`(35) / `observable`(33) / `geckolib`(31) / `libipn`(28) / `citadel`(24) / `fastload`(21) / `colorwheel`(21) / `codechickenlib`(18) / `cb_microblock`(17) / `smoothboot`(14) / `commoncapabilities`(10) / `measurements`(8) / `fusion`(8) / `treetap`(8) / `embeddium`(7) / `placebo`(6) / `almostunified`(6) / `packmenu`(5) / `crashutilities`(4) / `entityculling`(3) / `bcc`(2) / `betterfpsdist`(2) / `jeimultiblocks`(2) / `framework`(1) / `pandalib`(1) / `drivebywire_recipes`(0) / `ftbxmodcompat`(0) / `shetiphiancore`(0)

</details>

> この一覧は `python tools/scan_status.py "<インスタンスのパス>"` で再生成できます。

## ライセンス

- 本リポジトリの**翻訳物**は [Creative Commons 表示 - 非営利 - 継承 4.0 国際 (CC BY-NC-SA 4.0)](LICENSE) の下で提供されます。
- ただし、**原文**（クエスト・各Modのテキスト）の著作権は各権利者（ATMTeam および各Mod作者）に帰属します。本リポジトリはその翻訳（二次的著作物）です。
- 再配布・改変の際は、CC BY-NC-SA 4.0 の条件に加え、元パック [AllTheMods/Gravitas2](https://github.com/AllTheMods/Gravitas2) および各Modのライセンスにも従ってください。
- 非公式の有志翻訳であり、ATMTeam 公式とは関係ありません。

## 貢献・開発

翻訳は AI（Claude）による作成です。誤訳・表記ゆれの指摘・修正を歓迎します。ビルド方法・リリース手順・翻訳規約などの開発情報は [CLAUDE.md](CLAUDE.md) を参照してください。

