# EduCraft Agent — Skill Package (Kategori C, Hackathon Tencent Cloud ID 2026)

Paket ini adalah **orkestrasi multi-agent** untuk Kategori C (*The Creator Agent*), dikemas sebagai Skill WorkBuddy siap-impor.

## Struktur
```
skills_package/
├── edu-orchestrator/        # Master: intake menu, state, routing, loop max 3, HITL, audit, Format Rendering
│   ├── SKILL.md
│   └── assets/
│       ├── rulebook_ipas.md
│       ├── cp_ipas.md
│       ├── konteks_aktual.md
│       ├── format_rendering_spec.md
│       ├── intake_menu_ipas.md
│       ├── source_material_ipas.md
│       ├── source_material_energi.md
│       └── source_material_wujud_zat.md
├── edu-planner/             # Planner: dekomposisi topik → outline
│   ├── SKILL.md
│   └── assets/cp_ipas.md
├── edu-writer/              # Writer: draft per format, grounding [src:#]
│   ├── SKILL.md
│   └── assets/
│       ├── source_material_ipas.md
│       └── source_material_energi.md
└── edu-reviewer/            # Reviewer: evaluasi vs rulebook, cite rule
    ├── SKILL.md
    └── assets/
        ├── rulebook_ipas.md
        ├── cp_ipas.md
        ├── konteks_aktual.md
        ├── source_material_ipas.md
        └── source_material_energi.md
```

## Knowledge assets — mana dipakai run mana

Setiap skill bersifat self-contained: asset disalin ke `assets/` masing-masing skill,
bukan dirujuk lintas folder. Dua set sumber ada karena proyek memakai dua topik berbeda.

| File | Isi | Dipakai run |
|------|-----|-------------|
| `rulebook_ipas.md` | R001–R012 (identik di orchestrator & reviewer) | semua run |
| `cp_ipas.md` | Capaian Pembelajaran IPAS Fase B & C | semua run (R004) |
| `source_material_ipas.md` | Fakta topik **karhutla Kalimantan** `[src:1]`–`[src:8]` | run pra-remediasi 29 Okt |
| `source_material_energi.md` | Fakta topik **energi alternatif** `[src:1]`–`[src:9]` | run `EDU-ORCH-20261026-001` |
| `source_material_wujud_zat.md` | Fakta topik **perubahan wujud zat** `[src:W1]`–`[src:W11]` | run `EDU-ORCH-20261030-002` |
| `konteks_aktual.md` | Klaim dunia nyata `[src:CA1]`, `[src:CA6]` + URL resmi & tanggal akses | run `-001` (R011) |
| `format_rendering_spec.md` | Spesifikasi Stage 6: peta deliverable, aturan FR-01…FR-08, checklist verifikasi | semua run yang menghasilkan artefak siap pakai |
| `intake_menu_ipas.md` | Spesifikasi S0 Intake: katalog 20 bab (11 Fase B + 9 Fase C), status sumber per bab, penahapan menu L1–L3 | semua run, saat perintah awal belum menyebut topik |

> **Catatan jujur:** lembar fakta tersedia untuk **empat** bab saja — B3 (karhutla, data mock),
> B4 (wujud zat), B5 (energi), dan C4 (penghematan energi). Tujuh belas bab lain belum punya
> lembar fakta, sehingga berstatus `PERLU SUMBER` pada `intake_menu_ipas.md` dan tidak dapat
> diproduksi sampai guru memasok dokumen. Ini batas yang disengaja: mengarang fakta dilarang R001.

## Stage 0 — Intake (menu bab)

Guru sering datang dengan niat, bukan dengan nomor bab: "bantu saya", "tolong buatkan materi".
Sebelum apa pun ditulis, orchestrator menayangkan **menu pilihan bab** dari
`edu-orchestrator/assets/intake_menu_ipas.md`.

Menu ditayangkan bertahap karena mekanisme pertanyaan pilihan hanya menerima **4 opsi per
pertanyaan**: L1 fase (B/C) → L2 rumpun (Makhluk hidup · Zat & energi · Bumi & antariksa ·
Sosial & ekonomi) → L3 bab (maksimal 3 per rumpun). Tidak ada rumpun yang melebihi 4 bab, sehingga
batas opsi tidak pernah dilanggar.

Setiap bab membawa **status sumber**: `SIAP` (B3, B4, B5, C4) atau `PERLU SUMBER` (17 bab lain).
Bab berstatus `PERLU SUMBER` menghentikan run sampai guru memasok dokumen — mengarang bab atau fakta
dilarang R001. Bila perintah awal sudah menyebut topik, menu **tidak** ditayangkan.

## Stage 6 — Format Rendering (pasca-approval)

Setelah Reviewer APPROVE dan manusia menyetujui, orchestrator menjalankan fase **Format
Rendering** untuk mengubah draf Markdown menjadi artefak siap pakai. Spesifikasi lengkap ada di
`edu-orchestrator/assets/format_rendering_spec.md`.

| Format kanonik | Artefak | Alat |
|---|---|---|
| `lesson_plan` | `.docx` | `workbuddy-docx` (html-to-doc) |
| `slide_outline` | `.pptx` | `workbuddy-pptx` (`slidep`) |
| `quiz` | `.html` interaktif mandiri | enhancement inline |

**Aturan inti yang ditegakkan:**

- **FR-01** Artefak guru/siswa tidak memuat tag internal (`[src:#]`, `[UNVERIFIED]`, dll).
- **FR-02** Penghapusan tag wajib disertai **Source Resolution Map** di audit log.
- **FR-03** Tanpa dependensi CDN untuk fungsi inti — artefak harus berfungsi offline.
- **FR-04** Angka dan satuan identik lintas artefak (mis. `145 MWac (192 MWp)`).
- **FR-05** Kontrak kuis: keadaan awal hanya **Periksa Jawaban**; setelah diperiksa muncul
  **Ulangi Kuis**, **Export PDF**, **Cetak / Save PDF**. Ekspor & cetak memuat soal, jawaban
  siswa, dan kunci — dengan highlight hijau (benar), merah (salah), abu-abu (kosong).
- **FR-06** Catatan internal (mis. kepatuhan reviewer) tidak tampil di artefak.
- **FR-07** Satuan mengikuti sumber; dilarang menormalkan tanpa dasar.
- **FR-08** Checklist verifikasi wajib lulus sebelum serah terima.

Referensi implementasi lengkap: run `EDU-ORCH-20261026-001` (lihat `audit_log.md` §3.7).

## Cara Impor ke WorkBuddy

### Opsi A — Impor folder lokal
1. Buka WorkBuddy.
2. Jalankan perintah impor skill (mis. `/skills import <path-folder>`), atau salin folder skill ke direktori skill WorkBuddy:
   - Global: `~/.workbuddy/skills/<nama-skill>/SKILL.md`
   - Workspace: `{workspace}/.workbuddy/skills/<nama-skill>/SKILL.md`
3. Pastikan tiap folder berisi `SKILL.md` (WorkBuddy memindai file ini).
4. Verifikasi lewat `/skills` (daftar skill terpasang).

### Opsi B — Impor via repo GitHub (paling aman untuk "source code" lomba)
1. Push folder ini ke repo publik (tiap sub-folder = 1 skill, atau 1 repo berisi semua).
2. Di WorkBuddy: tempel URL repo + instruksi "install skill ini, pastikan ada SKILL.md".
3. WorkBuddy clone → deteksi `SKILL.md` → pasang.
4. Repo publik ini sekaligus **memenuhi syarat submission "public code repository"**.

### Opsi C — Zip
- Ekstrak zip ke direktori skill WorkBuddy, lalu restart/refresh.

> **Catatan penting:** jalur `.workbuddy` vs `.workbuddy-ai` dapat berbeda antar-versi aplikasi. Verifikasi direktori skill aktual di mesin kalian (menu Settings/ Skills) sebelum menyalin manual.

## Memenuhi Syarat "Exported Workflow + Evidence"
1. **Paket skill** (folder/zip/repo) = artefak workflow.
2. **Screenshot/bukti eksekusi**: ambil dari panel *Results / View Results* saat pipeline berjalan (Planner→Writer→Reviewer, reject→remediate→approve).
3. Simpan **audit log** (transcript inter-agent + revision history) sebagai lampiran.

## Dua Pola Integrasi
- **Pola A (disarankan untuk lomba):** `edu-orchestrator` memanggil 3 sub-skill peran secara berurutan. Memenuhi syarat "≥3 agents with distinct roles".
- **Pola B (fallback):** bila pemanggilan antar-skill tidak didukung, jalankan `edu-orchestrator` sebagai satu skill yang mengeksekusi fase Planner/Writer/Reviewer secara inline, dengan state & log eksplisit.

## Disclaimer
`source_material_ipas.md` bersifat **mock/ilustratif** untuk lomba. Ganti dengan data resmi (KLHK/BMKG/BPS/Kemenkes) bila diinginkan, tetap dengan tag `[src:#]`.
