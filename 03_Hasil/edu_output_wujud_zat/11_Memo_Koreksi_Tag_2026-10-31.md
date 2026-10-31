# MEMO KOREKSI — rujukan sumber pada paket cetak "Perubahan Wujud Zat"

**Untuk:** don Jimat Akbar (guru) · **Dari:** tim EduCraft · **Tanggal:** 31 Oktober 2026
**Berlaku untuk:** `08_Paket_Siswa_Cetak.pdf`, `09_Paket_Guru_Cetak.pdf`, `10_Lembar_Kerja_Pengamatan.pdf`

---

## 1. Apa yang berubah

Di kaki halaman paket cetak yang sudah Bapak/Ibu terima tertulis rujukan `[src:B4]`. Rujukan itu
kurang tepat: `B4` adalah **nomor topik** pada dokumen Capaian Pembelajaran, bukan dokumen yang
memuat faktanya.

Rujukan yang benar sekarang: **`[src:W1]`–`[src:W11]`** pada berkas
`source_material_wujud_zat.md`, yang seluruh entrinya dikutip dari *Panduan Mata Pelajaran IPAS,
Revisi 4 (3 Oktober 2025)*, bagian "Proses Perubahan Wujud Zat", halaman 26–27.

## 2. Apa yang TIDAK berubah

**Isi materi tidak diubah sama sekali.** Tidak ada kalimat yang ditambah, dihapus, atau diperhalus.
Jumlah butir kuis tetap 27, kunci jawaban tetap sama, dan tidak ada angka suhu yang ditambahkan.
Yang berubah hanya label rujukan di kaki halaman.

Karena itu, **paket yang sudah dicetak tetap layak dipakai di kelas.** Tidak perlu cetak ulang.

## 3. Satu hal yang perlu Bapak/Ibu putuskan

Sebelas entri sumber terdiri dari dua jenis:

| Jenis | Tag | Isi | Status |
|-------|-----|-----|--------|
| Kutipan resmi | `[src:W1]`–`[src:W9]` | Tiga wujud, enam nama proses, peran suhu, contoh fenomena, saran pengamatan, bentuk asesmen | Dapat dipertanggungjawabkan langsung ke Panduan IPAS |
| **Turunan tim** | `[src:W10]` | Pemetaan arah enam proses (padat→cair = mencair, dst.) | **Perlu validasi Bapak/Ibu** |
| **Turunan tim** | `[src:W11]` | Penerapan sehari-hari (butiran air di gelas, pakaian dijemur, air di freezer) dan konsep "zat tetap, wujud berubah" | **Perlu validasi Bapak/Ibu** |

Sumber resmi menyebut **nama** keenam proses, tetapi tidak memetakan arahnya secara eksplisit dan
tidak memuat contoh penerapan di atas. Isinya adalah pengetahuan sains standar yang disusun tim.
Karena butir kuis nomor 19–21, 35–43, dan 57 bertumpu pada pemetaan arah tersebut, mohon dikonfirmasi
apakah pemetaan itu boleh dipakai sebagai dasar penilaian.

**Cukup balas:** "pemetaan arah dan contoh penerapan disetujui" — atau tandai butir mana yang perlu
diubah.

## 4. Ringkasan pemeriksaan

| Pemeriksaan | Hasil |
|-------------|-------|
| Tag yang diperiksa | 115 |
| Tag tanpa rujukan (dangling) | 0 |
| Tag kelas salah (kurikulum dipakai untuk fakta) | 0 |
| Verdict | **PASS** — `03_Hasil/edu_output_wujud_zat/grounding_report.md` |

Pemeriksaan ini deterministik dan dapat diulang kapan saja oleh siapa pun:

```bash
python3 tools/check_grounding.py --run 03_Hasil/edu_output_wujud_zat \
    --knowledge 03_Hasil/referensi --out /tmp/cek.md
```
