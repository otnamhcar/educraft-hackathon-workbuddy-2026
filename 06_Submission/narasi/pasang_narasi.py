"""Gabungkan narasi TTS + subtitle ke video EduCraft.

Menghasilkan dua versi sekaligus:
  EduCraft_Demo_narasi.mp4        — video + suara, subtitle sebagai track .srt terpisah
  EduCraft_Demo_narasi_bakar.mp4  — video + suara + subtitle terbakar di gambar

Audio tiap blok ditempel pada posisinya di video, bukan dijejer dari nol. Blok yang
berkasnya tidak ada dilewati dengan peringatan, jadi bisa dicoba bertahap.

    python3 pasang_narasi.py --audio narasi/audio --cek
    python3 pasang_narasi.py --audio narasi/audio
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from buat_subtitle import senyap

HERE = Path(__file__).resolve().parent
VIDEO = HERE.parent / "EduCraft_Demo.mp4"
TIMING = HERE / "TIMING.json"
EKSTENSI = {".wav", ".mp3", ".m4a", ".aac", ".flac", ".ogg", ".opus"}

# Daftar segmen dibaca dari TIMING.json, bukan ditulis ulang di sini.
#
# Sebelumnya keempat skrip (pasang_narasi, pangkas_senyap, selaras_subtitle, ukur_tempo)
# masing-masing menyimpan daftar 8 nama yang sama. Begitu jumlah segmen berubah, keempatnya
# harus diubah serempak — dan kalau satu terlewat, hasilnya bukan error melainkan audio
# yang dipasang di segmen yang salah. Satu sumber, tidak ada yang bisa lupa.
_tim = json.loads(TIMING.read_text())
NAMA_URUT = list(_tim["mulai_di"].keys())
ORDER = [b["nomor"] for b in _tim["berkas"]]
NAMES = [b["segmen"] for b in _tim["berkas"]]

# Rentang waktu di mana subtitle disembunyikan karena kalimatnya SUDAH tertulis besar
# di layar. Menampilkan keduanya berarti penonton membaca kalimat yang sama dua kali
# di posisi berbeda, dan yang satu menutupi yang lain.
#
# Bukan tebakan: tiap rentang dicek dari bingkai videonya sendiri.
#   0,0–4,6      kartu judul, tulisan "…sebelum sampai ke kelas." ada di layar
#   398,0–403,2  kartu penutup, tiga barisnya sama dengan narasi penutup
#
# Kartu jembatan (87, 182, 236, 345, 384) TIDAK ada di sini: judulnya lain kata
# ("Agen menolak menebak") dibanding narasinya, jadi subtitle tetap diperlukan.
SRT_TERTUTUP = [(0.0, 4.6), (397.4, 403.234)]


def saring_srt(teks: str, tutup: list[tuple[float, float]]) -> str:
    """Buang cue yang bersinggungan dengan rentang tertutup.

    Syaratnya "bersinggungan", bukan "seluruhnya di dalam": cue penutup jatuh di
    398,0–401,0 sementara kartu penutup muncul tepat 398,0. Dengan syarat lama,
    cue sepanjang 4 detik yang lewat satu milidetik saja tetap lolos dan menampilkan
    kalimat yang sama di atas kartunya sendiri.
    """
    blok_cue = [c for c in teks.strip().split("\n\n") if c.strip()]
    sisa = []
    for cue in blok_cue:
        baris = cue.split("\n")
        if len(baris) < 3:
            continue
        a, b = baris[1].split(" --> ")

        def detik(s: str) -> float:
            jam, menit, rest = s.replace(",", ".").split(":")
            return int(jam) * 3600 + int(menit) * 60 + float(rest)

        mulai, selesai = detik(a), detik(b)
        # Bersinggungan: satu milidetik pun masuk rentang, cue dibuang.
        if any(selesai > t0 and mulai < t1 for t0, t1 in tutup):
            continue
        sisa.append("\n".join([baris[1]] + baris[2:]))
    return "\n\n".join(
        f"{i + 1}\n{isi}" for i, isi in enumerate(sisa)
    ) + "\n"


def durasi(berkas: Path) -> float:
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(berkas)],
        capture_output=True, text=True,
    )
    return float(r.stdout.strip())


TEMPO_ACUAN = 2.85  # kata/detik, diukur dari rekaman v2 — lihat ukur_tempo.py


def durasi_ucap(nomor: str) -> float:
    """Perkiraan panjang blok dari jumlah kata skrip, untuk blok yang belum direkam.

    Hanya untuk laporan. Angka sebenarnya baru ada setelah berkasnya ada — karena
    tempo mesin TTS dan jeda bawaannya tidak bisa ditebak dari teks.
    """
    import re as _re
    from buat_subtitle import baca_blok

    blok = baca_blok((HERE / "SKRIP_TTS_LAYAR.md").read_text())
    if nomor not in blok:
        return 0.0
    isi = blok[nomor]
    jeda = sum(int(x) for x in _re.findall(r"\(\(⏱️=(\d+)\)\)", isi)) / 1000
    kata = len(_re.sub(r"\(\(⏱️=\d+\)\)", " ", isi).split())
    return kata / TEMPO_ACUAN + jeda


def cari(folder: Path, nomor: str) -> Path | None:
    """Berkas audio untuk satu blok.

    Urutan prioritas: `_laras` (hasil regang_jeda.py) > `_rapi` (hasil
    pangkas_senyap.py) > rekaman asli. Tanpa aturan ini, urutan abjad yang
    kebetulan menang — dan yang terpilih bisa jadi rekaman mentah yang belum
    diregangkan, sehingga narasi habis sebelum slotnya selesai.

    Pencocokan nomor harus UTUH, bukan awalan. `09*` ikut menangkap `09b.mp3`,
    dan `1*` ikut menangkap `10.mp3` — yang terakhir berarti satu salah ketik
    nomor tanpa nol bisa memasang audio blok 10 di slot blok 1. Karena itu
    dipakai pencocokan tepat: stem harus `nomor`, `nomor_laras`, `nomor_rapi`,
    dan seterusnya — bukan sekadar diawali nomor.
    """
    calon = [
        c for c in sorted(folder.iterdir())
        if c.suffix.lower() in EKSTENSI
        and (c.stem == nomor or c.stem.startswith(nomor + "_"))
    ]
    if not calon:
        return None
    for akhiran in ("_laras", "_rapi"):
        cocok = [c for c in calon if c.stem == nomor + akhiran]
        if cocok:
            return cocok[0]
    return calon[0]


def jalankan(cmd: list[str]) -> None:
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-3000:], file=sys.stderr)
        raise SystemExit(f"gagal: {' '.join(cmd[:6])} …")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--audio", type=Path, required=True)
    p.add_argument("--video", type=Path, default=VIDEO)
    p.add_argument("--srt", type=Path, default=HERE / "subtitle_id.srt")
    p.add_argument("--cek", action="store_true", help="laporan saja, tidak merender")
    p.add_argument("--luar", type=Path, default=HERE)
    arg = p.parse_args()

    tim = json.loads(TIMING.read_text())
    total = tim["durasi_video_s"]
    # Slot dibaca per blok. Satu segmen bisa dipecah jadi beberapa blok narasi, jadi
    # batas_blok[segmen] - mulai_di[segmen] adalah panjang SEGMEN, bukan panjang blok.
    # Memakai itu membuat semua blok dalam satu segmen mendapat slot segmen penuh.
    _slot = {b["nomor"]: b["slot"] for b in tim["berkas"]}
    _mulai = {b["nomor"]: b["mulai"] for b in tim["berkas"]}

    # 1. Kumpulkan berkas dan periksa durasinya terhadap slot.
    blok_ada: list[dict] = []
    print(f"{'blok':5}{'berkas':>10}{'durasi':>9}{'slot':>7}{'lebih':>8}")
    print("-" * 40)
    masalah = 0
    for nomor in ORDER:
        berkas = cari(arg.audio, nomor)
        slot = _slot[nomor]
        if not berkas:
            terus = durasi_ucap(nomor)
            print(f"{nomor:5}{'—':>10}{terus:9.1f}{slot:7.1f}{terus - slot:+8.1f}  belum direkam")
            continue
        d = durasi(berkas)
        lebih = d - slot
        if lebih > 0.05:
            masalah += 1
        print(f"{nomor:5}{berkas.suffix:>10}{d:9.1f}{slot:7.1f}{lebih:+8.1f}"
              + ("  <<< LEWAT" if lebih > 0.05 else ""))
        blok_ada.append({
            "nomor": nomor, "berkas": berkas, "durasi": d,
            "mulai": _mulai[nomor], "slot": slot,
        })

    if not blok_ada:
        print("\ntidak ada berkas audio. taruh 01.ext … %s.ext di folder --audio."
              % ORDER[-1])
        return 1

    if masalah:
        print(f"\n{masalah} blok melewati slotnya. Perbaiki dulu dengan "
              f"regang_jeda.py --tulis, atau saya bisa potong di ujung slot — "
              f"tapi itu akan memotong kata terakhir. Lihat dulu apakah itu bisa diterima.")
    kurang = [b["nomor"] for b in blok_ada if b["slot"] - b["durasi"] > 3.0]
    if kurang:
        print(f"\n{len(kurang)} blok menyisakan lebih dari 3 detik kosong: "
              + ", ".join(kurang) + ". Suaranya muat, tapi layar akan diam setelah "
              f"narasinya habis. Jalankan ukur_tempo.py untuk melihat sebarannya.")
    print(f"\n{len(blok_ada)} dari {len(ORDER)} blok siap. Total video {total:.1f} s.")

    if arg.cek:
        print("\n(--cek: tidak ada yang dirender)")
        return 0

    # 2. Bangun filter: tiap blok di-delay ke posisinya, lalu dicampur di atas
    #    alas hening sepanjang video. alimiter mencegah klip saat dua blok bertumpuk.
    masukan: list[str] = []
    for b in blok_ada:
        masukan += ["-i", str(b["berkas"])]
    masukan += ["-i", str(arg.video)]

    filter_bagian = []
    label = []
    for i, b in enumerate(blok_ada):
        ms = int(round(b["mulai"] * 1000))
        # atrim + asetpts: tanpa ini, adelay memakai PTS asli berkas dan blok
        # yang panjang akan menggeser semua blok sesudahnya.
        # apad + atrim: berkas harus tepat sepanjang slot, supaya durasi campuran
        # tidak ditentukan oleh berkas terpendek.
        filter_bagian.append(
            f"[{i}:a]aformat=sample_rates=48000:channel_layouts=stereo,"
            f"atrim=0:{b['slot']:.3f},asetpts=N/SR/TB,"
            f"apad=whole_dur={b['slot']:.3f},atrim=0:{b['slot']:.3f},"
            f"adelay={ms}|{ms}[a{i}]"
        )
        label.append(f"[a{i}]")
    filter_bagian.append(f"anullsrc=r=48000:cl=stereo,atrim=0:{total:.3f}[alas]")
    # normalize=0 wajib: tanpa itu amix membagi volume dengan jumlah input, jadi
    # satu blok bersuara akan terdengar sangat pelan karena ada 8 input kosong.
    filter_bagian.append(
        "".join(label) + f"[alas]amix=inputs={len(label)+1}:duration=longest:normalize=0,"
        f"alimiter=limit=0.95,loudnorm=I=-16:TP=-1.5:LRA=11,"
        f"aformat=sample_rates=48000:channel_layouts=stereo,"
        f"atrim=0:{total:.3f}[aout]"
    )

    idx_video = len(blok_ada)
    dasar = arg.luar / "EduCraft_Demo_narasi"
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"] + masukan + [
        "-filter_complex", ";".join(filter_bagian),
        "-map", f"{idx_video}:v:0", "-map", "[aout]",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        f"{dasar}.mp4",
    ]
    print("\nmerender video bernarasi …")
    jalankan(cmd)
    keluaran = dasar.with_suffix(".mp4")
    print(f"  {keluaran.name}  ({keluaran.stat().st_size / 1e6:.1f} MB)")

    # SRT ditaruh di sebelah video supaya bisa dipasang di pemutar mana pun.
    # Versi terbakar memakai salinan tersaring; berkas ini tetap lengkap.
    if arg.srt.exists():
        (arg.luar / arg.srt.name).write_text(arg.srt.read_text())

    # 3. Versi subtitle terbakar. Font harus ada di sistem; DejaVu Sans selalu ada
    #    di Linux dan mendukung aksara Latin Indonesia.
    #
    #    BorderStyle=3 (kotak) dipilih setelah memeriksa bingkai sungguhan. Video ini
    #    rekaman layar dokumen: hampir seluruh bingkai berisi teks abu-abu, dan
    #    subtitle putih ber-outline hitam bertabrakan dengan teks halaman di setiap
    #    detik. Kotak hitam 50% memisahkan subtitle sebagai lapisan, tanpa menutupi
    #    halaman sepenuhnya — pada 100% halaman hilang, pada 0% kembali bertabrakan.
    #
    #    MarginV 88 mengangkat teks dari kotak komposisi WorkBuddy yang duduk di
    #    ±80 px terbawah rekaman. FontSize 18 terlalu kecil untuk 1366 px setelah
    #    kotak ditambahkan; 20 terbaca di 1080p maupun di ponsel.
    if arg.srt.exists():
        gaya = (
            "FontName=DejaVu Sans,FontSize=20,PrimaryColour=&H00FFFFFF,"
            "OutlineColour=&H00000000,BorderStyle=3,Outline=1,Shadow=0,"
            "MarginV=88,Bold=0,BackColour=&H80000000"
        )
        # Versi tersaring ditulis di sebelah video, bukan di folder narasi, supaya
        # subtitle_id.srt tetap lengkap dan bisa dipakai ulang.
        terbakar = arg.luar / "subtitle_bakar.srt"
        asli = arg.srt.read_text()
        terbakar.write_text(saring_srt(asli, SRT_TERTUTUP))
        dibuang = len([c for c in asli.strip().split("\n\n") if c.strip()]) - len(
            [c for c in terbakar.read_text().strip().split("\n\n") if c.strip()]
        )
        jalankan([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-i", f"{dasar}.mp4",
            "-vf", f"subtitles={terbakar.name}:force_style='{gaya}'",
            "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-pix_fmt", "yuv420p",
            "-c:a", "copy", "-movflags", "+faststart",
            f"{dasar}_bakar.mp4",
        ])
        print(f"  {dasar.name}_bakar.mp4  ({dibuang} cue disembunyikan: teksnya sudah di layar)")
    else:
        print(f"\n{arg.srt.name} belum ada — subtitle terbakar dilewati.")

    print("\nselesai.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
