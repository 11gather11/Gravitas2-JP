# Changelog

このプロジェクトの主要な変更点を記録します。
書式は [Keep a Changelog](https://keepachangelog.com/ja/1.1.0/) に準拠し、
バージョニングは [Semantic Versioning](https://semver.org/lang/ja/) に従います。

## [Unreleased]

## [0.20.0] - 2026-07-07

### Added

- **Patchouli ガイドブックの翻訳を完了**。同梱日本語版があるTFC本体/Apotheosis等を除く、未翻訳だった全ブックを本文まで翻訳（残りの独立3ブックを追加）。
  - **nuclearcraft**（NuclearCraft ガイド 全30章：核分裂/核融合炉・加速器〈線形/シンクロトロン〉・粒子チェンバー・クーゲルブリッツ・機械。物理数式は原文を保持）。
  - **buildinggadgets2**（Building Gadgets 2 全29章：建築/交換/コピペ/破壊ガジェット・各種モード・仕組み）。
  - **laserio**（LaserIO 全39章：ノード/コネクター/各種カード/フィルター/モードの完全マニュアル）。
- これで **Patchouli ガイドブック 19ブック（計約90章＋TFC相乗り章）** の翻訳が完了。ゲーム内ガイドがほぼ全編日本語化。


## [0.19.2] - 2026-07-07

### Added

- **ガイドブック翻訳（独立ブック・続き）**：**railcraft**（Railcraft Reborn ガイド 全42章：レールの種類・信号箱・マルチブロック〈高炉/コークス炉/蒸気ボイラー/タービン/鉄タンク〉・道具を本文まで翻訳）。既訳のUI用語と統一。


## [0.19.1] - 2026-07-07

### Added

- **ガイドブック翻訳（独立ブック・続き）**：**sgjourney**（Stargate Journey：惑星・スターゲート・DHD・考古学 全42章。作者未記載の "TODO" ページは原文維持）、**advancedperipherals**（CC:Tweaked 周辺機器マニュアル：オートマタコア・各種検知器/ブリッジ 全25章）を本文まで翻訳。


## [0.19.0] - 2026-07-07

### Added

- **Patchouli ガイドブックの翻訳を開始**。まず TFC フィールドガイドに相乗りする全アドオン章＋Beneath＋EnderIO を本文まで翻訳（13ブック・約350文字列）。TFC本体のガイドは Mod 同梱の日本語版があるため、その中に英語で並んでいた以下の章を日本語化。
  - **beneath**（Beneath 全11章：古代の祭壇・ゲップフラワー・作物・ヘルフォージ・供犠の一覧 等）
  - **firmaciv**（船・カヤック・スループ・航法〈経度/緯度/高度〉）、**tfc_ie_changes**（合金・化学・アーク炉・鉱石 等13章）、**survivorsdelight**（戸棚・調理鍋・フライパン・特殊効果 等8章）
  - **advancedtfctech**（ビームハウス・製粉機・動力織機 等）、**precisionprospecting**、**tfchannelcasting**、**tfships**、**workerstfc**、**castirongrill**、**tfcgyres_orehints**、**firmalife**（欠落2章）、**enderio**
  - Patchouli書式（`$(thing)`/`$(l:)`/`$(item)$(k:)`/`$(br)`/`$(li)`/色コード）を保持し、書式トークン整合を自動検証。
- **survivorsabilities の `appetite`（食欲）属性を補完**（Mod側が en_us 未登録のため生キー表示だった）。

### Note

- ApothicAttributes 属性画面の「Hide Unchanged」はMod内ハードコード文字列（翻訳キーなし）のためリソースパックでは翻訳不可。
- 残りのガイドブック（railcraft/sgjourney/laserio/buildinggadgets2/advancedperipherals/nuclearcraft ほか独立ブック 約180章）は今後のバージョンで順次翻訳予定。


## [0.18.1] - 2026-07-07

### Fixed

- **survivorsabilities の `appetite`（食欲）属性を補完**。Mod側が en_us にキーを登録し忘れており生キーが表示されていたため、`attribute.name.survivorsabilities.appetite` と効果名をリソースパックで追加。

### Note

- ApothicAttributes の属性画面の「Hide Unchanged」ボタンは、Mod内でハードコードされたリテラル文字列（翻訳キーなし）のため、リソースパックでは翻訳できない。Mod本体の修正が必要。

## [0.18.0] - 2026-07-07

### Added

- **未対応（翻訳候補）だった Mod 37種を一括翻訳**（計1,845キー）。これにより「未対応（翻訳候補）」が **37 → 0** になりました（残る37は軽量化/ライブラリ/未使用EMIで対象外）。
  - **xaeroworldmap（Xaero's World Map）**（272）：ワールドマップ全UI・洞窟モード・PNG書き出し・領地・ディメンション切替。
  - **integrateddynamicscompat（213）**：Integrated Dynamics の互換アスペクト/演算子（RF/Tesla/EU/Thaumcraft/Refined Storage/Charset）。エネルギー系は合成。
  - **tfcgenviewer（177）**：TFCワールド生成プレビュー・岩石エディター（岩石名はTFC準拠）。
  - **attributeslib（Apothic Attributes）**（130）：属性・効果・ダメージ源メッセージ。
  - **workers（114）／smallships（95）／sfcr（88）／precisionprospecting（69）／freecam（65）／tfships（63）**（船・工具は木材/金属で合成）。
  - **extremesoundmuffler（56）／deathpunishment（53）／ezvcsurvival（44）／zume（42）／fallingtrees（40）／tfcambiental（38）／tfcchannelcasting（37）／jadeaddons（36）／trashcans（32）／blazemap（32）** ほか小規模17種。
  - `%s`/`%d`/`%1$s`/`%%`・§カラーコード・改行を保持し検証（未訳0）。

## [0.17.0] - 2026-07-07

### Added

- **同梱翻訳が不完全だった Mod 25種の欠落・英語のまま部分を一括補完**（計1,293キー）。これにより「同梱翻訳が不完全（partial_jar）」が **25 → 0** になりました。
  - **xaerominimap（Xaero's Minimap）**（422）：ミニマップ全設定UI・洞窟モード・エンティティレーダー・ウェイポイント・領地オーバーレイ・情報表示（`%1$s`・§・改行・方位N/E/S/W保持）。
  - **ae2（Applied Energistics 2）**（150）：ME倉庫のUI・チャット・空間ストレージ・自動クラフト・パターン・ツールチップ。
  - **enchdesc（Enchantment Descriptions）**（128）：他Mod由来のエンチャント説明文。
  - **repurposed_structures（104）**：構造物名を〈バイオーム×構造種〉で合成。
  - **sophisticatedcore（77）／recruits（70）／jade（46）／inventoryprofilesnext（38）／comforts（37）／create_connected（32）／trackwork（24）／voicechat（24）／valkyrienskies（22）／nochatreports（21）／curios（16）／modernfix（16）／sodiumdynamiclights（15）／cloth-config2（12）／iris（12）／simpleradio（11）／tfcgroomer（5）／ae2ct（4）／controlling（3）／moonlight（3）／aeinfinitybooster（1）**。
  - `%s`/`%d`/`%1$s`/`%%`・§カラーコード・改行を保持し検証（未訳0）。

## [0.16.1] - 2026-07-07

### Fixed

- **gregitas（KubeJS追加アイテム）の翻訳漏れを補完**（+34キー、計377）。ポリマー6種のマレットヘッド（`Polytetrafluoroethylene Mallet Head` → ポリテトラフルオロエチレンのマレットヘッド 等）、gregitas流体9種の流体名・液体ブロック・バケツ（`Crimson Resin Bucket` → 真紅の樹脂バケツ 等）、青銅めっきレンガを追加。

## [0.16.0] - 2026-07-07

### Added

- **Mod・KubeJSコンテンツ 9種を翻訳**（計972キー）。うち1つは同梱 ja の欠落補完、1つはパック独自の KubeJS 追加アイテム。
  - **thoriumreactors（Thorium Reactors）**（369）：多ブロック式トリウム原子炉Mod。原子炉/タービン/熱交換器の構造ブロック・機械（濃縮機・結晶化装置・遠心分離機ほか）・制御GUI（原子炉概要インターフェース・緊急停止・バルブ操作）・金属/鉱石/流体を翻訳（金属系は合成）。
  - **gregitas（Gravitas² の KubeJS 追加アイテム）**（343）：クリエイティブ「KubeJS」タブに並ぶGregTech風のカスタム工具部品。金属17種×工具パーツ16種（肉切り刃・のこぎりの刃・ハンマーのヘッド等）、穀物マッシュ・木材の船体セグメント・各種素材を `assets/gregitas` の lang 上書きで合成翻訳。
  - **megacells（MEGA Cells）**（108）：AE2大容量ストレージ拡張。サイズ×セル種（アイテム/液体/化学物質/マナ/ソース）を合成、クラフト機構・圧縮を翻訳。
  - **workerstfc（WorkersTFC）**（33）：TFC村人の職業・アイテム。**tfclunchbox（49）**：保冷/電動ランチボックス。**ae2netanalyser（24）**：MEネットワーク可視化。**wirelesschargers（23）**：無線充電器。**expatternprovider（ExtendedAE, 8・補完）**。**tfcea（5）**：TFC冷蔵庫。
  - `%s`/`%d`/`%1$d`/`%%`・§コードを保持し検証（未訳0）。

### Note

- 依頼にあった「gravitas」は v0.1.0 で翻訳済みの FTB Quests 名前空間で、残る英語表記は Mod名・ブランド名・ASCIIアート（Create / GregTech / NuclearCraft / `uwu` 等）のため意図的に原語のまま。クリエイティブ「KubeJS」タブの未訳アイテムは上記 **gregitas** で対応。

## [0.15.0] - 2026-07-07

### Added

- **Mod 15種を翻訳**（計1,829キー）。うち3つは Mod 同梱 ja の欠落補完。
  - **createbigcannons（Create Big Cannons）**（352・補完）：大砲Mod。信管・砲弾・機関砲・鋳造・Ponder建築ガイド86・効果音字幕（`_強調_`保持）。
  - **hostilenetworks（Hostile Neural Networks）**（159）：Mob学習シミュ。GUI・各Mobのトリビア詩を翻訳。
  - **bits_n_bobs（174）**：Create装飾。岩石タイル・色椅子・ニキシー管・歯車チェーンを合成。
  - **railcraft（Railcraft Reborn）**（153・補完）：鉄道Mod。レール・信号・機関車・検知器の説明。
  - **fluxnetworks（123）／simpleplanes（108）／petrolsparts（69）／tfc_textile（69）／survivorsdelight（56）／sgjourney（64・補完）／tfcthermaldeposits（39）／createmoredrillheads（34）／siegemachines（34）／cb_microblock（17）／headlight（3）**。
  - `%s`/`%1$s`/`%%`・`_強調_`・改行を保持し検証（未訳0）。

## [0.14.0] - 2026-07-07

### Added

- **Mod 15種を翻訳**（計2,721キー）。うち3つは Mod 同梱 ja の欠落・英語のまま部分を補完。
  - **enderio（Ender IO）**（553）：同梱 ja が実質英語コピーだったため全面翻訳。機械・導管・合金・キャパシタ・エンチャント・GUI（色ガラス/石英は合成）。
  - **powergrid（Power Grid）**（413・補完）：電子回路シミュレーション。部品・計器・回路設計GUI・Ponder（電子回路チュートリアル160）。
  - **railways（Steam 'n' Rails）**（376・補完）：鉄道拡張。木材×レール・煙突（材質×形状）・台車・ロコメタルを合成。
  - **sfm（Super Factory Manager）**（255）：自動化プログラムMod。GUI・ログ・コンパイラメッセージ。
  - **gregitas_core（Gravitas² Core）**（129）：GregTech統合コア。素材・真空/圧力配管・岩石鉱石。
  - **laserio（90）／vs_eureka（40）／advancedtfctech（42）／betterp2p（47）／ae2wtlib（35）／merequester（23）／wirelessredstone（24）／ae2things（12）／castirongrill（6）／hangglider（5）**。
  - `%s`/`%d`/`%1$s`/`%.2f`・§コード・`_強調_`・改行を保持し検証（未訳0）。

## [0.13.0] - 2026-07-07

### Added

- **Mod 8種を翻訳**（計1,670キー）。うち2つは Mod 同梱 ja の欠落補完。
  - **everycomp（Every Compat）**（961・欠落補完）：他Mod家具の互換ブロック名。`block_type` 832件を語彙辞書で合成（`%s`保持）、他Mod木材名・中空丸太・GUI・ツールチップを翻訳。
  - **firmaciv（Firma: Civilization）**（238）：TFC。手漕ぎ船・スループ・丸木舟・カヌー部品・航海器具・屋根（木材合成）。
  - **potionsmaster（Potions Master）**（237）：鉱石探知・構造物高速移動ポーション。粉・効果を素材/構造物辞書で合成。
  - **mininggadgets（Mining Gadgets）**（85）：採掘ガジェット・アップグレード・GUI。
  - **tfceureka（41）**：TFC木材の操舵輪。**itemfilters（41）**：アイテムフィルター各種。
  - **gcyr（Gregicality Rocketry）**（42・欠落補完）：惑星岩・レゴリス・宇宙ステーション。
  - **eyesoficeandfire（5）**：ドラゴンの目。
  - `%s`/`%d`/`%1$s`・改行・`▶`等を保持し、キー一致とプレースホルダ整合を検証（未訳0）。

## [0.12.0] - 2026-07-07

### Added

- **create_factory_logistics（Create: Factory Logistics）**（27）を翻訳。瓶詰め機・ネットワークリンク・液体機構・在庫/予約モード・Ponder・液体属性フィルター（`%1$s` 保持）。v0.11.0 で漏れていた依頼分を補完。

## [0.11.0] - 2026-07-07

### Added

- **Mod 15 名前空間を翻訳**（計2,357キー）。うち3つは Mod 同梱 ja の欠落補完。
  - **vs_clockwork（VS: Clockwork）**（458）：Create×Valkyrien Skies。飛空艇部品・ガス/気球システム・ワンダーワンド・グラビトロン・Ponder。
  - **beneath（Beneath）**（267）：ネザー拡張（TFC統合）。真紅/歪んだ木材・鉱石・キノコ・儀式（木材はTFC規則で合成）。
  - **createdieselgenerators**（195・欠落補完）：燃料・機械・エンティティフィルター・Ponder。
  - **projectred_fabrication / illumination / integration / transmission / core**（496）：Project Red 全体。IC設計・16色照明・論理ゲート・配線・回路部品（色×形状は合成）。
  - **create_new_age（Create: New Age）**（158）：電力・原子炉・磁石発電・Ponder。
  - **buildinggadgets2（Building Gadgets 2）**（111）：建築補助ツールのGUI・メッセージ。
  - **createdeco**（85・欠落補完）：ファサード・塀・角レンガ（既存 ja の訳語に準拠して合成）。
  - **tfccaffeinated（61）**：コーヒー・茶・飲料。**cccbridge（32）**：CC×Create連携。**tfccanes（4）**：杖。
  - `%s`/`%d`/`%1$s`/`%%`・`_強調_`・§コード・改行を保持し、キー一致とプレースホルダ整合を検証（未訳0）。

### Changed

- `scan_status.py` に **同梱翻訳の網羅度チェック**を追加。`ja_jp` を同梱しつつ不完全な Mod を `partial_jar`（欠落15件以上またはカバレッジ85%未満）として分類し、欠落・英語のままキー数を表示する。
- README の「翻訳状況」に **📖 同梱翻訳が不完全・翻訳候補** セクションを追加。従来 `done_jar` に埋もれていた翻訳候補（enderio・railways・createbigcannons・ae2 ほか）を可視化。
- CLAUDE.md に「同梱翻訳が不完全な Mod の欠落補完」手順を追記。

## [0.10.0] - 2026-07-07

### Added

- **Mod 4種を翻訳**（計883キー）。
  - **NuclearCraft（加速器ほか）**（649）：Mod同梱 ja_jp の欠落分をリソースパックの lang 上書きで補完（キー単位でマージ）。加速器（線形加速器・標的チェンバー・粒子ビーム）、粒子物理（クォーク/レプトン/中間子/バリオン133）、クーゲルブリッツ（ブラックホール）チェンバー、同位体・スポレーション廃棄物、実績、Ponder建築ガイド、機械UI・レポートを翻訳。
  - **alekiships（aleki's Nifty Ships）**（120）：帆船Mod。ボート/スループ・区画・大砲・実績（木材はバニラ準拠）。
  - **create_tweaked_controllers（Create: Tweaked Controllers）**（85）：ゲームパッド対応リンクコントローラー。Create書式の `_強調_` マーカーを保持。
  - **drivebywire（Drive By Wire）**（29）：VS2船のケーブルネットワーク（Ponder含む）。
  - キー一致・プレースホルダ整合を検証済み（未訳0）。

## [0.9.0] - 2026-07-07

### Added

- **TFC系アドオン2種を翻訳**（計1,389キー）。
  - **tfcastikorcarts（TFC Astikor Carts）**（928）：木材×荷車の合成命名（補給/動物カート・鋤・ポスティリオン・車輪）。木材103種を辞書で合成。
  - **tfc_ie_addon（TFC-IE Crossover）**（461）：TFC×Immersive Engineering。鉱石ブロック（グレード×岩石×鉱石）はTFC規則で合成、金属加工品・鉱物・工具ヘッド・鉱脈名を翻訳。
  - キー一致・プレースホルダ整合を検証済み（未訳0）。

### Changed

- `build.py` を `tools/build.py` へ移動し、`tools/scan_status.py` と場所を統一。CI/リリースワークフローとドキュメントの参照を更新（`python tools/build.py ...`）。

## [0.8.0] - 2026-07-06

### Added

- **FTB系UIをまとめて翻訳**（計1,042キー）。
  - **ftbquests（FTB Quests）**（572）：クエストシステムのUI・エディタ・タスク・報酬・コマンド。
  - **ftbchunks（FTB Chunks）**（282）：チャンク取得・地図・ミニマップ・ウェイポイント・チーム保護設定。
  - **ftblibrary（FTB Library）**（99）：FTB系共通のGUI部品・サイドバー。
  - **ftbteams（FTB Teams）**（89）：チーム・パーティ管理のUIとメッセージ。
  - `%s`/`%d`/`%%`・改行を保持し、キー一致とプレースホルダ整合を検証済み（未訳0）。

## [0.7.0] - 2026-07-06

### Added

- **scguns（Scorched Guns）** を翻訳（971キー）。多数の銃・弾薬・防具・タレットを追加する銃Mod。
  銃の固有名はカタカナ、素材/弾薬/装備/アタッチメントは意訳、実績（フレーバー文）・エンチャント・特性・GUI・JEI説明・攻撃メッセージを翻訳。`%s`/`%d`/`§`/`♥` を保持し、キー一致とプレースホルダ整合を検証済み（未訳0）。

## [0.6.0] - 2026-07-06

### Added

- **framedblocks（FramedBlocks）** を翻訳（346キー）。他ブロックの見た目を纏えるカモフラージュ装飾Mod。
  幾何形状ブロック203種は語彙辞書で合成生成（`フレーム＋形状`）、設定・ツールチップ・メッセージ・アイテム（設計図/ハンマー/レンチ等）を翻訳。プレースホルダ整合を検証済み（未訳0）。

## [0.5.0] - 2026-07-06

### Added

- **vintage（Create: Vintage）** を翻訳（481キー）。Create アドオン（Vintage: Improvements の非公式移植）。
  金属×加工品（棒/ワイヤー/スプリング/板）はキーから合成生成（金属名はパック内の既訳と統一）、機械名・Ponder（世界内ガイド）・JEI・GUI・実績・トリム素材を翻訳。曲げヘッドのASCIIアートは保持。プレースホルダ整合を検証済み（未訳0）。

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

[Unreleased]: https://github.com/11gather11/Gravitas2-JP/compare/v0.18.1...HEAD
[0.18.1]: https://github.com/11gather11/Gravitas2-JP/compare/v0.18.0...v0.18.1
[0.18.0]: https://github.com/11gather11/Gravitas2-JP/compare/v0.17.0...v0.18.0
[0.17.0]: https://github.com/11gather11/Gravitas2-JP/compare/v0.16.1...v0.17.0
[0.16.1]: https://github.com/11gather11/Gravitas2-JP/compare/v0.16.0...v0.16.1
[0.16.0]: https://github.com/11gather11/Gravitas2-JP/compare/v0.15.0...v0.16.0
[0.15.0]: https://github.com/11gather11/Gravitas2-JP/compare/v0.14.0...v0.15.0
[0.14.0]: https://github.com/11gather11/Gravitas2-JP/compare/v0.13.0...v0.14.0
[0.13.0]: https://github.com/11gather11/Gravitas2-JP/compare/v0.12.0...v0.13.0
[0.12.0]: https://github.com/11gather11/Gravitas2-JP/compare/v0.11.0...v0.12.0
[0.11.0]: https://github.com/11gather11/Gravitas2-JP/compare/v0.10.0...v0.11.0
[0.10.0]: https://github.com/11gather11/Gravitas2-JP/compare/v0.9.0...v0.10.0
[0.9.0]: https://github.com/11gather11/Gravitas2-JP/compare/v0.8.0...v0.9.0
[0.8.0]: https://github.com/11gather11/Gravitas2-JP/compare/v0.7.0...v0.8.0
[0.7.0]: https://github.com/11gather11/Gravitas2-JP/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/11gather11/Gravitas2-JP/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/11gather11/Gravitas2-JP/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/11gather11/Gravitas2-JP/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/11gather11/Gravitas2-JP/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/11gather11/Gravitas2-JP/compare/v0.1.2...v0.2.0
[0.1.2]: https://github.com/11gather11/Gravitas2-JP/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/11gather11/Gravitas2-JP/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/11gather11/Gravitas2-JP/releases/tag/v0.1.0
