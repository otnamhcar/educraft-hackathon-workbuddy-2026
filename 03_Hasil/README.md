# 03_Hasil — apa yang ada di sini

Folder ini adalah **keluaran**: hasil run dan bukti auditnya. Dua hal yang bukan keluaran sudah
dipindah keluar — lapisan pengetahuan ke `08_Referensi/`, dokumen operasional ke
`06_Submission/panduan/`.

| Isi | Sifat | Boleh diubah? |
|-----|-------|---------------|
| `edu_output*/`, `materi_ajar/` | **Hasil run** — draf, vonis, audit log, artefak ter-render | Draf digantikan, bukan disunting. Audit log **append-only** |
| `audit/` | **Bukti audit `-001`** — log orchestration, dua laporan kepatuhan, adendum R012 | Tidak — arsip |
| `referensi/` | **Hanya penunjuk.** Berkasnya sudah pindah ke `08_Referensi/` | Hanya `README.md` di dalamnya |

## Lima run dan foldernya

| ID | Folder | Catatan |
|----|--------|---------|
| `EDU-ORCH-20261026-001` | `edu_output/` | **Tidak berakhiran angka.** Run pertama; satu-satunya yang punya empat artefak siap pakai |
| `EDU-ORCH-20261030-002` | `edu_output_wujud_zat/` | Fase B |
| `EDU-ORCH-20261105-003` | `edu_output_tata_surya/` | PENDING |
| `EDU-ORCH-20261104-004` | `edu_output_wujud_zat_faseC/` | Fase C. Sempat bernomor `-003` sebelum Tata Surya masuk |
| `EDU-ORCH-20261106-005` | `edu_output_energi_alternatif/` | Fase C, bab C4. **Satu-satunya run yang memakai konteks aktual** (CA1, CA6). 3 × REJECT → dieskalasi ke guru, belum disetujui. **Satu-satunya run yang punya artefak render tanpa approval** |

Angka pada ID adalah **urutan**, bukan tanggal. Tanggalnya ada di delapan digit sebelumnya.

## Tiga hal yang hanya terjadi di run `-005`

**1. Konteks aktual dipakai.** Run lain menyatakan R011 `N/A` karena tidak ada entri yang relevan.
Pada topik energi, `[src:CA1]` (PLTS Terapung Cirata) dan `[src:CA6]` (FOLU Net Sink 2030, NZE 2060)
relevan langsung, sehingga tautan tidak dipaksakan tetapi juga tidak dihindari.

**2. Cacat `check_grounding.py` ditemukan dan ditutup.** Dua lembar sumber memakai penomoran tag yang
sama (`source_material_ipas.md` dan `source_material_energi.md`), dan alat lama menyelesaikan bentrokan
itu diam-diam lewat urutan abjad. Laporan pertama run ini menyatakan PASS 237 tag padahal menunjuk
lembar yang salah. Anchor kini disimpan per berkas, bentrokan dinyatakan `AMBIG` (gagal), dan
`--primary-source` menetapkan lembar yang berlaku per run. Rincian di `edu_output_energi_alternatif/04_review.md` §D.

**3. Fase render dijalankan tanpa approval.** Ini satu-satunya run yang menghasilkan `.docx`, `.pptx`,
dan `.html` padahal `Human approver` masih `PENDING`. Pemicunya instruksi peminta, bukan persetujuan
approver — dua peran berbeda, dan spesifikasi tidak membolehkan menukarnya. Konsekuensinya dinyatakan
di tiga tempat: label "draf pra-persetujuan" pada setiap artefak, `00_run_config.md` baris
*Format Rendering*, dan `audit_log.md` §9.0. Publikasi tetap `LOCKED`.

Run ini juga mencatat satu penyimpangan yang **tidak** ditutup: FR-09 menuntut `.docx`/`.pptx`/`.html`
diturunkan dari `Materi_Guru_*.md`, sedangkan ketiganya diturunkan langsung dari draf bertag sehingga
ada tiga resolver terpisah. Hasilnya konsisten (diverifikasi), konstruksinya belum. `audit_log.md` §9.5.

## Kenapa `audit/` masih di sini

`audit/audit_log_edu_orchestrator.md` adalah log run `-001` yang tinggal di luar folder run `-001`.
Idealnya ia berada di dalam `edu_output/`, dan dua laporan kepatuhan di sebelahnya adalah bukti yang
seharusnya ikut run tersebut.

Ia **tidak dipindah** karena log itu merujuk foldernya sendiri di baris 113
(`03_Hasil/audit/addendum_R012_2026-10-31.md`). Memindahkan foldernya akan memutus rujukan itu, dan
memperbaikinya berarti menyunting log **append-only** — memalsukan jejak. Antara struktur yang rapi
dan jejak yang utuh, jejak yang menang.

Dicatat sebagai **G20** di `07_Dokumentasi/07_GAP_DAN_REKOMENDASI.md`.
