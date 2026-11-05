# 03_Hasil — apa yang ada di sini

Folder ini adalah **keluaran**: hasil run dan bukti auditnya. Dua hal yang bukan keluaran sudah
dipindah keluar — lapisan pengetahuan ke `08_Referensi/`, dokumen operasional ke
`06_Submission/panduan/`.

| Isi | Sifat | Boleh diubah? |
|-----|-------|---------------|
| `edu_output*/`, `materi_ajar/` | **Hasil run** — draf, vonis, audit log, artefak ter-render | Draf digantikan, bukan disunting. Audit log **append-only** |
| `audit/` | **Bukti audit `-001`** — log orchestration, dua laporan kepatuhan, adendum R012 | Tidak — arsip |
| `referensi/` | **Hanya penunjuk.** Berkasnya sudah pindah ke `08_Referensi/` | Hanya `README.md` di dalamnya |

## Empat run dan foldernya

| ID | Folder | Catatan |
|----|--------|---------|
| `EDU-ORCH-20261026-001` | `edu_output/` | **Tidak berakhiran angka.** Run pertama; satu-satunya yang punya empat artefak siap pakai |
| `EDU-ORCH-20261030-002` | `edu_output_wujud_zat/` | Fase B |
| `EDU-ORCH-20261105-003` | `edu_output_tata_surya/` | PENDING |
| `EDU-ORCH-20261104-004` | `edu_output_wujud_zat_faseC/` | Fase C. Sempat bernomor `-003` sebelum Tata Surya masuk |

Angka pada ID adalah **urutan**, bukan tanggal. Tanggalnya ada di delapan digit sebelumnya.

## Kenapa `audit/` masih di sini

`audit/audit_log_edu_orchestrator.md` adalah log run `-001` yang tinggal di luar folder run `-001`.
Idealnya ia berada di dalam `edu_output/`, dan dua laporan kepatuhan di sebelahnya adalah bukti yang
seharusnya ikut run tersebut.

Ia **tidak dipindah** karena log itu merujuk foldernya sendiri di baris 113
(`03_Hasil/audit/addendum_R012_2026-10-31.md`). Memindahkan foldernya akan memutus rujukan itu, dan
memperbaikinya berarti menyunting log **append-only** — memalsukan jejak. Antara struktur yang rapi
dan jejak yang utuh, jejak yang menang.

Dicatat sebagai **G20** di `07_Dokumentasi/07_GAP_DAN_REKOMENDASI.md`.
