from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.enums import TA_LEFT, TA_CENTER

# Brand colors
NAVY_DEEP = colors.HexColor('#05080f')
NAVY = colors.HexColor('#0d1b2a')
NAVY_MID = colors.HexColor('#112240')
BLUE_ACCENT = colors.HexColor('#4db8ff')
BLUE_DIM = colors.HexColor('#1e3a5f')
WHITE = colors.HexColor('#f0f4f8')
GRAY = colors.HexColor('#8899aa')
GRAY_DIM = colors.HexColor('#3a4a5c')

doc = SimpleDocTemplate(
    '/home/user/newSite/josh-soliz-brand-guidelines.pdf',
    pagesize=letter,
    leftMargin=0.75*inch,
    rightMargin=0.75*inch,
    topMargin=0.75*inch,
    bottomMargin=0.75*inch,
)

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY_DEEP)
    canvas.rect(0, 0, letter[0], letter[1], fill=1, stroke=0)
    canvas.restoreState()

story = []

# Styles
title_style = ParagraphStyle('Title', fontName='Helvetica-Bold', fontSize=28, textColor=WHITE, spaceAfter=4, alignment=TA_LEFT, leading=34)
subtitle_style = ParagraphStyle('Subtitle', fontName='Helvetica', fontSize=13, textColor=GRAY, spaceAfter=20, alignment=TA_LEFT)
h2_style = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=15, textColor=BLUE_ACCENT, spaceAfter=8, spaceBefore=22, leading=18)
h3_style = ParagraphStyle('H3', fontName='Helvetica-Bold', fontSize=11, textColor=WHITE, spaceAfter=4, spaceBefore=10, leading=14)
body_style = ParagraphStyle('Body', fontName='Helvetica', fontSize=10, textColor=GRAY, spaceAfter=6, leading=15)
label_style = ParagraphStyle('Label', fontName='Helvetica-Bold', fontSize=9, textColor=BLUE_ACCENT, spaceAfter=4, leading=12)
bullet_style = ParagraphStyle('Bullet', fontName='Helvetica', fontSize=10, textColor=GRAY, spaceAfter=4, leading=14, leftIndent=12)

def hr():
    return HRFlowable(width='100%', thickness=1, color=GRAY_DIM, spaceAfter=8, spaceBefore=4)

def h2(text):
    return Paragraph(text.upper(), h2_style)

def body(text):
    return Paragraph(text, body_style)

def bullet(text):
    return Paragraph(f'<bullet>&bull;</bullet> {text}', bullet_style)

# --- TITLE ---
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph('Josh Soliz', title_style))
story.append(Paragraph('Brand Guidelines', subtitle_style))
story.append(hr())
story.append(Spacer(1, 0.1*inch))

# --- BRAND IDENTITY ---
story.append(h2('Brand Identity'))
data = [
    [Paragraph('<b>Name</b>', ParagraphStyle('th', fontName='Helvetica-Bold', fontSize=9, textColor=BLUE_ACCENT)), Paragraph('Josh Soliz', body_style)],
    [Paragraph('<b>Domain</b>', ParagraphStyle('th', fontName='Helvetica-Bold', fontSize=9, textColor=BLUE_ACCENT)), Paragraph('joshsoliz.com', body_style)],
    [Paragraph('<b>Location</b>', ParagraphStyle('th', fontName='Helvetica-Bold', fontSize=9, textColor=BLUE_ACCENT)), Paragraph('Clarksville, TN (also Nashville, TN + nationally)', body_style)],
    [Paragraph('<b>Services</b>', ParagraphStyle('th', fontName='Helvetica-Bold', fontSize=9, textColor=BLUE_ACCENT)), Paragraph('Motion Design, Video Production, Photography', body_style)],
    [Paragraph('<b>Contact</b>', ParagraphStyle('th', fontName='Helvetica-Bold', fontSize=9, textColor=BLUE_ACCENT)), Paragraph('hello@joshsoliz.com', body_style)],
]
t = Table(data, colWidths=[1.4*inch, 5.4*inch])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), NAVY),
    ('ROWBACKGROUNDS', (0,0), (-1,-1), [NAVY, NAVY_MID]),
    ('BOX', (0,0), (-1,-1), 1, GRAY_DIM),
    ('INNERGRID', (0,0), (-1,-1), 0.5, GRAY_DIM),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 7),
    ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
]))
story.append(t)
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph('<b>Primary Tagline:</b> "Video that looks good and sounds like you"', body_style))
story.append(Paragraph('"I help businesses and brands create content that\'s actually worth watching — without losing what makes \'em feel like them"', body_style))

# --- BRAND PERSONALITY ---
story.append(h2('Brand Personality & Tone'))
bullets = [
    'Professional yet approachable — clear, not corporate',
    'Creative-first, storytelling-focused',
    'Client-centered — preserving the client\'s identity is a key differentiator',
    'Modern and refined — minimal aesthetic with intentional accents',
    'Multi-disciplinary — video + motion + photography under one voice',
]
for b in bullets:
    story.append(bullet(b))

# --- COLOR PALETTE ---
story.append(h2('Color Palette'))
color_data = [
    ['Name', 'Hex', 'Use'],
    ['Navy Deep', '#05080f', 'Main background, deep overlays'],
    ['Navy', '#0d1b2a', 'Card backgrounds, secondary surfaces'],
    ['Navy Mid', '#112240', 'Hover states, modals'],
    ['Blue Accent', '#4db8ff', 'Primary CTAs, labels, highlights'],
    ['Blue Glow', 'rgba(77,184,255,0.12)', 'Decorative glows, background effects'],
    ['Blue Dim', '#1e3a5f', 'Dimmed accents, dark overlays'],
    ['White', '#f0f4f8', 'Primary text, headings'],
    ['Gray', '#8899aa', 'Body copy, secondary text'],
    ['Gray Dim', '#3a4a5c', 'Borders, dividers, tertiary text'],
]

header_style = ParagraphStyle('ColHeader', fontName='Helvetica-Bold', fontSize=9, textColor=BLUE_ACCENT)
cell_style = ParagraphStyle('Cell', fontName='Helvetica', fontSize=9, textColor=GRAY)
mono_style = ParagraphStyle('Mono', fontName='Courier', fontSize=9, textColor=WHITE)

color_rows = []
hex_colors = [None, '#05080f', '#0d1b2a', '#112240', '#4db8ff', None, '#1e3a5f', '#f0f4f8', '#8899aa', '#3a4a5c']
for i, row in enumerate(color_data):
    if i == 0:
        color_rows.append([Paragraph(c, header_style) for c in row])
    else:
        color_rows.append([
            Paragraph(row[0], cell_style),
            Paragraph(row[1], mono_style),
            Paragraph(row[2], cell_style),
        ])

ct = Table(color_rows, colWidths=[1.3*inch, 1.7*inch, 3.8*inch])
ct_style = [
    ('BACKGROUND', (0,0), (-1,0), BLUE_DIM),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [NAVY, NAVY_MID]),
    ('BOX', (0,0), (-1,-1), 1, GRAY_DIM),
    ('INNERGRID', (0,0), (-1,-1), 0.5, GRAY_DIM),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 7),
    ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
]
# Add color swatches
swatch_colors = [None, NAVY_DEEP, NAVY, NAVY_MID, BLUE_ACCENT, None, BLUE_DIM, WHITE, GRAY, GRAY_DIM]
for i, sc in enumerate(swatch_colors):
    if sc:
        ct_style.append(('BACKGROUND', (1, i), (1, i), sc))
        if sc in [WHITE, GRAY]:
            ct_style.append(('TEXTCOLOR', (1, i), (1, i), NAVY_DEEP))
        else:
            ct_style.append(('TEXTCOLOR', (1, i), (1, i), WHITE))
ct.setStyle(TableStyle(ct_style))
story.append(ct)
story.append(Paragraph('Overall palette feel: Dark navy base + precise blue accent. No warm tones.', ParagraphStyle('note', fontName='Helvetica-Oblique', fontSize=9, textColor=GRAY, spaceBefore=6, spaceAfter=4)))

# --- TYPOGRAPHY ---
story.append(h2('Typography'))
story.append(Paragraph('<b>Headings: Archivo</b> (Google Fonts)', body_style))
story.append(Paragraph('Weights: 300, 400, 500, 600, 700, 800, 900 — Geometric, modern, strong', body_style))
story.append(Spacer(1, 4))
story.append(Paragraph('<b>Body: Sora</b> (Google Fonts)', body_style))
story.append(Paragraph('Weights: 300, 400, 500, 600 — Clean, readable, elegant', body_style))
story.append(Spacer(1, 8))

size_data = [
    ['Element', 'Size / Rule'],
    ['Hero Headline', 'clamp(44px, 7vw, 88px)'],
    ['Section Headings', 'clamp(26px, 4vw, 42px)'],
    ['Body Text', '16px base (15px–20px range)'],
    ['Labels / Tags', '11–12px, UPPERCASE, letter-spacing 0.12–0.18em'],
]
st = Table([[Paragraph(c, header_style if i == 0 else (cell_style if j == 0 else mono_style)) for j, c in enumerate(row)] for i, row in enumerate(size_data)], colWidths=[2.5*inch, 4.3*inch])
st.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), BLUE_DIM),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [NAVY, NAVY_MID]),
    ('BOX', (0,0), (-1,-1), 1, GRAY_DIM),
    ('INNERGRID', (0,0), (-1,-1), 0.5, GRAY_DIM),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 7),
    ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
]))
story.append(st)
story.append(Spacer(1, 4))
story.append(bullet('Labels and tags: always uppercase + letter-spaced'))
story.append(bullet('Never mix display fonts with decorative/serif fonts'))
story.append(bullet('Blue accent color used for eyebrow/label text above headings'))

# --- LAYOUT & SPACING ---
story.append(h2('Layout & Spacing'))
layout_items = [
    ('Max content width', '1140px'),
    ('Container padding', '32px horizontal'),
    ('Section padding', '~100px vertical'),
    ('Service card gap', '2px'),
    ('Work card gap', '24px'),
    ('Border radius', '4–6px (buttons and cards)'),
    ('Work thumbnail ratio', '16:9'),
]
for label, value in layout_items:
    story.append(Paragraph(f'<b><font color="#4db8ff">{label}:</font></b>  {value}', body_style))

# --- UI COMPONENTS ---
story.append(h2('UI Components'))

story.append(Paragraph('<b>Buttons</b>', h3_style))
story.append(bullet('Primary: Blue bg (#4db8ff), navy text, 14px bold, 4px radius, 14px 32px padding'))
story.append(bullet('Secondary: Blue text with bottom border only, no background'))
story.append(bullet('Tertiary/Ghost: Transparent with subtle border'))

story.append(Paragraph('<b>Cards</b>', h3_style))
story.append(bullet('Navy background (#0d1b2a), subtle borders'))
story.append(bullet('Hover: slightly darker + scale(1.02)'))
story.append(bullet('Work cards: image with dark gradient overlay at bottom, tag chips, title beneath'))

story.append(Paragraph('<b>Navigation</b>', h3_style))
story.append(bullet('Fixed header with gradient + backdrop blur'))
story.append(bullet('Logo: "Josh Soliz" text, 18px, 600 weight'))
story.append(bullet('CTA in nav: blue border button, 4px radius'))
story.append(bullet('Background opacity increases after 60px scroll'))

# --- ANIMATION ---
story.append(h2('Animation & Motion'))
story.append(bullet('Fade-up animation: 0.8s ease, staggered on hero (0.2s → 1.0s delays)'))
story.append(bullet('Scroll-triggered reveals: Intersection Observer for fade-ins'))
story.append(bullet('Hover transitions: color, opacity, scale — always smooth, never abrupt'))
story.append(bullet('Smooth scrolling enabled site-wide'))

# --- FOOTER ---
story.append(Spacer(1, 0.3*inch))
story.append(hr())
story.append(Paragraph('joshsoliz.com  ·  hello@joshsoliz.com  ·  Clarksville, TN', ParagraphStyle('footer', fontName='Helvetica', fontSize=9, textColor=GRAY, alignment=TA_CENTER)))

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print("PDF generated: josh-soliz-brand-guidelines.pdf")
