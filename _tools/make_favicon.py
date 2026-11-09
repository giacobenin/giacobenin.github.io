"""Regenerate the favicons ("g." in Inter Tight 800, orange dot) from the site's font.

Usage (in a throwaway virtualenv with fonttools, brotli and pillow):
  python _tools/make_favicon.py assets/fonts/inter-tight-latin-variable.woff2 OUTDIR
then copy favicon.svg, favicon.ico and apple-touch-icon.png from OUTDIR to the
repo root. OUTDIR also gets an instanced TTF and preview PNGs (don't commit).
"""
import sys
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen
from PIL import Image, ImageDraw, ImageFont
src, out = sys.argv[1], sys.argv[2]
f = TTFont(src); print("axes", [(a.axisTag, a.minValue, a.maxValue) for a in f["fvar"].axes])
f = instantiateVariableFont(f, {"wght": 800}); ttf = out + "/it800.ttf"; f.save(ttf)
upm = f["head"].unitsPerEm; cmap = f.getBestCmap(); gs = f.getGlyphSet()
g, dot = cmap[ord("g")], cmap[ord(".")]
ls = -0.045 * upm                          # same letter-spacing as the titles
dx = gs[g].width + ls                       # pen x of the dot
INK, ORANGE, BG = "#111111", "#ff4a1c", "#ffffff"
def bounds():
    bp = BoundsPen(gs); gs[g].draw(bp); b1 = bp.bounds
    bp = BoundsPen(gs); gs[dot].draw(TransformPen(bp, (1,0,0,1,dx,0))); b2 = bp.bounds
    return min(b1[0],b2[0]), min(b1[1],b2[1]), max(b1[2],b2[2]), max(b1[3],b2[3])
x0,y0,x1,y1 = bounds(); w,h = x1-x0, y1-y0
def layout(N, fill):
    s = fill * N / max(w,h)                 # px per font unit
    ox = (N - w*s)/2 - x0*s                 # x of origin
    by = (N - h*s)/2 + y1*s                 # baseline y (y-down)
    return s, ox, by
# SVG (viewBox 64)
N = 64; s, ox, by = layout(N, 0.80)
def path(name, tx):
    p = SVGPathPen(gs); gs[name].draw(TransformPen(p, (1,0,0,1,tx,0))); return p.getCommands()
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {N} {N}"><rect width="{N}" height="{N}" rx="10" fill="{BG}"/><g transform="translate({ox:.3f} {by:.3f}) scale({s:.5f} {-s:.5f})"><path fill="{INK}" d="{path(g,0)}"/><path fill="{ORANGE}" d="{path(dot,dx)}"/></g></svg>'''
open(out+"/favicon.svg","w").write(svg); print("svg bytes", len(svg))
def png(N, fill, rounded=True):
    SS = 8; M = N*SS; s, ox, by = layout(M, fill)
    im = Image.new("RGBA", (M,M), (0,0,0,0)); d = ImageDraw.Draw(im)
    if rounded: d.rounded_rectangle([0,0,M-1,M-1], radius=int(M*10/64), fill=BG)
    else: d.rectangle([0,0,M,M], fill=BG)
    font = ImageFont.truetype(ttf, round(upm*s))   # font size in px = em
    d.text((ox, by), chr(ord("g")), font=font, fill=INK, anchor="ls")
    d.text((ox + dx*s, by), ".", font=font, fill=ORANGE, anchor="ls")
    return im.resize((N,N), Image.LANCZOS)
png(180, 0.70, rounded=False).convert("RGB").save(out+"/apple-touch-icon.png", optimize=True)
icons = [png(n, 0.86 if n<=32 else 0.80) for n in (16,32,48)]
icons[2].save(out+"/favicon.ico", sizes=[(16,16),(32,32),(48,48)], append_images=icons[:2])
# preview sheet
sheet = Image.new("RGB", (420, 140), "#dddddd"); x = 10
for n in (16,32,48,64):
    im = png(n, 0.86 if n<=32 else 0.80); sheet.paste(im, (x, 10), im); big = im.resize((n*2 if n<64 else n, n*2 if n<64 else n), Image.NEAREST); x += n + 10
dark = Image.new("RGB", (420,60), "#202124"); x=10
for n in (16,32):
    im = png(n, 0.86); dark.paste(im,(x,10),im); x+= n+10
sheet.paste(dark,(0,80)); sheet.resize((840,280), Image.NEAREST).save(out+"/preview.png")
at = Image.open(out+"/apple-touch-icon.png"); at.save(out+"/preview-touch.png")
