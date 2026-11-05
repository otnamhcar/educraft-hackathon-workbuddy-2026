# 03_Hasil — apa yang ada di sini

Folder ini adalah **keluaran**: hasil run dan bukti auditnya. Lapisan pengetahuan tidak lagi di sini —
sejak 5 November 2026 ia berada di `08_Referensi/` (lihat `03_Hasil/referensi/README.md`).

| Isi | Sifat | Boleh diubah? |
|-----|-------|---------------|
| `edu_output*/`, `materi_ajar/` | **Hasil run** — draf, vonis, audit log, artefak ter-render | Draf digantikan, bukan disunting. Audit log **append-only** |
| `audit/` | **Bukti audit lintas-run** — log orchestration `-001`, laporan kepatuhan R001–R011 | Tidak — arsip |
| `panduan/` | Runbook demo dan panduan operasional | Ya, dokumen hidup |

`sumber fakta, rulebook, CP, konteks aktual` → **`08_Referensi/`**. Jangan menulis ke sana.

## Empat run dan foldernya

| ID | Folder | Catatan |
|----|--------|---------|
| `EDU-ORCH-20261026-001` | `edu_output/` | **Tidak berakhiran angka.** Run pertama; satu-satunya yang punya empat artefak siap pakai |
| `EDU-ORCH-20261030-002` | `edu_output_wujud_zat/` | Fase B |
| `EDU-ORCH-20261105-003` | `edu_output_tata_surya/` | PENDING |
| `EDU-ORCH-20261104-004` | `edu_output_wujud_zat_faseC/` | Fase C. Sempat bernomor `-003` sebelum Tata Surya masuk |

Angka pada ID adalah **urutan**, bukan tanggal. Tanggalnya ada di delapan digit sebelumnya.

## Sisa percampuran yang diketahui

Dua hal di sini belum murni hasil run:

- `panduan/` berisi dokumen operasional, bukan keluaran agen. Secara semantik ia milik
  `07_Dokumentasi/`, tetapi dipakai langsung saat demo — memindahkannya sekarang berarti menyunting
  11 rujukan tepat sebelum perekaman video.
- `audit/` berisi bukti audit `-001`, tetapi disimpan di luar folder run yang bersangkutan. Idealnya
  ia berada di dalam `edu_output/` atau di `05_Bukti_Proses/`.

Keduanya dicatat sebagai **G20** di `07_Dokumentasi/07_GAP_DAN_REKOMENDASI.md`, ditunda sampai
setelah submission dengan alasan yang sama seperti G19: memperbaiki struktur tidak boleh memutus
tautan bukti yang sedang dipakai.
