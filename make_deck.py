from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

INK   = RGBColor(0x0F, 0x17, 0x2A)
TEAL  = RGBColor(0x0D, 0x94, 0x88)
DTEAL = RGBColor(0x0F, 0x76, 0x6E)
MUTED = RGBColor(0x64, 0x74, 0x8B)
LIGHT = RGBColor(0xF4, 0xF6, 0xF8)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
ACCENT2 = RGBColor(0x25, 0x63, 0xEB)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
SW, SH = prs.slide_width, prs.slide_height

def slide():
    return prs.slides.add_slide(BLANK)

def box(s, x, y, w, h, fill=None, line=None, radius=True):
    from pptx.enum.shapes import MSO_SHAPE
    shp = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE, x, y, w, h)
    if radius:
        try: shp.adjustments[0] = 0.06
        except Exception: pass
    if fill is None:
        shp.fill.background()
    else:
        shp.fill.solid(); shp.fill.fore_color.rgb = fill
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line; shp.line.width = Pt(1)
    shp.shadow.inherit = False
    return shp

def txt(s, x, y, w, h, text, size=18, bold=False, color=INK, align=PP_ALIGN.LEFT, font="Calibri", anchor=MSO_ANCHOR.TOP, spacing=1.0):
    tb = s.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    lines = text.split("\n")
    for i, ln in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = ln
        p.alignment = align
        p.line_spacing = spacing
        for r in p.runs:
            r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color; r.font.name = font
    return tb

def bullets(s, x, y, w, h, items, size=17, color=INK, gap=8, marker="\u25B8  "):
    tb = s.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame; tf.word_wrap = True
    for i, it in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = marker + it
        p.space_after = Pt(gap)
        for r in p.runs:
            r.font.size = Pt(size); r.font.color.rgb = color; r.font.name = "Calibri"
    return tb

def header(s, kicker, title):
    box(s, 0, 0, SW, Inches(1.55), fill=INK, radius=False)
    txt(s, Inches(0.6), Inches(0.22), Inches(11), Inches(0.35), kicker, size=12, bold=True, color=RGBColor(0x5E,0xEA,0xD4))
    txt(s, Inches(0.6), Inches(0.52), Inches(12.1), Inches(0.9), title, size=30, bold=True, color=WHITE)

# ---------------- SLIDE 1 : TITLE ----------------
s = slide()
box(s, 0, 0, SW, SH, fill=INK, radius=False)
box(s, 0, SH - Inches(0.9), SW, Inches(0.9), fill=DTEAL, radius=False)
# decorative circles
for cx, cy, r, c in [(11.6, 0.7, 2.2, RGBColor(0x14,0x3C,0x3A)), (12.4, 1.6, 1.1, RGBColor(0x1A,0x4A,0x47))]:
    from pptx.enum.shapes import MSO_SHAPE
    o = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(cx), Inches(cy), Inches(r), Inches(r))
    o.fill.solid(); o.fill.fore_color.rgb = c; o.line.fill.background(); o.shadow.inherit = False
b = box(s, Inches(0.9), Inches(1.15), Inches(1.1), Inches(1.1), fill=WHITE)
txt(s, Inches(0.9), Inches(1.32), Inches(1.1), Inches(0.8), "S", size=48, bold=True, color=DTEAL, align=PP_ALIGN.CENTER)
txt(s, Inches(0.9), Inches(2.6), Inches(11.5), Inches(1.0), "SarafAI", size=54, bold=True, color=WHITE)
txt(s, Inches(0.9), Inches(3.55), Inches(11.5), Inches(0.9), "Alternate Credit Scoring & Cash-Flow Intelligence for MSMEs", size=22, color=RGBColor(0x99,0xF6,0xE4))
txt(s, Inches(0.9), Inches(4.35), Inches(11.5), Inches(0.6), "Turning khata ledgers, paper receipts and wallet histories into bankable credit scores", size=15, color=RGBColor(0xC2,0xC8,0xD4))
txt(s, Inches(0.9), Inches(6.75), Inches(11.5), Inches(0.5), "Bano Qabil \u00D7 Alibaba Cloud AI Hackathon 2026  \u2022  Finance Track  \u2022  Team SarafAI", size=13, bold=True, color=WHITE)

# ---------------- SLIDE 2 : PROBLEM ----------------
s = slide()
header(s, "THE PROBLEM", "70% of Pakistan's economy is invisible to banks")
b = box(s, Inches(0.6), Inches(2.0), Inches(5.9), Inches(4.6), fill=LIGHT)
txt(s, Inches(0.95), Inches(2.3), Inches(5.3), Inches(0.5), "Kiryana merchants have no credit identity", size=19, bold=True, color=DTEAL)
bullets(s, Inches(0.95), Inches(2.95), Inches(5.3), Inches(3.4), [
    "No bank statements, salary slips or collateral",
    "Handwritten khata + paper receipts = unusable data",
    "Banks cannot underwrite \u2192 micro-loans denied",
    "Forced to informal lenders at 30\u201360% interest",
    "Commerce stays undocumented \u2192 no tax net, no GDP visibility",
], size=16, gap=10)
b = box(s, Inches(6.85), Inches(2.0), Inches(5.9), Inches(4.6), fill=WHITE, line=TEAL)
txt(s, Inches(7.2), Inches(2.3), Inches(5.2), Inches(0.5), "The numbers", size=19, bold=True, color=DTEAL)
stats = [
    ("70%+", "of Pakistan's economy is informal"),
    ("5M+", "micro & small businesses, most unbanked"),
    ("PKR 9T", "estimated informal credit need unmet by banks"),
    ("0", "credit-scored kiryana merchants today"),
]
yy = 3.0
for num, lbl in stats:
    txt(s, Inches(7.2), Inches(yy), Inches(1.9), Inches(0.6), num, size=26, bold=True, color=ACCENT2)
    txt(s, Inches(9.15), Inches(yy+0.08), Inches(3.5), Inches(0.7), lbl, size=13.5, color=MUTED)
    yy += 0.88

# ---------------- SLIDE 3 : SOLUTION ----------------
s = slide()
header(s, "THE SOLUTION", "An AI ledger that scores what banks can't see")
txt(s, Inches(0.6), Inches(1.85), Inches(12.1), Inches(0.5), "SarafAI ingests the data merchants already produce and generates a verifiable SME Credit Health Score (300\u2013900).", size=16, color=MUTED)
steps = [
    ("1. INGEST", "Receipt photos, khata notes,\nsupplier invoices, wallet\nhistories (Easypaisa/JazzCash)", "Qwen-VL OCR"),
    ("2. RECONCILE", "Extract, classify & dedupe\ninto one verified transaction\nledger per merchant", "PostgreSQL / AnalyticDB"),
    ("3. SCORE", "Six explainable cash-flow\nfactors \u2192 Credit Health\nScore with full audit trail", "Risk Model"),
    ("4. LEND", "Fintechs/banks originate\ncollateral-free micro-loans\nsized to real cash flow", "Lender API"),
]
x = Inches(0.6); w = Inches(2.85); gap = Inches(0.28)
for i, (t, d, tech) in enumerate(steps):
    b = box(s, x, Inches(2.6), w, Inches(3.5), fill=WHITE, line=RGBColor(0xCB,0xD5,0xE1))
    box(s, x, Inches(2.6), w, Inches(0.62), fill=TEAL if i % 2 == 0 else DTEAL)
    txt(s, x, Inches(2.74), w, Inches(0.4), t, size=15, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    txt(s, x + Inches(0.18), Inches(3.45), w - Inches(0.36), Inches(2.0), d, size=13.5, color=INK, align=PP_ALIGN.CENTER)
    tb = box(s, x + Inches(0.5), Inches(5.45), w - Inches(1.0), Inches(0.45), fill=LIGHT)
    txt(s, x + Inches(0.5), Inches(5.55), w - Inches(1.0), Inches(0.3), tech, size=12, bold=True, color=DTEAL, align=PP_ALIGN.CENTER)
    x += w + gap

# ---------------- SLIDE 4 : SCORE FACTORS ----------------
s = slide()
header(s, "HOW IT SCORES", "Explainable \u2014 not a black box")
txt(s, Inches(0.6), Inches(1.9), Inches(12.1), Inches(0.5), "Every merchant sees exactly what drives their score. Trust drives adoption.", size=16, color=MUTED)
factors = [
    ("Revenue scale", "200", "Average monthly verified inflow"),
    ("Cash-flow consistency", "200", "Month-to-month stability (low volatility)"),
    ("Growth trend", "150", "Revenue trajectory over 8 months"),
    ("Business activity", "150", "Transaction frequency & counterparty diversity"),
    ("Digital documentation", "100", "Share of verifiable (OCR/wallet) records"),
    ("Recency", "100", "Days since last recorded activity"),
]
yy = 2.55
for name, pts, desc in factors:
    b = box(s, Inches(0.6), Inches(yy), Inches(7.6), Inches(0.62), fill=LIGHT)
    txt(s, Inches(0.85), Inches(yy+0.12), Inches(2.9), Inches(0.4), name, size=15, bold=True, color=INK)
    txt(s, Inches(3.8), Inches(yy+0.14), Inches(4.2), Inches(0.4), desc, size=12.5, color=MUTED)
    b2 = box(s, Inches(8.4), Inches(yy), Inches(1.0), Inches(0.62), fill=TEAL)
    txt(s, Inches(8.4), Inches(yy+0.12), Inches(1.0), Inches(0.4), pts, size=17, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    yy += 0.74
b = box(s, Inches(9.7), Inches(2.55), Inches(3.0), Inches(4.33), fill=INK)
txt(s, Inches(9.95), Inches(2.85), Inches(2.5), Inches(0.5), "SCORE BANDS", size=12, bold=True, color=RGBColor(0x5E,0xEA,0xD4))
bands = [("750\u2013900", "Excellent \u2014 pre-approved", "16% APR"), ("650\u2013749", "Good \u2014 bankable", "19% APR"), ("550\u2013649", "Fair \u2014 conditional", "24% APR"), ("< 550", "Thin file \u2014 keep scanning", "\u2014")]
yy = 3.3
for rng, lbl, apr in bands:
    txt(s, Inches(9.95), Inches(yy), Inches(2.5), Inches(0.35), rng + "  " + lbl, size=12.5, bold=True, color=WHITE)
    txt(s, Inches(9.95), Inches(yy+0.28), Inches(2.5), Inches(0.3), apr, size=11, color=RGBColor(0x99,0xF6,0xE4))
    yy += 0.82

# ---------------- SLIDE 5 : DEMO ----------------
s = slide()
header(s, "LIVE DEMO", "From a paper receipt to a loan offer in seconds")
flows = [
    ("Dashboard", "Credit Health Score with six explainable factors, cash-flow metrics, and an instant collateral-free loan offer sized to actual monthly inflows."),
    ("Scan Receipt", "Drop a receipt photo \u2014 OCR (Qwen-VL) extracts date, counterparty, line items and amount with confidence scores. Merchant confirms."),
    ("Instant Rescore", "The verified transaction hits the ledger and the score recalculates live \u2014 merchants literally watch their creditworthiness grow."),
]
yy = 2.05
for i, (t, d) in enumerate(flows):
    b = box(s, Inches(0.6), Inches(yy), Inches(12.1), Inches(1.42), fill=WHITE, line=RGBColor(0xCB,0xD5,0xE1))
    circ = s.shapes.add_shape(1, Inches(0.95), Inches(yy+0.38), Inches(0.66), Inches(0.66))  # oval
    from pptx.enum.shapes import MSO_SHAPE
    circ = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.95), Inches(yy+0.38), Inches(0.66), Inches(0.66))
    circ.fill.solid(); circ.fill.fore_color.rgb = TEAL; circ.line.fill.background(); circ.shadow.inherit = False
    txt(s, Inches(0.95), Inches(yy+0.52), Inches(0.66), Inches(0.4), str(i+1), size=20, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    txt(s, Inches(1.95), Inches(yy+0.18), Inches(3.3), Inches(0.5), t, size=17, bold=True, color=DTEAL)
    txt(s, Inches(5.3), Inches(yy+0.16), Inches(7.1), Inches(1.1), d, size=13.5, color=INK)
    yy += 1.62
txt(s, Inches(0.6), Inches(6.95), Inches(12.1), Inches(0.4), "Zero-dependency web app \u2014 runs in any browser, works on a low-end Android phone over 3G.", size=13, bold=True, color=MUTED, align=PP_ALIGN.CENTER)

# ---------------- SLIDE 6 : ARCHITECTURE ----------------
s = slide()
header(s, "ARCHITECTURE", "Built on Alibaba Cloud")
layers = [
    ("Merchant app (web / Android)", "Upload photos \u2022 connect wallet \u2022 view score & loan offers", LIGHT, INK),
    ("Intelligence layer", "Qwen-VL OCR (Urdu + English receipts) \u2022 transaction classifier \u2022 deduplication & fraud checks", TEAL, WHITE),
    ("Data layer", "Alibaba Cloud PostgreSQL \u2014 verified ledger  |  AnalyticDB \u2014 cash-flow analytics at scale", DTEAL, WHITE),
    ("Scoring & Lending API", "Cash-flow risk model (6 factors, 300\u2013900) \u2022 Lender API \u2022 loan offer engine", INK, WHITE),
]
yy = 2.1
for t, d, fill, fg in layers:
    b = box(s, Inches(0.9), Inches(yy), Inches(11.5), Inches(1.05), fill=fill, line=RGBColor(0xCB,0xD5,0xE1) if fill==LIGHT else None)
    txt(s, Inches(1.25), Inches(yy+0.14), Inches(3.9), Inches(0.5), t, size=16, bold=True, color=fg if fg else INK)
    txt(s, Inches(1.25), Inches(yy+0.55), Inches(10.9), Inches(0.4), d, size=12.5, color=fg if fill != LIGHT else MUTED)
    yy += 1.22
arrows = txt(s, Inches(0.9), Inches(2.0), Inches(11.5), Inches(0.1), "", size=8)
txt(s, Inches(0.6), Inches(7.0), Inches(12.1), Inches(0.4), "MVP today: full loop (ingest \u2192 extract \u2192 reconcile \u2192 score \u2192 offer) in a single-file app; cloud layers are drop-in for scale.", size=12.5, color=MUTED, align=PP_ALIGN.CENTER)

# ---------------- SLIDE 7 : IMPACT ----------------
s = slide()
header(s, "ECONOMIC IMPACT", "One score, three layers of impact")
cols = [
    ("FINANCIAL INCLUSION", "Unbanked kiryana merchants get collateral-free micro-loans from fintechs & banks \u2014 priced off verified cash flows, not guesswork.", TEAL),
    ("LOWER DEFAULT RATES", "Loans underwritten on actual transaction data reduce NPLs for lenders, making tiny-ticket MSME lending commercially viable at scale.", DTEAL),
    ("DOCUMENTED ECONOMY", "Every scanned receipt is a verifiable tax record \u2014 organic, incentive-driven documentation of the informal economy into the tax net.", ACCENT2),
]
x = Inches(0.6); w = Inches(3.95)
for t, d, c in cols:
    b = box(s, x, Inches(2.1), w, Inches(3.9), fill=WHITE, line=RGBColor(0xCB,0xD5,0xE1))
    box(s, x, Inches(2.1), w, Inches(0.75), fill=c)
    txt(s, x, Inches(2.28), w, Inches(0.5), t, size=15, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    txt(s, x + Inches(0.3), Inches(3.1), w - Inches(0.6), Inches(2.7), d, size=14.5, color=INK, align=PP_ALIGN.CENTER)
    x += w + Inches(0.25)
txt(s, Inches(0.6), Inches(6.5), Inches(12.1), Inches(0.6), "\"The fastest way to bank the unbanked is to score what they already do \u2014 not to ask them for documents they've never had.\"", size=15, color=MUTED, align=PP_ALIGN.CENTER)

# ---------------- SLIDE 8 : ROADMAP / CLOSE ----------------
s = slide()
box(s, 0, 0, SW, SH, fill=INK, radius=False)
txt(s, Inches(0.9), Inches(0.7), Inches(11.5), Inches(0.6), "WHAT'S NEXT", size=13, bold=True, color=RGBColor(0x5E,0xEA,0xD4))
txt(s, Inches(0.9), Inches(1.05), Inches(11.5), Inches(0.8), "From demo to deployment", size=34, bold=True, color=WHITE)
items = [
    ("NOW \u2014 MVP", "Full scoring loop working: ingest \u2192 OCR \u2192 reconcile \u2192 explainable score \u2192 loan offer"),
    ("NEXT 3 MONTHS", "Integrate Qwen-VL API for real receipt OCR (Urdu/English) \u2022 Easypaisa & JazzCash statement ingestion \u2022 Alibaba Cloud PostgreSQL backend"),
    ("MONTHS 3\u20136", "Calibrate risk model with partner fintech repayment data \u2022 pilot with 100 kiryana stores in Karachi"),
    ("SCALE", "Lender marketplace API \u2022 SBP sandbox for digital lending \u2022 expand to distributors & micro-transporters"),
]
yy = 2.15
for t, d in items:
    box(s, Inches(0.9), Inches(yy), Inches(11.5), Inches(1.0), fill=RGBColor(0x1E,0x29,0x3B))
    txt(s, Inches(1.2), Inches(yy+0.14), Inches(2.6), Inches(0.5), t, size=14, bold=True, color=RGBColor(0x5E,0xEA,0xD4))
    txt(s, Inches(3.9), Inches(yy+0.16), Inches(8.2), Inches(0.8), d, size=13, color=RGBColor(0xE2,0xE8,0xF0))
    yy += 1.15
txt(s, Inches(0.9), Inches(6.85), Inches(11.5), Inches(0.5), "SarafAI \u2014 Credit for the invisible economy.  Team SarafAI \u2022 Bano Qabil \u00D7 Alibaba Cloud AI Hackathon 2026", size=13, bold=True, color=WHITE)

prs.save(r"E:\hackathons\Alibaba\SarafAI\SarafAI_Presentation.pptx")
print("Saved deck:", len(prs.slides.slides if hasattr(prs.slides,'slides') else prs.slides._sldIdLst), "slides")
