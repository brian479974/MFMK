#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mfmk.markforged.tw：從繁中母版 index.html 產出簡中／英文版 + 三語切換列。

設計：
  · **母版可手改**：Brian 改 index.html 的繁中內容，重跑本檔即可同步三語。
  · 簡中不另寫一份：`cn_localize.localize()`（先換大陸用語再轉字形）＋ i18n.CN_OVERRIDE 少數人工定值。
  · 英文用 i18n.EN 對照表逐字串替換。

閘門（任一 fail 就不產出）：
  G1 對照覆蓋：EN 表中每個 key 都要在母版找得到（找不到＝母版改過、對照表過期）
  G2 中文殘留：英文版正文不得有 CJK（語言切換列與品牌字除外）
  G3 簡繁／台灣用語：簡中版 OpenCC t2s 回驗零差異，且不含台灣用語黑名單
  G4 結構同形：三版的標籤數、圖片數、連結數一致
  G5 資源存在：三版引用的圖片都在
  G6 切換列：三版都有，且互指的檔案都存在
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = HERE.parent
sys.path.insert(0, str(HERE))
# 沿用新聞站那支簡中在地化模組（同一套用語表，不重造）
NEWS_BUILD = (Path.home() / "Library/Mobile Documents/iCloud~md~obsidian/Documents"
              / "MF-GCR/84_Media-PR/Vietnam-Defense-2026-09/web-新聞稿/_build")
sys.path.insert(0, str(NEWS_BUILD))

from cn_localize import localize, TW_ONLY, _T2S  # noqa: E402
import i18n  # noqa: E402

MASTER = SITE / "index.html"


def inject_common(html, lang):
    """語言屬性、og:locale、hreflang、切換列與其樣式。"""
    html = re.sub(r'<html lang="[^"]*"', f'<html lang="{i18n.LANG_ATTR[lang]}"', html, count=1)
    html = re.sub(r'(<meta property="og:locale" content=")[^"]*(")',
                  rf'\g<1>{i18n.OG_LOCALE[lang]}\g<2>', html, count=1)

    # hreflang（先移除舊的再加，重跑不會疊加）
    html = re.sub(r'\s*<link rel="alternate" hreflang="[^"]*" href="[^"]*"\s*/?>', "", html)
    alts = "".join(
        f'\n  <link rel="alternate" hreflang="{i18n.LANG_ATTR[L]}" '
        f'href="https://mfmk.markforged.tw/{i18n.FILES[L]}">'
        for L in ("tw", "cn", "en"))
    html = html.replace("</head>", f"{alts}\n</head>", 1)

    # 切換列樣式（重跑先清舊的）
    html = re.sub(r"\s*/\* langbar \*/.*?/\* end langbar \*/", "", html, flags=re.S)
    html = html.replace("</style>", f"/* langbar */{i18n.SWITCHER_CSS}/* end langbar */\n</style>", 1)

    # 切換列本體：放進 <nav> 內、CTA 之前。
    # ⚠️ 不能放在 <nav> 外面：nav 是 position:sticky，外面多一條 bar 會把 hero 推位、
    #    捲動時 nav 蓋住封面標題（2026-09-07 截圖實際看到）。放進 nav 內零版位變動。
    html = re.sub(r'<div class="langbar">.*?</div>\s*', "", html, flags=re.S)
    html = html.replace('<a href="#register" class="nav-cta">',
                        i18n.SWITCHER[lang] + '<a href="#register" class="nav-cta">', 1)
    return html


def build(lang):
    src = MASTER.read_text(encoding="utf-8")
    if lang == "tw":
        out = src
    elif lang == "en":
        out = src
        # ⚠️ 一定要長字串優先：短 key（如「列印流程」「自動校準」）會先命中被包在長句裡的片段，
        # 造成「安全、辦公室友好的金屬How it runs。」這種半中半英殘句（2026-09-07 實際踩過）。
        for tw in sorted(i18n.EN, key=len, reverse=True):
            out = out.replace(tw, i18n.EN[tw])
    else:  # cn
        out = src
        # 長字串先換（避免短字串先命中造成殘句）
        for tw in sorted(set(list(i18n.EN.keys()) + list(i18n.CN_OVERRIDE.keys())), key=len, reverse=True):
            cn = i18n.CN_OVERRIDE.get(tw) or localize(tw)
            out = out.replace(tw, cn)
        # 母版中未列入對照表的其餘中文（按鈕、零星文案）一律走 localize
        out = localize(out) if False else out  # 不整檔轉：避免動到 URL 與程式碼
    return inject_common(out, lang)


def gates(pages):
    print("\n── 閘門 ──")
    src = MASTER.read_text(encoding="utf-8")

    missing = [k for k in i18n.EN if k not in src]
    if missing:
        sys.exit("✗ G1 對照覆蓋：母版找不到這些字串（對照表過期）：\n   " + "\n   ".join(m[:60] for m in missing))
    print(f"  ✅ G1 對照覆蓋：{len(i18n.EN)} 條對照全部在母版命中")

    def visible(h):
        h = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", h, flags=re.S)
        h = re.sub(r'<div class="langbar">.*?</div>', " ", h, flags=re.S)   # 切換列本就多語
        h = re.sub(r"<[^>]+>", " ", h)
        return re.sub(r"\s+", " ", h)

    cjk = re.findall(r"[一-鿿]", visible(pages["en"]))
    if cjk:
        sys.exit(f"✗ G2 英文純度：英文版正文殘留 {len(cjk)} 個中文字：{''.join(sorted(set(cjk))[:30])}")
    print("  ✅ G2 英文純度：英文版正文零中文殘留")

    cn_body = visible(pages["cn"])
    if _T2S.convert(cn_body) != cn_body:
        diff = sorted({a for a, b in zip(cn_body, _T2S.convert(cn_body)) if a != b})
        sys.exit("✗ G3 簡繁：簡中版殘留繁體字 " + "".join(diff)[:40])
    hit = [w for w in TW_ONLY if w in cn_body]
    if hit:
        sys.exit("✗ G3 台灣用語：簡中版殘留 " + "、".join(hit))
    print("  ✅ G3 簡繁／台灣用語：簡中版零殘留")

    shape = {L: (p.count("<div"), p.count("<img"), p.count("<a ")) for L, p in pages.items()}
    if len(set(shape.values())) != 1:
        sys.exit(f"✗ G4 結構同形：{shape}")
    print(f"  ✅ G4 結構同形：div/img/a = {shape['tw']}（三版一致）")

    for L, p in pages.items():
        for m in re.findall(r'src="((?!http|data:)[^"]+)"', p):
            if not (SITE / m).exists():
                sys.exit(f"✗ G5 資源缺：{i18n.FILES[L]} 參照 {m}")
    print("  ✅ G5 資源：三版引用的圖片全部存在")

    for L, p in pages.items():
        if 'class="langbar"' not in p:
            sys.exit(f"✗ G6 切換列：{i18n.FILES[L]} 沒有切換列")
        for target in i18n.FILES.values():
            if f'href="{target}"' not in p:
                sys.exit(f"✗ G6 切換列：{i18n.FILES[L]} 少了指向 {target} 的連結")
    print("  ✅ G6 切換列：三版都在，且互指的三個檔都存在")
    print("\n✅ 六道閘全綠")


def main():
    pages = {L: build(L) for L in ("tw", "cn", "en")}
    gates(pages)
    for L, html in pages.items():
        (SITE / i18n.FILES[L]).write_text(html, encoding="utf-8")
        print(f"✓ {i18n.FILES[L]}  {len(html)//1024} KB")
    print("\n（母版 index.html 已就地加上切換列與 hreflang；改繁中內容後重跑本檔即可同步三語）")


if __name__ == "__main__":
    main()
