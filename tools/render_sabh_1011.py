import pathlib, sys
from playwright.sync_api import sync_playwright
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "ad-images/sabh-1011"); OUT.mkdir(parents=True, exist_ok=True)

IND="#2A125D"; VIO="#5C269F"; YEL="#F9C929"; ORG="#FA7B14"; WH="#FFFFFF"
BASE = """<style>
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1080px;overflow:hidden;font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased}
</style>"""
def page(body, bg):
    return "<!doctype html><html><head><meta charset='utf-8'>"+BASE+"</head><body style='background:"+bg+"'>"+body+"</body></html>"
GRAD = f"linear-gradient(160deg,{IND} 0%,#3B1A7A 60%,{VIO} 100%)"

def frame(n, headline, inner, label="EBOOK PANDUAN LAPOR TAHUNAN PT · SABH"):
    return page(f"""
<div style="position:absolute;inset:0;padding:60px 64px 0">
  <div style="display:flex;justify-content:space-between;align-items:center">
    <div style="font-size:26px;font-weight:800;letter-spacing:2px;color:{YEL}">{label}</div>
    <div style="font-size:30px;font-weight:800;color:#C9B8F0">{n}/6</div>
  </div>
  <div style="font-size:84px;font-weight:900;line-height:1.04;color:{WH};margin-top:34px;letter-spacing:-2px">{headline}</div>
  <div style="margin-top:34px">{inner}</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:16px;background:{ORG}"></div>""", GRAD)

def check(items, size=46):
    return "".join(f"<div style='display:flex;gap:20px;align-items:flex-start;margin-bottom:22px;font-size:{size}px;font-weight:700;color:{WH};line-height:1.24'><span style='flex:none;width:46px;height:46px;border-radius:12px;background:{YEL};color:{IND};font-size:30px;font-weight:900;display:flex;align-items:center;justify-content:center;margin-top:2px'>✓</span><span>{t}</span></div>" for t in items)

def note(text, label):
    return f"""<div style="position:absolute;left:64px;right:64px;bottom:56px;background:{WH};border-radius:20px;padding:24px 32px;border-left:14px solid {ORG}">
  <div style="font-size:26px;font-weight:900;letter-spacing:2px;color:{VIO}">{label}</div>
  <div style="font-size:36px;font-weight:700;color:{IND};line-height:1.22;margin-top:8px">{text}</div></div>"""

c = {}
# ---- K01 carousel: PT Vakum ----
c["k01_c1"] = page(f"""
<div style="position:absolute;inset:0;padding:60px 64px;display:flex;flex-direction:column;justify-content:space-between">
  <div>
    <div style="display:inline-block;background:{YEL};color:{IND};font-size:27px;font-weight:900;letter-spacing:2px;border-radius:10px;padding:10px 20px">EBOOK PANDUAN LAPOR TAHUNAN PT KE SABH</div>
    <div style="font-size:30px;font-weight:800;letter-spacing:2px;color:{YEL};margin-top:20px">UNTUK PEMILIK &amp; PENGURUS PT YANG SUDAH VAKUM</div>
  </div>
  <div>
    <div style="font-size:124px;font-weight:900;line-height:.98;color:{WH};letter-spacing:-4px">PT Vakum? Tetap <span style="color:{YEL}">wajib lapor.</span></div>
    <div style="font-size:42px;font-weight:600;color:#E4DAF8;margin-top:28px;line-height:1.25">Sejak Permenkum 49/2025, PT yang tidak aktif pun tetap wajib lapor tahunan ke SABH.</div>
  </div>
  <div style="display:flex;justify-content:space-between;align-items:center">
    <div style="font-size:36px;font-weight:800;color:{WH}">Geser untuk lihat isinya →</div>
    <div style="font-size:28px;font-weight:800;color:#C9B8F0">1/6</div>
  </div>
</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:16px;background:{ORG}"></div>""", GRAD)

c["k01_c2"] = frame(2, "Dikira otomatis bebas kewajiban?", check([
  "PT sudah lama tidak aktif, dikira tidak punya kewajiban lagi",
  "Padahal tetap wajib lapor tahunan ke SABH",
  "Takut kena blokir akses AHU tapi bingung mulai dari mana"]),
  note("Ebook panduan untuk pemilik PT yang mau urus sendiri, tanpa bahasa hukum yang berbelit.", "UNTUK SIAPA"))

c["k01_c3"] = frame(3, "Lapor pasif atau bubar resmi?", check([
  "Simulasi skenario PT tidak aktif/vakum",
  "Alur dan pertimbangan biaya tiap pilihan",
  "BAB 7 di ebook + bonus Simulasi Skenario"]),
  note("Isi nyata ebook: pilih jalur yang paling aman dan hemat untuk PT-mu.", "BUKTI ISI · BAB 7"))

c["k01_c4"] = frame(4, "Jadwal setahun terpetakan", check([
  "Kapan RUPS Tahunan harus jalan",
  "Kapan batas lapor ke SABH",
  "Kapan tahap peringatan mulai berjalan"]),
  note("BAB 5 Kalender Kepatuhan Tahunan PT + bonus Kalender Kepatuhan.", "BUKTI ISI · BAB 5"))

c["k01_c5"] = frame(5, "Template & checklist siap pakai", check([
  "Template Susun Laporan Tahunan PT siap isi",
  "Checklist Dokumen RUPS Tahunan &amp; risalah rapat",
  "Panduan cepat reaktivasi akses SABH yang terblokir"]),
  note("4 bonus mini + 1 bonus Simulasi Skenario PT Tidak Aktif/Vakum.", "BONUS BERSAMA EBOOK"))

c["k01_c6"] = page(f"""
<div style="position:absolute;inset:0;padding:60px 64px;display:flex;flex-direction:column;justify-content:space-between">
  <div style="display:flex;justify-content:space-between;align-items:center">
    <div style="font-size:26px;font-weight:800;letter-spacing:2px;color:{YEL}">EBOOK PANDUAN LAPOR TAHUNAN PT · SABH</div>
    <div style="font-size:30px;font-weight:800;color:#C9B8F0">6/6</div></div>
  <div>
    <div style="font-size:86px;font-weight:900;line-height:1.05;color:{WH};letter-spacing:-2px">PT vakum pun bisa <span style="color:{YEL}">tertib lapor.</span></div>
    <div style="font-size:42px;font-weight:700;color:#E4DAF8;margin-top:30px;line-height:1.25">Ebook 8 bab + template laporan, checklist RUPS, kalender kepatuhan, dan panduan reaktivasi untuk pemilik &amp; pengurus PT.</div>
  </div>
  <div style="align-self:flex-start;background:{ORG};color:{WH};font-size:50px;font-weight:900;border-radius:60px;padding:26px 56px;margin-bottom:30px">Lihat isi lengkapnya →</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:16px;background:{ORG}"></div>""", GRAD)

# ---- K02 poster: takut diblokir ----
def step(n, t, sub, hot=False):
    bg = f"background:{ORG};color:{WH}" if hot else f"background:{WH};color:{IND}"
    sc = WH if hot else VIO
    return f"""<div style="display:flex;align-items:center;gap:22px;{bg};border-radius:18px;padding:12px 26px;margin-bottom:12px;{'box-shadow:0 0 0 6px '+YEL if hot else ''}">
  <div style="flex:none;width:54px;height:54px;border-radius:50%;background:{IND};color:{WH};font-size:32px;font-weight:900;display:flex;align-items:center;justify-content:center">{n}</div>
  <div><div style="font-size:38px;font-weight:900;line-height:1.1">{t}</div><div style="font-size:30px;font-weight:600;color:{sc};margin-top:3px">{sub}</div></div></div>"""

def chip(t):
    return f"<span style='display:inline-block;background:{YEL};color:{IND};font-size:31px;font-weight:800;border-radius:30px;padding:9px 22px;margin:0 12px 12px 0'>✓ {t}</span>"

c["k02"] = page(f"""
<div style="position:absolute;inset:0;padding:54px 64px 0">
  <div style="font-size:26px;font-weight:800;letter-spacing:2px;color:{YEL}">EBOOK LAPOR TAHUNAN PT · UNTUK DIREKSI &amp; PEMILIK</div>
  <div style="font-size:78px;font-weight:900;line-height:1.02;color:{WH};margin-top:14px;letter-spacing:-2px">Akses AHU diblokir? <span style="background:{ORG};padding:0 14px;border-radius:12px">Ganti direksi pun tak bisa.</span></div>
  <div style="margin-top:20px">
    {step(1,"Peringatan elektronik pertama","Laporan tahunan belum disampaikan")}
    {step(2,"Peringatan kedua","Belum juga lapor")}
    {step(3,"Akses SABH diblokir","Tak bisa ganti direksi, ubah akta, ajukan pinjaman", True)}
  </div>
  <div style="font-size:26px;font-weight:700;color:#C9B8F0;margin-top:2px">ILUSTRASI TAHAPAN SANKSI · Permenkum 49/2025</div>
  <div style="margin-top:12px">{chip("Panduan reaktivasi akses")}{chip("Kalender kepatuhan")}<br>{chip("Template laporan tahunan")}{chip("Checklist RUPS")}</div>
</div>
<div style="position:absolute;left:64px;bottom:34px;background:{ORG};color:{WH};font-size:44px;font-weight:900;border-radius:60px;padding:20px 50px">Cek isi ebooknya →</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:12px;background:{ORG}"></div>""", GRAD)

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width":1080,"height":1080})
    for k, html in c.items():
        pg.set_content(html); pg.wait_for_timeout(300)
        pg.screenshot(path=str(OUT/f"{k}.png"))
        print("ok", k)
    b.close()
