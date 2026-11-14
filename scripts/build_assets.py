"""Generate the profile README's SVG assets (light + dark) into ../assets.

Run:  python scripts/build_assets.py   (needs Pillow for text measurement)
Every visual is a static, self-hosted SVG, so nothing on the profile depends
on a third-party stats service. Edit the DATA section and re-run to update.
"""
from pathlib import Path
from html import escape
from PIL import ImageFont

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"

THEMES = {
    "dark": dict(bg="#0d1117", card="#151b23", card2="#10161e", border="#2a313c", text="#e6edf3",
                 muted="#9198a1", faint="#3d444d", grid="#1f2630", a1="#7aa2ff", a2="#3fd0c9", a3="#c297ff",
                 chip="#1b2330"),
    "light": dict(bg="#ffffff", card="#f6f8fa", card2="#ffffff", border="#d1d9e0", text="#1f2328",
                  muted="#59636e", faint="#c8d1da", grid="#e6ebf0", a1="#3657d6", a2="#0b8a83", a3="#7c4dce",
                  chip="#ffffff"),
}

# ---------------------------------------------------------------- text metrics
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


def t(x, y, s, size, fill, weight=400, mono=False, anchor="start", ls=None, extra=""):
    fam = MONO if mono else SANS
    lsp = f' letter-spacing="{ls}"' if ls is not None else ""
    return (f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}"{lsp}{extra}>{escape(s)}</text>')


def chip(x, y, label, c, size=12, h=24, mono=False, color=None):
    w = tw(label, size, mono=mono) + 20
    return (f'<rect x="{x}" y="{y}" width="{w:.1f}" height="{h}" rx="{h/2}" fill="{c["chip"]}" '
            f'stroke="{c["border"]}"/>'
            + t(x + w / 2, y + h / 2 + size * 0.36, label, size, color or c["text"], 500, mono, "middle")), w


def write(name, theme, content):
    (OUT / f"{name}-{theme}.svg").write_text(content)


# ---------------------------------------------------------------- banner
def banner(c, theme):
    W, H = 880, 280
    b = [f'<defs>'
         f'<linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c["a1"]}"/>'
         f'<stop offset="1" stop-color="{c["a2"]}"/></linearGradient>'
         f'<linearGradient id="bgg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c["card"]}"/>'
         f'<stop offset="1" stop-color="{c["card2"]}"/></linearGradient>'
         f'<radialGradient id="glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{c["a1"]}" '
         f'stop-opacity="{0.18 if theme == "dark" else 0.10}"/><stop offset="1" stop-color="{c["a1"]}" stop-opacity="0"/>'
         f'</radialGradient>'
         f'<clipPath id="clip"><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="16"/></clipPath>'
         f'</defs>',
         f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="url(#bgg)" stroke="{c["border"]}"/>',
         f'<g clip-path="url(#clip)">']
    # dot grid on the right
    for gx in range(560, W, 22):
        for gy in range(18, H, 22):
            b.append(f'<circle cx="{gx}" cy="{gy}" r="1.2" fill="{c["grid"]}"/>')
    b.append(f'<circle cx="720" cy="140" r="170" fill="url(#glow)"/>')
    # small network: 3 -> 4 -> 4 -> 2, with signals travelling along a few edges
    layers = [[95, 140, 185], [70, 115, 165, 210], [70, 115, 165, 210], [115, 165]]
    xs = [610, 680, 750, 820]
    nodes = [[(xs[i], y) for y in ys] for i, ys in enumerate(layers)]
    for i in range(len(nodes) - 1):
        for (x1, y1) in nodes[i]:
            for (x2, y2) in nodes[i + 1]:
                b.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c["faint"]}" stroke-width="1" '
                         f'opacity="0.7"/>')
    routes = [[(0, 0), (1, 1), (2, 2), (3, 1)], [(0, 2), (1, 3), (2, 1), (3, 0)], [(0, 1), (1, 0), (2, 3), (3, 1)]]
    for k, r in enumerate(routes):
        pts = [nodes[l][n] for l, n in r]
        d = "M" + " L".join(f"{x},{y}" for x, y in pts)
        b.append(f'<path d="{d}" fill="none" stroke="url(#g)" stroke-width="1.6" opacity="0.55"/>')
        dur = 3.2 + k * 0.7
        b.append(f'<circle r="3" fill="{c["a2"] if k % 2 else c["a1"]}"><animateMotion dur="{dur}s" '
                 f'repeatCount="indefinite" begin="{k * 0.9}s" path="{d}"/>'
                 f'<animate attributeName="opacity" values="0;1;1;0" dur="{dur}s" begin="{k * 0.9}s" '
                 f'repeatCount="indefinite"/></circle>')
    for li, layer in enumerate(nodes):
        for ni, (x, y) in enumerate(layer):
            b.append(f'<circle cx="{x}" cy="{y}" r="6.5" fill="{c["card"]}" stroke="url(#g)" stroke-width="1.8"/>')
            delay = (li * 0.45 + ni * 0.2) % 3
            b.append(f'<circle cx="{x}" cy="{y}" r="2.4" fill="{c["a1"] if li % 2 == 0 else c["a2"]}">'
                     f'<animate attributeName="opacity" values="0.35;1;0.35" dur="3s" begin="{delay:.2f}s" '
                     f'repeatCount="indefinite"/></circle>')
    b.append('</g>')
    # left text block
    x0 = 44
    b.append(f'<rect x="{x0}" y="40" width="8" height="8" rx="2" fill="url(#g)"/>')
    b.append(t(x0 + 16, 48, "AI RESEARCH SCIENTIST  ·  TORONTO", 12, c["muted"], 600, True, ls=1.2))
    b.append(t(x0 - 2, 98, "Sajjad Pakdamansavoji", 40, c["text"], 700, ls=-0.6))
    b.append(t(x0, 130, "Lead AI Research Scientist at Upwork", 18, c["a1"], 600))
    tag = ("I train, post-train and evaluate foundation models, from LLM agents and VLMs "
           "to robot VLAs and world models.")
    for i, line in enumerate(wrap(tag, 15, 470)):
        b.append(t(x0, 164 + i * 22, line, 15, c["muted"]))
    x = x0
    for lab in ["LLM post-training", "LLM agents", "Robot VLAs", "World models", "3D vision"]:
        s, w = chip(x, 220, lab, c, size=12)
        b.append(s)
        x += w + 8
    assert x < 560, f"banner chips overflow: {x}"
    write("banner", theme, svg(W, H, "".join(b), "Sajjad Pakdamansavoji, Lead AI Research Scientist at Upwork"))


# ---------------------------------------------------------------- highlights
HIGHLIGHTS = [
    ("1st", "place, NeurIPS 2026", "BEHAVIOR Challenge"),
    ("1M+", "daily users on the model", "my team post-trains"),
    ("13", "papers and preprints on", "LLMs, robots, 3D vision"),
    ("3", "patents on robot VLAs,", "world models, 3D vision"),
]


def highlights(c, theme):
    W, H, gap = 880, 112, 14
    tw_ = (W - gap * 3) / 4
    b = [f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c["a1"]}"/>'
         f'<stop offset="1" stop-color="{c["a2"]}"/></linearGradient></defs>']
    for i, (num, l1, l2) in enumerate(HIGHLIGHTS):
        x = i * (tw_ + gap)
        b.append(f'<rect x="{x + 0.5}" y="0.5" width="{tw_ - 1}" height="{H - 1}" rx="12" fill="{c["card"]}" '
                 f'stroke="{c["border"]}"/>')
        b.append(f'<rect x="{x + 18}" y="18" width="22" height="3" rx="1.5" fill="url(#g)"/>')
        b.append(t(x + 18, 58, num, 30, c["text"], 700, ls=-0.5))
        for j, line in enumerate((l1, l2)):
            assert tw(line, 12.5) < tw_ - 30, line
            b.append(t(x + 18, 80 + j * 17, line, 12.5, c["muted"]))
    write("highlights", theme, svg(W, H, "".join(b), "Highlights: 1st place NeurIPS 2026 BEHAVIOR Challenge; "
                                   "1M+ daily users; 13 papers and preprints; 3 patents"))


# ---------------------------------------------------------------- project cards
PROJECTS = [
    ("calvin-max", "CALVIN-MAX", "ROBOT LEARNING · BENCHMARK", "forall-labs",
     "When does a mid-execution change hurt a robot policy? Paired Base, Pre and Mid runs on CALVIN's "
     "long-horizon chains.",
     ["7,828 cases", "10 policies", "−4.4 to −9.9 pts"]),
    ("opencap", "OpenCaP", "CODE AS POLICIES · LLM EVAL", "forall-labs",
     "How open-weight LLMs fail at writing robot code, and the smallest verified fix for each failure.",
     ["7,560 trials", "21 open LLMs", "6 defect families"]),
    ("autopolish", "AutoPolish", "VISION · GENERATIVE EDITING", "forall-labs",
     "A training-free loop where persona-conditioned Qwen2-VL critics steer FLUX.1 Kontext toward "
     "better image aesthetics.",
     ["Training-free", "Synthetic audience", "0.96 human agreement"]),
    ("awesome-wsp", "Awesome WSP", "AGENTS · LIVING RESEARCH MAP", "SajjadPSavoji",
     "A daily-updated map of LLMs that read, edit and write neural network weights, curated by an "
     "autonomous agent.",
     ["600+ entries", "Updated daily", "Agent-run PR review"]),
    ("minivlmdoceval", "MiniVLMDocEval", "VLMS · DOCUMENT AI", "SajjadPSavoji",
     "Are sub-1B VLMs ready for documents? Six open models on five benchmarks, plus a pre-registered "
     "fine-tuning study.",
     ["6 VLMs", "5 benchmarks", "VLMEvalKit"]),
    ("colabctl", "colabctl", "DEV TOOLING · GPU RUNTIMES", "SajjadPSavoji",
     "Scriptable connect, status and disconnect for Google Colab GPU runtimes, so scripts and agents can "
     "drive them.",
     ["Stdlib-only Python", "CLI", "Agent-friendly"]),
]


def card(c, theme, key, name, kicker, owner, desc, chips):
    W, H = 432, 196
    b = [f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c["a1"]}"/>'
         f'<stop offset="1" stop-color="{c["a2"]}"/></linearGradient>'
         f'<clipPath id="cc"><rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12"/></clipPath></defs>',
         f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="{c["card"]}" stroke="{c["border"]}"/>',
         f'<rect x="0" y="0" width="{W}" height="3" fill="url(#g)" clip-path="url(#cc)"/>']
    b.append(t(22, 34, kicker, 11, c["a1"], 600, True, ls=0.8))
    b.append(t(W - 22, 34, owner, 11, c["muted"], 400, True, "end"))
    b.append(t(22, 68, name, 22, c["text"], 700, ls=-0.3))
    lines = wrap(desc, 13.5, W - 44)
    assert len(lines) <= 3, (name, lines)
    for i, line in enumerate(lines):
        b.append(t(22, 94 + i * 19, line, 13.5, c["muted"]))
    x = 22
    for lab in chips:
        s, w = chip(x, H - 42, lab, c, size=11.5, h=24)
        b.append(s)
        x += w + 7
    assert x < W - 10, (name, x)
    write(f"card-{key}", theme, svg(W, H, "".join(b), f"{name}: {desc}"))


# ---------------------------------------------------------------- experience timeline
EXPERIENCE = [
    ("2026 – now", "Upwork", "Lead AI Research Scientist",
     "Lead a 5-person team owning the job-post model behind Upwork's AI agent: post-training, continual "
     "learning, LLM-judge evals, A/B tests.", "1M+ daily users"),
    ("2024 – 2026", "Huawei Noah's Ark Lab", "Senior AI Researcher",
     "Post-trained robot VLAs (π0.5, GR00T, OpenVLA) and DiT world models; zero-shot 6D/9DoF pose "
     "estimation for warehouse robots.", "1st · NeurIPS BEHAVIOR"),
    ("2023 – 2024", "Vector Institute", "Machine Learning Engineer",
     "Multi-agent LLM workflows, hybrid RAG and pre-deployment LLM evaluation for CIBC and TD; trained 40+ "
     "startup engineers.", "+15% retrieval MRR"),
    ("2021 – 2023", "Trans-Plan", "Machine Learning Engineer",
     "Shipped a multi-camera 3D perception stack (detection, tracking, Re-ID, BEV) for traffic analytics.",
     "+28% MOTA"),
]


def timeline(c, theme):
    W, row = 880, 84
    H = 24 + row * len(EXPERIENCE)
    lx = 150
    b = [f'<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c["a1"]}"/>'
         f'<stop offset="1" stop-color="{c["a2"]}" stop-opacity="0.3"/></linearGradient></defs>',
         f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="{c["card"]}" stroke="{c["border"]}"/>',
         f'<line x1="{lx}" y1="36" x2="{lx}" y2="{H - 30}" stroke="url(#g)" stroke-width="2"/>']
    for i, (when, org, role, desc, hl) in enumerate(EXPERIENCE):
        y = 40 + i * row
        b.append(t(lx - 22, y + 5, when, 12.5, c["muted"], 500, True, "end"))
        if i == 0:
            b.append(f'<circle cx="{lx}" cy="{y}" r="11" fill="{c["a1"]}" opacity="0.18">'
                     f'<animate attributeName="r" values="7;13;7" dur="2.6s" repeatCount="indefinite"/></circle>')
        b.append(f'<circle cx="{lx}" cy="{y}" r="6" fill="{c["card"]}" stroke="{c["a1"] if i == 0 else c["a2"]}" '
                 f'stroke-width="2.2"/>')
        b.append(f'<text x="{lx + 24}" y="{y + 6}" font-family="{SANS}" font-size="17" fill="{c["text"]}">'
                 f'<tspan font-weight="700">{escape(org)}</tspan>'
                 f'<tspan fill="{c["muted"]}" font-weight="400">  ·  {escape(role)}</tspan></text>')
        s, w = chip(0, 0, hl, c, size=11.5, h=24, mono=True, color=c["a1"])
        b.append(f'<g transform="translate({W - 24 - w:.1f},{y - 12})">{s}</g>')
        head = tw(org, 17, True) + tw(f"  ·  {role}", 17)
        assert lx + 24 + head < W - 30 - w, org
        lines = wrap(desc, 13, W - lx - 24 - 30)
        assert len(lines) <= 2, (org, lines)
        for j, line in enumerate(lines):
            b.append(t(lx + 24, y + 28 + j * 18, line, 13, c["muted"]))
    write("experience", theme, svg(W, H, "".join(b), "Experience: Upwork, Huawei Noah's Ark Lab, Vector Institute, "
                                   "Trans-Plan"))


# ---------------------------------------------------------------- toolbox
STACK = [
    ("Training", ["PyTorch", "JAX", "DeepSpeed", "FSDP", "TRL", "PEFT", "LoRA / QLoRA", "SFT · DPO · GRPO"]),
    ("Serving & agents", ["vLLM", "SGLang", "TensorRT", "Triton", "LangGraph", "MCP", "RAG", "LLM-as-a-judge"]),
    ("Robotics", ["Isaac Sim", "MuJoCo", "ManiSkill", "OmniGibson", "LeRobot", "CALVIN", "ROS 2"]),
    ("Vision", ["SAM2", "DINOv2", "Diffusers", "Open3D", "PyTorch3D", "OpenCV", "OpenGL"]),
    ("Infra", ["Python", "C++", "AWS", "Slurm", "Kubernetes", "Ray", "Docker", "W&B"]),
]


def toolbox(c, theme):
    W, row = 880, 44
    H = 28 + row * len(STACK)
    colors = [c["a1"], c["a2"], c["a3"], c["a1"], c["a2"]]
    b = [f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="{c["card"]}" stroke="{c["border"]}"/>']
    for i, (cat, items) in enumerate(STACK):
        y = 20 + i * row
        b.append(f'<circle cx="30" cy="{y + 12}" r="4" fill="{colors[i]}"/>')
        b.append(t(44, y + 16.5, cat, 13, c["text"], 600))
        x = 190
        for it in items:
            s, w = chip(x, y, it, c, size=12, h=25)
            b.append(s)
            x += w + 8
        assert x < W - 16, (cat, x)
    write("toolbox", theme, svg(W, H, "".join(b), "Toolbox: " + "; ".join(f"{k}: {', '.join(v)}" for k, v in STACK)))


for theme, c in THEMES.items():
    banner(c, theme)
    highlights(c, theme)
    for p in PROJECTS:
        card(c, theme, *p)
    timeline(c, theme)
    toolbox(c, theme)
print("wrote", len(list(OUT.glob("*.svg"))), "svgs to", OUT)
