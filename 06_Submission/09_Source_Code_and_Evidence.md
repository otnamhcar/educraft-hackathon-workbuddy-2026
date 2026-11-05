# Item Submission 9 — Kode Sumber & Bukti Penggunaan

> Handbook §7 (WAJIB): *"A public code repository, or your exported WorkBuddy workflow with
> evidence of use."*

**Status: SELESAI — terbit di https://github.com/otnamhcar/educraft-hackathon-workbuddy-2026**
(publik, MIT, 31 Oktober 2026).

---

## 1. Kode ini sebenarnya apa

EduCraft bukan aplikasi web. Ia adalah **sekumpulan kontrak agen plus satu lapisan pengetahuan**, dan
itulah artefak yang tepat untuk challenge ini: juri bisa membaca setiap aturan yang ditaati agen.

```
05_Bukti_Proses/
├── skills_package/
│   ├── README.md
│   ├── edu-orchestrator/
│   │   ├── SKILL.md                     # mesin status, batas, gerbang approval, eskalasi
│   │   └── assets/
│   │       ├── rulebook_ipas.md         # R001–R012
│   │       ├── cp_ipas.md
│   │       ├── konteks_aktual.md
│   │       ├── source_material_ipas.md
│   │       ├── source_material_energi.md
│   │       ├── source_material_wujud_zat.md
│   │       ├── source_material_tata_surya.md
│   │       └── intake_menu_ipas.md      # katalog 20 bab, status sumber
│   ├── edu-planner/
│   │   ├── SKILL.md                     # kontrak pemecahan
│   │   └── assets/cp_ipas.md
│   ├── edu-writer/
│   │   ├── SKILL.md                     # kontrak penulisan draf, disiplin tag
│   │   └── assets/
│   │       ├── source_material_ipas.md
│   │       ├── source_material_energi.md
│   │       ├── source_material_wujud_zat.md
│   │       └── source_material_tata_surya.md
│   └── edu-reviewer/
│       ├── SKILL.md                     # kontrak vonis, wajib menyebut aturan + mengutip teks
│       └── assets/
│           ├── rulebook_ipas.md
│           ├── cp_ipas.md
│           ├── konteks_aktual.md
│           ├── source_material_ipas.md
│           ├── source_material_energi.md
│           ├── source_material_wujud_zat.md
│           └── source_material_tata_surya.md
└── evidence_bundle/                     # jejak run, slot screenshot, salinan audit
```

Repo publik mencerminkan bundel ini, dengan `README.md` sebagai halaman depan:
https://github.com/otnamhcar/educraft-hackathon-workbuddy-2026

**Catatan soal berkas yang terduplikasi:** rulebook dan source material ikut dikirim di dalam
`edu-orchestrator/assets/`, `edu-writer/assets/`, dan `edu-reviewer/assets/` supaya tiap skill mandiri
saat dipasang. Semua salinan identik byte (diverifikasi dengan checksum oleh `tools/doctor.py` —
11 passed / 0 failed); bila suatu saat berbeda, salinan milik Reviewer yang berlaku.

## 2. Bukti penggunaan (jejak run)

Juri bisa merekonstruksi seluruh run `EDU-ORCH-20261026-001` dari berkas-berkas ini, dalam urutan ini:

| Langkah | Berkas | Yang dibuktikan |
|---------|--------|-----------------|
| 1 | `03_Hasil/edu_output/00_run_config.md` | Topik, kode CP, sumber, penyetuju, status publikasi |
| 2 | `03_Hasil/audit/audit_log_edu_orchestrator.md` | Langkah Planner → Writer → Reviewer, riwayat revisi |
| 3 | `03_Hasil/audit/review_kepatuhan_R001-R011_2026-10-29.md` | **REJECT** (R001, R011, R004) |
| 4 | `08_Referensi/source_material_energi.md` | Sumber yang dibuat sebagai jawaban atas penolakan itu |
| 5 | `08_Referensi/konteks_aktual.md` | CA1/CA6 dengan URL resmi dan tanggal akses |
| 6 | `03_Hasil/materi_ajar/` | Kelima draf yang diperbaiki + kuis HTML interaktif |
| 7 | `03_Hasil/audit/review_kepatuhan_R001-R011_2026-10-30_REVISI.md` | **APPROVE** setelah remediasi |

Urutan itu — tolak, diagnosis, perbaiki, review ulang — adalah bukti penggunaannya. Screenshot statis
dari jalur yang mulus justru membuktikan lebih sedikit.

## 3. Cara mereproduksi

Dua perintah, lalu satu pemeriksaan kesehatan. Semua skrip Python, jadi Linux, macOS, dan Windows
menjalankan kode yang sama — hanya nama interpreter-nya berbeda (`python3` di Linux/macOS, `python`
atau `py` di Windows):

```bash
python3 tools/install_skills.py   # 4 skill ke ~/.workbuddy-ai/skills, jumlah diverifikasi
# restart WorkBuddy, lalu:
python3 tools/doctor.py           # 8 passed / 0 failed / 0 warning pada clone yang sehat
```

Lalu panggil orchestrator dengan: topik, fase (Fase C), kode CP, dan berkas sumber yang sudah ada di
`assets/` tiap skill. Harapkan
`Plan → Draft → Review → (REJECT → remediasi ≤3) → APPROVE → BERHENTI di gerbang approval`, berakhir di
`publish_status: PENDING`. Kalau ia menerbitkan sendiri, pemasangannya salah.

Folder `assets/` sudah terisi di dalam clone, jadi "salin lapisan pengetahuan" bukan langkah tersendiri.
Tanpa build, tanpa dependensi, tanpa API key miliknya sendiri. Panduan lengkap, dengan tabel perintah
per-OS: README → "Run it yourself".

## 4. Yang masih kurang (tindakan wajib sebelum submit)

| Celah | Kenapa penting | Status |
|-------|----------------|--------|
| **Repo publik** | Handbook menerima repo publik *atau* workflow yang diekspor beserta buktinya. | ✅ **SELESAI** — https://github.com/otnamhcar/educraft-hackathon-workbuddy-2026 (publik, MIT). Opsi (a) dipilih. |
| **Screenshot** | Diwajibkan §7 untuk hasil pengujian | ⏳ Ambil sesuai `04_Test_Results.md` §3; simpan di `05_Bukti_Proses/evidence_bundle/03_screenshots/` |
| **Video demo** | Wajib, 5–8 menit | ⏳ Skripnya siap: `07_Demo_Video_Script.md` |
| **Persetujuan manusia** | Gerbang etik, bukan formalitas | ✅ Run `-001` disetujui 4 Nov 2026 14:49 dan `-002` 30 Okt 2026 17:19; run `-003` dan `-004` masih PENDING |

## 5. Catatan lisensi dan data

- **Kode/kontrak:** **MIT** — `LICENSE` di akar repo; cakupannya dijelaskan di README §
  "Licence and data".
- **Source material — tiga dasar berbeda, dinyatakan terpisah:**
  - Run `-001` (`source_material_energi.md`) adalah dokumen **mock/ilustratif** yang ditulis untuk
    hackathon ini. Handbook §10 mengizinkan data mock (*"Mock data is acceptable"*). Pengecualiannya
    klaim dunia nyata, yang mengutip URL resmi di `konteks_aktual.md`.
  - Run `-002` (`source_material_wujud_zat.md`) **dikutip dari Panduan IPAS resmi, hlm. 26–27**, dengan
    rujukan baris. Sembilan entri adalah kutipan; dua (`[src:W10]`, `[src:W11]`) turunan tim dan
    ditandai demikian.
  - Run `-003` (`source_material_tata_surya.md`) **dikutip dari Panduan IPAS resmi, hlm. 45–47**, dengan
    rujukan baris. Sembilan entri (`[src:TS1]`–`[src:TS9]`) adalah kutipan; dua (`[src:TS10]`,
    `[src:TS11]`) turunan tim (daftar nama planet, definisi rotasi/revolusi) dan ditandai demikian.
- **Data siswa:** tabel skor memakai ID peserta yang sudah dianonimkan. Tidak ada data siswa nyata.
- **Dokumen kurikulum pihak ketiga IKUT diedarkan ulang**, tanpa perubahan dan dengan atribusi, di
  `02_Sumber/`: *Panduan Mata Pelajaran IPAS* resmi (Revisi 4) dan *Permendikdasmen No. 13/2025*, plus
  hasil ekstraksi teksnya. Keduanya di luar lisensi MIT dan dikecualikan di `THIRD_PARTY_NOTICES.md`.
  Intinya verifikasi: pembaca bisa menelusuri tag `[src:W#]` mana pun kembali ke halaman PDF aslinya
  alih-alih mempercayai ringkasan kami. Materi pihak ketiga yang **bukan** hak kami untuk menerbitkan —
  enam lembar RPP `centralpendidikan.com` dan handbook panitia — dikecualikan; `02_Sumber/README.md`
  mencantumkan setiap pengecualian beserta alasannya.
