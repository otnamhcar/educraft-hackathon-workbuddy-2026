# 00 — Indeks dokumentasi

> **Isi folder ini:** kumpulan dokumentasi rekayasa untuk EduCraft. Tujuannya supaya tidak ada satu
> pun pertanyaan tentang sistem ini yang punya dua jawaban berbeda di dua berkas berbeda.
>
> **Yang bukan isi folder ini:** naskah submission. Dokumen untuk juri ada di `06_Submission/` dan
> merupakan *turunan* dari folder ini.

**Bahasa:** seluruh dokumen dalam folder ini ditulis dalam Bahasa Indonesia, sesuai ketentuan proyek
(input maupun output). Istilah teknis yang tidak punya padanan baku (mis. `REJECT`, `APPROVE`,
`publish_status`) dipertahankan apa adanya karena merupakan nilai harfiah di dalam berkas state —
menerjemahkannya justru akan memutus jejak bukti.

---

## 1. Urutan membaca

| Pembaca | Baca dengan urutan ini | Waktu |
|---------|------------------------|-------|
| Juri / peninjau | `06_Submission/02_Project_Description.md` → `05_Architecture.md` → `03_Accountability_Sheet.md` → `04_Test_Results.md` → `06_TRACEABILITY.md` §A–C | 15 menit |
| Rekan tim yang bergabung hari ini | `01_ARSITEKTUR.md` → `02_WORKFLOW.md` → `03_SKILLS.md` → `05_TEST_PLAN.md` → `07_GAP_DAN_REKOMENDASI.md` | 40 menit |
| Perawat sistem di masa depan | Indeks ini → `04_RULEBOOK.md` → `01_ARSITEKTUR.md` §5 (kontrak data) → `tools/check_grounding.py` | 30 menit |

---

## 2. Sumber kebenaran

Satu berkas kanonik per topik. Sisanya turunan dan **tidak boleh menambah klaim baru**.

| Topik | Kanonik | Turunan (jangan disunting seolah primer) |
|-------|---------|------------------------------------------|
| Arsitektur | `07_Dokumentasi/01_ARSITEKTUR.md` | `06_Submission/05_Architecture.md`, `architecture_diagram.html`, `README.md` §Pipeline |
| Alur kerja / state machine | `02_WORKFLOW.md` | `edu-orchestrator/SKILL.md` (kontrak runtime), `02_Project_Description.md` §3.3 |
| Aturan | `03_Hasil/referensi/rulebook_ipas.md` (v2.0) | `skills_package/*/assets/rulebook_ipas.md` (salinan identik byte) |
| Batas peran skill | `03_SKILLS.md` | empat berkas `SKILL.md` |
| Pengujian | `05_TEST_PLAN.md` | `04_Diskusi/test_cases_matrix.md` (warisan), `04_Test_Results.md` (hasil), `03_screenshots/INDEX.md` (pelacak tangkap layar) |
| Pemenuhan persyaratan | `06_TRACEABILITY.md` | `06_Submission/00_SUBMISSION_CHECKLIST.md` |
| Kekurangan yang diketahui | `07_GAP_DAN_REKOMENDASI.md` | — |

**Kenapa ini penting:** sebelumnya arsitektur dijelaskan di empat tempat dan rulebook di tiga tempat,
dengan rumusan yang berbeda-beda. Begitulah inkonsistensi "empat agen vs lima format" bisa bertahan
berhari-hari.

---

## 3. Isi kumpulan dokumen

| Berkas | Menjawab pertanyaan |
|--------|---------------------|
| `01_ARSITEKTUR.md` | Apa saja bagiannya, apa yang boleh dilakukan masing-masing, di mana batas kepercayaannya, apa kontrak datanya? |
| `02_WORKFLOW.md` | Dalam urutan apa sebuah run berjalan, berkas apa yang ditulis di tiap langkah, kapan berhenti? |
| `03_SKILLS.md` | Peran mana yang memiliki keputusan mana, dan bagaimana membuktikan tidak ada dua peran yang tumpang tindih? |
| `04_RULEBOOK.md` | Bagaimana aturan dikelola, diberi versi, ditegakkan — dan mana yang benar-benar punya bukti? |
| `05_TEST_PLAN.md` | Apa persisnya yang diuji, dengan parameter apa, terhadap kriteria lulus apa, dibuktikan oleh berkas mana? |
| `06_TRACEABILITY.md` | Untuk setiap persyaratan handbook dan dimensi penilaian, di mana buktinya? |
| `07_GAP_DAN_REKOMENDASI.md` | Apa yang kurang, dalam urutan apa diperbaiki, dan seperti apa bentuk "selesai"? |

Peralatan pendukung: `tools/check_grounding.py` — cek R001 yang deterministik; menulis
`grounding_report.md` per run dan keluar dengan kode non-nol bila gagal.

---

## 4. Potret keadaan — 31 Oktober 2026

| Butir | Keadaan |
|-------|---------|
| Item submission | 8 SIAP · 1 SEBAGIAN · 2 BELUM (satu di antaranya bonus) |
| Rangkaian uji | 21 kasus terdefinisi dengan parameter; **0 screenshot tertangkap** |
| Cek deterministik | R001 — **PASS pada kedua run** (121 tag; 115 tag). D1 menemukan 84 pelanggaran, lalu ditutup dengan penandaan ulang |
| Rulebook | v2.0, tiga salinan, checksum terverifikasi |
| Repo publik | `github.com/otnamhcar/educraft-hackathon-workbuddy-2026`, MIT, 119 berkas ter-track |
| Tenggat | **7 Nov 2026** — dikonfirmasi pesan panitia 27/10 21:23 (`01_Dokumen/BUKTI_KOMITE_2026-10-31.md`). Target submit internal: **5 Nov** |
| Dataset & test case | Diberi keringanan oleh panitia; skenario dari peserta diperbolehkan (berkas bukti yang sama §3) |
| Cacat terbuka | **Tidak ada.** D1 ditutup 31 Okt lewat penandaan ulang; D2 ditutup 31 Okt dengan menambahkan §7 ke audit log `-001` |
| Di mana nilainya hilang | Bukan di desain — di bukti tangkap. Screenshot (0) dan video (belum ada) menahan tiga dimensi penilaian |

---

## 5. Aturan rumah

1. **Tidak ada klaim tanpa artefak.** Kalau sebuah berkas tidak bisa membuktikannya, kalimatnya harus
   berbunyi "dirancang untuk" atau tidak ada sama sekali.
2. **Satu berkas kanonik per topik.** Dokumen turunan yang bertentangan dengan sumber kanoniknya
   adalah bug pada dokumen turunan itu.
3. **Kosakata status bersifat tetap:** `SIAP` / `SEBAGIAN` / `GAP` / `UNVERIFIED` untuk dokumen;
   `PASS` / `BY DESIGN` / `TO RUN` / `FAIL` untuk pengujian.
4. **Sebut run-nya.** Jangan pernah menulis "run yang jadi acuan" tanpa ID dan status.
5. **Ungkap cacat di tempat ia ditemukan.** Cacat yang hanya disebut di percakapan tidak ada artinya
   bagi juri.

---

## 6. Riwayat perubahan

| Tanggal | Perubahan |
|---------|-----------|
| 31 Okt 2026 | Kumpulan dokumentasi dibuat; rulebook v2.0 (berparameter + R012); `check_grounding.py` dirilis; laporan grounding dibuat untuk kedua run; adendum R012 ditulis; cacat D1/D2 dicatat |
| 31 Okt 2026 | Seluruh dokumen diterjemahkan ke Bahasa Indonesia; angka-angka yang kedaluwarsa (jumlah berkas, jumlah kasus uji, durasi video) diselaraskan dengan keadaan repo |
