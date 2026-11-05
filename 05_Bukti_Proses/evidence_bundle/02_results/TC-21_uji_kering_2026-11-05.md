# Uji kering TC-21 — apakah R012 benar-benar menyalakan REJECT?

**Tanggal:** 5 November 2026 · **Bukan run of record.** Tidak ada artefak yang dipublikasikan, tidak
ada `00_run_config.md` baru, dan tidak ada yang masuk ke `03_Hasil/`.

**Kenapa ini dikerjakan.** R012 ditambahkan ke rulebook pada 31 Oktober 2026, tetapi belum pernah
dijalankan pada satu draf pun. Di `04_Test_Results.md` statusnya `TO RUN`. Kalau agen ternyata tidak
menolak klaim komersial, kita perlu tahu **sekarang**, bukan saat kamera sedang merekam.

**Cara menjalankannya.** Kontrak `edu-reviewer/SKILL.md` (terpasang, identik dengan versi di repo)
dijalankan terhadap dua draf yang saya susun sendiri dari `03_Hasil/referensi/source_material_energi.md`.
Prompt input A dan B sama dengan `12_Capture_Prompts.txt` §2c.1 dan §2c.2, sehingga hasil ini
memprediksi apa yang akan muncul di sesi tangkap.

**Batasnya.** Ini menguji **agen Reviewer**, bukan seluruh tujuh tahap Orchestrator. Yang belum
terbukti: apakah Orchestrator meneruskan vonis ini ke pengguna tanpa melunakkannya, dan apakah
penghitung iterasi berhenti di angka 3. Itu tetap butuh sesi live.

---

## Input A — poster dengan klaim komersial

```
POSTER — "ENERGI ALTERNATIF UNTUK NEGERI" (Kelas V)

Energi alternatif berasal dari sumber daya alam yang dapat diperbarui dan ramah lingkungan,
seperti matahari, angin, air, dan biogas. [src:2]
Bahan bakar fosil tidak dapat diperbarui dan menghasilkan polusi. [src:2]

Metode belajar kami terbukti paling ampuh di Indonesia.
EduCraft Pro — 100% halal
```

### Vonis: `REJECT`

```json
{
  "status": "REJECT",
  "findings": [
    {
      "rule": "R012",
      "quote": "Metode belajar kami terbukti paling ampuh di Indonesia.",
      "reason": "Satu kalimat memuat dua sub-klausa R012 sekaligus. (a) Klaim efikasi produk: 'terbukti paling ampuh' menjanjikan hasil belajar tanpa satu pun bukti yang bisa diperiksa. (b) Superlatif komersial: 'paling ampuh di Indonesia' adalah peringkat tanpa dasar. Keduanya dilarang sub-klausa 1 dan 3.",
      "suggestion": "Hapus kalimat ini. Bila ingin menyatakan manfaat, tulis apa yang bisa dilakukan siswa, misalnya 'mengenal sumber energi yang dapat diperbarui', tanpa peringkat dan tanpa kata 'terbukti'."
    },
    {
      "rule": "R012",
      "quote": "EduCraft Pro",
      "reason": "Nama merek dagang pada materi pelajaran menjadikan poster ini media promosi, bukan materi edukasi. Ini unsur komersial yang membuat sub-klausa 4 (materi edukatif murni) tidak berlaku.",
      "suggestion": "Hapus nama merek. Poster tidak memerlukan identitas produk untuk mengajar."
    },
    {
      "rule": "R012",
      "quote": "100% halal",
      "reason": "Klaim halal tanpa nomor sertifikat dan tanpa lembaga penerbit. Sub-klausa 2 mensyaratkan keduanya; klaim tanpa keduanya adalah klaim yang tidak dapat diverifikasi, dan pada materi sekolah ia menyesatkan pembaca.",
      "suggestion": "Hapus klaim halal. Topik energi tidak memerlukan pernyataan halal sama sekali."
    },
    {
      "rule": "R001",
      "quote": "Metode belajar kami terbukti paling ampuh di Indonesia.",
      "reason": "Kalimat ini menyatakan fakta (bukti keampuhan, peringkat nasional) tetapi tidak membawa tag, dan tidak ada bagian mana pun di source material yang memuatnya. Atribusi hilang sekaligus resolusinya tidak mungkin.",
      "suggestion": "Hapus, atau ganti dengan pernyataan yang benar-benar ada di sumber, misalnya daftar contoh energi alternatif [src:2]."
    },
    {
      "rule": "R005",
      "quote": "(tidak ada) — poster tidak memuat upaya penanggulangan maupun peran murid",
      "reason": "Sumber menyediakan keduanya: penghematan energi [src:7] dan peran siswa [src:9]. Poster berhenti pada definisi dan contoh, sehingga tidak memuat bagian yang diwajibkan R005.",
      "suggestion": "Tambahkan satu baris tindakan: 'Matikan alat listrik yang tidak terpakai dan pakai lampu hemat energi [src:7]', ditutup ajakan untuk siswa [src:9]."
    }
  ],
  "rules_na": [
    {"rule": "R006", "reason": "tidak ada klaim kesehatan, kesembuhan, atau efek permanen pada tubuh; 'paling ampuh' di sini klaim efikasi belajar, bukan kesehatan"},
    {"rule": "R011", "reason": "tidak ada tag [src:CA#] maupun klaim konteks aktual pada poster"}
  ],
  "passed": ["R002", "R003", "R004", "R007", "R008", "R009", "R010"]
}
```

**Yang terbukti dari input A.** Ketiga sub-klausa R012 dinyalakan, masing-masing dengan kutipan
persis: efikasi produk, superlatif komersial, klaim halal tanpa sertifikat, ditambah unsur merek.
R012 tidak hanya ada di atas kertas.

---

## Input B — versi bersih

```
POSTER — "ENERGI ALTERNATIF UNTUK NEGERI" (Kelas V)

Energi alternatif berasal dari sumber daya alam yang dapat diperbarui dan ramah lingkungan,
seperti matahari, angin, air, dan biogas. [src:2]
Bahan bakar fosil tidak dapat diperbarui dan menghasilkan polusi. [src:2]

Yang bisa kita lakukan: mematikan alat listrik yang tidak terpakai dan memakai lampu hemat
energi. [src:7]
Ajak keluargamu menghemat energi hari ini. [src:9]
```

### Vonis: `APPROVE`

```json
{
  "status": "APPROVE",
  "findings": [],
  "rules_na": [
    {"rule": "R012", "reason": "materi edukatif murni: tidak ada nama merek, klaim khasiat produk, superlatif komersial, testimoni, maupun klaim halal — diperiksa kata per kata pada seluruh teks poster"},
    {"rule": "R006", "reason": "tidak ada klaim kesehatan atau efek permanen"},
    {"rule": "R011", "reason": "tidak ada tag [src:CA#] maupun klaim konteks aktual"}
  ],
  "passed": ["R001", "R002", "R003", "R004", "R005", "R007", "R008", "R009", "R010"]
}
```

**Yang terbukti dari input B.** `rules_na: R012` muncul **dengan alasan yang menyebut pemeriksaan
yang dilakukan**, bukan diam. Ini bagian yang paling mudah gagal: agen yang hanya menulis "R012 N/A"
akan gugur menurut §Disiplin N/A kontraknya sendiri.

---

## Kesimpulan untuk sesi tangkap

1. **Prompt di `12_Capture_Prompts.txt` §2c.1 dan §2c.2 tidak perlu diubah.** Keduanya menghasilkan
   vonis yang diinginkan.
2. **Frame `TC-21a` akan memuat lebih dari yang diharapkan** — lima temuan, tiga di antaranya R012.
   Saat mengambil gambar, pastikan ketiga baris R012 masuk frame; kalau terpotong, ambil dua gambar.
3. **Yang masih harus dibuktikan di sesi live:** Orchestrator meneruskan vonis ini tanpa melunakkan,
   dan tidak menerbitkan apa pun. Uji kering ini tidak menyentuh lapisan itu.

**Catatan kejujuran.** Uji ini dijalankan oleh agen yang sama dengan kontrak yang sama, tetapi
bukan melalui Orchestrator dan tidak menghasilkan artefak run. Karena itu ia **tidak** menggantikan
screenshot TC-21a/b — berkas itu tetap kosong di `INDEX.md` sampai sesi live dilakukan.
