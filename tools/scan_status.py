#!/usr/bin/env python3
"""モッドパック内の各 Mod の日本語化状況を走査して一覧表示する.

判定:
  done_RP     … このリポジトリの pack/ で翻訳済み
  done_kubejs … パック側 kubejs/assets で ja_jp 提供
  done_jar    … Mod jar が ja_jp を同梱
  TODO        … 未翻訳（en_us はあるが ja_jp が無い）

使い方:
    python tools/scan_status.py <インスタンスのパス>
    # 例: python tools/scan_status.py "F:/Games/Minecraft/CurseForge/Instances/All The Mods - Gravitas"
"""
import zipfile, json, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def ns_of(path):
    """assets/<ns>/lang/... のパスから名前空間を取り出す."""
    return path.replace(os.sep, "/").split("/assets/")[1].split("/")[0]


def main(instance):
    if not os.path.isdir(os.path.join(instance, "mods")):
        raise SystemExit(f"mods フォルダが見つかりません: {instance}")

    # このリポジトリで翻訳済みの名前空間
    pack_ns = {ns_of(f) for f in glob.glob(f"{REPO}/pack/assets/*/lang/ja_jp.json")}
    # パック側 kubejs が提供する名前空間
    kubejs_ns = {ns_of(f) for f in glob.glob(f"{instance}/kubejs/assets/*/lang/ja_jp.json")}

    rows = []
    for jar in sorted(glob.glob(f"{instance}/mods/*.jar")):
        b = os.path.basename(jar)
        try:
            z = zipfile.ZipFile(jar)
        except Exception:
            continue
        names = z.namelist()
        for n in names:
            m = re.match(r"assets/([^/]+)/lang/en_us\.json$", n)
            if not m:
                continue
            ns = m.group(1)
            try:
                cnt = len(json.loads(z.read(n).decode("utf-8")))
            except Exception:
                cnt = 0
            if ns in pack_ns:
                st = "done_RP"
            elif ns in kubejs_ns:
                st = "done_kubejs"
            elif f"assets/{ns}/lang/ja_jp.json" in names:
                st = "done_jar"
            else:
                st = "TODO"
            rows.append((cnt, ns, st, b))

    todo = sorted([r for r in rows if r[2] == "TODO" and r[0] > 0], reverse=True)
    print(f"=== 未翻訳 (TODO): {len(todo)} 名前空間 / {sum(r[0] for r in todo):,} キー ===")
    print(f"{'keys':>6}  {'namespace':<28} jar")
    for cnt, ns, st, b in todo:
        print(f"{cnt:>6}  {ns:<28} {b}")

    done = sorted([r for r in rows if r[2] != "TODO"], reverse=True)
    print(f"\n=== 翻訳済み: {len(done)} 名前空間 ===")
    for cnt, ns, st, b in done:
        print(f"{cnt:>6}  {ns:<28} {st}")

    print(f"\n総 jar: {len(glob.glob(f'{instance}/mods/*.jar'))}  en_us 保有: {len(rows)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("使い方: python tools/scan_status.py <インスタンスのパス>")
    main(sys.argv[1])
