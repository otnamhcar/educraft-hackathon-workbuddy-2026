#!/usr/bin/env python3
"""Buat empat kartu jembatan untuk video demo EduCraft.

Kartu dipakai di titik sambungan rekaman, supaya lompatan waktu terbaca
sebagai lompatan yang disengaja — bukan rekaman yang rusak.

    python3 buat_kartu.py

Menulis ke 06_Submission/video_kit/kartu/.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUT = HERE / "kartu"
W, H = 1366, 768

BASE = (11, 12, 16)
INK = (243, 241, 234)
MUTED = (139, 136, 128)
FAINT = (87, 89, 95)
ACCENT = (127, 119, 221)
OK = (93, 202, 165)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

LANGKAH = "LANGKAH {}/5"
JUDUL_BUKTI = "Yang harus dibuktikan"
ALASAN = "Alasan potongan ini ada di video"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def kartu(berkas, nomor, judul, bukti, alasan):
    img = Image.new("RGB", (W, H), BASE)
    d = ImageDraw.Draw(img)

    f_langkah = font(BOLD, 20)
    f_judul = font(BOLD, 60)
    f_bukti = font(REG, 30)
    f_kecil = font(BOLD, 18)
    f_alasan = font(REG, 22)

    x = 110

    d.text((x, 130), LANGKAH.format(nomor), font=f_langkah, fill=ACCENT)
    d.line([(x, 168), (x + 56, 168)], fill=ACCENT, width=3)

    d.text((x, 224), judul, font=f_judul, fill=INK)

    y = 330
    d.text((x, y), JUDUL_BUKTI.upper(), font=f_kecil, fill=FAINT)
    y += 34
    for line in wrap(d, bukti, f_bukti, W - 2 * x):
        d.text((x, y), line, font=f_bukti, fill=INK)
        y += 44

    y += 46
    d.line([(x, y), (x + W - 2 * x, y)], fill=(42, 46, 58), width=2)
    y += 34
    d.text((x, y), ALASAN.upper(), font=font(BOLD, 18), fill=FAINT)
    y += 30
    for line in wrap(d, alasan, f_alasan, W - 2 * x):
        d.text((x, y), line, font=f_alasan, fill=MUTED)
        y += 32

    OUT.mkdir(parents=True, exist_ok=True)
    dst = OUT / berkas
    img.save(dst, optimize=True)
    print("  {}".format(dst))
    return dst


def main():
    print("Kartu:")
    kartu(
        "kartu_1_selisih.png",
        1,
        "Agen menolak menebak",
        "Agen menemukan dua jawaban yang bertentangan, menolak memilih "
        "sendiri, lalu meminta satu konfirmasi.",
        "Tidak ada sumber yang mendukung salah satu pilihan. Menebak akan "
        "melanggar aturan sumber, jadi agen berhenti dan bertanya.",
    )
    kartu(
        "kartu_2_keputusan.png",
        2,
        "Empat keputusan, bukan satu",
        "Agen merangkum empat hal yang harus diputuskan guru, menyebut aturan "
        "yang jadi dasarnya, lalu menunggu.",
        "Empat keputusan ini mengubah isi materi. Agen tidak berwenang "
        "memutuskan sendiri, jadi keputusan diserahkan ke guru.",
    )
    kartu(
        "kartu_3_cacat.png",
        3,
        "Agen memeriksa hasil sendiri",
        "Agen menemukan cacat penomoran daftar lintas bagian, memperbaikinya, "
        "lalu memeriksa halaman lain sebelum menyatakan lolos.",
        "Verifikasi tidak berhenti di satu temuan. Setelah memperbaiki, agen "
        "memeriksa ulang supaya cacat sejenis tidak lolos di halaman lain.",
    )
    kartu(
        "kartu_4_lingkup.png",
        4,
        "Permintaan di luar lingkup",
        "Diminta materi \"makanan halal\", agen menyatakan topik itu tidak ada "
        "di katalog CP IPAS, lalu menawarkan dua jalan.",
        "Membuatkan materi yang tidak punya acuan kurikulum akan menghasilkan "
        "bahan tanpa dasar. Agen menolak diam-diam mengarang acuan.",
    )
    kartu(
        "kartu_5_kuis.png",
        5,
        "Cacat ditemukan lewat pengujian",
        "Agen menguji kuis interaktifnya, menemukan label jawaban bertumpuk "
        "dan kolom cetak terlalu sempit, lalu mencatat cara menilainya.",
        "Cacat ditemukan sebelum diserahkan, bukan setelah dipakai murid. "
        "Temuan ditulis apa adanya beserta akibatnya.",
    )
    print("\nSelesai. {} kartu di {}".format(5, OUT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
