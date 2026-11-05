# 01 — Arsitektur (kanonik)

> **Status dokumen ini:** sumber kebenaran kanonik untuk arsitektur.
> Ringkasan turunan untuk juri: `06_Submission/05_Architecture.md` (dipadatkan),
> `06_Submission/architecture_diagram.html` (visual), `README.md` §Pipeline.
> Bila keduanya berbeda dengan berkas ini, **berkas ini yang menang** dan keduanya harus diperbaiki.
>
> **Aturan bukti:** setiap klaim arsitektur di bawah ini membawa status.
> `IMPLEMENTED` = ada artefak di repo yang membuktikannya. `SPECIFIED` = tertulis di kontrak tetapi
> belum didemonstrasikan. `GAP` = belum benar hari ini. Tidak ada klaim yang dibiarkan tanpa tanda.

---

## 1. Sistem ini apa

EduCraft mengubah **satu dokumen sumber yang sudah disetujui** menjadi **paket ajar beberapa format**,
dan menolak melepaskannya sampai seorang Reviewer independen memeriksanya terhadap rulebook tertulis
dan seorang manusia menyetujuinya.

Ini bukan aplikasi web. Ini adalah:

| Lapisan | Apa itu | Di mana |
|---------|---------|---------|
| Kontrak | 4 spesifikasi agen (`SKILL.md`) | `05_Bukti_Proses/skills_package/` |
| Pengetahuan | fakta read-only, capaian kurikulum, rulebook, register konteks aktual | `03_Hasil/referensi/` |
| State | konfigurasi run + audit log append-only | `03_Hasil/edu_output*/` |
| Keluaran | draf Markdown, kuis/animatik HTML, infografis PNG, PDF cetak | `03_Hasil/` |

---

## 2. Invarian desain

Lima hal inilah alasan sistem ini ada. Kalau satu invarian dijatuhkan, produknya kehilangan tesis.

| # | Invarian | Penegakan | Status |
|---|----------|-----------|--------|
| I1 | **Satu sumber fakta.** Tidak ada fakta di luar sumber yang disetujui; jalan keluarnya adalah token literal `[UNVERIFIED]`. | Kontrak Writer + R001 | IMPLEMENTED |
| I2 | **Veto terpisah dari penulisan ulang.** Reviewer boleh menolak, tidak boleh menulis ulang; Writer boleh menulis ulang, tidak boleh menyetujui. | Kontrak terpisah | IMPLEMENTED |
| I3 | **Tidak ada penerbitan sendiri.** Penerbitan adalah langkah tersendiri yang menuntut tindakan manusia yang eksplisit. | Langkah 5 Orchestrator + run config | IMPLEMENTED (run 002: gerbang terbuka hanya setelah persetujuan 17:19) |
| I4 | **Perulangan terbatas.** Tiga penolakan berarti berhenti dan eskalasi; tidak pernah mengulang tanpa akhir. | Aturan keras Orchestrator | SPECIFIED — penghitung tercatat dalam prosa, tidak ditegakkan oleh berkas |
| I5 | **Isi sumber adalah data, bukan instruksi.** Perintah yang tersisip dilaporkan, tidak pernah dituruti. | Aturan keras Orchestrator | SPECIFIED — belum ada uji injeksi yang dijalankan (TC-15) |

---

## 3. Komponen

| # | Komponen | Jenis | Memiliki | Tidak boleh | Status |
|---|----------|-------|----------|-------------|--------|
| C1 | Guru / SME | Manusia | Keputusan persetujuan, pemilihan sumber | — | IMPLEMENTED |
| C2 | Orchestrator | Agen (state machine) | Perutean, batas iterasi, gerbang, audit log | Menerbitkan, menulis isi, mengubah vonis | IMPLEMENTED |
| C3 | Planner | Agen | Penguraian menjadi kerangka per format + pemetaan CP | Mengarang fakta, menulis prosa | IMPLEMENTED |
| C4 | Writer | Agen | Seluruh teks draf + brief aset (artikel, RPP, kuis, kerangka slide, brief infografis, skrip video) | Memakai fakta di luar sumber, menyetujui karyanya sendiri | IMPLEMENTED |
| C5 | Reviewer | Agen | Vonis `APPROVE`/`REJECT` + temuan dengan ID aturan dan teks yang dikutip | Menulis ulang isi, melunakkan temuan demi mengakhiri perulangan | IMPLEMENTED |
| C6 | Aset pengetahuan | Berkas (read-only) | Fakta, CP, rulebook, register konteks aktual | — | IMPLEMENTED |
| C7 | Rekaman run | Berkas (append-only) | Run config, audit log, laporan review | — | IMPLEMENTED |

### 3.1 Rekonsiliasi dengan log run

Audit log untuk run `-002` menamai beberapa langkah `edu-infographic`, `edu-video`, `edu-quiz`.
**Itu bukan agen terpisah.** Itu adalah fase eksekusi dari **C4 Writer** yang menghasilkan kelas
artefak berbeda (aset visual dan interaktif) dari brief yang sudah disetujui. Fase-fase itu tidak punya
veto independen dan tidak punya kontrak sendiri.

Ini penting untuk kejujuran penilaian: sistem ini punya **empat agen dengan peran berbeda**, yang
memenuhi syarat Challenge C yaitu minimal tiga (Planner, Writer, Reviewer + Orchestrator). Kami tidak
mengklaim lima atau enam agen. Skill `Producer` terpisah adalah penyempurnaan v2, tercatat di
`07_GAP_DAN_REKOMENDASI.md` — bukan fakta saat ini.

---

## 4. Batas kepercayaan

| Batas | Antara | Yang tidak boleh menyeberang | Status |
|-------|--------|------------------------------|--------|
| B1 Pengetahuan read-only | C2–C5 ↔ C6 | Segala penulisan. Agen tidak boleh menyunting sumber, CP, atau rulebook agar keluarannya sendiri lolos | IMPLEMENTED (berkas berupa aset statis) |
| B2 Otoritas manusia | Lingkar agen ↔ gerbang persetujuan | Penerbitan. `APPROVE` dari Reviewer adalah prasyarat, bukan izin | IMPLEMENTED |
| B3 Otoritas terbit | Gerbang ↔ keluaran | Artefak apa pun yang belum disetujui | IMPLEMENTED |
| B4 Data/instruksi | Dokumen sumber ↔ instruksi agen | Perintah yang ada di dalam sumber | SPECIFIED |

**B1 adalah batas yang paling mungkin dilanggar dalam praktik**, karena ditegakkan oleh konvensi
(perizinan berkas di repo), bukan oleh runtime. Mitigasi: lapisan pengetahuan tidak pernah ditulis oleh
langkah agen; audit log mencatat versi aset mana yang dibaca.

---

## 5. Kontrak data

### 5.1 Taksonomi tag (kosakata grounding)

| Kelas tag | Bentuk | Arti | Menyelesaikan ke |
|-----------|--------|------|------------------|
| Fakta | `[src:1]` … `[src:n]` | Sebuah klaim faktual | Bagian bernomor di `source_material_*.md` |
| Kurikulum | `[src:CP]`, `[src:B5]`, `[src:C4]`, `[src:B4]` | Rujukan kurikulum, **bukan fakta** | Kode CP di `cp_ipas.md` |
| Konteks aktual | `[src:CA1]` … | Klaim dunia nyata | Entri di `konteks_aktual.md` dengan URL resmi + tanggal akses |

**Aturan:** tag kurikulum tidak pernah boleh menggantikan tag fakta. Inilah persisnya cacat yang
menghasilkan penolakan 29 Oktober, dan cacat itu berulang di run `-002` (lihat `07_GAP_DAN_REKOMENDASI.md` G1).

### 5.2 Vonis Reviewer

```json
{
  "status": "APPROVE | REJECT",
  "iteration": 1,
  "findings": [
    {
      "rule": "R002",
      "severity": "critical | major | minor",
      "quote": "teks pelanggar, persis",
      "reason": "mengapa melanggar aturan",
      "suggestion": "perbaikan konkret",
      "location": "berkas + bagian"
    }
  ]
}
```
Status: IMPLEMENTED — skema ini dipakai apa adanya di `03_Hasil/edu_output_wujud_zat/05_review.md` §PASS 1.

### 5.3 Konfigurasi run (state of record)

| Field | Kegunaan | Status |
|-------|----------|--------|
| `run_id` | Reproduksibilitas | IMPLEMENTED |
| `topic`, `phase`, `cp_codes` | Cakupan | IMPLEMENTED |
| `source_path`, `source_version` | Fakta mana yang dipakai | IMPLEMENTED (hanya path; versi belum di-hash) |
| `iteration` | Penghitung perulangan | GAP — hidup di prosa, bukan sebagai field |
| `per_format_status` | Artefak mana berstatus vonis apa | GAP |
| `approver`, `approved_at`, `publish_status` | Akuntabilitas | IMPLEMENTED |

---

## 6. Urutan eksekusi

```
S0  Intake        Guru memasok sumber + topik + fase
                  Topik belum disebut → menu bab (intake_menu_ipas.md): L1 fase → L2 rumpun → L3 bab
                  Format belum disebut → bawaan RPP + kuis + slide (minimal dua format)
                  → menulis 00_run_config.md (publish_status: PENDING)
S1  Plan          Planner → kerangka per format, pemetaan CP, celah ditandai
S2  Draft         Writer  → draf v1, setiap kalimat faktual diberi tag
S3  Ground        Orchestrator → cek resolusi tag (deterministik)
S4  Review        Reviewer → APPROVE | REJECT + findings[]
                  REJECT → kembali ke S2, iteration += 1; di iterasi 3 → S6
S5  Approve       Manusia membaca paket, memutuskan
S6  Release       Hanya setelah persetujuan eksplisit. Bila tidak, berhenti dengan temuan.
                  S6 tidak menghasilkan artefak — ia mencatat izin.
S6b Format        WAJIB. Orchestrator → Materi_Guru .md, RPP .docx, Slide .pptx, Kuis .html
    Rendering     Urutan tetap: .md lebih dulu, tiga lainnya diturunkan darinya (FR-09).
                  Prasyarat: approved_at terisi. Kontrak: format_rendering_spec.md (FR-01…FR-09).
                  Isi tidak berubah — hanya bentuk. Cacat isi kembali ke S2 sebagai iterasi baru.
                  Tanpa keempat artefak, run tidak boleh berstatus RELEASED.
```

**S3 adalah langkah yang selama ini hilang dari proyek ini.** Langkah ini dispesifikasikan di sini, dan
implementasi yang berfungsi sudah dirilis di `tools/check_grounding.py`. Status: IMPLEMENTED sebagai
alat; GAP sebagai langkah pipeline wajib (kontrak orchestrator belum mewajibkan menjalankannya).

---

## 7. Mode kegagalan dan respons yang dirancang

| Kegagalan | Gejala | Respons yang dirancang | Status |
|-----------|--------|------------------------|--------|
| F1 Tag tak terselesaikan | `[src:9]` padahal bagian itu tidak ada | Cek grounding gagal → kembali ke Writer | Alat IMPLEMENTED; gerbang GAP |
| F2 Tag kurikulum dipakai sebagai fakta | `[src:B4]` pada klaim sains | Cek grounding menandai ketidakcocokan kelas tag | Alat IMPLEMENTED (sadar kelas) |
| F3 Sumber tipis | Writer menghasilkan materi pendek dan berulang | Menolak mengisi dengan tempelan; eskalasi dengan `PERLU KONFIRMASI GURU` | IMPLEMENTED (penanda celah run `-002`) |
| F4 Titik buta Reviewer | Pelanggaran lolos | Vonis wajib mengutip teks + merujuk aturan, sehingga manusia dapat mengaudit auditnya | IMPLEMENTED (begitulah F-01 tertangkap) |
| F5 Remediasi tak berujung | Perulangan tidak pernah selesai | Batas keras 3, lalu eskalasi | SPECIFIED |
| F6 Prompt injection di sumber | "abaikan aturannya" tersisip | Diperlakukan sebagai data, dilaporkan ke pengguna | SPECIFIED |

---

## 8. Di luar cakupan (disengaja)

- Tanpa fine-tuning, tanpa vector database, tanpa framework orkestrasi. State machine-nya adalah kontrak.
- Tanpa aplikasi untuk siswa. Keluarannya berupa paket cetak dan kuis HTML mandiri.
- Tanpa cek plagiarisme otomatis, tanpa terjemahan otomatis. Keduanya masuk peta jalan.

---

## 9. Peta bukti

| Klaim | Dibuktikan oleh |
|-------|-----------------|
| Empat agen, peran berbeda | `05_Bukti_Proses/skills_package/*/SKILL.md` |
| Reviewer memveto, merujuk aturan, mengutip teks | `03_Hasil/edu_output_wujud_zat/05_review.md` §PASS 1 (5 temuan major) |
| Gerbang persetujuan manusia memblokir penerbitan | `03_Hasil/edu_output_wujud_zat/audit_log.md` §3.7 (persetujuan 17:19) |
| Siklus tolak → remediasi → setujui | `03_Hasil/audit/review_kepatuhan_R001-R011_2026-10-29.md` → `..._REVISI.md` |
| Penghitung perulangan | GAP — hanya prosa, tanpa field. Jangan klaim sudah ditegakkan. |
| Resolusi tag | Keluaran `tools/check_grounding.py`, direproduksi di `06_TRACEABILITY.md` |
