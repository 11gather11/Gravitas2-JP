#!/usr/bin/env python3
"""Gravitas2-JP リソースパックのビルドスクリプト.

pack/ 以下（pack.mcmeta + assets/）を zip 化してリソースパックを生成する。
- dist/Gravitas2-JP.zip を出力
- INSTANCE_RESOURCEPACKS が存在すれば、そこにもコピー（ゲームですぐ使える）

使い方:
    python build.py            # ビルドしてインスタンスにも配置
    python build.py --no-copy  # dist/ に出力するだけ
"""
import os
import sys
import json
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.join(ROOT, "pack")
DIST = os.path.join(ROOT, "dist")
ZIP_NAME = "Gravitas2-JP.zip"

# ゲーム内で使うインスタンスの resourcepacks フォルダ（環境に合わせて変更可）
INSTANCE_RESOURCEPACKS = (
    r"F:\Games\Minecraft\CurseForge\Instances\All The Mods - Gravitas\resourcepacks"
)


def validate_pack():
    """全 ja_jp.json / patchouli 本 JSON が妥当か検証し、キー総数を返す."""
    import glob

    errors = []
    total_keys = 0
    targets = glob.glob(os.path.join(PACK, "assets", "**", "*.json"), recursive=True)
    targets.append(os.path.join(PACK, "pack.mcmeta"))  # pack.mcmeta も JSON 検証する
    for f in targets:
        try:
            data = json.load(open(f, encoding="utf-8"))
            if f.endswith("ja_jp.json") and isinstance(data, dict):
                total_keys += len(data)
        except Exception as e:  # noqa: BLE001
            errors.append((os.path.relpath(f, ROOT), str(e)))
    if errors:
        for rel, msg in errors:
            print(f"  [JSON ERROR] {rel}: {msg}")
        raise SystemExit("JSON エラーがあるためビルドを中止しました。")
    return total_keys


def build():
    if not os.path.isfile(os.path.join(PACK, "pack.mcmeta")):
        raise SystemExit("pack/pack.mcmeta が見つかりません。")

    total_keys = validate_pack()
    os.makedirs(DIST, exist_ok=True)
    out = os.path.join(DIST, ZIP_NAME)

    # pack/ の中身を zip ルート直下に格納（pack.mcmeta と assets/ がルートに来る）
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for base, _, files in os.walk(PACK):
            for name in files:
                full = os.path.join(base, name)
                arc = os.path.relpath(full, PACK).replace(os.sep, "/")
                z.write(full, arc)

    size = os.path.getsize(out)
    print(f"ビルド完了: {out}")
    print(f"  サイズ: {size:,} バイト / lang キー総数: {total_keys:,}")
    return out


def copy_to_instance(zip_path):
    if not os.path.isdir(INSTANCE_RESOURCEPACKS):
        print(f"  （インスタンスの resourcepacks が見つからないためコピーはスキップ: {INSTANCE_RESOURCEPACKS}）")
        return
    import shutil

    dest = os.path.join(INSTANCE_RESOURCEPACKS, ZIP_NAME)
    shutil.copy(zip_path, dest)
    print(f"  インスタンスへ配置: {dest}")


if __name__ == "__main__":
    z = build()
    if "--no-copy" not in sys.argv:
        copy_to_instance(z)
