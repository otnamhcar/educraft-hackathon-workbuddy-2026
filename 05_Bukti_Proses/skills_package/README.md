# EduCraft Agent — Skill Package (Kategori C, Hackathon Tencent Cloud ID 2026)

Paket ini adalah **orkestrasi multi-agent** untuk Kategori C (*The Creator Agent*), dikemas sebagai Skill WorkBuddy siap-impor.

## Struktur
```
skills_package/
├── edu-orchestrator/        # Master: state, routing, loop max 3, HITL, audit
│   ├── SKILL.md
│   └── assets/
│       ├── rulebook_ipas.md
│       ├── cp_ipas.md
│       ├── konteks_aktual.md
│       ├── source_material_ipas.md
│       └── source_material_energi.md
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
| `konteks_aktual.md` | Klaim dunia nyata `[src:CA1]`, `[src:CA6]` + URL resmi & tanggal akses | run `-001` (R011) |

> **Catatan jujur:** run `EDU-ORCH-20261030-002` (Perubahan Wujud Zat) bertumpu pada
> anchor topik `[src:B4]` di `cp_ipas.md`, bukan pada lembar fakta tersendiri. Lembar
> fakta untuk topik itu belum ada di paket ini — lihat `Known limitations` di README repo.

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
