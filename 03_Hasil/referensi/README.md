# Folder ini sudah dipindah

Lapisan pengetahuan **tidak lagi berada di sini**. Sejak 5 November 2026 ia ada di:

```
08_Referensi/
```

Alasannya: `03_Hasil/` adalah folder hasil, tempat berkas dihapus dan ditimpa. Lapisan pengetahuan
bersifat read-only dan tidak boleh ditulis oleh langkah agen mana pun (batas kepercayaan **B1**).
Menyimpannya di dalam folder hasil membuat batas itu hanya berlaku sebagai konvensi, bukan struktur.

## Kalau Anda sampai di sini dari tautan lama

Beberapa artefak **append-only** — audit log, `grounding_report.md`, `00_run_config.md` — masih menulis
`03_Hasil/referensi/...` karena memang begitulah lokasinya saat artefak itu ditulis. Artefak itu tidak
disunting, sesuai aturan proyek. Peta berkasnya:

| Dulu | Sekarang |
|------|----------|
| `03_Hasil/referensi/rulebook_ipas.md` | `08_Referensi/rulebook_ipas.md` |
| `03_Hasil/referensi/cp_ipas.md` | `08_Referensi/cp_ipas.md` |
| `03_Hasil/referensi/konteks_aktual.md` | `08_Referensi/konteks_aktual.md` |
| `03_Hasil/referensi/source_material_energi.md` | `08_Referensi/source_material_energi.md` |
| `03_Hasil/referensi/source_material_ipas.md` | `08_Referensi/source_material_ipas.md` |
| `03_Hasil/referensi/source_material_tata_surya.md` | `08_Referensi/source_material_tata_surya.md` |
| `03_Hasil/referensi/source_material_wujud_zat.md` | `08_Referensi/source_material_wujud_zat.md` |

Perintah yang dulu memakai `--knowledge 03_Hasil/referensi` kini memakai `--knowledge 08_Referensi`.
`tools/doctor.py` sudah menunjuk lokasi baru dan memverifikasi checksum ketiga salinan seperti biasa.

Dicatat sebagai **G19** di `07_Dokumentasi/07_GAP_DAN_REKOMENDASI.md`.
