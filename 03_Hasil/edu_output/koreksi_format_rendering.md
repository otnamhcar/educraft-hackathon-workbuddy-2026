;; Koreksi Format Rendering — run EDU-ORCH-20261026-001
;; Transkripsi mesin dari koreksi yang SUDAH tercatat di audit_log.md §3.7.4
;; (Revisi Pasca-Konversi, 4 Nov 2026) dan 00_run_config.md §"Revisi pasca-konversi".
;; Berkas ini tidak menambah koreksi baru. Ia memindahkan koreksi yang sama ke bentuk
;; yang bisa dibaca tools/build_materi_md.py, supaya draf .md tidak memuat angka
;; yang sudah dikoreksi pada .docx dan .pptx.
;;
;; Satu baris = satu aturan: teks lama, pemisah, teks baru. Baris berawalan ;; diabaikan.
;; Alat berhenti dengan kode 1 bila teks lama masih tersisa di keluaran.

;; §3.7.4 butir 3 — koreksi faktual kapasitas PLTS Cirata
145 MWp => 145 MWac (192 MWp)

;; §3.7.4 butir 1 & 2 — catatan internal dan rujukan berkas pipeline
## D. Materi Pembelajaran (Fakta dari Source) => ## D. Materi Pembelajaran
- `assets/source_material_ipas.md` (R001 grounding) => - Bahan sumber IPAS yang disetujui guru (9 bagian bernomor)
- `assets/cp_ipas.md` (R004 alignment) => - Panduan Mata Pelajaran IPAS, Puskurjar, Kemendikdasmen (Revisi 4, 3 Oktober 2025)
lihat `02_quiz_pretest_posttest.md` => lihat bagian Kuis Pre-test & Post-test pada berkas ini
