# Audit Log — EDU-ORCH-20261106-009 (versi bersih)

## §1 Pipeline

| Waktu | Fase | Masukan | Keputusan |
|---|---|---|---|
| 17:24 | Intake | "Versi bersih: tanpa merek, tanpa klaim khasiat, tanpa kata halal, cukup fakta dari source" | Turunan `-008`; format tetap `infographic_brief` |
| 17:25 | Draft | Draf `-008` yang disetujui | `01_poster_bersih_draf.md` — blok merek + lencana CP dihapus, pita `[src:8]` ditambahkan |
| 17:26 | Review | Draf + rulebook + sumber | **`APPROVE`** — 0 blocking, 5 minor. `Iteration` tetap 0 |
| 17:26 | Revisi minor | M1–M4 | Judul pita ber-tag, CTA tanpa "sakelar/hari ini", glosa istilah Inggris |
| 17:27 | Format Rendering | Gate terpenuhi | HTML, PNG 300 dpi, PDF A2 |

## §2 Format Rendering

### §2.1 Artefak

| Artefak | Berkas | Alat |
|---|---|---|
| HTML interaktif/cetak | `03_poster_bersih.html` | CSS cetak A2, tanpa dependensi luar |
| Raster 300 dpi | `poster_bersih_A2.png` (4959 × 7016 px) | Chrome headless, `?export=1` |
| PDF cetak | `poster_bersih_A2.pdf` (420,0 × 594,0 mm, 1 halaman) | PyMuPDF dari raster 300 dpi |

### §2.2 Source Resolution Map (FR-02)

| Tag | Kelas | Kutipan sumber yang mendasari |
|---|---|---|
| `[src:2]` | Fakta | "Energi alternatif adalah energi yang berasal dari sumber daya alam yang **dapat diperbarui** dan **ramah lingkungan**. Contoh: **surya (matahari), angin, air, biogas**." |
| `[src:5]` | Fakta | "Lampu menyala: energi **listrik → cahaya + panas**." |
| `[src:6]` | Fakta | "Energi **tidak dapat diciptakan atau dimusnahkan**, hanya **diubah bentuknya**." |
| `[src:7]` | Fakta | "**Mematikan alat listrik yang tidak terpakai** (lampu, kipas, proyektor). **Menggunakan lampu hemat energi.**" |
| `[src:8]` | Fakta | "Sumber daya alam (**air, tanah, hutan, udara**) harus dijaga agar tersedia bagi generasi mendatang. Upaya: **reduce/reuse/recycle, menanam pohon, menghemat energi, transportasi ramah lingkungan**." |
| `[src:9]` | Fakta | "Menghemat energi, menanam pohon, dan menyebarkan informasi benar tentang lingkungan." |

### §2.3 Tabel verifikasi (checklist §5)

| # | Uji | Hasil |
|---|---|---|
| 1 | `grep -c "\[src:"` pada HTML | `0` — LULUS |
| 2 | DOCX | N/A — tidak ada `lesson_plan` |
| 3 | PPTX lint | N/A — tidak ada `slide_outline` |
| 4 | `grep -i "cdn\|jsdelivr\|unpkg\|cdnjs"` | `0` — LULUS |
| 5–6 | Tombol kuis | N/A — bukan kuis |
| 7 | PDF valid | 1 halaman, 420,0 × 594,0 mm — LULUS |
| 8 | Laporan cetak | N/A — bukan kuis |
| 9 | Konsistensi angka | Tidak ada angka selain label kelas; "Fase C" konsisten |
| 10 | Audit log + Source Resolution Map | Terisi — LULUS |

### §2.4 Pemeriksaan tambahan

| Uji | Hasil |
|---|---|
| `grep -ic "educraft"` | `0` |
| `grep -ic "halal"` | `0` |
| `grep -ic "terbukti\|paling ampuh\|terbaik\|nomor satu\|khasiat"` | `0` |
| `grep -c "UNVERIFIED\|PERLU KONFIRMASI"` | `0` |
| Tombol cetak pada artefak | Tidak muncul (`?export=1`) |

## §3 Catatan desain

- Lencana "SESUAI CP-C.2.1.4" dihapus; tanpa blok merek, lencana itu kehilangan konteks dan
  terbaca sebagai tanda sertifikasi produk.
- Pita `[src:8]` menggantikan blok merek pada posisi yang sama sehingga komposisi tetap berjangkar.
- Enam butir upaya disusun sebagai kisi 3 × 2 karena percobaan satu baris menghasilkan 5 + 1 yang
  tidak seimbang.

## §4 Batas

- PDF adalah raster 300 dpi, bukan vektor.
- Sumber menyatakan dirinya data ilustratif untuk keperluan lomba.
- Validasi akhir milik guru/SME (R004).
