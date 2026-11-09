import pathlib
from playwright.sync_api import sync_playwright
OUT = pathlib.Path("/home/claude/render/cmm/out"); OUT.mkdir(exist_ok=True)

BASE = """<style>
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1080px;overflow:hidden;font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased}
</style>"""
def page(body, bg):
    return "<!doctype html><html><head><meta charset='utf-8'>"+BASE+"</head><body style='background:"+bg+"'>"+body+"</body></html>"

# ================= K01 CAROUSEL (krem + oranye) =================
CR="#FFF4E6"; OR="#F97316"; INK="#1C1917"; OR2="#C2410C"
def frame(n, headline, inner, foot=""):
    return page(f"""
<div style="position:absolute;inset:0;padding:64px 64px 0">
  <div style="display:flex;justify-content:space-between;align-items:center">
    <div style="font-size:25px;font-weight:800;letter-spacing:3px;color:{OR2}">KELAS CLAUDE MONEY MACHINE</div>
    <div style="font-size:26px;font-weight:800;color:#A8A29E">{n}/6</div>
  </div>
  <div style="font-size:76px;font-weight:900;line-height:1.04;color:{INK};margin-top:30px;letter-spacing:-2px">{headline}</div>
  <div style="margin-top:36px">{inner}</div>
</div>
{foot}
<div style="position:absolute;left:0;right:0;bottom:0;height:16px;background:{OR}"></div>""", CR)

def check(items, size=40):
    return "".join(f"<div style='display:flex;gap:20px;align-items:flex-start;margin-bottom:22px;font-size:{size}px;font-weight:700;color:{INK};line-height:1.22'><span style='flex:none;width:46px;height:46px;border-radius:12px;background:{OR};color:#fff;font-size:30px;display:flex;align-items:center;justify-content:center;margin-top:2px'>✓</span><span>{t}</span></div>" for t in items)

def note(text, label):
    return f"""<div style="position:absolute;left:64px;right:64px;bottom:60px;background:#fff;border:4px solid {OR};border-radius:20px;padding:26px 32px">
  <div style="font-size:26px;font-weight:900;letter-spacing:2px;color:{OR2}">{label}</div>
  <div style="font-size:38px;font-weight:700;color:{INK};line-height:1.22;margin-top:8px">{text}</div></div>"""

c = {}
c["k01_c1"] = page(f"""
<div style="position:absolute;inset:0;padding:64px;display:flex;flex-direction:column;justify-content:space-between">
  <div>
    <div style="display:inline-block;background:{INK};color:#fff;font-size:27px;font-weight:900;letter-spacing:2px;border-radius:10px;padding:10px 20px">KELAS ONLINE · CLAUDE MONEY MACHINE</div>
    <div style="font-size:30px;font-weight:800;letter-spacing:2px;color:{OR2};margin-top:20px">UNTUK PEMULA TOTAL YANG GAPTEK</div>
  </div>
  <div>
    <div style="font-size:128px;font-weight:900;line-height:.98;color:{INK};letter-spacing:-4px">Gaptek soal <span style="color:{OR}">Claude?</span></div>
    <div style="font-size:64px;font-weight:900;color:{INK};margin-top:26px;letter-spacing:-1px">Nggak masalah.</div>
    <div style="font-size:42px;font-weight:600;color:#44403C;margin-top:26px;line-height:1.25">Bingung cara pakai Claude supaya benar-benar kerja buat kamu? Lihat apa yang Claude kerjakan.</div>
  </div>
  <div style="display:flex;justify-content:space-between;align-items:center">
    <div style="font-size:34px;font-weight:800;color:{INK}">Geser →</div>
    <div style="font-size:26px;font-weight:800;color:#A8A29E">1/6</div>
  </div>
</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:16px;background:{OR}"></div>""", CR)

c["k01_c2"] = frame(2, "Tanpa coding. Dipandu klik demi klik.", check([
  "Tanpa coding",
  "Tanpa pengalaman bisnis",
  "Setiap langkah dipandu klik demi klik",
  "Ada grup Telegram kalau kamu mentok"]),
  note("Dibuat untuk yang belum pernah pakai Claude sama sekali.", "UNTUK SIAPA"))

c["k01_c3"] = frame(3, "Claude yang riset produknya", f"""
<div style="background:#fff;border:4px solid {OR};border-radius:22px;padding:30px 34px">
  <div style="font-size:28px;font-weight:900;letter-spacing:2px;color:{OR2}">MODUL 1 · RISET YANG NEMUIN DUIT</div>
  <div style="font-size:52px;font-weight:800;color:{INK};line-height:1.22;margin-top:14px">Claude mencari produk yang SUDAH terbukti dicari orang, bukan nebak-nebak ide.</div>
</div>""", note("Brief produk tervalidasi, siap dikerjakan.", "HASILNYA"))

c["k01_c4"] = frame(4, "Claude yang bikin produk dan toko", check([
  "Produk jadi: jalur ebook atau AI tools",
  "Halaman jualan ditulis Claude, lalu diimpor",
  "Toko live dengan pembayaran dan pengiriman otomatis"]),
  note("Modul 2 dan 3: produk jadi dalam sehari, toko live dalam semalam.", "ISI KELAS"))

c["k01_c5"] = frame(5, "Claude tulis iklan, baca angka", check([
  "Iklan dalam 5 angle berbeda + bahan visual tanpa desainer",
  "Claude dihubungkan ke data penjualan dan iklanmu",
  "Laporan tiap pagi + rekomendasi SCALE atau KILL"]),
  note("Modul 4 sampai 6. Kamu tinggal ambil keputusan.", "ISI KELAS"))

c["k01_c6"] = page(f"""
<div style="position:absolute;inset:0;padding:64px;display:flex;flex-direction:column;justify-content:space-between">
  <div style="display:flex;justify-content:space-between"><div style="font-size:25px;font-weight:800;letter-spacing:3px;color:{OR2}">KELAS CLAUDE MONEY MACHINE</div><div style="font-size:26px;font-weight:800;color:#A8A29E">6/6</div></div>
  <div>
    <div style="font-size:84px;font-weight:900;line-height:1.02;color:{INK};letter-spacing:-2px">Lihat isi <span style="color:{OR}">8 modulnya.</span></div>
    <div style="margin-top:34px">
      <span style="display:inline-block;background:#fff;border:3px solid {OR};border-radius:999px;padding:12px 26px;font-size:32px;font-weight:800;color:{INK};margin:0 10px 14px 0">Kelas online + praktik langsung</span>
      <span style="display:inline-block;background:#fff;border:3px solid {OR};border-radius:999px;padding:12px 26px;font-size:32px;font-weight:800;color:{INK};margin:0 10px 14px 0">8 modul praktik</span>
      <span style="display:inline-block;background:#fff;border:3px solid {OR};border-radius:999px;padding:12px 26px;font-size:32px;font-weight:800;color:{INK};margin:0 10px 14px 0">Akses selamanya</span>
    </div>
    <div style="font-size:36px;font-weight:700;color:#44403C;line-height:1.3;margin-top:10px">Bonus: Prompt Skill Builder, ebook Mastery, dan grup Telegram eksklusif.</div>
  </div>
  <div style="background:{OR};color:#fff;font-size:46px;font-weight:900;border-radius:999px;padding:28px 44px;text-align:center">Lihat isi kelasnya →</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:16px;background:{INK}"></div>""", CR)

# ================= K02 ARTEFAK: laporan pagi (slate + hijau) =================
SL="#0B1220"; GR="#22C55E"; AM="#F59E0B"; RD="#EF4444"
def row(prod, clos, roas, tag, color, hi=False):
    bg = "background:#FEF3C7;outline:5px solid #F59E0B;" if hi else ""
    return f"""<div style="display:grid;column-gap:12px;grid-template-columns:1.3fr 1.05fr .85fr 1.2fr;align-items:center;padding:14px 18px;border-bottom:2px solid #E5E7EB;font-size:30px;font-weight:700;color:#111827;{bg}">
  <div>{prod}</div><div>{clos}</div><div>{roas}</div>
  <div><span style="background:{color};color:#fff;border-radius:10px;padding:6px 16px;font-size:28px;font-weight:900">{tag}</span></div></div>"""

c["k02"] = page(f"""
<div style="position:absolute;inset:0;padding:46px 56px 0">
  <div style="display:flex;gap:14px;align-items:center;flex-wrap:wrap">
    <div style="background:{GR};color:{SL};font-size:27px;font-weight:900;border-radius:10px;padding:8px 18px;letter-spacing:1px">KELAS CLAUDE MONEY MACHINE</div>
    <div style="font-size:26px;font-weight:800;color:#E2E8F0;letter-spacing:1px">UNTUK PEMILIK TOKO DIGITAL YANG MAU NAMBAH LINI PRODUK</div>
  </div>
  <div style="font-size:74px;font-weight:900;line-height:1.04;color:#fff;margin-top:20px;letter-spacing:-2px">Tiap pagi masih cek iklan <span style="background:{GR};color:{SL};padding:0 14px;border-radius:10px">satu per satu?</span></div>
</div>
<div style="position:absolute;left:56px;top:330px;width:590px;transform:rotate(-1.6deg);background:#fff;border-radius:16px;box-shadow:0 24px 50px rgba(0,0,0,.5);overflow:hidden">
  <div style="background:#111827;color:#fff;padding:14px 18px">
    <div style="font-size:30px;font-weight:900;letter-spacing:1px">LAPORAN PAGI</div>
    <div style="font-size:26px;font-weight:800;color:{AM};letter-spacing:1px;margin-top:2px">CONTOH FORMAT · DATA SAMARAN</div></div>
  <div style="display:grid;column-gap:12px;grid-template-columns:1.3fr 1.05fr .85fr 1.2fr;padding:10px 18px;font-size:26px;font-weight:800;color:#6B7280;background:#F3F4F6"><div>PRODUK</div><div>CLOSING</div><div>ROAS</div><div>AKSI</div></div>
  {row("Produk A","12","3,1x","SCALE",GR)}
  {row("Produk B","5","1,4x","WATCH",AM)}
  {row("Produk C","0","0,0x","KILL",RD,True)}
</div>
<div style="position:absolute;left:676px;top:350px;width:350px">
  <div style="font-size:26px;font-weight:900;letter-spacing:2px;color:{GR}">SOLUSINYA</div>
  <div style="font-size:36px;font-weight:800;color:#fff;line-height:1.2;margin-top:8px">Claude dihubungkan ke data penjualan dan iklanmu. Rekomendasi berbasis angka riil.</div>
</div>
<div style="position:absolute;left:56px;top:716px;right:56px">
  <div style="font-size:28px;font-weight:900;letter-spacing:2px;color:{GR};margin-bottom:12px">ISI KELAS · MODUL 6: CLAUDE BACA DUIT KAMU</div>
  <span style="display:inline-block;background:rgba(255,255,255,.12);color:#fff;border-radius:999px;padding:10px 24px;font-size:31px;font-weight:700;margin:0 10px 12px 0">Laporan tiap pagi</span>
  <span style="display:inline-block;background:rgba(255,255,255,.12);color:#fff;border-radius:999px;padding:10px 24px;font-size:31px;font-weight:700;margin:0 10px 12px 0">SCALE / KILL dari angka riil</span>
  <span style="display:inline-block;background:rgba(255,255,255,.12);color:#fff;border-radius:999px;padding:10px 24px;font-size:31px;font-weight:700;margin:0 10px 12px 0">8 modul · akses selamanya</span>
</div>
<div style="position:absolute;left:56px;right:56px;bottom:44px;display:flex;justify-content:space-between;align-items:center">
  <div style="font-size:30px;font-weight:600;color:#CBD5E1;line-height:1.25">Kamu bosnya.<br>Claude yang baca angkanya.</div>
  <div style="background:{GR};color:{SL};font-size:38px;font-weight:900;border-radius:999px;padding:22px 38px;white-space:nowrap">Lihat isi kelasnya →</div>
</div>""", SL)

# ================= K03 DIAGRAM alur (putih kebiruan) =================
BL="#2B59FF"; BG3="#F3F6FF"; IK="#0F172A"
def step(n, title, sub, hi=False):
    bg = BL if hi else "#fff"
    fg = "#fff" if hi else IK
    sb = "#DDE6FF" if hi else "#475569"
    nb = "#fff" if hi else BL
    nf = BL if hi else "#fff"
    return f"""<div style="display:flex;align-items:center;gap:22px;background:{bg};border-radius:22px;padding:9px 26px;margin-bottom:9px;border:3px solid {BL}">
  <div style="flex:none;width:54px;height:54px;border-radius:50%;background:{nb};color:{nf};display:flex;align-items:center;justify-content:center;font-size:31px;font-weight:900">{n}</div>
  <div><div style="font-size:37px;font-weight:900;color:{fg};letter-spacing:-.5px;line-height:1.1">{title}</div>
  <div style="font-size:30px;font-weight:600;color:{sb};line-height:1.15">{sub}</div></div></div>"""

c["k03"] = page(f"""
<div style="position:absolute;inset:0;padding:44px 56px 0">
  <div style="display:flex;gap:14px;align-items:center;flex-wrap:wrap">
    <div style="background:{IK};color:#fff;font-size:27px;font-weight:900;border-radius:10px;padding:8px 18px;letter-spacing:1px">KELAS CLAUDE MONEY MACHINE</div>
    <div style="font-size:26px;font-weight:800;color:{BL};letter-spacing:1px">UNTUK YANG CAPEK BELAJAR AI TAPI BELUM ADA HASIL</div>
  </div>
  <div style="font-size:74px;font-weight:900;line-height:1.04;color:{IK};margin-top:18px;letter-spacing:-2px">Capek nonton tutorial AI, <span style="color:{BL}">hasil jualan masih nol?</span></div>
</div>
<div style="position:absolute;left:56px;right:56px;top:322px">
  {step(1,"IDE","riset produk yang terbukti dicari")}
  {step(2,"CLAUDE PRODUKSI","produk jadi: ebook atau AI tools",True)}
  {step(3,"TOKO LIVE","halaman jualan + bayar otomatis")}
  {step(4,"IKLAN JALAN","iklan 5 angle + bahan visual")}
  {step(5,"LAPORAN TIAP PAGI","Claude baca data jualan & iklanmu")}
</div>
<div style="position:absolute;left:56px;right:56px;top:872px">
  <div style="font-size:38px;font-weight:800;color:{IK};line-height:1.2">Claude yang mengerjakan, <span style="color:{BL}">kamu jadi bosnya.</span></div>
</div>
<div style="position:absolute;left:56px;right:56px;bottom:40px;display:flex;justify-content:space-between;align-items:center">
  <div style="font-size:28px;font-weight:700;color:#475569;line-height:1.25">Kelas online · 8 modul praktik<br>Akses selamanya</div>
  <div style="background:{BL};color:#fff;font-size:36px;font-weight:900;border-radius:999px;padding:20px 34px;white-space:nowrap">Lihat urutannya →</div>
</div>""", BG3)

# ================= K04 POSTER tipografi (teal gelap + kuning) =================
TE="#042F2E"; YE="#FACC15"
c["k04"] = page(f"""
<div style="position:absolute;inset:0;padding:48px 60px 0">
  <div style="display:flex;gap:14px;align-items:center;flex-wrap:wrap">
    <div style="background:{YE};color:{TE};font-size:27px;font-weight:900;border-radius:10px;padding:8px 18px;letter-spacing:1px">KELAS ONLINE CLAUDE MONEY MACHINE</div>
    <div style="font-size:26px;font-weight:800;color:#fff;letter-spacing:1px">UNTUK PEMULA YANG BINGUNG MAU JUALAN APA</div>
  </div>
  <div style="font-size:92px;font-weight:900;line-height:1.02;color:#fff;margin-top:24px;letter-spacing:-3px">Sudah bikin produk digital, ternyata <span style="background:{YE};color:{TE};padding:0 16px;border-radius:12px;display:inline-block;margin-top:8px">nggak ada yang cari.</span></div>
</div>
<div style="position:absolute;left:60px;right:60px;top:470px">
  <div style="font-size:30px;font-weight:900;letter-spacing:2px;color:{YE}">SOLUSINYA: RISET DULU</div>
  <div style="font-size:42px;font-weight:800;color:#fff;line-height:1.2;margin-top:8px">Claude mencari produk yang <u style="text-decoration-color:{YE};text-decoration-thickness:6px">sudah terbukti dicari orang</u>, bukan nebak-nebak ide.</div>
</div>
<div style="position:absolute;left:60px;right:60px;top:690px;background:#fff;border-radius:22px;padding:24px 32px;transform:rotate(-.8deg);box-shadow:0 20px 44px rgba(0,0,0,.4)">
  <div style="display:flex;justify-content:space-between;align-items:center">
    <div style="font-size:28px;font-weight:900;letter-spacing:1px;color:#0F766E">MODUL 1 · RISET YANG NEMUIN DUIT</div>
    <div style="font-size:22px;font-weight:800;color:#64748B">DARI 8 MODUL PRAKTIK</div></div>
  <div style="font-size:35px;font-weight:700;color:#0F172A;line-height:1.22;margin-top:8px">Output: brief produk tervalidasi. Lanjut ke produk jadi, toko live, dan iklan jalan.</div>
</div>
<div style="position:absolute;left:60px;right:60px;bottom:44px;display:flex;justify-content:space-between;align-items:center">
  <div style="font-size:30px;font-weight:600;color:#CCFBF1;line-height:1.25">Akses selamanya.<br>Tanpa coding.</div>
  <div style="background:{YE};color:{TE};font-size:38px;font-weight:900;border-radius:999px;padding:22px 38px;white-space:nowrap">Lihat isi kelasnya →</div>
</div>""", TE)

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width":1080,"height":1080}, device_scale_factor=1)
    for k, html in c.items():
        pg.set_content(html); pg.wait_for_timeout(350)
        pg.screenshot(path=str(OUT/f"{k}.png"))
    b.close()
print(sorted(c))
