# 08 — Review pascamerge

> **Cakupan:** bagaimana perubahan yang sudah masuk `main` ditelaah dan dikoreksi, siapa yang berwenang,
> dan bukti apa yang harus menyertai sebuah koreksi.
>
> **Yang bukan cakupan dokumen ini:** alur kerja run EduCraft (`02_WORKFLOW.md`) dan pengujian
> (`05_TEST_PLAN.md`). Dokumen ini hanya mengatur tata cara telaah atas riwayat git.

---

## 1. Mengapa mekanismenya pascamerge

Lima commit hasil run `EDU-ORCH-20261026-001` dipublikasikan **langsung ke `main`** pada 5 Nov 2026
06:17 GMT+7, tanpa Pull Request. Alasannya teknis, bukan keputusan desain:

| Jalur pembuatan PR | Status saat itu |
|--------------------|-----------------|
| `gh` CLI | Tidak terpasang di PATH maupun lokasi umum |
| Token API (`GH_TOKEN` / `GITHUB_TOKEN`) | Kosong |
| Konfigurasi `~/.config/gh` | Tidak ada |
| SSH (`Hi a121ef!`) | Bekerja, tetapi tidak dapat memanggil REST API GitHub |

Karena tidak ada jalur untuk membuka PR, telaah dipindahkan ke **setelah** merge. Konsekuensi yang
diterima secara sadar: `main` memuat perubahan sebelum ada persetujuan rekan tim. Kompensasinya adalah
prosedur di §3 — koreksi tetap dapat diajukan, dan riwayatnya tetap dapat ditelusuri.

**Alternatif yang ditolak:** menulis ulang `main` dengan `--force-with-lease` lalu membuka PR. Ditolak
karena `main` adalah branch bersama; penulisan ulang riwayat berisiko bagi siapa pun yang sudah menarik
perubahan, sementara manfaatnya hanya mengembalikan tahap review yang bisa dicapai lewat prosedur §3.

---

## 2. Lima commit yang dipublikasikan

Rentang `7c7114b..af9e1f3` — **24 berkas, +2.768 / −17**.

| Commit | Lingkup | Berkas | Fokus telaah |
|--------|---------|--------|--------------|
| `10c72b1` | `.gitignore`: `.cache/`, `.slidep/`, `output/` | 1 (+8) | Apakah ketiganya benar artefak build, dan tidak ada berkas sumber yang ikut terabaikan |
| `6f6b682` | Artefak siap pakai: RPP `.docx`, 10 slide `.pptx` + DSL, kuis HTML | 13 (+1.274) | Kebenaran faktual; konsistensi `145 MWac (192 MWp)`; 0 tag internal; kuis berfungsi tanpa jaringan |
| `b4740dd` | `00_run_config.md`, `audit_log.md` §3.7.1–3.7.9 | 2 (+179 / −14) | Kesesuaian catatan audit dengan berkas nyata; kelengkapan Source Resolution Map |
| `5d6d0de` | Stage 6: `format_rendering_spec.md` + `SKILL.md` + `README.md` | 3 (+180 / −3) | Apakah FR-01…FR-08 dapat diuji; keselarasan dengan dokumen kanonik |
| `af9e1f3` | Isi `evidence_bundle/` | 5 (+1.127) | Apakah berkas di bundle identik dengan sumbernya |

**Berkas kanonik yang wajib dibandingkan saat menelaah:**

| Bila menelaah | Bandingkan dengan |
|---------------|-------------------|
| `5d6d0de` (`SKILL.md`) | `02_WORKFLOW.md` §1 dan §2 — kanonik untuk alur kerja |
| `b4740dd` (`audit_log.md`) | `05_TEST_PLAN.md` dan artefak di `03_Hasil/edu_output/` |
| `6f6b682` (RPP/slide/kuis) | `03_Hasil/referensi/konteks_aktual.md` dan `rulebook_ipas.md` v2.0 |
| `af9e1f3` (evidence) | Berkas asal di `03_Hasil/edu_output/` — harus identik byte |

---

## 3. Cara mengajukan koreksi

Tidak ada yang boleh menulis langsung ke `main`. Prosedurnya:

1. **Buat branch dari `main` terbaru**, beri nama menurut topik, bukan menurut nama orang:
   ```
   git checkout main && git pull
   git checkout -b koreksi/<topik-singkat>
   ```
2. **Satu commit = satu koreksi.** Jangan gabungkan perbaikan faktual dengan perapian tata letak.
   Pesan commit memuat **alasan**, bukan hanya daftar berkas:
   ```
   fix(konten): koreksi satuan PLTS Cirata pada slide 8

   Sumber menyebut 145 MWac (192 MWp). Slide menulis 145 MWp, yang
   keliru pada dua tingkat: satuan daya dan angka puncak.
   ```
3. **Sertakan bukti.** Koreksi faktual wajib menyebut sumber (berkas + bagian). Koreksi kode wajib
   menyertakan perintah yang membuktikan, mis. `grep -c "\[src:" <berkas>` → `0`.
4. **Push dan buka PR** ke `main`. Bila `gh` belum tersedia, buka lewat antarmuka web:
   `https://github.com/otnamhcar/educraft-hackathon-workbuddy-2026/compare`
5. **Jangan** memakai `git push --force` ke `main`, dan **jangan** menulis ulang commit yang sudah
   dipublikasikan.

---

## 4. Kriteria lulus telaah

Sebuah koreksi diterima bila seluruh butir berikut terpenuhi:

| # | Kriteria | Cara membuktikan |
|---|----------|------------------|
| 1 | Tidak ada tag internal (`[src:`, `[UNVERIFIED]`) pada artefak guru/siswa | `grep -rc "\[src:"` → 0 pada setiap berkas |
| 2 | Setiap klaim faktual dapat ditelusuri ke sumber | Baris Source Resolution Map di `audit_log.md` |
| 3 | Angka dan satuan identik lintas artefak | Bandingkan RPP, slide, dan kuis untuk besaran yang sama |
| 4 | Dokumen turunan tidak bertentangan dengan kanonik | `00_INDEX.md` §2 |
| 5 | Fungsi inti berjalan tanpa jaringan | Buka artefak HTML dengan koneksi dimatikan |
| 6 | Tidak ada catatan internal yang terbawa ke artefak | Baca artefak sebagai guru, bukan sebagai agen |

Butir 1–6 adalah penerapan langsung FR-01…FR-08 pada `format_rendering_spec.md`; bila keduanya
berbeda, spesifikasi yang menang dan dokumen ini yang harus diperbaiki.

---

## 5. Temuan yang sudah tercatat

| ID | Temuan | Bukti | Tindakan | Status |
|----|--------|-------|----------|--------|
| K1 | `02_WORKFLOW.md` — dokumen kanonik alur kerja — tidak memuat Format Rendering, sementara `SKILL.md` sudah 7 langkah. Melanggar aturan rumah §2 (`00_INDEX.md`): turunan bertentangan dengan kanonik. | `grep -ni "format rendering" 07_Dokumentasi/02_WORKFLOW.md` → 0 hasil pada `af9e1f3` | Menambahkan baris `S6b` pada `02_WORKFLOW.md` §1, transisi `S6→S6b→RELEASED` pada §2, catatan prasyarat `approved_at`, dan entri `S6b` pada daftar pipeline `01_ARSITEKTUR.md` §6 | **DITUTUP** 5 Nov 2026 |

**Cara membaca tabel ini:** temuan yang hanya disebut di percakapan tidak dihitung. Setiap baris wajib
memuat perintah yang dapat dijalankan ulang untuk membuktikannya.

---

## 6. Pembatalan

Bila sebuah perubahan harus dicabut, urutannya dari yang paling aman:

| Metode | Perintah | Kapan dipakai | Risiko |
|--------|----------|---------------|--------|
| `git revert` | `git revert <hash>` | Perubahan sudah ditarik orang lain | Rendah — riwayat utuh, jejak audit tetap ada |
| Reset branch lokal | `git reset --hard <hash>` | Belum di-push | Rendah — hanya lokal |
| Tulis ulang remote | `git push --force-with-lease origin <hash>:main` | Hanya bila kebocoran data | **Tinggi** — memutus riwayat peninjau lain |

`git revert` adalah pilihan bawaan. Tulis ulang riwayat hanya sah untuk kasus kebocoran kredensial atau
data pribadi, dan harus disertai catatan di `audit_log.md`.

---

## 7. Yang tidak boleh diubah lewat koreksi rutin

Perubahan pada daftar ini memerlukan persetujuan manusia yang tercatat, bukan sekadar PR:

1. **Sumber fakta** — `source_material_*.md`, `konteks_aktual.md`, `cp_ipas.md`.
2. **Rulebook** — `rulebook_ipas.md` v2.0; perubahan aturan menaikkan versi.
3. **Audit log historis** — entri yang sudah ditulis tidak disunting; koreksi ditambahkan sebagai pass baru.
4. **Ambang keputusan** — batas 3 iterasi dan syarat persetujuan.

Alasannya: keempatnya adalah dasar bagi klaim akuntabilitas. Mengubahnya tanpa jejak akan membuat
seluruh Source Resolution Map kehilangan makna.

---

## 8. Riwayat perubahan

| Tanggal | Perubahan |
|---------|-----------|
| 5 Nov 2026 | Dokumen dibuat setelah `main` dipublikasikan tanpa PR; temuan K1 dicatat dan ditutup pada hari yang sama |
