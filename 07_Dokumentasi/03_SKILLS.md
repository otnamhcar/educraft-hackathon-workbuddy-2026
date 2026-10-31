# 03 — Skill dan batas peran (kanonik)

> **Tujuan:** membuktikan bahwa tidak ada dua agen yang memiliki keputusan yang sama. Sebuah peran
> didefinisikan oleh tiga hal: apa yang wajib dihasilkannya, apa yang tidak boleh pernah dilakukannya,
> dan apa yang boleh dibacanya.

---

## 1. Peta peran

| Skill | Peran | Mandat satu kalimat | Membaca | Menulis |
|-------|-------|---------------------|---------|---------|
| `edu-orchestrator` | State machine | Memegang state, mengarahkan pekerjaan, menegakkan batas dan gerbang | run config, semua artefak | field status run config, audit log, laporan grounding |
| `edu-planner` | Pengurai | Mengubah satu topik menjadi kerangka per format yang dipetakan ke kode CP | sumber, CP | `00_plan.md` |
| `edu-writer` | Penyusun | Menghasilkan setiap artefak teks dan aset, ketat dari sumber | kerangka, sumber, temuan | draf, brief, aset ter-render |
| `edu-reviewer` | Gerbang | Mengembalikan `APPROVE`/`REJECT` dengan ID aturan dan teks kutipan | draf, rulebook, sumber | `05_review.md` |

Empat skill. Bukan lima, bukan enam. Label di audit log — `edu-infographic`, `edu-video`, `edu-quiz` —
adalah **fase di dalam `edu-writer`** (rendering aset), bukan agen terpisah; fase-fase itu tidak punya veto.

---

## 2. Bukti tidak ada tumpang tindih (RACI)

`R` = mengerjakan · `A` = bertanggung jawab atas keputusan · `C` = dikonsultasi · `I` = diberi tahu.
**Setiap baris punya tepat satu `R`.** Bila suatu saat ada dua, desainnya sudah melenceng.

| Artefak | Orchestrator | Planner | Writer | Reviewer | Manusia |
|---------|:---:|:---:|:---:|:---:|:---:|
| Konfigurasi run | **R** | I | I | I | A |
| Rencana konten / kerangka | I | **R** | I | C | A |
| Teks draf (semua format) | I | I | **R** | C | A |
| Brief aset (infografis, video) | I | I | **R** | C | A |
| Aset ter-render (PNG, HTML, PDF) | I | I | **R** | C | A |
| Laporan grounding | **R** | I | I | C | I |
| Vonis review | I | I | C | **R** | A |
| Audit log | **R** | I | I | I | I |
| Catatan persetujuan | I | I | I | I | **R** |

Dua pemisahan menopang seluruh desain:

- **Veto ≠ tulis ulang.** Reviewer memegang `R` atas vonis dan tidak atas apa pun selain itu. Writer
  memegang `R` atas isi dan tidak atas vonis. Agen yang bisa menilai sekaligus memperbaiki karyanya
  sendiri pada akhirnya akan menilai dirinya dengan longgar.
- **Merutekan ≠ memutuskan.** Orchestrator memutuskan *kapan* sebuah gerbang berjalan, tidak pernah
  *apa* vonisnya.

---

## 3. Skema kontrak

### 3.1 Keluaran Planner

```json
{
  "topic": "string",
  "phase": "Fase B | Fase C",
  "formats": ["lesson_plan", "quiz", "slide_outline", "short_article", "infographic_brief", "video_script"],
  "curriculum_refs": ["CP-B.1.1.4", "CP-C.2.2"],
  "outline": { "format_name": ["poin 1", "poin 2"] },
  "gaps": ["PERLU KONFIRMASI GURU: ..."]
}
```
`gaps` bersifat wajib. Larik kosong adalah klaim bahwa tidak ada yang kurang, dan klaim itu harus benar.

### 3.2 Keluaran Writer (per artefak)

```markdown
<!-- front-matter -->
format: short_article | lesson_plan | quiz | slide_outline | infographic_brief | video_script
word_count: 400
sources_used: [src:1, src:3, src:CA1]

<!-- body: setiap kalimat faktual membawa tag -->
```

Aturan tag: fakta → `[src:n]`; kurikulum → `[src:CP]`/`[src:B4]`; dunia nyata → `[src:CA n]`;
tidak diketahui → `[UNVERIFIED]` **plus** catatan `PERLU KONFIRMASI GURU`. Tag kurikulum tidak pernah
boleh menopang fakta.

### 3.3 Keluaran Reviewer

Lihat `01_ARSITEKTUR.md` §5.2. Batasan tambahan:

- `findings[]` tidak boleh kosong saat `status = REJECT`.
- Setiap temuan butuh `rule`, `quote`, `reason`, `suggestion`. Temuan tanpa kutipan tidak sah.
- Reviewer tidak boleh mengusulkan penulisan ulang penuh; `suggestion` adalah arahan, bukan prosa pengganti.

---

## 4. Daftar "tidak boleh pernah" (rambu yang sebenarnya)

| Peran | Tidak boleh pernah |
|-------|--------------------|
| Orchestrator | Menerbitkan; menulis atau menyunting isi; mengubah vonis; melewati 3 iterasi; menyunting rulebook atau sumber |
| Planner | Memasukkan fakta yang tidak ada di sumber; menulis prosa; menyetujui apa pun |
| Writer | Memakai fakta di luar sumber; menyetujui drafnya sendiri; menerbitkan; menyunting rulebook; membuang temuan tanpa menanganinya |
| Reviewer | Menulis ulang isi; menyetujui berdasarkan aturan yang tidak ada di rulebook; mengakhiri perulangan dengan melunakkan temuan |

---

## 5. Tumpang tindih yang ada hari ini (dan perbaikannya)

| Tumpang tindih | Mengapa bermasalah | Perbaikan | Status |
|----------------|--------------------|-----------|--------|
| Rulebook dikirim 2× (aset orchestrator + reviewer) | Dua salinan bisa melenceng; lalu "aturan mana yang berlaku?" tak terjawab | Simpan satu berkas kanonik, hasilkan salinan, verifikasi lewat checksum | Kanonik: `03_Hasil/referensi/rulebook_ipas.md`. Salinan identik byte hari ini (terverifikasi). Cek checksum sudah otomatis di `tools/doctor.py` |
| Daftar format berbeda antar dokumen | Kontrak menyebut 3 format; submission mengklaim 5 + kuis | Satu daftar hidup di `01_ARSITEKTUR.md` §3 dan skema Planner; kontrak diperbarui agar cocok | **DITUTUP 31 Okt** — keempat kontrak kini memakai enam format kanonik dengan aturan "subset apa pun, minimal dua" |
| "Run yang jadi acuan" ambigu | Dua run, status berbeda | Selalu sebut ID run; `02_WORKFLOW.md` §7 menetapkan tujuan tiap run | **DITUTUP 31 Okt** — `03_Accountability_Sheet.md` dan `04_Test_Results.md` kini menyebut run di setiap pernyataan |
| Arsitektur dijelaskan di 4 tempat | Melenceng | `01_ARSITEKTUR.md` kanonik; yang lain turunan dan tidak boleh menambah klaim | Tercatat di `00_INDEX.md` |
| Bahasa keluaran tidak diatur kontrak | Proyek berbahasa Indonesia, tetapi kontrak tidak pernah mewajibkannya, sehingga bahasa keluaran bergantung kebiasaan | Setiap kontrak memuat bagian **Bahasa**; Writer dan Reviewer menegakkannya | **DITUTUP 31 Okt** — keempat kontrak berbahasa Indonesia dan mewajibkan keluaran berbahasa Indonesia |

---

## 6. Tata letak instalasi

```
skills_package/
├── edu-orchestrator/
│   ├── SKILL.md
│   └── assets/   rulebook · cp_ipas · konteks_aktual · source_material_ipas · source_material_energi
├── edu-planner/
│   ├── SKILL.md
│   └── assets/   cp_ipas
├── edu-writer/
│   ├── SKILL.md
│   └── assets/   source_material_ipas · source_material_energi
└── edu-reviewer/
    ├── SKILL.md
    └── assets/   rulebook · cp_ipas · konteks_aktual · source_material_ipas · source_material_energi
```

Setiap skill mandiri: aset berupa **salinan**, tidak pernah rujukan antar-folder, sehingga satu skill
bisa dipasang sendiri. Biayanya duplikasi; kendalinya adalah cek checksum sebelum submission
(`tools/doctor.py`, cek 5).
