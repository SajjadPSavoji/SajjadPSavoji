"""Generate the profile README's SVG assets (light + dark) into ../assets.

Run:  python scripts/build_assets.py   (needs Pillow for text measurement, macOS fonts)
Every visual is a static, self-hosted SVG, so nothing on the profile depends
on a third-party stats service. Edit the DATA sections and re-run to update.

Repo stats and result numbers on the project cards are a snapshot (sources listed above PROJECTS). Refresh with
  gh api repos/OWNER/REPO/languages        # bytes per language
  gh api repos/OWNER/REPO --jq .stargazers_count
and count non-blank lines of tracked source files in a shallow clone.
"""
from pathlib import Path
from html import escape
from PIL import ImageFont

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"

THEMES = {
    "dark": dict(card="#151b23", card2="#10161e", border="#2a313c", text="#e6edf3", muted="#9198a1",
                 faint="#363d47", grid="#1f2630", chip="#1b2330", track="#262d37",
                 blue="#7aa2ff", teal="#3fd0c9", amber="#f2b552", coral="#ff8f7a",
                 green="#6fd08c",
                 b1="#6f97ff", b2="#93b2ff", b3="#b9cdff", b4="#dfe8ff", wash="#eef3ff"),
    "light": dict(card="#f6f8fa", card2="#ffffff", border="#d1d9e0", text="#1f2328", muted="#59636e",
                  faint="#c8d1da", grid="#e3e8ee", chip="#ffffff", track="#e3e8ee",
                  blue="#3657d6", teal="#0b8a83", amber="#b26a00", coral="#c4472f",
                  green="#2c8a4b",
                  b1="#2f54d1", b2="#5677e0", b3="#87a0ec", b4="#b3c4f4", wash="#e9effd"),
}

# ---------------------------------------------------------------- helpers
_FONTS = {}


def tw(text, size, bold=False, mono=False):
    """Approximate rendered width; padded so wider fonts (Segoe UI) still fit."""
    key = (size, bold, mono)
    if key not in _FONTS:
        if mono:
            _FONTS[key] = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", size * 4)
        else:
            _FONTS[key] = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size * 4, index=1 if bold else 0)
    return _FONTS[key].getlength(text) / 4 * (1.0 if mono else 1.06)


def wrap(text, size, width, bold=False):
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if tw(trial, size, bold) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    lines.append(cur)
    return lines


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{escape(title)}"><title>{escape(title)}</title>{body}</svg>\n')


def t(x, y, s, size, fill, weight=400, mono=False, anchor="start", ls=None):
    fam = MONO if mono else SANS
    lsp = f' letter-spacing="{ls}"' if ls is not None else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{fam}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}"{lsp}>{escape(s)}</text>')


RADIUS = 12  # one radius for every card, tile and panel


def tchip(x, y, label, c, hue, size=12, h=25):
    """The one chip style: neutral fill, outline tinted with the hue, text in the text colour."""
    w = tw(label, size) + 20
    s = (f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{h}" rx="{h/2}" fill="{c["chip"]}" '
         f'stroke="{c[hue]}" stroke-opacity="0.5"/>'
         + t(x + w / 2, y + h / 2 + size * 0.36, label, size, c["text"], 500, anchor="middle"))
    return s, w


def write(name, theme, content):
    (OUT / f"{name}-{theme}.svg").write_text(content)


# ---------------------------------------------------------------- banner
BANNER_TEXT = ("I post-train foundation models and keep them improving after they ship: today the LLM "
               "behind Upwork's job-post agent, before that robot VLAs and world models at Huawei.")
BANNER_CHIPS = [("LLM post-training", "blue"), ("Continual learning", "green"), ("LLM evaluation", "teal"),
                ("Robot VLAs", "coral"), ("World models", "amber"), ("3D vision", "blue")]


def banner(c, theme):
    W, H = 880, 320
    hues = ["blue", "teal", "coral", "amber"]
    b = [f'<defs>'
         f'<linearGradient id="bgg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c["card"]}"/>'
         f'<stop offset="1" stop-color="{c["card2"]}"/></linearGradient>'
         f'<linearGradient id="rb" x1="0" y1="0" x2="1" y2="0">'
         + f'<stop offset="0" stop-color="{c["b1"]}"/><stop offset="0.55" stop-color="{c["b3"]}"/>'
         + f'<stop offset="1" stop-color="{c["wash"]}"/>'
         + f'</linearGradient>'
         f'<radialGradient id="glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{c["blue"]}" '
         f'stop-opacity="{0.16 if theme == "dark" else 0.08}"/><stop offset="1" stop-color="{c["blue"]}" '
         f'stop-opacity="0"/></radialGradient>'
         f'<clipPath id="clip"><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="{RADIUS}"/></clipPath>'
         f'</defs>',
         f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="{RADIUS}" fill="url(#bgg)" stroke="{c["border"]}"/>',
         f'<g clip-path="url(#clip)">',
         f'<rect x="0" y="0" width="{W}" height="4" fill="url(#rb)"/>']
    for gx in range(580, W, 22):
        for gy in range(22, H, 22):
            b.append(f'<circle cx="{gx}" cy="{gy}" r="1.2" fill="{c["grid"]}"/>')
    b.append(f'<circle cx="725" cy="150" r="170" fill="url(#glow)"/>')
    # a small network whose layers are labeled with the loop I run: data -> train -> eval -> ship
    layers = [[100, 145, 190], [78, 122, 168, 212], [78, 122, 168, 212], [122, 168]]
    xs = [622, 692, 762, 832]
    nodes = [[(xs[i], y) for y in ys] for i, ys in enumerate(layers)]
    for i in range(len(nodes) - 1):
        for (x1, y1) in nodes[i]:
            for (x2, y2) in nodes[i + 1]:
                b.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c["faint"]}" stroke-width="1"/>')
    routes = [[(0, 0), (1, 1), (2, 2), (3, 1)], [(0, 2), (1, 3), (2, 1), (3, 0)], [(0, 1), (1, 0), (2, 3), (3, 1)]]
    for k, r in enumerate(routes):
        pts = [nodes[l][n] for l, n in r]
        d = "M" + " L".join(f"{x},{y}" for x, y in pts)
        hue = ["blue", "coral", "amber"][k]
        b.append(f'<path d="{d}" fill="none" stroke="{c[hue]}" stroke-width="1.6" opacity="0.5"/>')
        dur = 3.2 + k * 0.7
        b.append(f'<circle r="3.2" fill="{c[hue]}"><animateMotion dur="{dur}s" repeatCount="indefinite" '
                 f'begin="{k * 0.9}s" path="{d}"/><animate attributeName="opacity" values="0;1;1;0" '
                 f'dur="{dur}s" begin="{k * 0.9}s" repeatCount="indefinite"/></circle>')
    for li, layer in enumerate(nodes):
        hue = hues[li]
        for ni, (x, y) in enumerate(layer):
            b.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{c["card"]}" stroke="{c[hue]}" stroke-width="1.8"/>')
            b.append(f'<circle cx="{x}" cy="{y}" r="2.6" fill="{c[hue]}"><animate attributeName="opacity" '
                     f'values="0.35;1;0.35" dur="3s" begin="{(li * 0.45 + ni * 0.2) % 3:.2f}s" '
                     f'repeatCount="indefinite"/></circle>')
    for li, lab in enumerate(["data", "train", "eval", "ship"]):
        b.append(t(xs[li], 248, lab, 11.5, c[hues[li]], 600, True, "middle"))
    for li in range(3):
        b.append(t((xs[li] + xs[li + 1]) / 2, 248, "→", 11.5, c["muted"], 400, True, "middle"))
    b.append('</g>')
    # left text block
    x0 = 44
    b.append(f'<rect x="{x0}" y="38" width="8" height="8" rx="2" fill="{c["b1"]}"/>')
    b.append(t(x0 + 16, 46, "AI RESEARCH SCIENTIST  ·  TORONTO, CANADA", 12, c["muted"], 600, True, ls=1.1))
    b.append(t(x0 - 2, 94, "Sajjad Pakdamansavoji", 40, c["text"], 700, ls=-0.6))
    b.append(t(x0, 126, "Lead AI Research Scientist at Upwork", 18, c["blue"], 600))
    lines = wrap(BANNER_TEXT, 15, 490)
    assert len(lines) <= 3, lines
    for i, line in enumerate(lines):
        b.append(t(x0, 160 + i * 22, line, 15, c["muted"]))
    x, y = x0, 160 + len(lines) * 22 + 6
    for i, (lab, hue) in enumerate(BANNER_CHIPS):
        if i == 3:  # two even rows of three
            x, y = x0, y + 34
        s, w = tchip(x, y, lab, c, hue, size=12, h=26)
        b.append(s)
        x += w + 8
        assert x < 580, lab
    assert y + 26 < H - 14, f"banner chips overflow: {y}"
    write("banner", theme, svg(W, H, "".join(b), "Sajjad Pakdamansavoji, Lead AI Research Scientist at Upwork. "
                               + BANNER_TEXT))


# ---------------------------------------------------------------- highlights
HIGHLIGHTS = [
    ("1st", "amber", "NeurIPS 2026 BEHAVIOR Challenge",
     "Our household-robot team, The North Star, won it after placing 4th in 2025."),
    ("1M+", "blue", "daily users at Upwork",
     "My team's post-trained LLM writes job posts in Upwork's AI agent, replacing a paid API model."),
    ("13", "coral", "papers and preprints",
     "On LLM post-training and evaluation, robot VLAs and world models, and 6D pose estimation."),
    ("3", "teal", "patents filed",
     "On robot VLAs, world models and 3D vision, filed during my time at Huawei Noah's Ark Lab."),
]


def highlights(c, theme):
    W, H, gap = 880, 180, 12
    tw_ = (W - gap * 3) / 4
    b = []
    for i, (num, hue, head, body) in enumerate(HIGHLIGHTS):
        x = i * (tw_ + gap)
        b.append(f'<rect x="{x + 0.5}" y="0.5" width="{tw_ - 1}" height="{H - 1}" rx="{RADIUS}" fill="{c["card"]}" '
                 f'stroke="{c["border"]}"/>')
        b.append(f'<rect x="{x + 18}" y="18" width="24" height="3" rx="1.5" fill="{c[hue]}"/>')
        b.append(t(x + 18, 56, num, 30, c[hue], 700, ls=-0.5))
        hl = wrap(head, 13, tw_ - 34, bold=True)
        for j, line in enumerate(hl):
            b.append(t(x + 18, 80 + j * 17, line, 13, c["text"], 700))
        y0 = 80 + len(hl) * 17 + 4
        bl = wrap(body, 12, tw_ - 34)
        assert y0 + (len(bl) - 1) * 16 < H - 14, (head, bl)
        for j, line in enumerate(bl):
            b.append(t(x + 18, y0 + j * 16, line, 12, c["muted"]))
    write("highlights", theme, svg(W, H, "".join(b), "Highlights. " + " ".join(
        f"{n} {h}: {d}" for n, _, h, d in HIGHLIGHTS)))


# ---------------------------------------------------------------- project cards
# Each card shows the project's own result as a small visual (taste-skill: show the real thing).
# Numbers come from each repo: CALVIN-MAX results/analysis/maxA_core_pooled.json (pooled success),
# OpenCaP README highlights, AutoPolish README (its loop), awesome-wsp data/entries.json ("added"),
# MiniVLMDocEval README results table (mean column), colabctl README (commands).
WSP_GROWTH = [31, 58, 242, 544, 560, 570, 576, 587, 595, 596, 605, 606]  # cumulative, Nov 4 -> Nov 15

# (key, name, kicker, owner, description, visual, language, footer facts)
PROJECTS = [
    ("calvin-max", "CALVIN-MAX", "ROBOT LEARNING · BENCHMARK", "forall-labs",
     "What happens when the world changes mid-task? 7,828 test cases across 10 released robot "
     "policies.",
     ("bars", "TASK SUCCESS, 10 POLICIES POOLED",
      [("No change", 69.9, "Base"), ("Change before", 60.5, "Pre"), ("Change mid-task", 63.0, "Mid")]),
     "Python", ["8.7k lines", "MIT"]),
    ("opencap", "OpenCaP", "CODE AS POLICIES · LLM EVAL", "forall-labs",
     "21 open-weight LLMs write robot code in 7,560 trials; each failure gets the smallest fix "
     "that works.",
     ("pairs", "SHARE OF FAILING PROGRAMS", ("with helpers (S1)", "low-level API (S3/S4)"),
      [("Frame errors", 4, 47), ("API misuse", 26, 60)]),
     "Python", ["25.5k lines", "MIT"]),
    ("autopolish", "AutoPolish", "VISION · IMAGE EDITING", "forall-labs",
     "Persona VLM critics steer image edits with no training, and agree with human raters at up "
     "to 0.96.",
     ("flow", "ONE EDITING ROUND",
      [("Image", "input"), ("Critics", "Qwen2-VL"), ("Edit", "FLUX Kontext"), ("Keep", "score rises")]),
     "Python", ["12.3k lines", "MIT"]),
    ("awesome-wsp", "Awesome WSP", "AGENTS · LIVING RESEARCH MAP", "SajjadPSavoji",
     "A daily map of LLMs that read, edit and write other networks' weights, kept current by an agent "
     "I built.",
     ("growth", "ENTRIES IN THE LIST", WSP_GROWTH, ("Nov 4", "Nov 15")),
     "Python", ["606 entries", "★ 4", "CC0"]),
    ("minivlmdoceval", "MiniVLMDocEval", "VLMS · DOCUMENT AI", "SajjadPSavoji",
     "Six sub-1B VLMs on five document benchmarks; a 450M model beats both 0.9B models on "
     "ChartQA.",
     ("bars", "MEAN SCORE, 5 BENCHMARKS",
      [("Qwen3.5-0.8B", 70.3, ""), ("InternVL3-1B", 63.3, ""), ("LFM2.5-VL-450M", 59.9, ""),
       ("LLaVA-OV-0.5B", 52.8, ""), ("SmolVLM2-500M", 49.4, ""), ("FastVLM-0.5B", 36.8, "")]),
     "Python", ["3.7k lines"]),
    ("colabctl", "colabctl", "DEV TOOLING · GPU RUNTIMES", "SajjadPSavoji",
     "Start, check and stop Colab GPU runtimes from the shell, so scripts and coding agents can "
     "drive them.",
     ("terminal", "zsh",
      [("colabctl up -a T4 --bridge", "allocate a T4"), ("colabctl status --quota", "RAM, disk, GPU"),
       ("colabctl down", "shut it down")]),
     "Python", ["2.0k lines", "stdlib only"]),
]
LANG_DOT = {"Python": "#3572A5"}  # GitHub's colour for the one language shown


def viz_panel(c, x, y, w, h, spec):
    """The inset panel holding a card's visual: one box inside the card, never deeper."""
    kind, title = spec[0], spec[1]
    b = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{c["card2"]}" stroke="{c["border"]}"/>']
    px, pw = x + 14, w - 28
    if kind != "terminal":
        b.append(t(px, y + 20, title, 10, c["muted"], 600, True, ls=0.6))
    if kind == "bars":
        rows = spec[2]
        top, bottom = y + 32, y + h - 10
        rh = (bottom - top) / len(rows)
        lab_w = max(tw(r[0], 10.5, mono=True) for r in rows) + 12
        track_w = pw - lab_w - 40
        best = max(r[1] for r in rows)
        for i, (lab, v, _) in enumerate(rows):
            cy = top + rh * i + rh / 2
            bh = min(8, rh * 0.45)
            b.append(t(px, cy + 3.6, lab, 10.5, c["text"], 500, True))
            b.append(f'<rect x="{px + lab_w:.1f}" y="{cy - bh/2:.1f}" width="{track_w:.1f}" height="{bh:.1f}" '
                     f'rx="{bh/2:.1f}" fill="{c["track"]}"/>')
            fill = c["b1"] if v == best else c["b3"]
            b.append(f'<rect x="{px + lab_w:.1f}" y="{cy - bh/2:.1f}" width="{track_w * v / 100:.1f}" '
                     f'height="{bh:.1f}" rx="{bh/2:.1f}" fill="{fill}"/>')
            b.append(t(px + pw, cy + 3.8, f"{v:.1f}", 11, c["text"], 700, anchor="end"))
    elif kind == "pairs":
        (l1, l2), rows = spec[2], spec[3]
        top, bottom = y + 30, y + h - 26
        rh = (bottom - top) / len(rows)
        lab_w = max(tw(r[0], 10.5, mono=True) for r in rows) + 12
        track_w = pw - lab_w - 78
        for i, (lab, a, z) in enumerate(rows):
            cy = top + rh * i + rh / 2
            b.append(t(px, cy + 3.6, lab, 10.5, c["text"], 500, True))
            for j, (v, col) in enumerate(((a, c["b3"]), (z, c["b1"]))):
                by = cy - 8 + j * 9
                b.append(f'<rect x="{px + lab_w:.1f}" y="{by:.1f}" width="{track_w:.1f}" height="7" rx="3.5" '
                         f'fill="{c["track"]}"/>')
                b.append(f'<rect x="{px + lab_w:.1f}" y="{by:.1f}" width="{track_w * v / 100:.1f}" height="7" '
                         f'rx="3.5" fill="{col}"/>')
            b.append(f'<text x="{px + pw}" y="{cy + 4:.1f}" font-family="{SANS}" font-size="11" text-anchor="end" '
                     f'fill="{c["muted"]}">{a}% → <tspan fill="{c["text"]}" font-weight="700">{z}%</tspan></text>')
        lx = px  # legend along the bottom edge of the panel
        for lab, col in ((l1, c["b3"]), (l2, c["b1"])):
            b.append(f'<rect x="{lx}" y="{y + h - 18}" width="8" height="8" rx="2" fill="{col}"/>')
            b.append(t(lx + 13, y + h - 10.5, lab, 10, c["muted"], 500))
            lx += 13 + tw(lab, 10) + 18
    elif kind == "flow":
        steps = spec[2]
        n, gap = len(steps), 14
        nw = (pw - gap * (n - 1)) / n
        ny, nh = y + 32, 40
        for i, (name, sub) in enumerate(steps):
            nx = px + i * (nw + gap)
            last = i == n - 1
            b.append(f'<rect x="{nx:.1f}" y="{ny}" width="{nw:.1f}" height="{nh}" rx="8" fill="{c["card"]}" '
                     f'stroke="{c["b1"] if last else c["border"]}"/>')
            b.append(t(nx + nw / 2, ny + 17, name, 11.5, c["text"], 700, anchor="middle"))
            assert tw(sub, 9.5, mono=True) < nw - 6, sub
            b.append(t(nx + nw / 2, ny + 31, sub, 9.5, c["muted"], 400, True, "middle"))
            if not last:
                ax = nx + nw + 3
                b.append(f'<path d="M{ax:.1f},{ny + nh/2} h{gap - 8}" stroke="{c["b2"]}" stroke-width="1.5"/>'
                         f'<path d="M{ax + gap - 9:.1f},{ny + nh/2 - 3.5} l4,3.5 l-4,3.5" fill="none" '
                         f'stroke="{c["b2"]}" stroke-width="1.5"/>')
        # the loop back from Keep to Critics: the next round
        x2 = px + 1 * (nw + gap) + nw / 2
        x4 = px + 3 * (nw + gap) + nw / 2
        ly = ny + nh + 12
        b.append(f'<path d="M{x4:.1f},{ny + nh} V{ly} H{x2:.1f} V{ny + nh + 4}" fill="none" stroke="{c["b2"]}" '
                 f'stroke-width="1.5" stroke-dasharray="3 3"/>'
                 f'<path d="M{x2 - 3.5:.1f},{ny + nh + 8} l3.5,-4 l3.5,4" fill="none" stroke="{c["b2"]}" '
                 f'stroke-width="1.5"/>')
        b.append(t((x2 + x4) / 2, ly - 3, "next round", 9.5, c["muted"], 400, True, "middle"))
    elif kind == "growth":
        series, (d0, d1) = spec[2], spec[3]
        top, bottom = y + 32, y + h - 22
        lx0, lx1 = px, px + pw - 40
        mx = max(series)
        pts = [(lx0 + (lx1 - lx0) * i / (len(series) - 1), bottom - (bottom - top) * v / mx)
               for i, v in enumerate(series)]
        line = " L".join(f"{a:.1f},{b_:.1f}" for a, b_ in pts)
        b.append(f'<line x1="{lx0}" y1="{bottom}" x2="{lx1}" y2="{bottom}" stroke="{c["border"]}"/>')
        b.append(f'<path d="M{lx0},{bottom} L{line} L{lx1},{bottom} Z" fill="{c["b1"]}" fill-opacity="0.14"/>')
        b.append(f'<path d="M{line}" fill="none" stroke="{c["b1"]}" stroke-width="2" stroke-linejoin="round"/>')
        ex, ey = pts[-1]
        b.append(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="3.5" fill="{c["b1"]}"/>')
        b.append(t(ex + 8, ey + 4, f"{series[-1]}", 12, c["text"], 700))
        b.append(t(lx0, bottom + 14, d0, 9.5, c["muted"], 400, True))
        b.append(t(lx1, bottom + 14, d1, 9.5, c["muted"], 400, True, "end"))
    elif kind == "terminal":
        lines = spec[2]
        for k in range(3):
            b.append(f'<circle cx="{px + 4 + k * 13}" cy="{y + 15}" r="4" fill="{c["faint"]}"/>')
        b.append(t(x + w / 2, y + 19, title, 10, c["muted"], 500, True, "middle"))
        b.append(f'<line x1="{x}" y1="{y + 27}" x2="{x + w}" y2="{y + 27}" stroke="{c["border"]}"/>')
        rh = (h - 36) / len(lines)
        for i, (cmd, note) in enumerate(lines):
            ly = y + 27 + rh * i + rh / 2 + 4
            b.append(t(px, ly, "$", 11.5, c["b1"], 700, True))
            b.append(t(px + 14, ly, cmd, 11.5, c["text"], 500, True))
            b.append(t(px + pw, ly, f"# {note}", 11, c["muted"], 400, True, "end"))
            assert tw(cmd, 11.5, mono=True) + tw(f"# {note}", 11, mono=True) + 30 < pw, cmd
    return "".join(b)


def card(c, theme, key, name, kicker, owner, desc, spec, lang, facts):
    W, H = 432, 292
    b = [f'<defs><clipPath id="cc"><rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="{RADIUS}"/></clipPath>'
         f'<linearGradient id="tb" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c["b1"]}"/>'
         f'<stop offset="1" stop-color="{c["wash"]}"/></linearGradient></defs>',
         f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="{RADIUS}" fill="{c["card"]}" stroke="{c["border"]}"/>',
         f'<rect x="0" y="0" width="{W}" height="4" fill="url(#tb)" clip-path="url(#cc)"/>']
    b.append(t(22, 34, kicker, 11, c["b1"], 700, True, ls=0.8))
    b.append(t(W - 22, 34, owner, 11, c["muted"], 400, True, "end"))
    b.append(t(22, 66, name, 22, c["text"], 700, ls=-0.3))
    lines = wrap(desc, 13.5, W - 44)
    assert len(lines) <= 2, (name, lines)
    for i, line in enumerate(lines):
        b.append(t(22, 92 + i * 19, line, 13.5, c["muted"]))
    b.append(viz_panel(c, 22, 128, W - 44, 118, spec))
    # footer: language (GitHub colour), size, licence, stars
    fy = H - 20
    b.append(f'<circle cx="26" cy="{fy - 4}" r="4.5" fill="{LANG_DOT[lang]}"/>')
    b.append(t(36, fy, lang, 12, c["muted"]))
    b.append(t(W - 22, fy, "  ·  ".join(facts), 12, c["text"], 600, anchor="end"))
    write(f"card-{key}", theme, svg(W, H, "".join(b), f"{name}: {desc} ({', '.join(facts)})"))



# ---------------------------------------------------------------- experience timeline
EXPERIENCE = [
    ("2026 – now", "Upwork", "Lead AI Research Scientist", "green",
     "Lead a 5-person team owning the job-post model behind Upwork's AI agent: post-training, continual "
     "learning, LLM-judge evals, A/B tests.", "1M+ daily users"),
    ("2024 – 2026", "Huawei Noah's Ark Lab", "Senior AI Researcher", "coral",
     "Post-trained robot VLAs (π0.5, GR00T, OpenVLA) and DiT world models; zero-shot 6D/9DoF pose "
     "estimation for warehouse robots.", "1st · NeurIPS BEHAVIOR"),
    ("2023 – 2024", "Vector Institute", "Machine Learning Engineer", "teal",
     "Multi-agent LLM workflows, hybrid RAG and pre-deployment LLM evaluation for CIBC and TD; trained 40+ "
     "startup engineers.", "+15% retrieval MRR"),
    ("2021 – 2023", "Trans-Plan", "Machine Learning Engineer", "amber",
     "Shipped a multi-camera 3D perception stack (detection, tracking, Re-ID, BEV) for traffic analytics.",
     "+28% MOTA"),
]


def timeline(c, theme):
    W, row = 880, 84
    H = 24 + row * len(EXPERIENCE)
    lx = 150
    b = [f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="{RADIUS}" fill="{c["card"]}" stroke="{c["border"]}"/>']
    for i in range(len(EXPERIENCE) - 1):
        y1, y2 = 40 + i * row, 40 + (i + 1) * row
        b.append(f'<line x1="{lx}" y1="{y1}" x2="{lx}" y2="{y2}" stroke="{c[EXPERIENCE[i + 1][3]]}" '
                 f'stroke-width="2" opacity="0.55"/>')
    for i, (when, org, role, hue, desc, hl) in enumerate(EXPERIENCE):
        y = 40 + i * row
        b.append(t(lx - 22, y + 5, when, 12.5, c["muted"], 500, True, "end"))
        if i == 0:
            b.append(f'<circle cx="{lx}" cy="{y}" r="11" fill="{c[hue]}" opacity="0.2">'
                     f'<animate attributeName="r" values="7;13;7" dur="2.6s" repeatCount="indefinite"/></circle>')
        b.append(f'<circle cx="{lx}" cy="{y}" r="6" fill="{c["card"]}" stroke="{c[hue]}" stroke-width="2.4"/>')
        b.append(f'<text x="{lx + 24}" y="{y + 6}" font-family="{SANS}" font-size="17" fill="{c["text"]}">'
                 f'<tspan font-weight="700">{escape(org)}</tspan>'
                 f'<tspan fill="{c["muted"]}" font-weight="400">  ·  {escape(role)}</tspan></text>')
        s, w = tchip(0, 0, hl, c, hue, size=11.5, h=24)
        b.append(f'<g transform="translate({W - 24 - w:.1f},{y - 12})">{s}</g>')
        assert lx + 24 + tw(org, 17, True) + tw(f"  ·  {role}", 17) < W - 30 - w, org
        lines = wrap(desc, 13, W - lx - 24 - 30)
        assert len(lines) <= 2, (org, lines)
        for j, line in enumerate(lines):
            b.append(t(lx + 24, y + 28 + j * 18, line, 13, c["muted"]))
    write("experience", theme, svg(W, H, "".join(b), "Experience: Upwork, Huawei Noah's Ark Lab, Vector Institute, "
                                   "Trans-Plan"))


# ---------------------------------------------------------------- toolbox
STACK = [
    ("Training", "blue", ["PyTorch", "JAX", "DeepSpeed", "FSDP", "TRL", "PEFT", "LoRA / QLoRA", "SFT · DPO · GRPO"]),
    ("Serving & agents", "green", ["vLLM", "SGLang", "TensorRT", "Triton", "LangGraph", "MCP", "RAG",
                                    "LLM-as-a-judge"]),
    ("Robotics", "coral", ["Isaac Sim", "MuJoCo", "ManiSkill", "OmniGibson", "LeRobot", "CALVIN", "ROS 2"]),
    ("Vision", "amber", ["SAM2", "DINOv2", "Diffusers", "Open3D", "PyTorch3D", "OpenCV", "OpenGL"]),
    ("Infra", "teal", ["Python", "C++", "AWS", "Slurm", "Kubernetes", "Ray", "Docker", "W&B"]),
]


def toolbox(c, theme):
    W, row = 880, 44
    H = 28 + row * len(STACK)
    b = [f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="{RADIUS}" fill="{c["card"]}" stroke="{c["border"]}"/>']
    for i, (cat, hue, items) in enumerate(STACK):
        y = 20 + i * row
        b.append(f'<rect x="26" y="{y + 5}" width="4" height="15" rx="2" fill="{c[hue]}"/>')
        b.append(t(42, y + 16.5, cat, 13, c["text"], 600))
        x = 190
        for it in items:
            s_, w = tchip(x, y, it, c, hue)
            b.append(s_)
            x += w + 8
        assert x < W - 16, (cat, x)
    write("toolbox", theme, svg(W, H, "".join(b), "Toolbox: " + "; ".join(
        f"{k}: {', '.join(v)}" for k, _, v in STACK)))


# ---------------------------------------------------------------- link buttons
# Real marks from the taste-skill icon resolver (assets/icons, credits in icons-credits.json).
# (file, label, icon file or None, how to colour it)
LINKS = [
    ("website", "Website", "ui-globe", "blue"),
    ("scholar", "Google Scholar", "googlescholar", None),
    ("huggingface", "Hugging Face", "hugging-face", None),
    ("linkedin", "LinkedIn", "linkedin", None),
    ("x", "X", "x", "ink"),
    ("forall", "Forall Labs", None, "blue"),
    ("cv", "Read my CV (PDF)", "ui-file-text", "blue"),
]


def icon(name, x, y, size, c, tone):
    import re
    src = (OUT / "icons" / f"{name}.svg").read_text()
    vb = re.search(r'viewBox="([^"]+)"', src).group(1)
    inner = re.sub(r"^<svg[^>]*>|</svg>\s*$", "", src.strip())
    if tone == "ink":
        # a black mark (X) takes the text colour, so it reads on both themes
        inner = re.sub(r'fill="#0{3}(0{3})?"', f'fill="{c["text"]}"', inner)
        inner = f'<g fill="{c["text"]}">{inner}</g>'
    colour = f' color="{c[tone]}"' if tone in ("blue", "teal", "amber", "coral", "green") else ""
    fill = ' fill="#4285F4"' if name == "googlescholar" else ""
    return (f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="{vb}"{colour}{fill} '
            f'preserveAspectRatio="xMidYMid meet">{inner}</svg>')


def link_button(c, theme, key, label, ic, tone):
    H, pad, isz, gap = 34, 13, 16, 8
    lw = tw(label, 13, True)
    W = round(pad + isz + gap + lw + pad)
    b = [f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="8" fill="{c["card"]}" stroke="{c["border"]}"/>']
    if ic:
        b.append(icon(ic, pad, (H - isz) / 2, isz, c, tone))
    else:  # Forall Labs has no mark; its name is the symbol for "for all"
        b.append(t(pad + isz / 2, H / 2 + 6, "∀", 17, c[tone], 700, anchor="middle"))
    b.append(t(pad + isz + gap, H / 2 + 4.6, label, 13, c["text"], 600))
    write(f"link-{key}", theme, svg(W, H, "".join(b), label))


for theme, c in THEMES.items():
    for l in LINKS:
        link_button(c, theme, *l)
    banner(c, theme)
    highlights(c, theme)
    for p in PROJECTS:
        card(c, theme, *p)
    timeline(c, theme)
    toolbox(c, theme)
print("wrote", len(list(OUT.glob("*.svg"))), "svgs to", OUT)
