"""Regenerate the social preview image (Open Graph / Twitter card), 1200x630.

Usage (in a throwaway virtualenv with fonttools, brotli and pillow):
  python _tools/make_og_image.py assets/fonts/inter-tight-latin-variable.woff2 assets/images/og.png
Text comes from the arguments below; keep it in step with _config.yml.
"""
import sys, tempfile, os
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from PIL import Image, ImageDraw, ImageFont

src, out = sys.argv[1], sys.argv[2]
NAME = ["Giacomo", "Benincasa"]
TAGLINE = "Senior Software Engineer & Researcher"
TOPICS = "Distributed systems · Cloud platforms · Networking research"
DOMAIN = "gbenin.casa"
INK, MUTED, RULE, ORANGE, BG = "#111111", "#6b6b6b", "#dddddd", "#ff4a1c", "#ffffff"
W, H, M = 1200, 630, 80
SS = 2  # supersample

tmp = tempfile.mkdtemp()
def weight(w):
    f = instantiateVariableFont(TTFont(src), {"wght": w}); p = os.path.join(tmp, f"w{w}.ttf"); f.save(p); return p
f800, f500, f400 = weight(800), weight(500), weight(400)

im = Image.new("RGB", (W*SS, H*SS), BG); d = ImageDraw.Draw(im)
def font(path, px): return ImageFont.truetype(path, px*SS)
def text(x, y, s, path, px, fill, tracking=0.0):
    """Draw s with baseline at y; tracking in em (like CSS letter-spacing)."""
    f = font(path, px); cx = x*SS
    for i, ch in enumerate(s):
        d.text((cx, y*SS), ch, font=f, fill=fill, anchor="ls")
        nxt = s[i+1] if i+1 < len(s) else ""
        adv = f.getlength(ch + nxt) - f.getlength(nxt) if nxt else f.getlength(ch)
        cx += adv + tracking*px*SS
    return cx/SS

# top bar: domain + rule, like the site header
text(M, M+20, DOMAIN, f500, 26, INK)
d.rectangle([M*SS, (M+44)*SS, (W-M)*SS, (M+44)*SS + 2*SS], fill=INK)
# name, two lines, heavy and tight, orange full stop
size, lh = 138, 0.92
y1 = 300; y2 = y1 + size*lh
text(M, y1, NAME[0], f800, size, INK, -0.045)
end = text(M, y2, NAME[1], f800, size, INK, -0.045)
text(end, y2, ".", f800, size, ORANGE)
# bottom: rule, tagline and topics
d.rectangle([M*SS, (H-150)*SS, (W-M)*SS, (H-150)*SS + 1*SS], fill=RULE)
text(M, H-100, TAGLINE, f500, 34, INK)
text(M, H-58, TOPICS, f400, 26, MUTED)

im.resize((W, H), Image.LANCZOS).save(out, optimize=True)
print("wrote", out)
