# 04 — Spesifikasi rulebook (penunjuk kanonik)

> **Rulebook-nya sendiri ada di** `03_Hasil/referensi/rulebook_ipas.md` (v2.0).
> Berkas ini tidak mengulang aturannya — berkas ini menetapkan bagaimana rulebook dikelola, bagaimana
> tiap aturan ditegakkan, dan bukti apa yang ada untuk penegakan itu. Menyalin teks aturan ke sini
> akan menciptakan sumber kebenaran kedua, dan itu persis mode kegagalan yang ingin dihapus oleh
> kumpulan dokumentasi ini.

---

## 1. Tata kelola

| Sifat | Aturan |
|-------|--------|
| Berkas kanonik | `03_Hasil/referensi/rulebook_ipas.md` |
| Salinan | `skills_package/edu-orchestrator/assets/`, `skills_package/edu-reviewer/assets/` |
| Integritas salinan | Identik byte; diverifikasi dengan checksum sebelum setiap submission |
| Kendali perubahan | Hanya disunting manusia. Agen boleh mengusulkan aturan, tidak pernah menetapkannya |
| Pemberian versi | `vMAJOR.MINOR` + tabel changelog di bagian atas berkas |
| Kompatibilitas mundur | Perubahan yang melonggarkan aturan menuntut tinjauan ulang atas setiap artefak yang lolos di bawah aturan lama |

**Bukti checksum (31 Okt 2026, v2.0):**

```
9fe6336872159a65  03_Hasil/referensi/rulebook_ipas.md
9fe6336872159a65  05_Bukti_Proses/skills_package/edu-orchestrator/assets/rulebook_ipas.md
9fe6336872159a65  05_Bukti_Proses/skills_package/edu-reviewer/assets/rulebook_ipas.md
```

Jalankan ulang dengan:
```bash
python3 -c "import hashlib,sys,pathlib; [print(hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()[:16], p) for p in sys.argv[1:]]" \
  03_Hasil/referensi/rulebook_ipas.md \
  05_Bukti_Proses/skills_package/*/assets/rulebook_ipas.md
```

---

## 2. Himpunan aturan dan status penegakan

| Aturan | Menjaga terhadap | Penegakan | Bukti bahwa ia bekerja |
|--------|------------------|-----------|------------------------|
| R001 | Sitasi tak terselesaikan atau salah kelas | Prompt + **alat deterministik** | `tools/check_grounding.py`; run `-001` 121 tag → PASS; run `-002` 115 tag → PASS setelah perbaikan D1 (sebelumnya 84 pelanggaran kelas, dan itulah yang menemukan cacatnya) |
| R002 | Menakut-nakuti | Hanya prompt | Temuan Reviewer di `05_review.md`; screenshot langsung **TO RUN** |
| R003 | Bahasa tak sesuai usia | Hanya prompt | Aturan ada; tangkapan langsung **TO RUN** |
| R004 | Penyimpangan kurikulum | Prompt + persetujuan manusia | Run `-002` menandai `PERLU KONFIRMASI GURU`, guru menyetujui 30 Okt 17:19 |
| R005 | Isi yang hanya berisi bahaya | Hanya prompt | Tinjau ulang run `-001`: R005 PASS dengan bagian aksi siswa |
| R006 | Klaim kesehatan | Hanya prompt | **TO RUN** (TC-08/09, kritis) |
| R007 | Promosi berbahaya | Hanya prompt | **TO RUN** (TC-10, kritis) |
| R008 | Nada | Hanya prompt | Lingkar render infografis ditolak 2 iterasi karena kejelasan (audit log §3.6) |
| R009 | Bahasa + CTA | Hanya prompt | CTA ada di artikel/slide/brief; diperiksa manual |
| R010 | Diksi yang menstigma | Hanya prompt | Aturan ada; belum ada contoh gagal yang tertangkap |
| R011 | Klaim dunia nyata tanpa sumber | Prompt + syarat URL | Penolakan 29 Okt (F-02) — dua klaim CA tanpa dokumen |
| R012 | Klaim komersial / halal | Hanya prompt | **BARU di v2.0.** Ada kasus ujinya sekarang (TC-21) tetapi **belum pernah dijalankan**; untuk kedua run yang ada berlaku `N/A` dengan alasan |

**Ringkasan jujur:** satu aturan (R001) punya penegakan deterministik. Sebelas sisanya ditegakkan lewat
prompt dan diaudit oleh manusia yang membaca temuan terkutip. Itulah keadaan sebenarnya; jangan
menggambarkannya sebagai mesin kebijakan otomatis.

---

## 3. Apa yang berubah di v2.0 dan mengapa

| Perubahan | Alasan | Risiko bila tidak dilakukan |
|-----------|--------|-----------------------------|
| R003 dikaitkan ke fase di `00_run_config.md`, bukan "kelas 5–6" | Proyek ini melayani Fase B (III–IV) **dan** Fase C (V–VI). Aturan yang hanya menyebut kelas 5–6 tidak bisa menilai artefak Fase B | Paket Fase B akan dinilai dengan jenjang usia yang salah |
| R005/R006/R007 kehilangan penunjuk keras `[src:6]`/`[src:7]`/`[src:8]` | Angka itu milik satu berkas sumber tertentu. Ganti sumbernya, aturan menunjuk bagian yang salah — bertentangan dengan klaim bahwa mesin ini berparameter domain | Klaim "ganti sumbernya dan tetap jalan" akan jadi bohong |
| R004 kehilangan daftar topiknya | Alasan sama: aturan itu menyebut tema satu topik | Topik baru akan secara teknis melanggar R004 |
| R012 ditambahkan | Handbook Challenge C menyebut *iklan dan halal* sebagai kriteria tinjauan. Tanpa aturan, Reviewer tidak punya dasar menolak klaim komersial atau halal | Kasus uji juri tentang klaim halal akan lolos tanpa diperiksa — lubang yang terlihat |
| §0 taksonomi tag ditambahkan | Cacat 29 Okt dan run `-002` sama-sama berasal dari tag kurikulum yang menggantikan tag fakta | Aturan bilang "wajib menyitir sumber" tetapi tidak pernah mendefinisikan apa yang dihitung sebagai sumber |
| §0b aturan N/A ditambahkan | "Dilewati diam-diam" dan "dinilai tidak berlaku" terlihat identik di dalam laporan | Juri tidak bisa membedakan apakah sebuah aturan diterapkan |

**Kompatibilitas mundur:** tidak ada aturan yang dilonggarkan. Setiap vonis yang terbit di bawah v1.1
tetap sah tanpa tinjauan ulang. R012 tercatat `N/A` untuk kedua run yang ada karena keduanya tidak
memuat klaim komersial, khasiat, testimoni, atau halal — diverifikasi lewat pencarian, lihat
`03_Hasil/audit/addendum_R012_2026-10-31.md`.

---

## 4. Cara menambah aturan (prosedur)

1. Nyatakan bahaya yang dicegah aturan itu, dalam satu kalimat.
2. Tulis aturannya sebagai **predikat yang bisa diuji**: apa yang harus benar di dalam teks agar lolos.
3. Tambahkan satu contoh kalibrasi yang seharusnya `REJECT` dan satu yang seharusnya `APPROVE`.
4. Naikkan versi dan catat di changelog.
5. Sinkronkan kedua salinan aset; verifikasi checksum.
6. Bila aturannya lebih ketat dari sebelumnya, tinjau ulang setiap artefak yang lolos di versi lama.
7. Tambahkan minimal satu kasus uji ke `05_TEST_PLAN.md` supaya aturannya bisa didemonstrasikan, bukan
   hanya dideklarasikan.

Aturan tanpa kasus uji hanyalah keinginan. Aturan tanpa contoh kalibrasi bersifat ambigu.

---

## 5. Keterbatasan yang diketahui

Rulebook tidak lebih baik daripada penulisnya. Aturan yang tidak ada berarti pemeriksaan yang tidak
ada, dan Reviewer tidak bisa menolak apa yang tidak dilarang rulebook. Inilah alasan R012 ada: ia
sempat hilang, dan handbook menyebutnya secara eksplisit. Argumen yang sama berlaku untuk apa pun yang
masih hilang.
