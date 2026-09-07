# -*- coding: utf-8 -*-
"""mfmk.markforged.tw 三語內容源（繁中為母版，英文在此，簡中由 cn_localize 衍生）。

原則：繁中母版 index.html 保持可手改；本檔只放「繁中 → 英文」對照，
簡中不另寫一份（先換大陸用語再轉字形），再由 build_i18n.py 的閘門回頭驗。
"""

# 繁中（母版字串，必須與 index.html 完全一致）→ 英文
EN = {
    # ── head / meta
    "AI實體化製造新紀元 | Markforged FX10 大中華區 VIP 體驗日":
        "Making AI Physical | Markforged FX10 Greater China VIP Experience Day",
    "Markforged FX10 大中華區 VIP 專屬體驗日。全球首台工業級金屬複合材料 3D 列印機，一對一客製化展示，預約制。立即申請，感受 AI 實體化製造新紀元。":
        "The Markforged FX10 Greater China VIP Experience Day. The first industrial printer to run both metal and continuous-fibre composites, shown one to one by appointment. Apply now.",
    "Markforged,Markforged 大中華區,Markforged GCR,Markforged China,Markforged Hong Kong,Markforged Vietnam,Markforged ":
        "Markforged,Markforged Greater China,Markforged GCR,Markforged China,Markforged Hong Kong,Markforged Vietnam,Markforged ",
    "全球首台工業級金屬複合材料 3D 列印機 FX10，大中華區一對一 VIP 體驗日。預約制，由 Markforged 原廠工程師親自展示。":
        "The FX10, the first industrial printer for both metal and continuous-fibre composites. A one-to-one VIP experience day across Greater China, by appointment, demonstrated by Markforged engineers.",
    "全球首台工業級金屬複合材料 3D 列印機，大中華區 VIP 專屬體驗日。預約制，一對一展示。":
        "The first industrial printer for both metal and continuous-fibre composites. A VIP experience day across Greater China, by appointment, one to one.",
    # ── nav / hero
    "💎 VIP 預約制": "💎 By appointment",
    "申請體驗名額": "Request a place",
    "🌏 大中華區 · 一對一 VIP 專屬展示": "🌏 Greater China · one-to-one VIP demonstration",
    "AI實體化": "Making AI",
    "製造新紀元": "Physical",
    "Markforged FX10 大中華區體驗日": "Markforged FX10 Greater China Experience Day",
    "全球首台工業級金屬複合材料 3D 列印機，\n      大中華區 VIP 專屬展示，\n      由 Markforged 原廠工程師針對您的需求客製化演示。":
        "The first industrial printer to run both metal and continuous-fibre composites.\n      A VIP demonstration across Greater China,\n      tailored to your parts by Markforged engineers.",
    "台灣 · 中國 · 香港 · 越南": "Taiwan · China · Hong Kong · Vietnam",
    "時間彈性預約": "Flexible scheduling",
    "原廠工程師一對一": "One to one with our engineers",
    "免費參加": "No charge",
    "立即申請 VIP 體驗名額 →": "Request your VIP place →",
    # ── product
    "全球首台金屬複合材料工業列印機": "The first industrial printer for metal and composites",
    "最大列印尺寸（寬）": "Maximum print size (width)",
    "複合材料 + 金屬 一機雙用": "Composite and metal on one machine",
    "一對一客製化展示，名額有限": "One-to-one demonstration, limited places",
    "★ 主打產品": "★ Featured",
    "主打產品": "Featured",
    "FX10 是 Markforged 革命性的里程碑 — 全球首台同時具備複合材料與金屬列印能力的工業機。\n        模組化設計讓您輕鬆切換材料，自動校準讓人人都能操作，無需專職技術人員。":
        "The FX10 is the first industrial machine to carry both continuous-fibre composite and metal printing.\n        A modular design lets you switch material, and automatic calibration means no dedicated operator is required.",
    "列印尺寸": "Build volume",
    "列印技術": "Process",
    "FFF + 連續碳纖維": "FFF with continuous carbon fibre",
    "層厚精度": "Layer height",
    "材料支援": "Materials",
    "金屬 + 複合材料": "Metal and composite",
    "自動校準": "Calibration",
    "光學感測器驗證": "Verified by optical sensor",
    "管理軟體": "Software",
    "Eiger™ 雲端平台": "Eiger™ platform",
    "預約親眼看這台機器 →": "Book a time to see it →",
    # ── pain points
    "為什麼選 FX10": "Why the FX10",
    "您的製造痛點，": "The problems on your floor,",
    "FX10 一次解決": "answered by one machine",
    "不再依賴外包，不再等待漫長交期，不再為小批量零件頭痛。":
        "No more waiting on an outside shop, no more multi-week lead times, no more pain over low-volume parts.",
    "大幅縮短交期": "Lead time cut",
    "從設計到成品最快當天完成。告別傳統外包 4～8 週等待，即時響應生產與維修需求。":
        "From design to finished part in as little as a day, against the four to eight weeks an outside shop takes.",
    "降低模具與庫存成本": "Lower tooling and inventory cost",
    "小批量、多樣化零件無需開模。按需生產，大幅減少庫存壓力與高昂模具費用。":
        "Low-volume and varied parts need no tooling. Produce on demand and hold less stock.",
    "金屬 × 複合材料一機雙用": "Metal and composite on one machine",
    "全球唯一可切換金屬與複合材料列印的工業機。一台 FX10，兩種材料，無限可能。":
        "The only industrial machine that switches between metal and continuous-fibre composite. One machine, two material routes.",
    "工廠級可靠度": "Built for the factory floor",
    "精密鋁製平台，光學感測器自動驗證尺寸精度，自動校準，無需專職操作員。":
        "A precision aluminium bed, dimensional accuracy verified by optical sensor, and automatic calibration; no dedicated operator needed.",
    "Eiger 雲端管理": "Managed in Eiger",
    "從任何地點遠端監控、管理、下單列印。Eiger 讓多地工廠統一管理成為可能。":
        "Monitor, manage and queue prints from anywhere. Eiger lets several sites run under one system.",
    "快速 ROI": "Fast payback",
    "以治具、夾具、備品自製為起點，快速回收投資，並逐步擴展到終端零件生產。":
        "Start with jigs, fixtures and spares made in house, recover the investment, then extend into end-use parts.",
    # ── process
    "列印流程": "How it runs",
    "從設計到成品，就這麼簡單": "From design to finished part",
    "複合材料列印": "Composite printing",
    "設計 → 強化 → 列印 → 使用": "Design → reinforce → print → use",
    "連續碳纖維強化技術，讓列印件強度媲美金屬。4 個步驟，當天完成。":
        "Continuous carbon fibre brings printed parts close to metal in strength. Four steps, finished the same day.",
    "金屬列印": "Metal printing",
    "設計 → 列印 → 清洗 → 燒結 → 使用": "Design → print → wash → sinter → use",
    "安全、辦公室友好的金屬列印流程。無需傳統加工設備，直接產出高強度金屬零件。":
        "A metal process safe enough for an office environment, with no conventional machining required.",
    # ── value band
    "貴": "Price",
    "從來不是": "was never",
    "好產品的缺點": "the problem",
    "FX10 + Metal Kit 讓您省下的每一筆外包費、每一天等待的交期損失，\n      都是真實的競爭優勢。來現場親眼見證。":
        "Every outsourced job you stop paying for, and every day of waiting you remove,\n      is competitive ground you keep. Come and see it in person.",
    "預約 VIP 體驗 →": "Book the VIP session →",
    # ── line-up
    "Markforged 產品線": "The product line",
    "適合每個階段的解決方案": "A machine for each stage",
    "★ 今日主角": "★ On show",
    "全球首台金屬複合材料工業列印機。複合材料 + 金屬一機雙用，工廠首選。":
        "The first industrial printer for both metal and composite, on one machine.",
    "大尺寸旗艦": "Large format",
    "超大列印空間，專為大型工業零件設計。高強度連續碳纖維，媲美鋁合金強度。":
        "A large build volume for big industrial parts, with continuous carbon fibre for strength close to aluminium.",
    "金屬黏結劑噴射": "Metal binder jetting",
    "Digital Metal® 下一代金屬黏結劑噴射技術。高精度、高可靠性，專為高量金屬零件生產設計。":
        "Digital Metal® binder jetting for higher-volume metal production, with high accuracy and repeatability.",
    # ── experience flow
    "體驗流程": "What the day looks like",
    "您的專屬": "Your own",
    "VIP 體驗日": "VIP experience day",
    "填寫申請表": "Send the form",
    "提供您的需求資訊，讓我們為您量身準備最相關的展示內容。":
        "Tell us what you make, so the demonstration is prepared around your parts.",
    "Markforged 大中華區審核確認": "We confirm",
    "我們在 3 個工作日內與您聯繫，確認專屬體驗時間與地點。":
        "We come back to you within three working days with a time and a place.",
    "一對一 VIP 展示": "One-to-one demonstration",
    "原廠工程師針對您的產業與痛點，客製化展示實際應用場景。":
        "Markforged engineers work through the applications that matter in your industry.",
    "親手觸碰真實成品": "Handle the parts",
    "現場感受金屬零件與複合材料成品，比較傳統製程的差異。":
        "Pick up metal and composite parts and compare them against conventionally made ones.",
    "量身規劃導入方案": "A plan built for you",
    "依您需求提供客製化建議與報價，零壓力，完全依您步調。":
        "A recommendation and quotation shaped to your requirement, at your pace.",
    "彈性預約，由您決定時間": "Scheduled around you",
    # ── contact / form / footer
    "聯絡我們": "Contact",
    "掃描加入 Markforged 官方 LINE": "Add Markforged on LINE",
    "掃描下方 QR Code 加入 Markforged 官方 LINE，": "Scan the QR code below to add Markforged on LINE,",
    "即時獲得產品資訊、技術支援與最新活動通知。": "for product information, technical support and event notices.",
    "申請 VIP 體驗名額": "Request a VIP place",
    "點擊下方按鈕填寫申請表，Markforged 將在 3 個工作日內與您聯繫確認。":
        "Fill in the form below and we will come back to you within three working days.",
    "填寫您的基本資料及需求，我們的原廠工程師將為您安排專屬一對一展示。":
        "Give us your details and requirement, and our engineers will arrange a one-to-one session.",
    "名額有限，歡迎盡早申請。": "Places are limited.",
    "📋 立即填寫 VIP 申請表": "📋 Open the VIP application form",
    "點擊後將開啟申請表單": "The form opens in a new tab",
    "官網": "Website",
    "申請體驗": "Apply",
    # ── image alt
    "Markforged FX10 工業級 3D 列印機": "The Markforged FX10 industrial 3D printer",
    "Markforged 複合材料列印流程": "The Markforged composite printing process",
    "Markforged 金屬列印流程": "The Markforged metal printing process",
    "Markforged FX10 等角視圖": "The Markforged FX10, isometric view",
}

# 簡中：只列 cn_localize 換不掉、且行銷語感需要人工定的少數幾條
CN_OVERRIDE = {
    "您的製造痛點，": "您的制造痛点，",
    "貴": "贵",
    "從來不是": "从来不是",
    "好產品的缺點": "好产品的缺点",
}

# 語言切換列（三語共用結構，文字各自語言）
SWITCHER = {
    "tw": ('<div class="langbar"><span>語言</span>'
           '<a href="index.html" class="on">繁體中文</a>'
           '<a href="index-sc.html">简体中文</a>'
           '<a href="index-en.html">English</a></div>'),
    "cn": ('<div class="langbar"><span>语言</span>'
           '<a href="index.html">繁體中文</a>'
           '<a href="index-sc.html" class="on">简体中文</a>'
           '<a href="index-en.html">English</a></div>'),
    "en": ('<div class="langbar"><span>Language</span>'
           '<a href="index.html">繁體中文</a>'
           '<a href="index-sc.html">简体中文</a>'
           '<a href="index-en.html" class="on">English</a></div>'),
}

SWITCHER_CSS = """
  .langbar{display:flex;gap:6px;align-items:center;margin-left:auto;margin-right:14px}
  .langbar span{display:none}
  .langbar a{color:#9a9a9a;text-decoration:none;font-size:11.5px;font-weight:700;
    padding:4px 10px;border:1px solid #2e2e2e;border-radius:20px;white-space:nowrap;line-height:1}
  .langbar a:hover{color:#FFC500;border-color:#FFC500}
  .langbar a.on{background:#FFC500;color:#000;border-color:#FFC500}
  @media(max-width:600px){.langbar{margin-right:8px;gap:4px}.langbar a{padding:3px 7px;font-size:10.5px}}
"""

LANG_ATTR = {"tw": "zh-TW", "cn": "zh-CN", "en": "en"}
OG_LOCALE = {"tw": "zh_TW", "cn": "zh_CN", "en": "en_US"}
FILES = {"tw": "index.html", "cn": "index-sc.html", "en": "index-en.html"}
