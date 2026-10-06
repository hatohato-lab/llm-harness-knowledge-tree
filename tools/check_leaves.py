# 知識の木の葉を、決まった形でそろっているか機械で採点する（2026-10-04、評価して直すループの採点役）。
# 使い方: python check_leaves.py [枝のフォルダ名 ...]  （省略すると6つの枝すべて）
# 結果は同じフォルダの 結果_YYYYMMDD_HHMM.json に保存し、画面には合格率と不合格の多い項目を出す。
import json
import re
import sys
from datetime import datetime
from pathlib import Path

TREE = Path(__file__).resolve().parent.parent
BRANCHES = ["01_原理", "02_扱い方", "03_文脈と記憶", "04_工程", "05_評価と改善", "06_失敗と安全"]
SECTIONS = ["要点", "仕組み", "使い方", "試し方", "出典", "試した記録", "関連"]
LEVELS = ["本体と公式で確認", "公式で確認", "論文で確認", "元の出典で確認", "体験談だけ", "誤りの疑い", "未確認"]


def is_leaf(p: Path) -> bool:
    if p.suffix != ".md" or p.name.startswith(("00_", "_")):
        return False
    return not any(part.startswith("_") for part in p.relative_to(TREE).parts[:-1])


def sections(text: str) -> dict:
    out, cur = {}, None
    for line in text.splitlines():
        m = re.match(r"^##\s+(\d+)\.\s*(.+)$", line)
        if m:
            cur = m.group(2)
            out[cur] = []
        elif cur:
            out[cur].append(line)
    return {k: "\n".join(v) for k, v in out.items()}


def find(secs: dict, name: str) -> str | None:
    for k, v in secs.items():
        if k.startswith(name):
            return v
    return None


def check(p: Path) -> list[str]:
    t = p.read_text(encoding="utf-8", errors="replace")
    fails = []
    h1 = re.search(r"^#\s+(.+)$", t, re.M)
    if not h1 or h1.group(1).strip() != p.stem:
        fails.append("1行目の見出しがファイル名と違う")
    if "## 目次" not in t:
        fails.append("目次が無い")
    secs = sections(t)
    for s in SECTIONS:
        if find(secs, s) is None:
            fails.append(f"節「{s}」が無い")
    heads = [k for k in secs]
    if heads and not all("（" in k and "）" in k for k in heads):
        fails.append("見出しが「概念（説明）」の形でない")
    youten = find(secs, "要点") or ""
    if not any(lv in youten for lv in LEVELS):
        fails.append("要点に根拠の段階が無い")
    # 使いどころは「使いどころ」の語か、モデルの種類・指示の細かさ・向く作業の3つがそろっていれば合格（10/4 23:13 の見本で調整）
    has_label = "使いどころ" in youten
    has_three = bool(re.search(r"賢い|軽い|モデル", youten)) and bool(re.search(r"抽象|具体", youten)) and bool(re.search(r"向く|向き|使う|作業", youten))
    if not (has_label or has_three):
        fails.append("要点に使いどころが無い")
    shikumi = find(secs, "仕組み") or ""
    if len(shikumi.strip()) < 80:
        fails.append("仕組みが短すぎる（80字未満）")
    tameshi = find(secs, "試し方") or ""
    if not re.search(r"測|数え|比べ|確かめ", tameshi):
        fails.append("試し方に測り方が無い")
    shutten = find(secs, "出典") or ""
    if not re.search(r"https?://", shutten):
        fails.append("出典に URL が無い")
    kanren = find(secs, "関連") or ""
    if not re.search(r"\]\([^)]+\.md\)", kanren):
        fails.append("関連にほかの葉へのリンクが無い")
    quotes = [ln for ln in t.splitlines() if ln.startswith(">")]
    if len(quotes) > 6:
        fails.append("引用が長すぎる（7行以上）")
    return fails


def main() -> int:
    targets = sys.argv[1:] or BRANCHES
    leaves = [p for b in targets for p in sorted((TREE / b).rglob("*.md")) if is_leaf(p)]
    result = {str(p.relative_to(TREE)): check(p) for p in leaves}
    passed = sum(1 for v in result.values() if not v)
    counts: dict[str, int] = {}
    for v in result.values():
        for f in v:
            counts[f] = counts.get(f, 0) + 1
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = Path(__file__).resolve().parent / f"結果_{stamp}.json"
    out.write_text(json.dumps({"targets": targets, "leaves": len(leaves), "passed": passed, "fail_counts": counts, "detail": result}, ensure_ascii=False, indent=2), encoding="utf-8")
    rate = passed / len(leaves) * 100 if leaves else 0
    print(f"葉 {len(leaves)}枚、合格 {passed}枚（{rate:.0f}%）")
    for k, v in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"  {v:>4}枚  {k}")
    print(f"結果のファイル {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
