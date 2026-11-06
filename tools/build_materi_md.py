#!/usr/bin/env python3
"""Bangun materi siap pakai (.md) dari draf yang sudah disetujui.

Keluaran alat ini adalah LAPISAN KONTEN TERESOLUSI: satu berkas Markdown tanpa
tag internal, tanpa catatan pipeline, dengan koreksi pasca-render sudah diterapkan.
docx, pptx, dan html WAJIB diturunkan dari berkas ini — bukan dari draf bertag —
supaya FR-04 (konsistensi angka lintas artefak) tidak bergantung pada disiplin manual.

Pemakaian:
    python3 tools/build_materi_md.py \
        --run 03_Hasil/edu_output \
        --out 03_Hasil/edu_output/06_Materi_Guru_Energi_Alternatif.md \
        --koreksi 03_Hasil/edu_output/koreksi_format_rendering.md \
        --judul "Energi Alternatif dan Penghematan Energi" \
        --fase "Fase C (kelas V–VI)" \
        --run-id EDU-ORCH-20261026-001 \
        --approver "Don Jimat Akbar" \
        --approved-at "2026-11-04 14:49 GMT+7"

Keluar dengan kode 1 bila verifikasi gagal (FR-01/FR-06/FR-09).
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

# Berkas draf yang masuk ke bundel, berurutan.
BERKAS_BAWAAN = [
    "01_lesson_plan.md",
    "02_quiz_pretest_posttest.md",
    "03_slide_outline.md",
    "04_artikel.md",
]

# Judul bagian yang isinya catatan internal pipeline — tidak boleh sampai ke guru.
JUDUL_INTERNAL = re.compile(
    r"^(catatan kepatuhan|catatan produksi|catatan kurikulum|catatan internal|"
    r"catatan reviewer|catatan pipeline|catatan audit|catatan slide|"
    # Daftar tag per bagian: artefak pipeline, bukan isi materi. Setiap bagian
    # sudah membawa baris "Sumber:" sendiri, dan .docx pun membuang lampiran ini.
    r"sumber yang dipakai)\b",
    re.IGNORECASE,
)

# Awalan penomoran pada judul ("H. ", "3. ", "IV. ") dibuang sebelum dicocokkan.
AWALAN_NOMOR = re.compile(r"^(?:[A-Z]|\d{1,2}|[IVX]{1,4})[.)]\s+")

# Kutipan pembuka yang menjelaskan proses penyusunan, bukan isi materi.
KUTIPAN_INTERNAL = [
    # Catatan internal, dalam bentuk apa pun pemisahnya (titik dua, em dash, atau
    # tanpa pemisah). Versi lama hanya mengenali `catatan kurikulum:` bertitik dua,
    # sehingga varian `catatan kurikulum — …` lolos ke artefak guru (temuan FR-06).
    # Sengaja TIDAK memakai pola umum `catatan\b`: "Catatan pencetakan", "Catatan
    # penilaian", dan "Catatan penyajian" adalah keterangan untuk guru, bukan untuk
    # pipeline, dan harus tetap ada di berkas materi.
    re.compile(r"^>\s*\*\*catatan (kepatuhan|produksi|kurikulum|internal|"
               r"reviewer|pipeline|audit|slide)\b", re.IGNORECASE),
    re.compile(r"^>\s*\*\*kepatuhan:\*\*", re.IGNORECASE),
    # Front matter draf yang ditulis sebagai kutipan: metadata pipeline, bukan isi.
    re.compile(r"^>\s*\*\*(format|run|topik|status|fase)\s*:", re.IGNORECASE),
    re.compile(r"^>\s*\*\*aturan penulisan sumber", re.IGNORECASE),
    re.compile(r"^>\s*\*\*flow c\b", re.IGNORECASE),
    re.compile(r"^>\s*setiap slide merujuk tag", re.IGNORECASE),
    re.compile(r"^>\s*brief ini diserahkan", re.IGNORECASE),
    re.compile(r"^>\s*disusun oleh educraft", re.IGNORECASE),
]

TAG_RE = [
    (re.compile(r"`?\[src:[^\]]+\]`?"), ""),
    (re.compile(r"`?\[UNVERIFIED\]`?"), ""),
    (re.compile(r"\s*PERLU KONFIRMASI GURU:?"), ""),
]

# Draf menuliskan sumber judul sebagai segmen miring di ujung: "… — *`[src:2]`*".
# Menghapus tag saja menyisakan "— **" atau "— *; CP fondasi *" di judul artefak.
JUDUL_SUMBER = re.compile(r"\s*[—–-]\s*\*[^*]*\[src:[^\]]+\][^*]*\*\s*$")

# Pasangan penanda "tidak ada di sumber" adalah pesan nyata bagi guru; menghapus
# keduanya menyisakan tanda pisah menggantung. Ditulis ulang sebagai prosa.
PASANGAN_UNVERIFIED = re.compile(
    r"`?\[UNVERIFIED\]`?\s*[—–,-]\s*`?PERLU KONFIRMASI GURU`?", re.IGNORECASE)

# Diperiksa SETELAH keluaran dirakit. Sengaja memakai penanda yang tidak mungkin
# muncul di prosa guru yang sah — "catatan" saja tidak boleh, karena itu kata biasa.
PEMERIKSAAN = [
    (re.compile(r"\[src:[^\]]*\]"), "FR-01: tag sumber lolos"),
    (re.compile(r"\[UNVERIFIED\]"), "FR-01: tag UNVERIFIED lolos"),
    (re.compile(r"PERLU KONFIRMASI GURU"), "FR-01: penanda konfirmasi lolos"),
    (re.compile(r"\bR0\d{2}\b"), "FR-06: ID aturan rulebook lolos"),
    (re.compile(r"assets/"), "FR-06: path aset internal lolos"),
    (re.compile(r"Catatan (Kepatuhan|Produksi|Kurikulum|Internal)", re.IGNORECASE), "FR-06: bagian catatan internal lolos"),
]


def baca_koreksi(path: Path | None) -> list[tuple[str, str]]:
    """Berkas koreksi: satu baris `SEBELUM => SESUDAH`; `;;` untuk komentar."""
    if path is None:
        return []
    aturan: list[tuple[str, str]] = []
    for baris in path.read_text(encoding="utf-8").splitlines():
        baris = baris.strip()
        if not baris or baris.startswith(";;"):
            continue
        if "=>" not in baris:
            continue
        kiri, kanan = baris.split("=>", 1)
        aturan.append((kiri.strip(), kanan.strip()))
    return aturan


def buang_bagian_internal(teks: str) -> tuple[str, list[str]]:
    """Buang bagian yang judulnya menandai catatan internal. Kembalikan judul yang dibuang."""
    keluaran: list[str] = []
    dibuang: list[str] = []
    level_lewati: int | None = None
    # Kutipan internal sering lebih dari satu baris. Menyaring baris demi baris
    # hanya membuang baris pertama, dan butir penjelas di bawahnya ikut lolos.
    lewati_kutipan = False

    for baris in teks.splitlines():
        cocok = re.match(r"^(#{1,6})\s+(.*)$", baris)
        if cocok:
            lewati_kutipan = False
            level = len(cocok.group(1))
            judul = cocok.group(2).strip()
            if level_lewati is not None and level <= level_lewati:
                level_lewati = None
            if level_lewati is None and JUDUL_INTERNAL.match(AWALAN_NOMOR.sub("", judul)):
                level_lewati = level
                dibuang.append(judul)
                continue
        if level_lewati is not None:
            continue
        if baris.lstrip().startswith(">"):
            if not lewati_kutipan and any(pola.match(baris) for pola in KUTIPAN_INTERNAL):
                lewati_kutipan = True
                dibuang.append(baris.strip())
                continue
            if lewati_kutipan:
                continue
        else:
            lewati_kutipan = False
        keluaran.append(baris)

    return "\n".join(keluaran), dibuang


def terapkan_koreksi(teks: str, aturan: list[tuple[str, str]]) -> str:
    for kiri, kanan in aturan:
        teks = teks.replace(kiri, kanan)
    return teks


def bersihkan_tag(teks: str) -> str:
    """Hapus penanda internal, baris demi baris, tanpa merusak indentasi.

    Indentasi menentukan apakah sebuah baris adalah lanjutan butir daftar atau
    paragraf baru. Versi lama merapatkan seluruh blok dengan `[ \\t]{2,}` → satu
    spasi, sehingga setiap lanjutan kehilangan indentasinya dan satu daftar
    bernomor pecah menjadi belasan daftar satu-butir (cacat yang sama pernah
    terjadi di `tools/render_docx.py`).
    """
    keluaran: list[str] = []
    for baris in teks.splitlines():
        cocok = re.match(r"^(\s*)(.*)$", baris)
        indent, badan = cocok.group(1), cocok.group(2)

        if badan.lstrip().startswith("#"):
            badan = JUDUL_SUMBER.sub("", badan)

        badan = PASANGAN_UNVERIFIED.sub("belum terverifikasi", badan)
        for pola, ganti in TAG_RE:
            badan = pola.sub(ganti, badan)
        badan = badan.replace("`[UNVERIFIED]`", "belum ada di lembar sumber")
        badan = badan.replace("[UNVERIFIED]", "belum ada di lembar sumber")
        badan = badan.replace("`PERLU KONFIRMASI GURU`", "perlu konfirmasi guru")
        badan = badan.replace("PERLU KONFIRMASI GURU", "perlu konfirmasi guru")

        badan = re.sub(r"[ \t]{2,}", " ", badan)
        # Sisa penghapusan tag: "— **", "— *;", "—,", tanda pisah menggantung,
        # dan sel tabel yang diawali "| — ".
        badan = re.sub(r"\s*[—–-]\s*\*\s*\*\s*$", "", badan)
        badan = re.sub(r"\s*[—–-]\s*\*\s*;", ";", badan)
        badan = re.sub(r"\s*[—–-]\s*,", ",", badan)
        # Lookbehind mencegah "---" (garis pemisah) ikut terpotong menjadi "--".
        badan = re.sub(r"(?<=[^\s—–-])\s*[—–-]\s*$", "", badan)
        badan = re.sub(r"(\|\s*)[—–-]\s+", r"\1", badan)
        badan = re.sub(r"\s+([.,;:!?)])", r"\1", badan)
        badan = re.sub(r"\(\s*\)", "", badan)
        badan = re.sub(r"—\s*—", "—", badan)
        badan = re.sub(r"([.!?]\s+)(belum ada|belum terverifikasi|perlu konfirmasi)",
                       lambda m: m.group(1) + m.group(2)[0].upper() + m.group(2)[1:], badan)
        keluaran.append(indent + badan.rstrip())
    return "\n".join(keluaran)


def turunkan_judul(teks: str) -> str:
    """Judul tiap berkas diturunkan satu tingkat agar bisa digabung di bawah satu H1."""
    keluaran = []
    for baris in teks.splitlines():
        cocok = re.match(r"^(#{1,5})\s+(.*)$", baris)
        if cocok:
            baris = "#" + cocok.group(1) + " " + cocok.group(2)
        keluaran.append(baris)
    return "\n".join(keluaran)


def rapikan_spasi(teks: str) -> str:
    teks = re.sub(r"\n{3,}", "\n\n", teks)
    # Tanda baca yang jatuh ke awal baris setelah baris sebelumnya dipangkas:
    # "**listrik**\n. Bagaimana" -> "**listrik**. Bagaimana".
    teks = re.sub(r"\n\s*([.,;:!?])", r"\1", teks)
    # Huruf besar setelah titik yang jatuh di ujung baris sebelumnya. Pemeriksaan
    # per baris tidak bisa melihat titik itu, jadi dilakukan setelah penggabungan.
    teks = re.sub(r"([.!?]\s+)(belum terverifikasi|perlu konfirmasi)",
                  lambda m: m.group(1) + m.group(2)[0].upper() + m.group(2)[1:], teks)
    # Draf kadang menempelkan judul langsung di bawah paragraf tanpa baris kosong;
    # sebagian penampil Markdown lalu membaca judul itu sebagai teks biasa.
    teks = re.sub(r"(?m)([^\n])\n(#{2,6}\s)", r"\1\n\n\2", teks)
    return teks.strip()


def rapikan_pemisah(teks: str) -> str:
    """Pembuangan kutipan internal menyisakan `---` ganda atau menggantung di bawah judul."""
    teks = re.sub(r"\n\s*---\s*\n\s*---\s*\n", "\n---\n", teks)
    teks = re.sub(r"(#{1,6}[^\n]*\n)\s*---\s*\n", r"\1", teks)
    return teks


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--run", required=True, type=Path, help="folder run berisi draf")
    p.add_argument("--out", required=True, type=Path, help="berkas .md yang dihasilkan")
    p.add_argument("--koreksi", type=Path, default=None, help="berkas koreksi SEBELUM => SESUDAH")
    p.add_argument("--judul", required=True)
    p.add_argument("--fase", required=True)
    p.add_argument("--run-id", required=True)
    p.add_argument("--approver", required=True)
    p.add_argument("--approved-at", required=True)
    p.add_argument("--berkas", default=",".join(BERKAS_BAWAAN), help="daftar berkas, dipisah koma")
    p.add_argument("--tanggal", default=None, help="tanggal build (bawaan: hari ini)")
    p.add_argument("--status", default="siap pakai",
                   help="status pada front matter (mis. 'draf pra-persetujuan')")
    args = p.parse_args()

    tanggal = args.tanggal or dt.date.today().isoformat()
    aturan = baca_koreksi(args.koreksi)

    bagian: list[str] = []
    dipakai: list[str] = []
    dibuang_semua: list[str] = []

    for nama in [b.strip() for b in args.berkas.split(",") if b.strip()]:
        path = args.run / nama
        if not path.exists():
            print(f"GAGAL  berkas draf tidak ada: {path}", file=sys.stderr)
            return 1
        teks = path.read_text(encoding="utf-8")
        teks, dibuang = buang_bagian_internal(teks)
        teks = terapkan_koreksi(teks, aturan)
        teks = bersihkan_tag(teks)
        teks = turunkan_judul(teks)
        teks = rapikan_spasi(teks)
        teks = rapikan_pemisah(teks)
        bagian.append(teks)
        dipakai.append(nama)
        dibuang_semua.extend(dibuang)

    isi = "\n\n---\n\n".join(bagian)

    daftar_isi = [
        f"- {m.group(1).strip()}"
        for m in re.finditer(r"^##\s+(.*)$", isi, re.MULTILINE)
        if not m.group(1).strip().lower().startswith(("cara pakai", "daftar isi"))
    ]

    kepala = f"""---
judul: "{args.judul}"
run: "{args.run_id}"
fase: "{args.fase}"
disetujui_oleh: "{args.approver}"
disetujui_pada: "{args.approved_at}"
dibangun: "{tanggal}"
status: "{args.status}"
sumber_konten: "{', '.join(dipakai)}"
---

# Materi Ajar — {args.judul}

| | |
|---|---|
| **Jenjang** | SD/MI — {args.fase} |
| **Mata pelajaran** | IPAS (Ilmu Pengetahuan Alam dan Sosial) |
| **Kurikulum** | Kurikulum Merdeka |
| **Disetujui oleh** | {args.approver} |
| **Tanggal persetujuan** | {args.approved_at} |
| **Run** | `{args.run_id}` |

> Berkas ini adalah versi {args.status}: seluruh penanda internal pipeline sudah diselesaikan,
> dan angka yang dipakai sama dengan versi cetak (`.docx`) serta tayangan (`.pptx`).
> Guru dapat menyunting berkas ini langsung tanpa perlu aplikasi perkantoran.

## Daftar isi

{chr(10).join(daftar_isi)}

---
"""

    keluaran = rapikan_spasi(kepala + "\n" + isi) + "\n"

    # --- verifikasi (FR-01, FR-04, FR-06, FR-09) ---
    gagal: list[str] = []
    for pola, pesan in PEMERIKSAAN:
        temuan = pola.search(keluaran)
        if temuan:
            gagal.append(f"{pesan}: {temuan.group(0)!r}")
    for kiri, _ in aturan:
        if kiri in keluaran:
            gagal.append(f"FR-04: koreksi belum diterapkan: {kiri!r}")
    if not daftar_isi:
        gagal.append("FR-09: daftar isi kosong — berkas draf tidak terbaca")

    if gagal:
        for g in gagal:
            print(f"GAGAL  {g}", file=sys.stderr)
        return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(keluaran, encoding="utf-8")

    print(f"OK     {args.out} ({len(keluaran.splitlines())} baris)")
    print(f"       bagian dibuang: {', '.join(dibuang_semua) if dibuang_semua else '—'}")
    print(f"       koreksi diterapkan: {len(aturan)}")
    print(f"       tag internal tersisa: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
