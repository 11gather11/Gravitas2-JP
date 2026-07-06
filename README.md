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

モッドパック内の Mod を走査した結果です（`en_us` を持つ名前空間 218 個）。数値は英語キー数の目安。

- ✅ **このパックで翻訳**：23／📦 **Mod同梱で対応済み**：69／🧩 **パック側 kubejs で対応済み**：3／❌ **未対応（翻訳候補）**：84（ほかにライブラリ・未使用など 39 は対象外）

### ✅ このパックで翻訳

| 名前空間 | 内容 | キー数 |
|------|------|-------:|
| `dfc` | DecoFirmaCraft（TFC装飾ブロック大量追加） | 3,062 |
| `nuclearcraft` | NuclearCraft（原子力Mod。Mod同梱ja_jpの欠落分649=加速器・粒子物理・標的チェンバー・クーゲルブリッツ等を補完） | 2,851 |
| `immersivegeology` | Immersive Geology（地質・鉱石加工） | 2,120 |
| `mcw_tfc_aio` | Macaw's 家具（TFC統合版） | 2,033 |
| `integrateddynamics` | Integrated Dynamics 本体（本・アイテム・オペレーター・アスペクト・実績） | 1,754 |
| `tombstone` | Corail Tombstone（墓・死亡管理。アイテム・実績・メッセージ・コンペンディウム） | 1,112 |
| `scguns` | Scorched Guns（銃Mod。銃/弾薬/防具・実績・エンチャント・タレット・GUI） | 971 |
| `tfcastikorcarts` | TFC Astikor Carts（木材×荷車。補給/動物カート・鋤・車輪） | 928 |
| `ftbquests` | FTB Quests（クエストシステムのUI・エディタ・タスク・報酬） | 572 |
| `integratedtunnels` | Integrated Tunnels（転送） | 487 |
| `vintage` | Create: Vintage（Createアドオン。金属加工品・機械・Ponder・JEI） | 481 |
| `tfc_ie_addon` | TFC-IE Crossover（TFC×IE。鉱石・金属加工・鉱物） | 461 |
| `framedblocks` | FramedBlocks（カモフラージュ装飾。幾何形状ブロック・設定・ツールチップ） | 346 |
| `ftbchunks` | FTB Chunks（チャンク取得・地図・ミニマップ・ウェイポイント） | 282 |
| `integratedterminals` | Integrated Terminals（ストレージ端末） | 176 |
| `alekiships` | aleki's Nifty Ships（帆船Mod。ボート/スループ・区画・大砲・実績） | 120 |
| `integratedcrafting` | Integrated Crafting（自動クラフト） | 110 |
| `ftblibrary` | FTB Library（FTB系共通UI・GUI部品） | 99 |
| `patchouli` | Patchouli 本ビューアUI（全Patchouli本共通） | 90 |
| `ftbteams` | FTB Teams（チーム・パーティ管理） | 89 |
| `advancedperipherals` | Advanced Peripherals（アイテム・Patchouli本） | 88 |
| `create_tweaked_controllers` | Create: Tweaked Controllers（ゲームパッド対応コントローラー） | 85 |
| `drivebywire` | Drive By Wire（VS2船のケーブルネットワーク） | 29 |
| **合計** | 23名前空間 ＋ Patchouli本26ファイル | **18,346** |

### 🧩 パック側 kubejs で対応済み

| 名前空間 | Mod | キー数 |
|------|------|-------:|
| `tfc` | TerraFirmaCraft | 8,481 |
| `gtceu` | gtceu | 5,921 |
| `create` | create | 3,646 |

### 📦 Mod同梱で対応済み（69）

各 Mod が自前で `ja_jp` を同梱しており、そのまま日本語表示されます。

<details><summary>一覧を開く（69）</summary>

| 名前空間 | Mod | キー数 |
|------|------|-------:|
| `immersiveengineering` | ImmersiveEngineering | 1,405 |
| `iceandfire` | iceandfire | 1,322 |
| `railways` | Steam_Rails | 1,293 |
| `railcraft` | railcraft-reborn | 1,025 |
| `apotheosis` | Apotheosis | 1,014 |
| `firmalife` | Firmalife | 1,013 |
| `ae2` | appliedenergistics2 | 999 |
| `everycomp` | everycomp | 962 |
| `createbigcannons` | createbigcannons | 744 |
| `powergrid` | powergrid | 663 |
| `sgjourney` | Stargate Journey | 661 |
| `xaerominimap` | Xaeros_Minimap | 611 |
| `enderio` | EnderIO | 553 |
| `inventoryprofilesnext` | InventoryProfilesNext | 519 |
| `recruits` | recruits | 519 |
| `createdeco` | createdeco | 418 |
| `alltheores` | alltheores | 333 |
| `farmersdelight` | FarmersDelight | 323 |
| `create_connected` | create_connected | 307 |
| `createdieselgenerators` | createdieselgenerators | 286 |
| `allthemodium` | allthemodium | 282 |
| `jade` | Jade | 280 |
| `sophisticatedcore` | sophisticatedcore | 276 |
| `createaddition` | createaddition | 255 |
| `computercraft` | cc-tweaked | 233 |
| `sophisticatedbackpacks` | sophisticatedbackpacks | 228 |
| `voicechat` | voicechat | 228 |
| `waystones` | waystones | 199 |
| `enchdesc` | EnchantmentDescriptions | 183 |
| `gcyr` | gcyr | 183 |
| `expatternprovider` | ExtendedAE | 172 |
| `advanced_ae` | AdvancedAE | 167 |
| `repurposed_structures` | repurposed_structures | 161 |
| `modernfix` | modernfix | 137 |
| `storagedrawers` | StorageDrawers | 133 |
| `jei` | jei | 132 |
| `nochatreports` | NoChatReports | 129 |
| `immersive_aircraft` | immersive_aircraft | 123 |
| `petrolpark` | petrolpark | 81 |
| `xaerobetterpvp` | Xaeros_Minimap | 77 |
| `comforts` | comforts | 77 |
| `iris` | oculus | 72 |
| `copycats` | copycats | 67 |
| `chalk` | chalk | 64 |
| `simpleradio` | simpleradio | 55 |
| `trackwork` | trackwork | 55 |
| `valkyrienskies` | valkyrienskies-120 | 55 |
| `projectred_core` | ProjectRed | 54 |
| `lootr` | lootr | 51 |
| `cloth-config2` | cloth-config | 49 |
| `curios` | curios | 48 |
| `immersive_machinery` | immersive_machinery | 40 |
| `tfcagedalcohol` | TFCAgedAlcohol | 38 |
| `bellsandwhistles` | bellsandwhistles | 38 |
| `sodiumdynamiclights` | sodiumdynamiclights | 34 |
| `bookshelf` | Bookshelf | 32 |
| `enderchests` | enderchests | 28 |
| `allthetweaks` | allthetweaks | 26 |
| `minecraft` | TerraFirmaCraft | 21 |
| `ae2ct` | ae2ct | 19 |
| `waterflasks` | waterflasks | 17 |
| `tfcgroomer` | tfcgroomer | 16 |
| `astikorcarts` | astikorcarts | 15 |
| `controlling` | Controlling | 12 |
| `moonlight` | moonlight | 9 |
| `aeinfinitybooster` | AEInfinityBooster | 3 |
| `pccard` | Programmed Circuit Card | 1 |
| `searchables` | Searchables | 1 |
| `endertanks` | endertanks | 0 |

</details>

### ❌ 未対応・翻訳候補（84）

プレイに関わる未翻訳 Mod（キー数の多い順）。

<details><summary>一覧を開く（84）</summary>

| 名前空間 | Mod | キー数 |
|------|------|-------:|
| `vs_clockwork` | clockwork | 458 |
| `thoriumreactors` | thoriumreactors | 369 |
| `xaeroworldmap` | XaerosWorldMap | 272 |
| `beneath` | beneath | 268 |
| `sfm` | Super Factory Manager (SFM) | 255 |
| `firmaciv` | FirmaCivilization | 239 |
| `potionsmaster` | potionsmaster | 237 |
| `integrateddynamicscompat` | IntegratedDynamics | 214 |
| `tfcgenviewer` | tfcgenviewer | 177 |
| `projectred_fabrication` | ProjectRed | 174 |
| `bits_n_bobs` | bits_n_bobs | 174 |
| `projectred_illumination` | ProjectRed | 162 |
| `hostilenetworks` | HostileNeuralNetworks | 160 |
| `create_new_age` | create-new-age | 158 |
| `attributeslib` | ApothicAttributes | 130 |
| `gregitas_core` | gregitas-core | 129 |
| `fluxnetworks` | FluxNetworks | 123 |
| `workers` | workers | 114 |
| `buildinggadgets2` | buildinggadgets2 | 111 |
| `megacells` | megacells | 108 |
| `simpleplanes` | simpleplanes | 108 |
| `smallships` | smallships | 95 |
| `laserio` | laserio | 90 |
| `sfcr` | sfcr | 88 |
| `mininggadgets` | mininggadgets | 85 |
| `projectred_transmission` | ProjectRed | 71 |
| `precisionprospecting` | precisionprospecting | 70 |
| `petrolsparts` | petrolsparts | 69 |
| `tfc_textile` | tfc_textile | 69 |
| `freecam` | freecam | 65 |
| `tfships` | tfships | 63 |
| `tfccaffeinated` | tfccaffeinated | 61 |
| `extremesoundmuffler` | ExtremeSoundMuffler | 56 |
| `survivorsdelight` | survivorsdelight | 56 |
| `deathpunishment` | TFC_punishment_for_death | 53 |
| `tfclunchbox` | tfclunchbox | 49 |
| `betterp2p` | betterp2p | 47 |
| `ezvcsurvival` | Voiceless Survival | 44 |
| `advancedtfctech` | AdvancedTFCTech | 43 |
| `zume` | zume | 42 |
| `tfceureka` | tfceureka | 41 |
| `vs_eureka` | eureka-1201 | 40 |
| `fallingtrees` | fallingtrees | 40 |
| `tfcthermaldeposits` | TFCVolcanoes | 39 |
| `tfcambiental` | tfcambiental | 38 |
| `tfcchannelcasting` | tfcchannelcasting | 38 |
| `jadeaddons` | JadeAddons | 36 |
| `projectred_integration` | ProjectRed | 35 |
| `ae2wtlib` | ae2wtlib | 35 |
| `siegemachines` | 1.20.1]-Siege-Machines | 34 |
| `createmoredrillheads` | createmoredrillheads | 34 |
| `workerstfc` | workerstfc | 33 |
| `blazemap` | BlazeMap | 32 |
| `cccbridge` | cccbridge | 32 |
| `trashcans` | trashcans | 32 |
| `create_factory_logistics` | create_factory_logistics | 27 |
| `woodencog` | woodencog | 27 |
| `ae2netanalyser` | AE2NetworkAnalyzer | 24 |
| `wirelessredstone` | wirelessredstone | 24 |
| `merequester` | merequester | 23 |
| `tfcseedsoftime` | tfcseedsoftime | 23 |
| `wirelesschargers` | wirelesschargers | 23 |
| `createhorsepower` | createhorsepower | 21 |
| `cartography` | Cartography | 15 |
| `ae2things` | AE2-Things | 12 |
| `integratedterminalscompat` | IntegratedTerminals | 12 |
| `jade_vs` | Jade-VS | 10 |
| `coldsgrappler` | ColdGrapplerAndRopes(Forge1.20.1)vs1.0.0 | 8 |
| `survivorsabilities` | survivorsabilities | 7 |
| `castirongrill` | CastIronGrill | 6 |
| `hangglider` | HangGlider | 5 |
| `create_hp_ts` | create_hp_ts | 5 |
| `createimmersiveunnecessaryshaft` | createimmersiveunnecessaryshaft | 5 |
| `eyesoficeandfire` | eyesoficeandfire | 5 |
| `tfc_support_indicator` | tfc_support_indicator | 5 |
| `tfcea` | tfcea | 5 |
| `findme` | findme | 4 |
| `tfccanes` | tfccanes | 4 |
| `easynametags` | EasyNameTags | 3 |
| `headlight` | Headlight | 3 |
| `showcaseitem` | showcaseitem | 2 |
| `auroras` | Auroras | 1 |
| `justenoughprofessions` | JustEnoughProfessions | 1 |
| `waves` | Waves | 1 |

</details>

### ⚪ 対象外（39）

ライブラリ・軽量化・API・設定・未使用など、翻訳しても表示に影響しない Mod。

<details><summary>一覧を開く（39）</summary>

| 名前空間 | Mod | キー数 |
|------|------|-------:|
| `emi` | NuclearCraft | 2,129 |
| `distanthorizons` | DistantHorizons | 466 |
| `chloride` | chloride | 154 |
| `sodium` | embeddium | 65 |
| `configured` | configured | 62 |
| `titanium` | titanium | 48 |
| `creativecore` | CreativeCore | 44 |
| `cyclopscore` | CyclopsCore | 42 |
| `itemfilters` | item-filters | 41 |
| `configuration` | configuration | 40 |
| `guideme` | guideme | 36 |
| `balm` | balm | 35 |
| `observable` | observable | 33 |
| `geckolib` | geckolib | 31 |
| `libipn` | libIPN | 28 |
| `citadel` | citadel | 24 |
| `fastload` | Fastload-Reforged | 21 |
| `colorwheel` | colorwheel | 21 |
| `codechickenlib` | CodeChickenLib | 18 |
| `cb_microblock` | CBMultipart | 17 |
| `smoothboot` | smoothboot(reloaded) | 14 |
| `commoncapabilities` | CommonCapabilities | 10 |
| `measurements` | Measurements | 8 |
| `fusion` | fusion | 8 |
| `treetap` | treetap | 8 |
| `embeddium` | embeddium | 7 |
| `placebo` | Placebo | 6 |
| `almostunified` | almostunified | 6 |
| `packmenu` | PackMenu | 5 |
| `crashutilities` | crashutilities | 4 |
| `entityculling` | entityculling | 3 |
| `bcc` | BetterCompatibilityChecker | 2 |
| `betterfpsdist` | betterfpsdist | 2 |
| `jeimultiblocks` | jeimultiblocks | 2 |
| `framework` | framework | 1 |
| `pandalib` | pandalib | 1 |
| `drivebywire_recipes` | drivebywire_recipes | 0 |
| `ftbxmodcompat` | ftb-xmod-compat | 0 |
| `shetiphiancore` | shetiphiancore | 0 |

</details>

> `emi` は EMI 用のタグ表示名だが、本パックは JEI を使い EMI 未導入のため対象外。

> この一覧は `python tools/scan_status.py "<インスタンスのパス>"` で再生成できます。

## ライセンス

- 本リポジトリの**翻訳物**は [Creative Commons 表示 - 非営利 - 継承 4.0 国際 (CC BY-NC-SA 4.0)](LICENSE) の下で提供されます。
- ただし、**原文**（クエスト・各Modのテキスト）の著作権は各権利者（ATMTeam および各Mod作者）に帰属します。本リポジトリはその翻訳（二次的著作物）です。
- 再配布・改変の際は、CC BY-NC-SA 4.0 の条件に加え、元パック [AllTheMods/Gravitas2](https://github.com/AllTheMods/Gravitas2) および各Modのライセンスにも従ってください。
- 非公式の有志翻訳であり、ATMTeam 公式とは関係ありません。

## 貢献・開発

翻訳は AI（Claude）による作成です。誤訳・表記ゆれの指摘・修正を歓迎します。ビルド方法・リリース手順・翻訳規約などの開発情報は [CLAUDE.md](CLAUDE.md) を参照してください。

