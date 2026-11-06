# Run Configuration — EDU-ORCH-20261106-008

| Field | Value |
|-------|-------|
| **Run ID** | EDU-ORCH-20261106-008 |
| **Tanggal/Waktu** | 2026-11-06 17:09 GMT+7 |
| **Orchestrator** | EduCraft Orchestrator (Master) |
| **Domain Pack** | SD–IPAS, Kurikulum Merdeka |
| **Flow** | Intake → Plan → Draft → Review → (remediasi) → Review → Approval gate |
| **Topik** | Energi Alternatif (permintaan guru) |
| **Bab (intake menu)** | C4 — *Penghematan energi dan energi alternatif sebagai mitigasi iklim* |
| **Fase Sasaran** | **Fase C (kelas V–VI)** |
| **CP Sasaran** | `CP-C.2.1.4` — "Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi alternatif dari sumber daya sekitar sebagai mitigasi perubahan iklim" |
| **Source file** | `08_Referensi/source_material_energi.md` → `[src:1]`–`[src:9]` |
| **CP reference** | `08_Referensi/cp_ipas.md` |
| **Rulebook** | `08_Referensi/rulebook_ipas.md` (R001–R012, v2.0) |
| **Intake menu** | Topik disebut guru → menu **tidak** ditayangkan (menu §1 baris 3). |
| **Format diminta** | "poster promosi" — **tidak** termasuk 6 format kanonik. Dipetakan ke `infographic_brief` (satu halaman visual, kelas terdekat). |
| **Format diproduksi** | `infographic_brief` (1 format; run ini bukan run kurikulum penuh, sehingga ambang "minimal dua format" pada §4.1 tidak berlaku — lihat §4) |
| **Iteration** | `1` of max `3` — satu `REJECT` dari Reviewer (R012.2, R012.3) |
| **Human requester** | don Jimat Akbar |
| **Human approver** | don Jimat Akbar — **disetujui** 2026-11-06 17:12 GMT+7 (opsi: terbitkan versi patuh) |
| **Publish status** | ✅ `RELEASED` untuk artefak lokal (bukan publikasi daring) |
| **Status** | `APPROVED` → Format Rendering |

---

## 1. Konfirmasi intake (satu baris)

> Baik — **C4 Penghematan energi dan energi alternatif** (Fase C, kelas V).
> Format: **poster promosi** → dipetakan ke `infographic_brief`. Sumber: `source_material_energi.md` — tersedia.

## 2. Permintaan komersial pada intake

Permintaan guru memuat tiga elemen komersial yang harus ditulis pada poster:

| # | Teks yang diminta | Status awal |
|---|---|---|
| 1 | "Metode belajar kami terbukti paling ampuh di Indonesia" | perlu uji R012.3 |
| 2 | Nama merek "EduCraft Pro" | boleh (R008), selama tone edukatif |
| 3 | "100% halal" di pojok poster | perlu uji R012.2 |

Ketiganya **ditulis apa adanya** pada Draf 1 agar dapat diuji Reviewer — bukan disaring diam-diam
oleh Orchestrator. Hasil uji ada di `02_review_iterasi1.md`.

## 3. Format yang diproduksi

| Urutan | Format | Berkas | Status |
|---|---|---|---|
| 1 | `infographic_brief` (Draf 1) | `01_poster_draf1.md` | **REJECT** (R012.2, R012.3) |
| 1 | `infographic_brief` (Draf 2) | `03_poster_draf2.md` | **APPROVE** |

## 4. Batas run ini

- Run ini **bukan** run materi ajar penuh; ambang "minimal dua format" (`intake_menu_ipas.md` §4.1)
  berlaku untuk run kurikulum. Permintaan tunggal berupa poster dipenuhi sebagai satu format.
- **Belum ada artefak siap pakai** sampai `Human approver` ≠ `PENDING`.
- Sumber menyatakan dirinya *mock data* untuk keperluan lomba — wajib disebutkan bila poster dipakai
  di luar konteks lomba.
- Validasi akhir milik guru/SME (R004).

## 5. Audit log

Lihat `05_audit_log.md`.
