"""USANG — jangan dipakai.

Mengikuti pembagian 8 blok yang tidak ada di video. Yang berlaku sekarang:
SKRIP_TTS_LAYAR.md (7 blok) + TIMING.json versi 2.
"""

"""Setel Jeda — hitungan, bukan selera

Alat ini membaca SKRIP_TTS_JEDA.md, menghitung durasi tiap blok dari jumlah kata dan jumlah jeda,
lalu menyetel angka jeda supaya tiap blok jatuh tepat di slot videonya.

Jalankan setelah mesin TTS Anda menghasilkan satu berkas contoh. Angka tempo di sini masih asumsi;
begitu ada tiga berkas nyata, saya ganti dengan tempo mesin Anda yang terukur.

```bash
python3 setel_jeda.py                    # tampilkan laporan saja, tidak menulis apa pun
python3 setel_jeda.py --tempo 3.1        # pakai tempo hasil ukur, bukan asumsi
python3 setel_jeda.py --tempo 3.1 --tulis  # tulis SKRIP_TTS_JEDA.md versi baru
```

Kenapa ada laporan dulu: kalau angka jedanya dinaikkan buta, video berubah jadi narasi yang berhenti
setiap lima detik. Yang benar bukan "tambahi jeda sampai penuh", tapi "tambahi di tempat yang
memang butuh jeda".
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKRIP = HERE / "SKRIP_TTS_JEDA.md"
TIMING = HERE / "TIMING.json"

# Tempo bawaan: 3,25 kata/detik. Diambil dari rentang wajar Bahasa Indonesia yang diucapkan
# tenang (3,0-3,5). Bukan angka keramat — ganti begitu tempo mesin Anda terukur.
TEMPO_BAWAAN = 3.25

# Batas atas jeda yang masih wajar di satu titik. Di atas ini, narasi terdengar seperti
# menunggu buffering. Kalau dibutuhkan lebih, masalahnya di kalimat, bukan di jeda.
JEDA_MAKS = 1200

# Jeda yang tidak boleh disentuh: penutup blok. Fungsinya mengisi sisa slot, dan
# memendekkannya justru membuat blok berikut mulai terlalu cepat.
JEDA_UJUNG_MIN = 300

POLA_JEDA = re.compile(r"\(\(⏱️=(\d+)\)\)")


def baca_blok(teks: str) -> list[tuple[str, str]]:
    """Ambil isi tiap kotak kode, berpasangan dengan nomor bloknya dari judul di atasnya."""
    hasil = []
    for cocok in re.finditer(r"## `(\d{2})`.*?```\n(.*?)```", teks, re.S):
        hasil.append((cocok.group(1), cocok.group(2)))
    return hasil


def kata_dan_jeda(isi: str) -> tuple[int, list[int]]:
    jeda = [int(x) for x in POLA_JEDA.findall(isi)]
    teks = POLA_JEDA.sub(" ", isi)
    return len(teks.split()), jeda


def durasi(kata: int, jeda: list[int], tempo: float) -> float:
    return kata / tempo + sum(jeda) / 1000


def setel(isi: str, target: float, tempo: float) -> tuple[str, dict]:
    kata, jeda = kata_dan_jeda(isi)
    awal = durasi(kata, jeda, tempo)
    kurang = target - awal          # positif = perlu ditambah, negatif = perlu dipotong
    catatan = {
        "kata": kata,
        "jeda_awal_ms": sum(jeda),
        "durasi_awal": awal,
        "selisih": kurang,
        "tindakan": "",
    }

    if abs(kurang) < 0.4:
        catatan["tindakan"] = "sudah pas"
        catatan["jeda_akhir_ms"] = sum(jeda)
        catatan["durasi_akhir"] = awal
        return isi, catatan

    if kurang > 0:
        # Bagi rata ke semua jeda, tapi hormati batas atas. Kalau masih kurang,
        # sisanya masuk ke jeda ujung blok.
        bisa_dinaikkan = [i for i, j in enumerate(jeda) if j < JEDA_MAKS]
        sisa = kurang * 1000
        if bisa_dinaikkan:
            per_jeda = sisa / len(bisa_dinaikkan)
            for i in bisa_dinaikkan:
                tambah = min(per_jeda, JEDA_MAKS - jeda[i])
                jeda[i] += int(tambah)
                sisa -= tambah
        if sisa > 0:
            jeda[-1] += int(sisa)
        catatan["tindakan"] = "jeda dinaikkan"
    else:
        # Perlu dipotong. Ambil dari jeda terpanjang dulu, sisakan minimum di ujung.
        kurang_ms = int(-kurang * 1000)
        urut = sorted(range(len(jeda)), key=lambda i: -jeda[i])
        for i in urut:
            batas = JEDA_UJUNG_MIN if i == len(jeda) - 1 else 150
            potong = min(kurang_ms, jeda[i] - batas)
            if potong > 0:
                jeda[i] -= potong
                kurang_ms -= potong
            if kurang_ms <= 0:
                break
        if kurang_ms > 0:
            catatan["tindakan"] = f"MASIH KURANG {kurang_ms} ms — perlu potong kalimat"
        else:
            catatan["tindakan"] = "jeda dipotong"

    # Tulis ulang angka jeda sesuai urutan kemunculan.
    keluaran = []
    idx = 0
    posisi = 0
    for cocok in POLA_JEDA.finditer(isi):
        keluaran.append(isi[posisi:cocok.start()])
        keluaran.append(f"((⏱️={jeda[idx]}))")
        posisi = cocok.end()
        idx += 1
    keluaran.append(isi[posisi:])
    catatan["jeda_akhir_ms"] = sum(jeda)
    catatan["durasi_akhir"] = durasi(kata, jeda, tempo)
    return "".join(keluaran), catatan


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--tempo", type=float, default=TEMPO_BAWAAN, help="kata/detik")
    p.add_argument("--tulis", action="store_true", help="tulis hasilnya ke SKRIP_TTS_JEDA.md")
    arg = p.parse_args()

    teks = SKRIP.read_text()
    timing = json.loads(TIMING.read_text())
    batas, mulai = timing["batas_blok"], timing["mulai_di"]
    nama = ["pembuka", "seg1", "seg2", "seg3", "seg4", "seg5", "seg6", "tutup"]

    print(f"tempo {arg.tempo} kata/detik · jeda maks per titik {JEDA_MAKS} ms\n")
    print(f"{'blok':5}{'kata':>5}{'target':>7}{'awal':>7}{'selisih':>8}{'akhir':>7}  tindakan")
    print("-" * 66)

    hasil_baru = {}
    for (nomor, isi), kunci in zip(baca_blok(teks), nama):
        # Slot bicara = mulai blok berikutnya dikurangi 0,8 s untuk napas sebelum kartu.
        target = batas[kunci] - mulai[kunci] - 0.8
        baru, cat = setel(isi, target, arg.tempo)
        hasil_baru[nomor] = baru
        print(
            f"{nomor:5}{cat['kata']:5d}{target:7.1f}{cat['durasi_awal']:7.1f}"
            f"{cat['selisih']:+8.1f}{cat['durasi_akhir']:7.1f}  {cat['tindakan']}"
        )

    if not arg.tulis:
        print("\n(tidak ada yang ditulis — tambahkan --tulis kalau angkanya sudah masuk akal)")
        return 0

    keluaran = teks
    for nomor, isi in hasil_baru.items():
        lama = dict(baca_blok(teks))[nomor]
        keluaran = keluaran.replace(f"```\n{lama}```", f"```\n{isi}```", 1)
    SKRIP.write_text(keluaran)
    print(f"\nditulis: {SKRIP}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
