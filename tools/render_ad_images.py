import sys, pathlib
from playwright.sync_api import sync_playwright

OUT = pathlib.Path("/home/claude/render/out"); OUT.mkdir(exist_ok=True)

BASE = """
<style>
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1080px;overflow:hidden;font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased}
.chip{display:inline-block;border-radius:999px;padding:10px 26px;font-weight:700;font-size:30px}
</style>
"""

def page(body, bg):
    return f"<!doctype html><html><head><meta charset='utf-8'>{BASE}</head><body style='background:{bg}'>{body}</body></html>"

TEAL="#0B3D3A"; TEAL2="#0F766E"; YEL="#F2C94C"

# ---------- Carousel ----------
def card_frame(tag, title, inner, n, note=""):
    return page(f"""
<div style="position:absolute;inset:0;padding:64px 64px 56px">
  <div style="display:flex;justify-content:space-between;align-items:center">
    <div style="font-size:24px;font-weight:800;letter-spacing:3px;color:{TEAL2}">{tag}</div>
    <div style="font-size:24px;font-weight:700;color:#94a3b8">{n}/7</div>
  </div>
  <div style="font-size:56px;font-weight:900;line-height:1.08;color:{TEAL};margin-top:22px;letter-spacing:-1px">{title}</div>
  <div style="margin-top:34px">{inner}</div>
</div>
<div style="position:absolute;left:64px;right:64px;bottom:62px;background:#FFF6C9;border-left:10px solid {YEL};border-radius:12px;padding:24px 28px;font-size:33px;font-weight:700;color:{TEAL};line-height:1.25;display:{'block' if note else 'none'}">{note}</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:14px;background:{TEAL2}"></div>
""", "#FFFFFF")

def li(items, size=33, gap=16):
    return "".join(f"<div style='display:flex;gap:18px;align-items:flex-start;margin-bottom:{gap}px;font-size:{size}px;font-weight:600;color:#16302D;line-height:1.25'><span style='flex:none;width:34px;height:34px;border-radius:9px;background:{TEAL2};color:#fff;font-size:22px;display:flex;align-items:center;justify-content:center;margin-top:3px'>✓</span><span>{t}</span></div>" for t in items)

slides = {}

slides["c1"] = page(f"""
<div style="position:absolute;inset:0;padding:70px;display:flex;flex-direction:column;justify-content:space-between">
  <div style="font-size:26px;font-weight:800;letter-spacing:4px;color:{YEL}">PAKET DOKUMEN IPCN & KOMITE/TIM PPI RS 2026</div>
  <div>
    <div style="font-size:250px;font-weight:900;line-height:.9;color:#fff;letter-spacing:-8px">66</div>
    <div style="font-size:84px;font-weight:900;line-height:1;color:{YEL};margin-top:6px;letter-spacing:-2px">file di dalamnya.</div>
    <div style="font-size:46px;font-weight:700;color:#d5ece8;margin-top:34px;line-height:1.2">Isinya dibuka satu per satu.<br>Geser →</div>
  </div>
  <div style="display:flex;gap:18px">
    <span class="chip" style="background:rgba(255,255,255,.12);color:#fff">60 Word</span>
    <span class="chip" style="background:rgba(255,255,255,.12);color:#fff">6 Excel</span>
    <span class="chip" style="background:{YEL};color:{TEAL}">13 SPO</span>
  </div>
</div>""", TEAL)

slides["c2"] = card_frame("FOLDER 00 & 01", "Mulai di sini, lalu pedoman & organisasi", li([
 "Panduan Penggunaan & Peta Isi Paket",
 "Rencana Kerja 30 Hari IPCN dan Komite/Tim PPI",
 "Peta kewajiban K01–K30 ke dokumen & standar PPI",
 "SK Komite/Tim PPI dan penetapan IPCN-IPCLN",
 "Uraian tugas & wewenang, matriks koordinasi lintas unit",
 "Panduan ICRA program tahunan & ICRA konstruksi",
], 38, 34, ), 2, "Strukturnya sudah jadi: SK, uraian tugas, matriks koordinasi, tinggal sesuaikan nama dan unit RS kamu.")

slides["c3"] = card_frame("FOLDER 02", "13 SPO inti, tinggal sesuaikan", f"""
<div style="columns:2;column-gap:28px;font-size:32px;font-weight:600;color:#16302D;line-height:1.2">
"""+"".join(f"<div style='break-inside:avoid;background:#E6F4F1;border-radius:16px;padding:13px 20px;margin-bottom:12px'>{t}</div>" for t in [
 "Kebersihan Tangan","APD","Kewaspadaan Transmisi & Isolasi","Transfer Pasien Airborne & Outbreak","Benda Tajam & Pajanan Petugas","Limbah Infeksius","Linen & Laundry","Pembersihan Lingkungan","Dekontaminasi & Sterilisasi","Reuse Alat Sekali Pakai","Pelaksanaan ICRA Konstruksi","Surveilans HAIs","Investigasi & Penanggulangan KLB"])+"</div>", 3, "13 SPO ini bagian dari 60 dokumen Word yang siap kamu sunting.")

# logbook mock
slides["c4"] = card_frame("FOLDER 03", "Logbook dengan baris contoh terisi", f"""
<div style="font-size:28px;font-weight:700;color:#475569;margin-bottom:16px">CONTOH · Observasi Kebersihan Tangan (data samaran)</div>
<table style="width:100%;border-collapse:collapse;font-size:34px;color:#16302D">
 <tr style="background:{TEAL};color:#fff;font-weight:800"><td style="padding:20px 18px">Unit</td><td style="padding:20px 18px">Peluang</td><td style="padding:20px 18px">Patuh</td><td style="padding:20px 18px">%</td></tr>
 <tr style="background:#FFF6C9;font-weight:700"><td style="padding:20px 18px;border-bottom:2px solid #e2e8f0">Rawat Inap A</td><td style="padding:20px 18px;border-bottom:2px solid #e2e8f0">50</td><td style="padding:20px 18px;border-bottom:2px solid #e2e8f0">41</td><td style="padding:20px 18px;border-bottom:2px solid #e2e8f0">82%</td></tr>
 <tr style="background:#fff"><td style="padding:20px 18px;border-bottom:2px solid #e2e8f0;color:#94a3b8">…isi dengan data RS kamu</td><td style="border-bottom:2px solid #e2e8f0"></td><td style="border-bottom:2px solid #e2e8f0"></td><td style="border-bottom:2px solid #e2e8f0"></td></tr>
 <tr style="background:#fff"><td style="padding:34px 18px;border-bottom:2px solid #e2e8f0"></td><td style="border-bottom:2px solid #e2e8f0"></td><td style="border-bottom:2px solid #e2e8f0"></td><td style="border-bottom:2px solid #e2e8f0"></td></tr>
</table>
<div style="margin-top:30px;font-size:36px;font-weight:700;color:#16302D;line-height:1.3">8 logbook: surveilans, bundle, kebersihan tangan, APD, lingkungan, ruang isolasi, limbah & benda tajam, supervisi linen.</div>
""", 4, "Tiap logbook punya baris CONTOH terisi, jadi langsung tahu cara mengisinya.")

slides["c5"] = card_frame("FOLDER 04", "Kalender audit 12 bulan + pelacak terlambat", f"""
<div style="font-size:28px;font-weight:700;color:#475569;margin-bottom:16px">CONTOH · Pelacak audit (data samaran)</div>
<table style="width:100%;border-collapse:collapse;font-size:33px;color:#16302D">
 <tr style="background:{TEAL};color:#fff;font-weight:800"><td style="padding:20px 18px">Audit / supervisi</td><td style="padding:24px 18px">Status</td></tr>
""" + "".join(f"<tr><td style='padding:24px 18px;border-bottom:2px solid #e2e8f0;font-weight:600'>{a}</td><td style='padding:24px 18px;border-bottom:2px solid #e2e8f0'><span style='padding:6px 16px;border-radius:999px;font-weight:800;font-size:28px;background:{bg};color:{fg}'>{s}</span></td></tr>" for a,s,bg,fg in [
 ("Audit Kebersihan Tangan & APD","Selesai","#D1FADF","#05603A"),
 ("Audit Sterilisasi & CSSD","Terlambat","#FEE4E2","#B42318"),
 ("Audit Limbah, Benda Tajam & Linen","Dijadwalkan","#E0EAFF","#1D3FA6"),
 ("Simulasi Telusur Pokja PPI","Dijadwalkan","#E0EAFF","#1D3FA6")]) + """
</table>
<div style="margin-top:28px;font-size:35px;font-weight:700;color:#16302D;line-height:1.3">Plus instrumen supervisi IPCN terpadu & matriks bukti akreditasi PPI 1–13.</div>
""", 5, "Kegiatan yang terlambat ditandai merah otomatis di Excel E03.")

slides["c6"] = card_frame("FOLDER 06 · EXCEL", "6 alat Excel tanpa makro", li([
 "E01 Surveilans HAIs & laju per hari-alat (merah otomatis di atas ambang)",
 "E02 Audit kepatuhan kebersihan tangan & APD",
 "E03 Pelacak kalender audit 12 bulan",
 "E04 Skoring ICRA program tahunan",
 "E05 Kalkulator kelas ICRA konstruksi",
 "E06 Dashboard PPI berjenjang: bulanan → triwulan → semester → tahunan",
], 36, 28), 6, "Tanpa makro: bisa dibuka di Excel maupun LibreOffice.")

slides["c7"] = page(f"""
<div style="position:absolute;inset:0;padding:70px;display:flex;flex-direction:column;justify-content:space-between">
  <div style="font-size:26px;font-weight:800;letter-spacing:4px;color:{YEL}">7/7 · SEKALI BAYAR</div>
  <div>
    <div style="font-size:50px;font-weight:800;color:#d5ece8">Semua 66 file</div>
    <div style="font-size:150px;font-weight:900;color:#fff;letter-spacing:-5px;line-height:1.05;margin-top:6px">Rp149.000</div>
    <div style="font-size:36px;font-weight:700;color:{YEL};margin-top:20px;line-height:1.3">Bukan langganan · update gratis jika regulasi berubah</div>
  </div>
  <div>
    <div style="font-size:30px;font-weight:600;color:#d5ece8;line-height:1.4;margin-bottom:26px">Ganti kolom berstabilo kuning dengan data RS kamu, lalu tinjau bersama praktisi sebelum ditetapkan.</div>
    <span class="chip" style="background:{YEL};color:{TEAL};font-size:38px;padding:18px 40px">Lihat isi lengkap →</span>
  </div>
</div>""", TEAL)

# ---------- K04: poster tipografi ----------
slides["k04"] = page(f"""
<div style="position:absolute;inset:0;padding:78px 74px;display:flex;flex-direction:column;justify-content:space-between">
  <div style="font-size:27px;font-weight:800;letter-spacing:4px;color:#111">LAPORAN PPI · DIREKTUR BERTANYA</div>
  <div>
    <div style="font-size:98px;font-weight:900;line-height:1.02;color:#111;letter-spacing:-3px">Angka di laporan <span style="background:#FF3B30;color:#fff;padding:0 16px;border-radius:6px">tahunan</span> tidak sama dengan jumlah laporan <span style="text-decoration:underline;text-decoration-thickness:10px;text-decoration-color:#FF3B30;text-underline-offset:10px">bulanan.</span></div>
    <div style="font-size:48px;font-weight:700;color:#333;margin-top:42px;line-height:1.2">Kamu yang diminta menjelaskan.</div>
  </div>
  <div style="display:flex;justify-content:space-between;align-items:flex-end">
    <div style="font-size:28px;font-weight:700;color:#222;line-height:1.35">Laporan bulanan → triwulan →<br>semester → tahunan, angkanya tertaut.</div>
    <span class="chip" style="background:#111;color:#fff;font-size:30px;padding:16px 30px;white-space:nowrap">66 file · Rp149.000</span>
  </div>
</div>""", "#F3EEE3")

# ---------- K05: artefak izin kerja ICRA ----------
def f(label,val,hl=False):
    v = f"<span style='background:#FFEF5E;padding:2px 10px'>{val}</span>" if hl else val
    return f"<div style='display:flex;gap:14px;font-size:23px;margin-bottom:13px;border-bottom:1.5px solid #cbd5e1;padding-bottom:7px'><span style='width:250px;flex:none;color:#475569;font-weight:600'>{label}</span><span style='font-weight:700;color:#0f172a'>{v}</span></div>"

slides["k05"] = page(f"""
<div style="position:absolute;inset:0;background:linear-gradient(160deg,#2b3544,#1b222d)"></div>
<div style="position:absolute;left:56px;top:300px;width:640px;height:690px;background:#fff;border-radius:6px;box-shadow:0 30px 80px rgba(0,0,0,.55);transform:rotate(-3deg);padding:40px 44px;overflow:hidden">
  <div style="font-size:18px;font-weight:800;letter-spacing:2px;color:#b45309">CONTOH FORMAT · DATA SAMARAN</div>
  <div style="font-size:35px;font-weight:900;color:#0f172a;margin:6px 0 22px;line-height:1.1">IZIN KERJA ICRA<br>KONSTRUKSI / RENOVASI</div>
  {f("Lokasi pekerjaan","Lantai 3 Rawat Inap, plafon",True)}
  {f("Jenis pekerjaan","Pembongkaran plafon")}
  {f("Kelas ICRA","……… (isi dengan kalkulator)")}
  {f("Barrier debu terpasang","☐ Ya   ☐ Tidak")}
  {f("Inspeksi harian","☐ H1  ☐ H2  ☐ H3")}
  <div style="display:flex;gap:30px;margin-top:20px">
    <div style="flex:1;border:2px dashed #94a3b8;border-radius:8px;height:105px;padding:10px;font-size:19px;color:#64748b;font-weight:700">Tanda tangan IPCN<div style="margin-top:20px;font-size:36px;color:#DC2626;font-weight:900;transform:rotate(-6deg)">BELUM ADA</div></div>
    <div style="flex:1;border:2px dashed #94a3b8;border-radius:8px;height:105px;padding:10px;font-size:19px;color:#64748b;font-weight:700">Serah terima area</div>
  </div>
</div>
<div style="position:absolute;left:70px;top:64px;right:70px">
  <div style="font-size:26px;font-weight:800;letter-spacing:4px;color:{YEL}">PPI · KONSTRUKSI & RENOVASI RS</div>
  <div style="font-size:68px;font-weight:900;line-height:1.06;color:#fff;margin-top:14px;letter-spacing:-2px">Plafon sudah dibongkar.<br><span style="color:{YEL}">Izin kerja ICRA-nya mana?</span></div>
</div>
<div style="position:absolute;right:48px;bottom:62px;width:300px;text-align:right">
  <div style="font-size:23px;font-weight:700;color:#cbd5e1;line-height:1.3;margin-bottom:16px">Izin kerja, inspeksi harian & serah terima ada di paket IPCN</div>
  <span class="chip" style="background:{YEL};color:#0b3d3a;font-size:30px">Rp149.000</span>
</div>
""", "#1b222d")

if __name__=="__main__":
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width":1080,"height":1080}, device_scale_factor=1)
        for k,h in slides.items():
            pg.set_content(h); pg.wait_for_timeout(250)
            pg.screenshot(path=str(OUT/f"{k}.png"))
        b.close()
    print("ok", list(slides))
