#!/usr/bin/env python3
"""Собирает SVG-ассеты профиля: шапку, карточки флагманов, полосу MCP.

Шрифты и картинки вшиваются в SVG (base64): GitHub показывает SVG через <img>,
внешние ресурсы там не грузятся. Палитра и шрифты — как на лендингах флагманов.
Запуск: python3 tools/build.py  → assets/*.svg
"""
import base64, pathlib
from html import escape

ROOT = pathlib.Path(__file__).resolve().parent
SRC, OUT = ROOT / "src", ROOT.parent / "assets"

BG, SURFACE, LINE = "#111814", "#19221c", "#39453b"
TEXT, MUTED, AMBER, LIME, RED = "#eeece2", "#acb3a7", "#edb56d", "#cee19c", "#f8a198"


SUBSET = ROOT / ".subset"   # урезанные под текст ассетов шрифты, собираются в main
FONT_FILES = ["alumni-sans-latin-var.woff2", "alumni-sans-cyrillic-var.woff2",
              "jetbrains-mono-latin-400-normal.woff2", "onest-latin-400-normal.woff2",
              "onest-cyrillic-400-normal.woff2"]


def b64(name):
    p = SUBSET / name if (SUBSET / name).exists() else SRC / name
    return base64.b64encode(p.read_bytes()).decode()


def subset_fonts(texts):
    """Режет шрифты до символов, которые реально есть в ассетах. Без fonttools — полные шрифты."""
    import re, shutil, subprocess
    chars = set()
    for s in texts:
        for m in re.findall(r"<text[^>]*>(.*?)</text>", s):
            chars |= set(m) | set(m.upper()) | set(m.lower())
    chars |= set("&;")
    SUBSET.mkdir(exist_ok=True)
    text = "".join(sorted(chars))
    for f in FONT_FILES:
        cmd = ["uvx", "--from", "fonttools", "--with", "brotli", "pyftsubset", str(SRC / f),
               f"--text={text}", "--flavor=woff2", f"--output-file={SUBSET / f}"]
        if not shutil.which("uvx") or subprocess.run(cmd, capture_output=True).returncode:
            shutil.rmtree(SUBSET, ignore_errors=True)
            print("fonttools недоступен: шрифты вшиваются целиком")
            return


def fonts():
    face = "@font-face{{font-family:{f};src:url(data:font/woff2;base64,{d}) format('woff2');{extra}}}"
    return "".join([
        face.format(f="Alumni", d=b64("alumni-sans-latin-var.woff2"), extra="font-weight:100 900;"),
        face.format(f="Alumni", d=b64("alumni-sans-cyrillic-var.woff2"), extra="font-weight:100 900;unicode-range:U+0400-052F;"),
        face.format(f="Mono", d=b64("jetbrains-mono-latin-400-normal.woff2"), extra=""),
        face.format(f="Onest", d=b64("onest-latin-400-normal.woff2"), extra=""),
        face.format(f="Onest", d=b64("onest-cyrillic-400-normal.woff2"), extra="unicode-range:U+0400-052F;"),
    ])


BASE_CSS = f"""
.d{{font-family:Alumni,'Arial Narrow',sans-serif;font-weight:640;text-transform:uppercase;letter-spacing:.2px}}
.m{{font-family:Mono,ui-monospace,Menlo,monospace;letter-spacing:1.4px;text-transform:uppercase}}
.b{{font-family:Onest,system-ui,sans-serif}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
"""


def svg(w, h, body, css="", title=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}">'
            f'<title>{escape(title)}</title><style>{fonts()}{BASE_CSS}{css}</style>{body}</svg>')


def lines(x, y, rows, cls, size, fill, gap):
    return "".join(f'<text x="{x}" y="{y + i * gap}" class="{cls}" font-size="{size}" fill="{fill}">{escape(r)}</text>'
                   for i, r in enumerate(rows))



# Первый кадр каждой анимации — полная картинка: если анимация стоит, карточка всё равно законченная.
# Только бесконечные анимации: одноразовые (появление с задержкой) Chrome в SVG-картинке
# замораживает на первом кадре, и элемент остаётся невидимым (проверено на живом профиле).
# Размеры шрифтов подобраны под показ на GitHub: шапка и полоса MCP ужимаются примерно
# до 0.65, карточки в две колонки — до 0.48. Мельче 16px в карточке не читается.

# ---------- шапка ----------
def hero():
    W, H = 1280, 520
    css = """
@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:0}}
@keyframes sweep{0%{transform:translateY(-120px)}100%{transform:translateY(640px)}}
.caret{animation:blink 1.1s steps(1) infinite}
.scan{animation:sweep 7s linear infinite}
"""
    stats = [("2612", "API METHODS OVER MCP"), ("34", "SMB SKILLS"), ("0", "AI INSIDE CORDON")]
    st = "".join(
        f'<g class="s{i+1}"><text x="{64 + i*250}" y="440" class="d" font-size="62" fill="{AMBER}">{n}</text>'
        f'<text x="{64 + i*250}" y="474" class="m" font-size="16" fill="{MUTED}">{escape(l)}</text></g>'
        for i, (n, l) in enumerate(stats))
    body = f"""
<defs>
 <linearGradient id="fade" x1="0" x2="1"><stop offset="0" stop-color="{BG}"/><stop offset=".40" stop-color="{BG}"/><stop offset=".64" stop-color="{BG}" stop-opacity=".35"/><stop offset="1" stop-color="{BG}" stop-opacity="0"/></linearGradient>
 <linearGradient id="bot" x1="0" y1="0" x2="0" y2="1"><stop offset=".6" stop-color="{BG}" stop-opacity="0"/><stop offset="1" stop-color="{BG}"/></linearGradient>
 <linearGradient id="band" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{AMBER}" stop-opacity="0"/><stop offset=".5" stop-color="{AMBER}" stop-opacity=".10"/><stop offset="1" stop-color="{AMBER}" stop-opacity="0"/></linearGradient>
 <clipPath id="c"><rect width="{W}" height="{H}" rx="14"/></clipPath>
</defs>
<g clip-path="url(#c)">
 <rect width="{W}" height="{H}" fill="{BG}"/>
 <image x="330" y="-30" width="1000" height="580" preserveAspectRatio="xMidYMid slice" href="data:image/jpeg;base64,{b64('hero.jpg')}"/>
 <rect width="{W}" height="{H}" fill="url(#fade)"/>
 <rect width="{W}" height="{H}" fill="url(#bot)"/>
 <rect class="scan" x="560" y="0" width="720" height="110" fill="url(#band)"/>
 <text x="64" y="80" class="m" font-size="18" fill="{AMBER}">ILYA UTOV / AI FRONTIER LAB</text>
 <line x1="64" y1="102" x2="200" y2="102" stroke="{AMBER}" stroke-width="1.5"/>
 <text x="60" y="194" class="d" font-size="100" fill="{TEXT}">AI tools that do</text>
 <text x="60" y="288" class="d" font-size="100" fill="{AMBER}">the actual work.</text>
 <rect class="caret" x="622" y="214" width="32" height="76" fill="{AMBER}"/>
 {lines(64, 338, ["Agent skills, MCP servers and on-prem systems.",
                  "The math runs in code, the data comes from registries."], "b", 23, MUTED, 32)}
 <line x1="64" y1="386" x2="760" y2="386" stroke="{LINE}"/>
 {st}
 <rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="{LINE}"/>
</g>"""
    return svg(W, H, body, css, "Ilya Utov — AI tools that do the actual work")


# ---------- карточка флагмана ----------
def card(num, kicker, title, accent, body_rows, url, img, widget, wcss, alt, solid=".30"):
    W, H = 840, 460
    body = f"""
<defs>
 <linearGradient id="f" x1="0" x2="1"><stop offset="{solid}" stop-color="{BG}"/><stop offset=".68" stop-color="{BG}" stop-opacity=".55"/><stop offset="1" stop-color="{BG}" stop-opacity=".05"/></linearGradient>
 <clipPath id="c"><rect width="{W}" height="{H}" rx="14"/></clipPath>
</defs>
<g clip-path="url(#c)">
 <rect width="{W}" height="{H}" fill="{BG}"/>
 <image x="{W-620}" y="0" width="620" height="{H}" preserveAspectRatio="xMidYMid slice" href="data:image/jpeg;base64,{b64(img)}"/>
 <rect width="{W}" height="{H}" fill="url(#f)"/>
 <text x="40" y="62" class="m" font-size="19" fill="{AMBER}">{num} / {escape(kicker)}</text>
 <text x="37" y="138" class="d" font-size="70" fill="{TEXT}">{escape(title)}</text>
 <text x="37" y="202" class="d" font-size="70" fill="{AMBER}">{escape(accent)}</text>
 {lines(40, 250, body_rows, "b", 25, MUTED, 34)}
 {widget}
 <line x1="40" y1="392" x2="{W-40}" y2="392" stroke="{LINE}"/>
 <text x="40" y="430" class="m" font-size="19" fill="{TEXT}" style="text-transform:none">{escape(url)}</text>
 <text x="{W-40}" y="432" text-anchor="end" class="m" font-size="26" fill="{AMBER}">→</text>
 <rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="{LINE}"/>
</g>"""
    return svg(W, H, body, wcss, alt)


def humanizer():
    css = """
@keyframes fill{0%,55%{width:300px}62%,70%{width:90px}95%,100%{width:300px}}
@keyframes lo{0%,57%{opacity:0}60%,78%{opacity:1}82%,100%{opacity:0}}
@keyframes hi{0%,55%{opacity:1}58%,80%{opacity:0}85%,100%{opacity:1}}
.bar{animation:fill 6s ease-in-out infinite}.lo{animation:lo 6s infinite}.hi{animation:hi 6s infinite}
"""
    w = f"""
 <text x="40" y="350" class="m" font-size="18" fill="{MUTED}">PURITY</text>
 <rect x="134" y="334" width="320" height="18" rx="9" fill="{SURFACE}" stroke="{LINE}"/>
 <rect class="bar" x="134" y="334" width="300" height="18" rx="9" fill="{AMBER}"/>
 <text class="lo d" x="472" y="354" font-size="38" fill="{RED}" opacity="0">38</text>
 <text class="hi d" x="472" y="354" font-size="38" fill="{LIME}">94</text>
 <text x="516" y="354" class="m" font-size="18" fill="{MUTED}">/100</text>"""
    return card("01", "SKILL · RUSSIAN TEXT", "Strips the AI", "from Russian text.",
                ["Bureaucratese, calques, the tells", "of ChatGPT. Scanner included."],
                "github.com/ilyautov/humanizer-ru", "humanizer.jpg", w, css,
                "humanizer-ru — strips AI tells out of Russian text", solid=".50")


def inn():
    css = """
@keyframes l1{0%,40%{opacity:1}45%,55%{opacity:.2}60%,100%{opacity:1}}
@keyframes l2{0%,55%{opacity:1}60%,70%{opacity:.2}75%,100%{opacity:1}}
@keyframes l3{0%,70%{opacity:1}75%,85%{opacity:.2}90%,100%{opacity:1}}
.g{animation:l1 4.5s infinite}.y{animation:l2 4.5s infinite}.r{animation:l3 4.5s infinite}
"""
    w = f"""
 <rect x="40" y="318" width="150" height="50" rx="25" fill="{SURFACE}" stroke="{LINE}"/>
 <circle class="g" cx="72" cy="343" r="13" fill="#7ccf85"/>
 <circle class="y" cx="115" cy="343" r="13" fill="{AMBER}"/>
 <circle class="r" cx="158" cy="343" r="13" fill="#e8705f"/>
 <text x="212" y="350" class="m" font-size="18" fill="{TEXT}">EVERY FACT HAS A SOURCE</text>"""
    return card("02", "SKILL · MCP · CLI", "One tax ID.", "A sourced dossier.",
                ["Status, finances, debts, courts", "and owners of a Russian company."],
                "github.com/ilyautov/inn-check-ru", "inn.jpg", w, css,
                "inn-check-ru — a sourced company dossier by Russian tax ID")


def cordon():
    css = """
@keyframes call{0%,70%{opacity:1;transform:none}74%,78%{opacity:0;transform:translateX(-12px)}84%,100%{opacity:1;transform:none}}
@keyframes stamp{0%,70%{opacity:1;transform:scale(1) rotate(-7deg)}74%,88%{opacity:0;transform:scale(1.8) rotate(-7deg)}94%,100%{opacity:1;transform:scale(1) rotate(-7deg)}}
.call{animation:call 5s ease-out infinite}
.stamp{transform-box:fill-box;transform-origin:center;transform:rotate(-7deg);animation:stamp 5s cubic-bezier(.2,.9,.3,1.2) infinite}
"""
    w = f"""
 <g class="call">
  <rect x="40" y="316" width="270" height="56" rx="6" fill="{AMBER}"/>
  <text x="58" y="352" class="m" font-size="21" fill="{BG}">send_email →</text>
 </g>
 <g class="stamp">
  <rect x="332" y="314" width="176" height="60" rx="4" fill="{BG}" stroke="{RED}" stroke-width="3.5"/>
  <text x="420" y="357" text-anchor="middle" class="d" font-size="40" fill="{RED}">REFUSED</text>
 </g>"""
    return card("03", "PROMPT-INJECTION FIREWALL", "Reads anything.", "Obeys only you.",
                ["No AI inside: plain code decides,", "so it cannot be talked round."],
                "github.com/ilyautov/cordon", "cordon.jpg", w, css,
                "Cordon — your agent reads anything and takes orders only from you")


def smb():
    css = """
@keyframes tick{0%,75%{opacity:1}80%,86%{opacity:0}92%,100%{opacity:1}}
.t1{animation:tick 6s infinite}.t2{animation:tick 6s .5s infinite}
"""
    rows = [("taxes, cash, payroll", "COMPUTED", LIME), ("the model's guess", "NEVER", RED)]
    w = "".join(
        f'<g class="t{i+1}"><text x="40" y="{334 + i*36}" class="b" font-size="23" fill="{TEXT}">{escape(a)}</text>'
        f'<text x="300" y="{334 + i*36}" class="m" font-size="18" fill="{c}">{b}</text></g>'
        for i, (a, b, c) in enumerate(rows))
    return card("04", "34 SKILLS · SMALL BUSINESS", "AI that doesn't", "lie with numbers.",
                ["Taxes, cash, contracts, checks", "for Russian small business."],
                "github.com/ilyautov/small-business-ru", "smb.jpg", w, css,
                "small-business-ru — 34 AI skills for Russian small business")


# ---------- заголовок раздела MCP ----------
def mcp():
    W, H = 1280, 210
    body = f"""
<defs><clipPath id="c"><rect width="{W}" height="{H}" rx="14"/></clipPath></defs>
<g clip-path="url(#c)">
 <rect width="{W}" height="{H}" fill="{SURFACE}"/>
 <text x="64" y="62" class="m" font-size="18" fill="{AMBER}">05 / MCP SERVERS · 2612 API METHODS</text>
 <text x="61" y="140" class="d" font-size="70" fill="{TEXT}">Into Russian business.<tspan fill="{AMBER}" dx="20">Bundle or solo.</tspan></text>
 <text x="64" y="186" class="m" font-size="16" fill="{MUTED}">OFFICIAL APIS · NO BROWSER · NO SCRAPING · SAFETY GATE BEFORE EVERY WRITE</text>
 <rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="{LINE}"/>
</g>"""
    return svg(W, H, body, "", "MCP servers for Russian business systems: take a bundle or one service")


# ---------- плитки MCP-серверов ----------
TILES = [
    # (файл, группа, название, число, единица, репо, сборник)
    ("marketplaces", "BUNDLE · 4 SERVERS", "Marketplaces", "1022", "METHODS", "marketplaces-mcp-ru", True),
    ("ozon", "MARKETPLACE", "Ozon Seller", "441", "+ 45 ADS", "ozon-mcp-ru", False),
    ("wildberries", "MARKETPLACE", "Wildberries", "307", "METHODS", "wildberries-mcp-ru", False),
    ("yandex-market", "MARKETPLACE", "Yandex Market", "165", "METHODS", "yandex-market-mcp-ru", False),
    ("avito", "MARKETPLACE", "Avito", "64", "METHODS", "avito-mcp-ru", False),
    ("moysklad", "ERP", "MoySklad", "892", "METHODS", "moysklad-mcp-ru", False),
    ("business", "BUNDLE · 5 SERVERS", "Business", "698", "METHODS", "business-mcp-ru", True),
    ("hh", "HIRING", "hh.ru", "133", "METHODS", "hh-mcp-ru", False),
    ("vk", "SOCIAL · SHOP · ADS", "VK", "373", "METHODS", "vk-mcp-ru", False),
    ("diadoc", "EDI · KONTUR", "Diadoc", "114", "METHODS", "diadoc-mcp-ru", False),
    ("sbis", "EDI · SABY", "SBIS", "45", "COMMANDS", "sbis-mcp-ru", False),
    ("chestny-znak", "PRODUCT MARKING", "Chestny ZNAK", "33", "METHODS", "chestny-znak-mcp-ru", False),
]


def tile(group, name, num, unit, repo, bundle):
    W, H = 420, 250
    edge = AMBER if bundle else LINE
    bg = BG if bundle else SURFACE
    body = f"""
<defs><clipPath id="c"><rect width="{W}" height="{H}" rx="12"/></clipPath></defs>
<g clip-path="url(#c)">
 <rect width="{W}" height="{H}" fill="{bg}"/>
 <text x="28" y="48" class="m" font-size="18" fill="{AMBER if bundle else MUTED}">{escape(group)}</text>
 <text x="26" y="112" class="d" font-size="56" fill="{TEXT}">{escape(name)}</text>
 <text x="25" y="190" class="d" font-size="84" fill="{AMBER}">{num}<tspan class="m" font-size="18" fill="{MUTED}" dx="16">{escape(unit)}</tspan></text>
 <text x="28" y="230" class="m" font-size="18" fill="{TEXT}" style="text-transform:none">{repo}</text>
 <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="12" fill="none" stroke="{edge}" stroke-width="{2 if bundle else 1}"/>
</g>"""
    return svg(W, H, body, "", f"{repo}: {name}, {num} {unit.lower()}")


def assets():
    out = [("hero", hero), ("card-humanizer-ru", humanizer), ("card-inn-check-ru", inn),
           ("card-cordon", cordon), ("card-small-business-ru", smb), ("mcp", mcp)]
    out += [(f"mcp-{f}", (lambda a=a: tile(*a))) for f, *a in TILES]
    return out


if __name__ == "__main__":
    import shutil
    OUT.mkdir(exist_ok=True)
    shutil.rmtree(SUBSET, ignore_errors=True)
    subset_fonts([fn() for _, fn in assets()])
    for name, fn in assets():
        p = OUT / f"{name}.svg"
        p.write_text(fn(), encoding="utf-8")
        print(f"{p.name}: {p.stat().st_size // 1024} KB")
    shutil.rmtree(SUBSET, ignore_errors=True)
