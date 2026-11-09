"""Selaraskan subtitle dengan audio hasil TTS yang sebenarnya.

Kenapa perlu: `buat_subtitle.py` menghitung waktu dari jumlah kata dibagi tempo perkiraan
(3,25 kata/detik). Mesin TTS kenyataannya lain — ada yang 3,0, ada yang 3,6. Kalau dibiarkan,
subtitle akan bergeser dari suara, dan makin ke belakang makin jauh.

Cara kerja:
  1. Deteksi keheningan di audio (ffmpeg silencedetect).
  2. Ubah keheningan menjadi REGION BICARA — bagian berkas yang tidak senyap.
     Ini penting: jumlah keheningan TIDAK sama dengan jumlah kalimat. Mesin
     menyisipkan napas di tengah kalimat, jadi satu kalimat bisa terpecah menjadi
     dua atau tiga region. Pada blok 02 ada 39 keheningan untuk 28 kalimat.
  3. Kelompokkan region bicara menjadi tepat satu kelompok per kalimat, dengan
     pemrograman dinamis: panjang ucapan tiap kelompok dibuat sedekat mungkin
     dengan proporsi jumlah kata kalimatnya, dan batas kelompok dihukum ringan
     kalau jatuh di sel pendek (napas di tengah kalimat).
  4. Waktu tiap cue = rentang kalimat itu, dibagi lagi menurut jumlah kata.

Kalau audio tidak punya cukup region untuk 3 kalimat (blok `01`: satu region),
pemetaan region tidak mungkin; bagian itu dibagi menurut jumlah kata saja.

    python3 selaras_subtitle.py --audio narasi/audio
    python3 selaras_subtitle.py --audio narasi/audio --ambang -40 --lapor
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

from buat_subtitle import (
    MAKS_BARIS,
    BARIS_PER_CUE,
    baca_blok,
    bungkus,
    pecah,
    pecah_cue,
    senyap,
    waktu,
    NAPAS,
    MIN_CUE,
    MAKS_CUE,
)

HERE = Path(__file__).resolve().parent
TIMING = HERE / "TIMING.json"
# Dibaca dari TIMING.json supaya jumlah segmen tidak perlu disalin ke tiap skrip.
_tim = json.loads(TIMING.read_text())
ORDER = [b["nomor"] for b in _tim["berkas"]]
NAMES = [b["segmen"] for b in _tim["berkas"]]
EKSTENSI = {".wav", ".mp3", ".m4a", ".aac", ".flac", ".ogg", ".opus"}


def slot_blok(tim: dict, nomor: str) -> float:
    """Slot satu blok, dibaca dari TIMING.json.

    Satu segmen bisa dipecah jadi beberapa blok narasi. Karena itu
    `batas_blok[segmen] - mulai_di[segmen]` adalah panjang SEGMEN, bukan panjang
    blok — memakainya membuat semua blok dalam satu segmen mendapat slot yang
    sama (seluruh blok tercetak 174 detik). Nilai `slot` per blok sudah dihitung
    saat TIMING.json dibuat, jadi pakai itu.
    """
    for b in tim["berkas"]:
        if b["nomor"] == nomor:
            return b["slot"]
    raise KeyError(f"blok {nomor} tidak ada di TIMING.json")


def mulai_blok(tim: dict, nomor: str) -> float:
    for b in tim["berkas"]:
        if b["nomor"] == nomor:
            return b["mulai"]
    raise KeyError(f"blok {nomor} tidak ada di TIMING.json")



def durasi(berkas: Path) -> float:
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(berkas)],
        capture_output=True, text=True,
    )
    return float(r.stdout.strip())


def cari(folder: Path, nomor: str) -> Path | None:
    """Berkas audio untuk satu blok, `_laras` lalu `_rapi` didahulukan.

    Subtitle diselaraskan ke waktu bicara di berkas ini. Kalau yang terpilih rekaman
    asli sementara video memakai versi yang sudah diregangkan, setiap cue setelah
    jeda pertama akan bergeser lebih awal — dan tidak ada yang memberi tahu.

    Pencocokan nomor harus UTUH, bukan awalan: `09*` ikut menangkap `09b.mp3` dan
    `1*` ikut menangkap `10.mp3`. Di berkas ini akibatnya lebih halus daripada
    sekadar salah audio — cue akan diselaraskan ke blok yang salah dan tetap
    terlihat wajar.
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


def region_bicara(senyap: list[tuple[float, float]], total: float) -> list[tuple[float, float]]:
    """Bagian berkas yang TIDAK senyap — yaitu tempat kata diucapkan."""
    hasil = []
    pos = 0.0
    for a, b in senyap:
        if a > pos + 0.01:
            hasil.append((pos, a))
        pos = max(pos, b)
    if total > pos + 0.01:
        hasil.append((pos, total))
    return hasil


def selaras_kata(kal: list, mulai: float, akhir: float) -> list[float]:
    """Pembagian waktu sederhana menurut jumlah kata, tanpa melihat region bicara.

    Dipakai kalau audio tidak punya cukup senyap untuk menemukan batas kalimat —
    blok `01` misalnya sama sekali tidak punya senyap terdeteksi, hanya satu region
    untuk tiga kalimat. Memaksakan DP di situ menghasilkan semua batas di ujung yang
    sama, lalu cue menumpuk dan meluber ke blok berikutnya.
    """
    kata = [max(1, k.kata) for k in kal]
    total = sum(kata) or 1
    rentang = max(0.1, akhir - mulai)
    hasil = []
    t = mulai
    for k in kata:
        t += rentang * k / total
        hasil.append(t)
    return hasil


def selaras_dp(kal: list, ucap: list[tuple[float, float]],
               senyap: list[tuple[float, float]] | None = None) -> list[float]:
    """Kelompokkan region bicara menjadi len(kal) kelompok, sebanding jumlah kata.

    Kembalikan waktu akhir (relatif terhadap berkas) untuk tiap kalimat.

    Kenapa dinamis, bukan bagi rata: satu kalimat bisa terdiri atas beberapa region
    karena mesin menyisipkan napas di tengahnya, dan jumlah region per kalimat tidak
    diketahui. Yang bisa dipakai sebagai patokan hanyalah panjang ucapannya: kalimat
    9 kata memakan waktu kira-kira tiga kali kalimat 3 kata.

    Dua biaya digabung:

      1. Selisih durasi ucapan kelompok terhadap proporsi kata kelompok itu. Ini
         menjaga kalimat panjang tidak "dirampas" kalimat pendek di sebelahnya.
      2. Sela di antara dua region yang dipisah di titik itu. Kalau selanya panjang
         (≥ JEDA_KALIMAT), memisah di sana tidak dihukum — memang di situlah jeda
         skrip berada. Sel pendek berarti mesin cuma menarik napas di tengah
         kalimat; memisah di sana dihukum ringan supaya pengelompokan tidak
         terbelah hanya karena panjangnya kebetulan cocok.

    Tanpa biaya kedua, pembagian hanya mengejar panjang dan batas kalimat bisa
    bergeser satu region — cukup untuk membuat subtitle tampil saat tidak ada
    suara.
    """
    n, m = len(kal), len(ucap)
    if n == 0 or m == 0:
        return [ucap[-1][1] if ucap else 0.0] * n

    JEDA_KALIMAT = 0.70   # detik. Di atas ini dianggap jeda antar-kalimat.
    BOBOT_SELA = 0.55     # seberapa berat memisah di sel pendek

    def sela(j: int) -> float:
        """Jarak antara region j-1 dan region j (j = titik belah)."""
        return max(0.0, ucap[j][0] - ucap[j - 1][1])

    kata = [max(1, k.kata) for k in kal]
    total_kata = sum(kata)
    kum = [0.0]
    for a, b in ucap:
        kum.append(kum[-1] + (b - a))
    total_ucap = kum[-1]

    TAK = float("inf")
    biaya = [[TAK] * (m + 1) for _ in range(n + 1)]
    dari = [[0] * (m + 1) for _ in range(n + 1)]
    biaya[0][0] = 0.0

    for i in range(1, n + 1):
        harap_i = total_ucap * kata[i - 1] / total_kata
        for j in range(i, m + 1):
            for p in range(i - 1, j):
                if biaya[i - 1][p] == TAK:
                    continue
                panjang = kum[j] - kum[p]
                c = biaya[i - 1][p] + (panjang - harap_i) ** 2
                if i > 1 and p > 0:
                    s = sela(p)
                    if s < JEDA_KALIMAT:
                        # Sel pendek: kemungkinan besar masih di dalam kalimat.
                        c += BOBOT_SELA * (JEDA_KALIMAT - s)
                if c < biaya[i][j]:
                    biaya[i][j] = c
                    dari[i][j] = p

    # Telusuri balik untuk mendapat batas kelompok.
    batas = [m]
    j = m
    for i in range(n, 0, -1):
        j = dari[i][j]
        batas.append(j)
    batas.reverse()          # batas[0]=0, batas[n]=m

    akhir = []
    for i in range(n):
        p, j = batas[i], batas[i + 1]
        if i < n - 1:
            akhir.append(ucap[j - 1][1])   # ujung region terakhir kelompok ini
        else:
            akhir.append(ucap[-1][1])
    return akhir


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--audio", type=Path, required=True)
    p.add_argument("--ambang", type=int, default=-35, help="dB untuk deteksi senyap")
    p.add_argument("--min-dur", type=float, default=0.18, help="detik minimum senyap")
    p.add_argument("--keluar", type=Path, default=HERE / "subtitle_id.srt")
    p.add_argument("--lapor", action="store_true")
    arg = p.parse_args()

    blok = baca_blok(HERE.joinpath("SKRIP_TTS_LAYAR.md").read_text())
    tim = json.loads(TIMING.read_text())

    cues: list[tuple[float, float, str]] = []
    print(f"{'blok':5}{'diharap':>8}{'nyata':>7}{'durasi':>9}{'slot':>7}{'beda':>8}")
    print("-" * 44)

    for nomor, nama in zip(ORDER, NAMES):
        berkas = cari(arg.audio, nomor)
        if not berkas:
            print(f"{nomor:5}  berkas tidak ditemukan — dilewati")
            continue

        kal = pecah(blok[nomor])
        harap = sum(1 for k in kal if k.jeda_ms >= arg.min_dur * 1000)
        nyata = senyap(berkas, arg.ambang, arg.min_dur)
        slot = slot_blok(tim, nomor)
        nyata_dur = durasi(berkas)

        # Jeda di skrip, urut. Jeda terakhir sebuah blok biasanya tepat di ujung
        # berkas, jadi tidak selalu muncul sebagai "keheningan tengah".
        jeda = [k.jeda_ms for k in kal if k.jeda_ms >= arg.min_dur * 1000]

        # ---- Penyelarasan ----
        #
        # Versi lama memetakan kalimat ke keheningan SECARA PROPORSIONAL:
        #   rasio = (i+1)/len(kal); idx = round(rasio*len(nyata))-1
        # Itu tidak memakai isi audio sama sekali — hanya "keheningan ke berapa
        # kira-kira di tengah berkas". Hasilnya meleset begitu jumlah keheningan
        # tidak sama dengan jumlah kalimat, dan di blok 02 jumlahnya 39 lawan 28.
        #
        # Yang benar: kalimat terucap sebagai deret REGIO BICARA, dan mesin kadang
        # menyisipkan napas di tengah kalimat sehingga satu kalimat bisa terpecah
        # jadi dua-tiga region. Jadi tugasnya bukan mencocokkan keheningan, tapi
        # mengelompokkan region bicara menjadi tepat len(kal) kelompok.
        #
        # Patokan pengelompokan: panjang ucapan tiap kalimat sebanding jumlah
        # katanya. Diselesaikan dengan pemrograman dinamis — pilih titik belah yang
        # membuat jumlah region tiap kelompok paling dekat dengan proporsi katanya.
        # Ini tetap menghasilkan waktu monoton, tanpa perlu koreksi manual.
        ucap = region_bicara(nyata, nyata_dur)
        nyata_sah = [s for s in nyata if (s[1] - s[0]) >= arg.min_dur * 0.8]

        # Cukup bukti untuk memetakan batas kalimat? Butuh setidaknya satu region
        # lebih banyak daripada jumlah kalimat — tanpa itu, tidak ada tempat untuk
        # meletakkan batas.
        if len(ucap) <= len(kal):
            ucap_awal = ucap[0][0] if ucap else 0.0
            ucap_akhir = ucap[-1][1] if ucap else nyata_dur
            ujung_rel = selaras_kata(kal, ucap_awal, ucap_akhir)
            cara = "kata"
        else:
            ujung_rel = selaras_dp(kal, ucap, nyata)
            cara = "region"

        if arg.lapor:
            print(f"\nblok {nomor}: {len(jeda)} jeda di skrip, {len(nyata)} keheningan, "
                  f"{len(ucap)} region bicara untuk {len(kal)} kalimat — selaras lewat {cara}")
            for i, j in enumerate(jeda):
                if i < len(nyata_sah):
                    s = nyata_sah[i]
                    print(f"   jeda {i+1:2d}: skrip {j:5d} ms | audio {1000*(s[1]-s[0]):5.0f} ms")
                else:
                    print(f"   jeda {i+1:2d}: skrip {j:5d} ms | audio — tidak ada keheningan")

        # Bangun cue: waktu dihitung di dalam berkas blok, lalu digeser ke posisi
        # blok di dalam video. Tanpa geseran ini semua cue mulai dari detik nol.
        awal_berkas = mulai_blok(tim, nomor)
        ujung = [awal_berkas + u for u in ujung_rel]

        # Bagi waktu tiap kalimat ke cue-nya secara proporsional menurut jumlah kata.
        #
        # `selesai` sudah menunjuk ujung ucapan kalimat itu — termasuk jeda sesudahnya,
        # karena ujung itu diambil dari awal region bicara berikutnya. Jadi SETELAH
        # cue terakhir kalimat, `t` harus dilompatkan ke `selesai`, bukan ditambah
        # k.jeda_ms lagi. Versi lama menambahkan jeda di atas rentang yang sudah
        # memuat jeda itu, sehingga cue berikutnya mulai sesudah suaranya selesai —
        # pada blok 02 cue "Lalu topiknya apa." tampil 1,9 s setelah kalimatnya habis.
        t = awal_berkas
        for k, selesai in zip(kal, ujung):
            dur_kal = max(0.3, selesai - t)
            bagian = pecah_cue(k)
            total_kata = sum(x for _, x in bagian) or 1
            for teks_cue, kata_cue in bagian:
                panjang = dur_kal * kata_cue / total_kata
                # Cue lebih dari 6,5 detik sulit dibaca sekaligus. Pengenal kalimat
                # kadang menggabungkan dua kalimat asli ("Ia mengembalikan pertanyaan
                # kepada orang yang berhak memutuskan. Keputusan tercatat."), sehingga
                # satu cue tampil 7 detik. Pecah di titik akhir kalimat, bagi waktunya
                # menurut jumlah kata.
                if panjang > 6.5 and re.search(r"[.!?]\s", teks_cue):
                    keping = [x.strip() for x in re.split(r"(?<=[.!?])\s+", teks_cue) if x.strip()]
                    if len(keping) > 1:
                        n_kata = [len(x.split()) for x in keping]
                        tot = sum(n_kata) or 1
                        tt = t
                        for kp, nk in zip(keping, n_kata):
                            pk = panjang * nk / tot
                            cues.append((tt, tt + pk - NAPAS, kp))
                            tt += pk
                        t += panjang
                        continue
                cues.append((t, t + panjang - NAPAS, teks_cue))
                t += panjang
            t = max(t, selesai)

        print(f"{nomor:5}{harap:8d}{len(nyata):7d}{nyata_dur:9.1f}{slot:7.0f}{nyata_dur-slot:+8.1f}")

    # Gabung cue yang terlalu pendek, sama seperti di buat_subtitle.
    gabung: list[tuple[float, float, str]] = []
    for a, b, teks_cue in cues:
        if gabung and len(teks_cue.split()) < 3:
            prev_a, prev_b, prev_t = gabung[-1]
            calon = f"{prev_t} {teks_cue}"
            if len(calon) <= MAKS_BARIS * BARIS_PER_CUE:
                gabung[-1] = (prev_a, b, calon)
                continue
        gabung.append((a, b, teks_cue))

    # Penggabungan di atas bisa menghasilkan cue 7 detik berisi dua kalimat:
    # "Keputusan tercatat." hanya dua kata, jadi ia menempel ke kalimat sebelumnya.
    # Pemeriksaan panjang di loop utama tidak pernah melihat hasil gabungan ini.
    # Pecah lagi di titik akhir kalimat, bagi waktunya menurut jumlah kata.
    gabung2: list[tuple[float, float, str]] = []
    for a, b, teks_cue in gabung:
        if (b - a) > 6.5 and len(teks_cue.split()) >= 3 and re.search(r"[.!?]\s", teks_cue):
            keping = [x.strip() for x in re.split(r"(?<=[.!?])\s+", teks_cue) if x.strip()]
            if len(keping) > 1:
                n_kata = [len(x.split()) for x in keping]
                tot = sum(n_kata) or 1
                tt = a
                for kp, nk in zip(keping, n_kata):
                    pk = (b - a) * nk / tot
                    gabung2.append((tt, tt + pk - NAPAS, kp))
                    tt += pk
                continue
        gabung2.append((a, b, teks_cue))
    gabung = gabung2

    # Pemenggal kata bisa memotong di tengah frasa: "…kepala" lalu "sekolah:" lalu
    # "dari mana materinya." Cue tengah yang sangat pendek TIDAK boleh diberi durasi
    # tambahan — harus disatukan kembali ke tetangganya. Menambah durasi hanya membuat
    # potongan yang sama tampil lebih lama.
    gabung3: list[tuple[float, float, str]] = []
    for a, b, teks_cue in gabung:
        terlalu_pendek = (b - a) < 1.0 and len(teks_cue.split()) <= 2
        if terlalu_pendek and gabung3:
            pa, pb, pt = gabung3[-1]
            calon = f"{pt} {teks_cue}"
            # Kelonggaran 6 karakter: menolak penggabungan karena lewat 2 karakter
            # hanya memindahkan masalahnya — kata jadi berdiri sendiri 0,6 detik.
            # Tiga baris singkat masih terbaca; kata terisolasi tidak.
            if len(calon) <= MAKS_BARIS * BARIS_PER_CUE + 6:
                gabung3[-1] = (pa, b, calon)
                continue
        # Cue pendek di awal blok: gabung ke cue SESUDAHNYA tidak bisa dilakukan di
        # sini (belum dibaca), tapi ini hanya terjadi pada kata pertama blok dan
        # durasinya sudah wajar.
        gabung3.append((a, b, teks_cue))
    gabung = gabung3

    out = []
    for i, (a, b, teks_cue) in enumerate(gabung):
        berikut = gabung[i + 1][0] if i + 1 < len(gabung) else None
        if b - a < MIN_CUE:
            b = a + MIN_CUE
        # Cue tidak boleh melewati awal cue berikutnya. Tanpa batas ini, dua cue
        # yang berdekatan akan tampil bertumpuk di layar.
        if berikut is not None:
            b = min(b, berikut - NAPAS)
        if b <= a:
            b = a + 0.4
        if b - a > MAKS_CUE:
            b = a + MAKS_CUE
        out.append(f"{i + 1}\n{waktu(a)} --> {waktu(b)}\n")
        for l in bungkus(teks_cue):
            out.append(l.rstrip() + "\n")
        out.append("\n")
    arg.keluar.write_text("".join(out))
    print(f"\n{len(gabung)} cue → {arg.keluar.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
