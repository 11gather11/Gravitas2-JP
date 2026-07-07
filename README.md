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

- ✅ **このパックで翻訳**：76／📦 **Mod同梱で対応済み**：33／🧩 **パック側 kubejs で対応済み**：3／📖 **同梱翻訳が不完全（翻訳候補）**：25／❌ **未対応（翻訳候補）**：44（ほかにライブラリ・未使用など 37 は対象外）

### ✅ このパックで翻訳

| 名前空間 | 内容 | キー数 |
|------|------|-------:|
| `dfc` | DecoFirmaCraft（TFC装飾ブロック大量追加） | 3,062 |
| `nuclearcraft` | NuclearCraft（原子力Mod。Mod同梱ja_jpの欠落分649=加速器・粒子物理・標的チェンバー・クーゲルブリッツ等を補完） | 2,851 |
| `immersivegeology` | Immersive Geology（地質・鉱石加工） | 2,120 |
| `mcw_tfc_aio` | Macaw's 家具（TFC統合版） | 2,033 |
| `integrateddynamics` | Integrated Dynamics 本体（本・アイテム・オペレーター・アスペクト・実績） | 1,754 |
| `railways` | Steam n Rails（鉄道拡張。同梱ja欠落376=レール/煙突/台車を補完） | 1,293 |
| `tombstone` | Corail Tombstone（墓・死亡管理。アイテム・実績・メッセージ・コンペンディウム） | 1,112 |
| `railcraft` | Railcraft Reborn（鉄道Mod。同梱ja欠落153=レール/信号/機関車を補完） | 1,025 |
| `scguns` | Scorched Guns（銃Mod。銃/弾薬/防具・実績・エンチャント・タレット・GUI） | 971 |
| `everycomp` | Every Compat（他Mod家具の互換ブロック名。同梱ja欠落961を補完） | 962 |
| `tfcastikorcarts` | TFC Astikor Carts（木材×荷車。補給/動物カート・鋤・車輪） | 928 |
| `createbigcannons` | Create Big Cannons（大砲Mod。同梱ja欠落352=信管・砲弾・Ponderを補完） | 744 |
| `powergrid` | Power Grid（電子回路シミュレーション。同梱ja欠落413を補完） | 663 |
| `sgjourney` | Stargate Journey（同梱ja欠落64=DHD/インターフェース補完） | 661 |
| `ftbquests` | FTB Quests（クエストシステムのUI・エディタ・タスク・報酬） | 572 |
| `enderio` | Ender IO（機械・導管・合金。同梱jaが実質英語のため553を翻訳） | 553 |
| `integratedtunnels` | Integrated Tunnels（転送） | 487 |
| `vintage` | Create: Vintage（Createアドオン。金属加工品・機械・Ponder・JEI） | 481 |
| `tfc_ie_addon` | TFC-IE Crossover（TFC×IE。鉱石・金属加工・鉱物） | 461 |
| `vs_clockwork` | VS: Clockwork（Create×Valkyrien Skies。飛空艇・ガス・気球） | 458 |
| `createdeco` | Create Deco（装飾。同梱ja欠落＝ファサード・塀・角レンガを補完） | 418 |
| `framedblocks` | FramedBlocks（カモフラージュ装飾。幾何形状ブロック・設定・ツールチップ） | 346 |
| `createdieselgenerators` | Create: Diesel Generators（同梱ja欠落＝燃料・機械・Ponderを補完） | 286 |
| `ftbchunks` | FTB Chunks（チャンク取得・地図・ミニマップ・ウェイポイント） | 282 |
| `beneath` | Beneath（ネザー拡張。TFC統合。木材・鉱石・キノコ・儀式） | 268 |
| `sfm` | Super Factory Manager（自動化プログラムMod。GUI/ログ/コンパイラ） | 255 |
| `firmaciv` | Firma: Civilization（TFC。手漕ぎ船・カヌー・航海器具・屋根） | 239 |
| `potionsmaster` | Potions Master（鉱石探知・構造物高速移動ポーション。粉・効果） | 237 |
| `gcyr` | Gregicality Rocketry（宇宙。惑星岩・レゴリス。同梱ja欠落補完） | 183 |
| `integratedterminals` | Integrated Terminals（ストレージ端末） | 176 |
| `projectred_fabrication` | Project Red: Fabrication（IC設計・製造） | 174 |
| `bits_n_bobs` | Bits n Bobs（Create装飾。岩石タイル・ニキシー管・歯車チェーン） | 174 |
| `projectred_illumination` | Project Red: Illumination（16色ランプ・照明） | 162 |
| `hostilenetworks` | Hostile Neural Networks（Mob学習シミュ。トリビア詩含む） | 160 |
| `create_new_age` | Create: New Age（電力・原子炉・磁石発電） | 158 |
| `gregitas_core` | Gravitas² Core Mod（GregTech統合。素材・真空/圧力配管） | 129 |
| `fluxnetworks` | Flux Networks（無線送電網） | 123 |
| `alekiships` | aleki's Nifty Ships（帆船Mod。ボート/スループ・区画・大砲・実績） | 120 |
| `buildinggadgets2` | Building Gadgets 2（建築補助ツール・GUI） | 111 |
| `integratedcrafting` | Integrated Crafting（自動クラフト） | 110 |
| `simpleplanes` | Simple Planes（飛行機・ヘリ） | 108 |
| `ftblibrary` | FTB Library（FTB系共通UI・GUI部品） | 99 |
| `patchouli` | Patchouli 本ビューアUI（全Patchouli本共通） | 90 |
| `laserio` | LaserIO（アイテム/液体/エネルギー転送・カード） | 90 |
| `ftbteams` | FTB Teams（チーム・パーティ管理） | 89 |
| `advancedperipherals` | Advanced Peripherals（アイテム・Patchouli本） | 88 |
| `create_tweaked_controllers` | Create: Tweaked Controllers（ゲームパッド対応コントローラー） | 85 |
| `mininggadgets` | （重複） | 85 |
| `projectred_transmission` | Project Red: Transmission（配線・ケーブル） | 71 |
| `petrolsparts` | Petrol's Parts（Create運動部品・Ponder） | 69 |
| `tfc_textile` | TFC Textile（獣皮防具・繊維） | 69 |
| `tfccaffeinated` | TFC Caffeinated（TFC。コーヒー・茶・飲料） | 61 |
| `survivorsdelight` | Survivor's Delight（TFC。戸棚・フライパン） | 56 |
| `projectred_core` | Project Red: Core（回路部品・イルマー染料。同梱ja欠落補完） | 54 |
| `betterp2p` | Better P2P（AE2 P2P管理カード） | 47 |
| `advancedtfctech` | Advanced TFC Tech（TFC。脱穀機・製粉所・力織機） | 43 |
| `itemfilters` | Item Filters（アイテムフィルター各種） | 41 |
| `tfceureka` | TFC Eureka Compat（TFC木材の操舵輪） | 41 |
| `vs_eureka` | VS Eureka（VS飛空艇。操舵輪・気球・エンジン） | 40 |
| `tfcthermaldeposits` | TFC Thermal Deposits（火山鉱物） | 39 |
| `projectred_integration` | Project Red: Integration（論理ゲート） | 35 |
| `ae2wtlib` | AE2 Wireless Terminals（ワイヤレス端末） | 35 |
| `siegemachines` | Medieval Siege Machines（攻城兵器） | 34 |
| `createmoredrillheads` | Create: More Drill Heads（ドリルヘッド） | 34 |
| `cccbridge` | CC:C Bridge（ComputerCraft×Create連携） | 32 |
| `drivebywire` | Drive By Wire（VS2船のケーブルネットワーク） | 29 |
| `create_factory_logistics` | Create: Factory Logistics（物流。瓶詰め・ネットワークリンク・液体） | 27 |
| `wirelessredstone` | Wireless Redstone（無線レッドストーン） | 24 |
| `merequester` | ME Requester（AE2自動リクエスト） | 23 |
| `cb_microblock` | CB MicroBlocks（マイクロブロック） | 17 |
| `ae2things` | AE2 Things（ディスクドライブ） | 12 |
| `castirongrill` | TFC Cast Iron Grill（鋳鉄グリル） | 6 |
| `hangglider` | Hang Glider（ハンググライダー） | 5 |
| `eyesoficeandfire` | Eyes of Ice and Fire（ドラゴンの目） | 5 |
| `tfccanes` | TFC Canes（TFC。杖） | 4 |
| `headlight` | Headlight（ヘッドライト） | 3 |
| **合計** | 76名前空間 ＋ Patchouli本26ファイル | **28,992** |

### 🧩 パック側 kubejs で対応済み

| 名前空間 | Mod | キー数 |
|------|------|-------:|
| `tfc` | TerraFirmaCraft | 8,481 |
| `gtceu` | gtceu | 5,921 |
| `create` | create | 3,646 |

### 📦 Mod同梱で対応済み（33）

各 Mod が自前で `ja_jp` を同梱しており、そのまま日本語表示されます。

<details><summary>一覧を開く（33）</summary>

| 名前空間 | Mod | キー数 |
|------|------|-------:|
| `immersiveengineering` | ImmersiveEngineering | 1,405 |
| `iceandfire` | iceandfire | 1,322 |
| `apotheosis` | Apotheosis | 1,014 |
| `firmalife` | Firmalife | 1,013 |
| `alltheores` | alltheores | 333 |
| `farmersdelight` | FarmersDelight | 323 |
| `allthemodium` | allthemodium | 282 |
| `createaddition` | createaddition | 255 |
| `computercraft` | cc-tweaked | 233 |
| `sophisticatedbackpacks` | sophisticatedbackpacks | 228 |
| `waystones` | waystones | 199 |
| `expatternprovider` | ExtendedAE | 172 |
| `advanced_ae` | AdvancedAE | 167 |
| `storagedrawers` | StorageDrawers | 133 |
| `jei` | jei | 132 |
| `immersive_aircraft` | immersive_aircraft | 123 |
| `petrolpark` | petrolpark | 81 |
| `xaerobetterpvp` | Xaeros_Minimap | 77 |
| `copycats` | copycats | 67 |
| `chalk` | chalk | 64 |
| `lootr` | lootr | 51 |
| `immersive_machinery` | immersive_machinery | 40 |
| `tfcagedalcohol` | TFCAgedAlcohol | 38 |
| `bellsandwhistles` | bellsandwhistles | 38 |
| `bookshelf` | Bookshelf | 32 |
| `enderchests` | enderchests | 28 |
| `allthetweaks` | allthetweaks | 26 |
| `minecraft` | TerraFirmaCraft | 21 |
| `waterflasks` | waterflasks | 17 |
| `astikorcarts` | astikorcarts | 15 |
| `pccard` | Programmed Circuit Card | 1 |
| `searchables` | Searchables | 1 |
| `endertanks` | endertanks | 0 |

</details>

### 📖 同梱翻訳が不完全・翻訳候補（25）

`ja_jp` を同梱しているものの、Mod 更新で追加された要素が未翻訳だったり、英語のまま放置されているもの。NuclearCraft と同様に **欠落分だけをリソースパックの lang 上書きで補完**できます（lang はキー単位でマージされる）。

- **欠落**：`en_us` にあるが `ja_jp` に無いキー（Mod 更新で増えた新要素など）
- **英語のまま**：`ja_jp` に有るが値が英語のキー（※固有名詞が含まれ得るため目安）

<details><summary>一覧を開く（25）</summary>

| 名前空間 | Mod | 欠落 | 英語のまま | en総数 |
|------|------|-------:|-------:|-------:|
| `xaerominimap` | Xaeros_Minimap | 417 | 5 | 611 |
| `ae2` | appliedenergistics2 | 140 | 10 | 999 |
| `enchdesc` | EnchantmentDescriptions | 128 | 0 | 169 |
| `repurposed_structures` | repurposed_structures | 101 | 3 | 161 |
| `sophisticatedcore` | sophisticatedcore | 61 | 16 | 276 |
| `recruits` | recruits | 59 | 11 | 519 |
| `jade` | Jade | 34 | 12 | 279 |
| `inventoryprofilesnext` | InventoryProfilesNext | 32 | 6 | 519 |
| `comforts` | comforts | 35 | 2 | 77 |
| `create_connected` | create_connected | 28 | 4 | 307 |
| `trackwork` | trackwork | 22 | 2 | 55 |
| `voicechat` | voicechat | 23 | 1 | 228 |
| `valkyrienskies` | valkyrienskies-120 | 21 | 1 | 55 |
| `nochatreports` | NoChatReports | 16 | 5 | 129 |
| `curios` | curios | 16 | 0 | 48 |
| `modernfix` | modernfix | 15 | 1 | 137 |
| `sodiumdynamiclights` | sodiumdynamiclights | 15 | 0 | 34 |
| `cloth-config2` | cloth-config | 4 | 8 | 49 |
| `iris` | oculus | 10 | 2 | 72 |
| `simpleradio` | simpleradio | 8 | 3 | 55 |
| `tfcgroomer` | tfcgroomer | 5 | 0 | 16 |
| `ae2ct` | ae2ct | 4 | 0 | 19 |
| `controlling` | Controlling | 3 | 0 | 12 |
| `moonlight` | moonlight | 3 | 0 | 9 |
| `aeinfinitybooster` | AEInfinityBooster | 0 | 1 | 3 |

</details>

### ❌ 未対応・翻訳候補（44）

プレイに関わる未翻訳 Mod（キー数の多い順）。

<details><summary>一覧を開く（44）</summary>

| 名前空間 | Mod | キー数 |
|------|------|-------:|
| `thoriumreactors` | thoriumreactors | 369 |
| `xaeroworldmap` | XaerosWorldMap | 272 |
| `integrateddynamicscompat` | IntegratedDynamics | 214 |
| `tfcgenviewer` | tfcgenviewer | 177 |
| `attributeslib` | ApothicAttributes | 130 |
| `workers` | workers | 114 |
| `megacells` | megacells | 108 |
| `smallships` | smallships | 95 |
| `sfcr` | sfcr | 88 |
| `precisionprospecting` | precisionprospecting | 70 |
| `freecam` | freecam | 65 |
| `tfships` | tfships | 63 |
| `extremesoundmuffler` | ExtremeSoundMuffler | 56 |
| `deathpunishment` | TFC_punishment_for_death | 53 |
| `tfclunchbox` | tfclunchbox | 49 |
| `ezvcsurvival` | Voiceless Survival | 44 |
| `zume` | zume | 42 |
| `fallingtrees` | fallingtrees | 40 |
| `tfcambiental` | tfcambiental | 38 |
| `tfcchannelcasting` | tfcchannelcasting | 38 |
| `jadeaddons` | JadeAddons | 36 |
| `workerstfc` | workerstfc | 33 |
| `blazemap` | BlazeMap | 32 |
| `trashcans` | trashcans | 32 |
| `woodencog` | woodencog | 27 |
| `ae2netanalyser` | AE2NetworkAnalyzer | 24 |
| `tfcseedsoftime` | tfcseedsoftime | 23 |
| `wirelesschargers` | wirelesschargers | 23 |
| `createhorsepower` | createhorsepower | 21 |
| `cartography` | Cartography | 15 |
| `integratedterminalscompat` | IntegratedTerminals | 12 |
| `jade_vs` | Jade-VS | 10 |
| `coldsgrappler` | ColdGrapplerAndRopes(Forge1.20.1)vs1.0.0 | 8 |
| `survivorsabilities` | survivorsabilities | 7 |
| `create_hp_ts` | create_hp_ts | 5 |
| `createimmersiveunnecessaryshaft` | createimmersiveunnecessaryshaft | 5 |
| `tfc_support_indicator` | tfc_support_indicator | 5 |
| `tfcea` | tfcea | 5 |
| `findme` | findme | 4 |
| `easynametags` | EasyNameTags | 3 |
| `showcaseitem` | showcaseitem | 2 |
| `auroras` | Auroras | 1 |
| `justenoughprofessions` | JustEnoughProfessions | 1 |
| `waves` | Waves | 1 |

</details>

### ⚪ 対象外（37）

ライブラリ・軽量化・API・設定・未使用など、翻訳しても表示に影響しない Mod。

<details><summary>一覧を開く（37）</summary>

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

