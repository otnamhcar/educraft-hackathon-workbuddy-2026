# Evidence Bundle — Submission "Exported Workflow + Evidence of Use"
### Tencent Cloud Hackathon Indonesia 2026 · Kategori C

> **Tujuan:** mengemas bukti dari WorkBuddy menjadi satu bundel yang memenuhi syarat handbook:
> *"Source code: A public code repository, **or your exported WorkBuddy workflow with evidence of use**."*

---

## Realita di WorkBuddy
Tidak ada tombol tunggal "Export Workflow". Bukti dirakit dari **4 komponen**. Jika versi WorkBuddy kalian punya menu *Export/Share* pada task, pakai itu sebagai bonus — tetapi 4 komponen ini tetap wajib.

---

## Struktur Bundel (yang harus diisi)
```
evidence_bundle/
├── 01_workflow/       # Skill/workflow artifact (folder skill -> zip)
├── 02_results/        # File hasil (lesson plan, quiz, slide outline) dari Results panel
├── 03_screenshots/    # Screenshot eksekusi pipeline (timestamp terlihat)
├── 04_audit_log/      # Transcript inter-agent + revision history
└── README.md          # Index bukti (file ini)
```

---

## Cara Mengisi Tiap Komponen

### 01_workflow — Artefak Workflow
1. Cari folder skill WorkBuddy:
   - Global: `~/.workbuddy/skills/<nama-skill>/`
   - Workspace: `{workspace}/.workbuddy/skills/<nama-skill>/`
2. Salin seluruh folder skill (`edu-orchestrator`, `edu-planner`, `edu-writer`, `edu-reviewer`) ke `01_workflow/`.
3. Pastikan tiap folder punya `SKILL.md`.
4. Alternatif: push ke repo publik → cantumkan URL di index (memenuhi opsi "public code repository").

### 02_results — Bukti Hasil
1. Buka panel **Results / View Results** di WorkBuddy.
2. Unduh artifact yang dihasilkan (lesson plan, quiz, slide outline, caption).
3. Simpan ke `02_results/` dengan nama jelas (mis. `lesson_plan_v1.md`, `quiz_final.md`).

### 03_screenshots — Bukti Eksekusi
Ambil screenshot yang **menampilkan timestamp & nama task**, minimal:
- [ ] Planner menghasilkan outline
- [ ] Writer menghasilkan draft (dengan tag `[src:#]`)
- [ ] Reviewer **REJECT** + alasan rule (R00x)
- [ ] Writer **remediate**
- [ ] Reviewer **APPROVE**
- [ ] **Human approval** sebelum publish
- [ ] **Escalation** ke manusia (iterasi ke-3)

### 04_audit_log — Jejak Audit
- Ekspor/ salin transcript percakapan inter-agent.
- Simpan revision history (v1 → v2 → v3).
- Jika tidak ada fitur ekspor, screenshot log task history.

---

## Index Bukti (isi manual)
| # | Komponen | File/Lokasi | Waktu | Keterangan |
|---|----------|-------------|-------|------------|
| 1 | Workflow | `01_workflow/` | | 4 skill + assets |
| 2 | Results | `02_results/` | | 3 format konten |
| 3 | Screenshots | `03_screenshots/` | | 7 adegan wajib |
| 4 | Audit log | `04_audit_log/` | | transcript + revisi |
| 5 | Repo (opsional) | `<URL>` | | public repo |

---

## Cara Paket
Jalankan `make_evidence_bundle.py` (di folder kerja) untuk zip otomatis:
```bash
python make_evidence_bundle.py --bundle evidence_bundle --out evidence_bundle.zip
```
Atau zip manual seluruh folder `evidence_bundle/`.

---

## Checklist Final (sebelum submit)
- [ ] 01_workflow berisi 4 skill + SKILL.md valid
- [ ] 02_results berisi ≥2 format konten
- [ ] 03_screenshots memuat reject→remediate→approve + human approval + escalation
- [ ] 04_audit_log berisi transcript & revision history
- [ ] Index README terisi (waktu & keterangan)
- [ ] Zip dibuat & diberi nama jelas (mis. `EduCraft_Evidence_<tim>.zip`)
- [ ] (Opsional) repo publik tersedia & URL dicantumkan
