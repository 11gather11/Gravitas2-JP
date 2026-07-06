#!/usr/bin/env python3
"""モッドパック内の各 Mod の日本語化状況を走査して一覧表示する.

判定:
  done_RP     … このリポジトリの pack/ で翻訳済み
  done_kubejs … パック側 kubejs/assets で ja_jp 提供
  done_jar    … Mod jar が ja_jp を同梱（かつ十分に網羅）
  partial_jar … Mod jar が ja_jp を同梱するが不完全（欠落や英語のまま多数）
  TODO        … 未翻訳（en_us はあるが ja_jp が無い）

使い方:
    python tools/scan_status.py <インスタンスのパス>
    # 例: python tools/scan_status.py "F:/Games/Minecraft/CurseForge/Instances/All The Mods - Gravitas"
"""
import zipfile, json, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 同梱翻訳が %s テンプレ方式で実質網羅されるため不完全判定から除外する Mod
TEMPLATE_MODS = {"everycomp"}


def ns_of(path):
    """assets/<ns>/lang/... のパスから名前空間を取り出す."""
    return path.replace(os.sep, "/").split("/assets/")[1].split("/")[0]


def jar_coverage(z, ns):
    """Mod同梱 ja_jp の翻訳網羅度を測る.

    Returns:
        (missing, same, total): en_us にあって ja_jp に無いキー数、
        ja_jp が英語のままのキー数（値が en と同一かつ英字を含む）、
        en_us の実キー数（``_`` 始まりの内部キーを除く）。
    """
    try:
        en = json.loads(z.read(f"assets/{ns}/lang/en_us.json").decode("utf-8"))
        ja = json.loads(z.read(f"assets/{ns}/lang/ja_jp.json").decode("utf-8"))
    except Exception:
        return (0, 0, 0)
    en = {k: v for k, v in en.items() if not k.startswith("_")}
    missing = sum(1 for k in en if k not in ja)
    same = sum(1 for k, v in en.items()
               if k in ja and str(ja[k]) == str(v) and any(c.isalpha() for c in str(v)))
    return (missing, same, len(en))


def is_partial(missing, same, total):
    """同梱 ja が不完全かを判定する（欠落15件以上、またはカバレッジ85%未満）."""
    if total == 0:
        return False
    coverage = (total - missing - same) / total
    return missing >= 15 or coverage < 0.85


def main(instance):
    if not os.path.isdir(os.path.join(instance, "mods")):
        raise SystemExit(f"mods フォルダが見つかりません: {instance}")

    # このリポジトリで翻訳済みの名前空間
    pack_ns = {ns_of(f) for f in glob.glob(f"{REPO}/pack/assets/*/lang/ja_jp.json")}
    # パック側 kubejs が提供する名前空間
    kubejs_ns = {ns_of(f) for f in glob.glob(f"{instance}/kubejs/assets/*/lang/ja_jp.json")}

    # 名前空間ごとに en_us キー数が最大の jar を採用する
    best = {}  # ns -> (cnt, jar_path)
    for jar in sorted(glob.glob(f"{instance}/mods/*.jar")):
        try:
            z = zipfile.ZipFile(jar)
        except Exception:
            continue
        for n in z.namelist():
            m = re.match(r"assets/([^/]+)/lang/en_us\.json$", n)
            if not m:
                continue
            ns = m.group(1)
            try:
                cnt = len(json.loads(z.read(n).decode("utf-8")))
            except Exception:
                cnt = 0
            if ns not in best or cnt > best[ns][0]:
                best[ns] = (cnt, jar)

    rows = []  # (cnt, ns, state, jar_basename, missing, same)
    for ns, (cnt, jar) in best.items():
        b = os.path.basename(jar)
        names = zipfile.ZipFile(jar).namelist()
        missing = same = 0
        if ns in pack_ns:
            st = "done_RP"
        elif ns in kubejs_ns:
            st = "done_kubejs"
        elif f"assets/{ns}/lang/ja_jp.json" in names:
            missing, same, total = jar_coverage(zipfile.ZipFile(jar), ns)
            st = "partial_jar" if (ns not in TEMPLATE_MODS and is_partial(missing, same, total)) else "done_jar"
        else:
            st = "TODO"
        rows.append((cnt, ns, st, b, missing, same))

    todo = sorted([r for r in rows if r[2] == "TODO" and r[0] > 0], reverse=True)
    print(f"=== 未翻訳 (TODO): {len(todo)} 名前空間 / {sum(r[0] for r in todo):,} キー ===")
    print(f"{'keys':>6}  {'namespace':<28} jar")
    for cnt, ns, st, b, mi, sa in todo:
        print(f"{cnt:>6}  {ns:<28} {b}")

    partial = sorted([r for r in rows if r[2] == "partial_jar"], key=lambda r: -(r[4] + r[5]))
    print(f"\n=== 同梱翻訳が不完全 (partial_jar): {len(partial)} 名前空間 ===")
    print(f"{'欠落':>6} {'英語':>6}  {'namespace':<28} jar")
    for cnt, ns, st, b, mi, sa in partial:
        print(f"{mi:>6} {sa:>6}  {ns:<28} {b}")

    done = sorted([r for r in rows if r[2] in ("done_RP", "done_kubejs", "done_jar")], reverse=True)
    print(f"\n=== 翻訳済み: {len(done)} 名前空間 ===")
    for cnt, ns, st, b, mi, sa in done:
        print(f"{cnt:>6}  {ns:<28} {st}")

    print(f"\n総 jar: {len(glob.glob(f'{instance}/mods/*.jar'))}  en_us 保有: {len(rows)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("使い方: python tools/scan_status.py <インスタンスのパス>")
    main(sys.argv[1])
