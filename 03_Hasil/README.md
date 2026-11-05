# 03_Hasil — apa yang ada di sini

Folder ini memuat **tiga jenis isi yang berbeda**, dan hanya satu di antaranya yang boleh dihapus
atau ditimpa. Sebelum menyunting apa pun di sini, baca tabel ini.

| Isi | Sifat | Boleh diubah? |
|-----|-------|---------------|
| `edu_output*/`, `materi_ajar/` | **Hasil run** — draf, vonis, audit log, artefak ter-render | Draf digantikan, bukan disunting. Audit log **append-only** |
| `audit/` | **Laporan audit lintas-run** (kepatuhan R001–R011, adendum R012) | Tidak — arsip |
| `referensi/` | **Lapisan pengetahuan read-only** — rulebook, CP, konteks aktual, source material | **Tidak pernah.** Agen tidak boleh menulis ke sini; kalau nilai di sini salah, yang diperbaiki adalah sumbernya, bukan hasilnya |
| `panduan/` | Runbook demo dan panduan operasional | Ya, dokumen hidup |

## Empat run dan foldernya

| ID | Folder | Catatan |
|----|--------|---------|
| `EDU-ORCH-20261026-001` | `edu_output/` | **Tidak berakhiran angka.** Ini run pertama dan satu-satunya yang punya empat artefak siap pakai |
| `EDU-ORCH-20261030-002` | `edu_output_wujud_zat/` | Fase B |
| `EDU-ORCH-20261105-003` | `edu_output_tata_surya/` | PENDING |
| `EDU-ORCH-20261104-004` | `edu_output_wujud_zat_faseC/` | Fase C. Sempat bernomor `-003` sebelum Tata Surya masuk |

Angka pada ID adalah **urutan**, bukan tanggal. Tanggalnya ada di delapan digit sebelumnya.

## Kenapa `referensi/` ada di sini — dan kenapa itu akan dipindah

Secara arsitektur, lapisan pengetahuan seharusnya **tidak** berada di dalam folder hasil: batas
kepercayaan B1 menyatakan agen tidak boleh menulis ke sana, dan folder bernama "hasil" adalah tempat
orang menghapus. Penempatan ini warisan dari saat proyek baru punya satu folder.

Memindahkannya sekarang akan memutus path di 25 berkas dan meninggalkan enam artefak append-only
dengan rujukan yang tidak lagi resolve. Karena itu pemindahan ditunda sampai setelah submission, dan
dicatat sebagai **G19** di `07_Dokumentasi/07_GAP_DAN_REKOMENDASI.md`.

Sampai saat itu: **perlakukan `referensi/` sebagai read-only**, meskipun ia berada di folder ini.
