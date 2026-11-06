# Audit Log — EDU-ORCH-20261106-008

## §1 Pipeline inti

| Waktu | Fase | Masukan | Keputusan |
|---|---|---|---|
| 17:09 | Intake | Topik "Energi Alternatif", kelas V, source `source_material_energi.md`, format "poster promosi" | Dipetakan ke bab **C4**, Fase C. Menu tidak ditayangkan (topik sudah disebut). "Poster" bukan format kanonik → dipetakan ke `infographic_brief` |
| 17:09 | Intake | Tiga elemen komersial diminta guru | Ditulis apa adanya di Draf 1 untuk diuji, tidak disaring diam-diam |
| 17:10 | Plan | `[src:1]`–`[src:9]`, `[src:CP]` | Kerangka poster 9 lapis disusun |
| 17:11 | Draft | Kerangka + sumber | `01_poster_draf1.md` |
| 17:11 | Review 1 | Draf 1 + rulebook + sumber | **`REJECT`** — R001, R012.2, R012.3, R006. `Iteration` = 1 |
| 17:12 | Draft ulang | Remediasi minimal dari Reviewer | `03_poster_draf2.md` — klaim superlatif dan label halal dihapus |
| 17:13 | Review 2 | Draf 2 | **`APPROVE`** — 0 blocking, 4 minor. `Iteration` tetap 1 |
| 17:12 | Approval gate | Persetujuan manusia | **Disetujui** — opsi "terbitkan versi patuh" |
| 17:15 | Format Rendering | Gate terpenuhi | `06_poster_energi_alternatif.html`, `.png`, `.pdf` |

## §2 Keputusan atas permintaan komersial

| Elemen diminta | Putusan | Dasar | Pengganti |
|---|---|---|---|
| "Metode belajar kami terbukti paling ampuh di Indonesia" | **Ditolak** | R001 (tanpa tag, tidak ada bagian sumber yang memuat data efikasi), R012.3 (superlatif komersial tanpa bukti), R006 (efikasi absolut) | "Belajar dari matahari, angin, air, dan biogas" `[src:2]` |
| "100% halal" | **Ditolak** | R012.2 (klaim halal tanpa nomor sertifikat dan lembaga penerbit) | Lencana sudut "SESUAI CP-C.2.1.4" `[src:CP]` |
| Nama merek "EduCraft Pro" | **Diterima** | R008 — nama merek tidak dilarang; tone tetap edukatif | — |

Catatan: label halal dapat dikembalikan bila guru menyertakan nomor sertifikat dan lembaga penerbit.

## §3 Format Rendering

### §3.1 Konversi `infographic_brief` → artefak

| Artefak | Berkas | Alat |
|---|---|---|
| HTML interaktif/cetak | `06_poster_energi_alternatif.html` | tulis langsung, CSS cetak A2 |
| Raster 300 dpi | `poster_energi_alternatif_A2.png` (4959 × 7016 px) | Chrome headless, `?export=1` |
| PDF cetak | `poster_energi_alternatif_A2.pdf` (420 × 594 mm, 1 halaman) | PyMuPDF dari raster 300 dpi |

PDF tidak dibuat lewat `--print-to-pdf` Chrome karena mode CLI mengabaikan `@page size` dan
menghasilkan Letter 2 halaman. PDF disusun dari raster 300 dpi pada kanvas A2 eksak.

### §3.2 Source Resolution Map (FR-02)

| Tag | Kelas | Kutipan sumber yang mendasari |
|---|---|---|
| `[src:1]` | Fakta | "Jenjang: SD kelas V–VI (Fase C)… Alokasi waktu: 2 pertemuan × 40 menit." |
| `[src:2]` | Fakta | "Energi alternatif adalah energi yang berasal dari sumber daya alam yang **dapat diperbarui** dan **ramah lingkungan**. Contoh: **surya (matahari), angin, air, biogas**." |
| `[src:5]` | Fakta | "Lampu menyala: energi **listrik → cahaya + panas**." |
| `[src:6]` | Fakta | "Energi **tidak dapat diciptakan atau dimusnahkan**, hanya **diubah bentuknya**." |
| `[src:7]` | Fakta | "**Mematikan alat listrik yang tidak terpakai** (lampu, kipas, proyektor). **Menggunakan lampu hemat energi.**" |
| `[src:9]` | Fakta | "Menghemat energi, menanam pohon, dan menyebarkan informasi benar tentang lingkungan." |
| `[src:CP]` | Kurikulum | `CP-C.2.1.4` — "Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi alternatif dari sumber daya sekitar sebagai mitigasi perubahan iklim" |

Tag dihapus dari artefak sesuai FR-01; peta ini menjaga jejak penelusuran.

### §3.3 Tabel verifikasi (checklist §5)

| # | Uji | Hasil |
|---|---|---|
| 1 | `grep -c "\[src:"` pada HTML | `0` — LULUS |
| 2 | DOCX | N/A — tidak ada format `lesson_plan` pada run ini |
| 3 | PPTX lint | N/A — tidak ada `slide_outline` |
| 4 | `grep -i "cdn\|jsdelivr\|unpkg\|cdnjs"` | `0` — LULUS, seluruh CSS/JS inline |
| 5–6 | Tombol kuis | N/A — bukan kuis |
| 7 | PDF valid | 1 halaman, 420,0 × 594,0 mm, header `%PDF-1.4` — LULUS |
| 8 | Laporan cetak | N/A — bukan kuis |
| 9 | Konsistensi angka | "2 pertemuan × 40 menit" dan "Fase C (kelas V–VI)" konsisten dengan `[src:1]` — LULUS |
| 10 | Audit log + Source Resolution Map | Terisi — LULUS |

### §3.4 Pemeriksaan tambahan

| Uji | Hasil |
|---|---|
| `grep -ic "halal"` | `0` |
| `grep -ic "terbukti\|paling ampuh\|terbaik\|nomor satu"` | `0` |
| `grep -c "UNVERIFIED\|PERLU KONFIRMASI"` | `0` |
| Tombol cetak pada artefak | Tidak muncul (`?export=1`) |

## §4 Batas yang diakui

- PDF adalah raster 300 dpi, bukan vektor. Untuk cetak A2 hasilnya memadai; untuk pembesaran
  melebihi A2, render ulang dari HTML.
- Sumber menyatakan dirinya data ilustratif untuk keperluan lomba; poster mencantumkannya di kaki.
- Validasi akhir tetap milik guru/SME (R004).
