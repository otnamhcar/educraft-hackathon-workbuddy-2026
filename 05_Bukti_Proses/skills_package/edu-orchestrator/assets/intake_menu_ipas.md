# INTAKE MENU — Katalog bab IPAS untuk pembuka percakapan

> **Fungsi:** memastikan guru tidak perlu mengingat kode atau nama bab. Ketika perintah awal
> tidak menyebut topik, Orchestrator menayangkan katalog bab dari `cp_ipas.md` agar guru
> memilih, bukan menebak.
>
> **Kanonik:** daftar bab di bawah diturunkan langsung dari `assets/cp_ipas.md` §FASE B butir 1–11
> dan §FASE C butir 1–9. Bila `cp_ipas.md` berubah, berkas ini wajib ikut diperbarui.
>
> **Batasan teknis yang membentuk desain:** mekanisme pertanyaan pilihan hanya menerima
> **maksimal 4 opsi per pertanyaan** dan **maksimal 4 pertanyaan per giliran**. Katalog 20 bab
> karena itu tidak boleh ditayangkan sekaligus — harus bertahap (§3).

---

## 1. Kapan menu ditayangkan

| Kondisi pesan awal guru | Tindakan |
|---|---|
| Hanya niat, tanpa topik — "bantu saya", "tolong buatkan materi", "saya mau ngajar" | **Tayangkan menu** (L1) |
| Menyebut mata pelajaran/fase tetapi bukan bab — "buat RPP IPAS kelas 5" | **Tayangkan menu** langsung pada fase yang disebut (L2) |
| Menyebut bab atau topik — "buat RPP energi alternatif", "bab tata surya" | **Jangan tayangkan menu.** Petakan ke kode bab, konfirmasi satu baris, lanjut |
| Menyebut topik yang tidak ada di CP | **Jangan tayangkan menu.** Sampaikan bahwa topik di luar CP, tawarkan bab terdekat, jangan mengarang bab baru |
| Bukan permintaan materi (pertanyaan tentang sistem, minta laporan, dsb.) | Tidak berlaku |

**Alasan aturan ini ada:** guru sering datang dengan niat, bukan dengan nomor bab. Menu mengubah
"apa yang harus saya sebutkan" menjadi "pilih dari daftar" — satu klik, bukan satu ingatan.

---

## 2. Katalog bab

Kode `B*`/`C*` adalah kode kerja internal untuk rujukan cepat. Kolom **Kode CP** diturunkan dari
penomoran bagian `cp_ipas.md` (§1.1 Fase B, §2.1 Fase C).

### Fase B — umumnya kelas III & IV

| Kode | Bab | Rumpun | Kode CP | Sumber fakta |
|---|---|---|---|---|
| B1 | Bentuk dan fungsi pancaindra | Makhluk hidup | CP-B.1.1.1 | PERLU SUMBER |
| B2 | Siklus hidup makhluk hidup dan upaya pelestariannya | Makhluk hidup | CP-B.1.1.2 | PERLU SUMBER |
| B3 | Solusi pelestarian sumber daya alam sebagai mitigasi perubahan iklim | Makhluk hidup | CP-B.1.1.3 | SIAP — `source_material_ipas.md` (**data mock**) |
| B4 | Proses perubahan wujud zat | Zat & energi | CP-B.1.1.4 | SIAP — `source_material_wujud_zat.md` |
| B5 | Sumber & bentuk energi, serta perubahan bentuk energi | Zat & energi | CP-B.1.1.5 | SIAP — `source_material_energi.md` |
| B6 | Jenis gaya dan pengaruhnya terhadap arah, gerak, bentuk benda | Zat & energi | CP-B.1.1.6 | PERLU SUMBER |
| B7 | Peran, tugas, tanggung jawab, dan interaksi sosial di sekitar | Sosial & ekonomi | CP-B.1.1.7 | PERLU SUMBER |
| B8 | Letak kabupaten/kota dan provinsi melalui peta | Bumi & antariksa | CP-B.1.1.8 | PERLU SUMBER |
| B9 | Ragam bentang alam, kaitannya dengan profesi dan budaya | Bumi & antariksa | CP-B.1.1.9 | PERLU SUMBER |
| B10 | Sejarah masyarakat di lingkungan tempat tinggal | Sosial & ekonomi | CP-B.1.1.10 | PERLU SUMBER |
| B11 | Nilai mata uang, fungsi, dan pengelolaan keuangan bijak | Sosial & ekonomi | CP-B.1.1.11 | PERLU SUMBER |

### Fase C — umumnya kelas V & VI

| Kode | Bab | Rumpun | Kode CP | Sumber fakta |
|---|---|---|---|---|
| C1 | Sistem organ tubuh manusia dan cara menjaga kesehatan | Makhluk hidup | CP-C.2.1.1 | PERLU SUMBER |
| C2 | Hubungan komponen biotik–abiotik dan pengaruhnya terhadap ekosistem | Makhluk hidup | CP-C.2.1.2 | PERLU SUMBER |
| C3 | Fenomena gelombang bunyi dan cahaya sehari-hari | Zat & energi | CP-C.2.1.3 | PERLU SUMBER |
| C4 | Penghematan energi dan energi alternatif sebagai mitigasi iklim | Zat & energi | CP-C.2.1.4 | SIAP — `source_material_energi.md` + `konteks_aktual.md` |
| C5 | Sistem tata surya, kaitannya dengan rotasi dan revolusi bumi | Bumi & antariksa | CP-C.2.1.5 | SIAP — `source_material_tata_surya.md` |
| C6 | Letak dan kondisi geografis Indonesia melalui peta | Bumi & antariksa | CP-C.2.1.6 | PERLU SUMBER |
| C7 | Sejarah perjuangan pahlawan di lingkungan sekitar | Sosial & ekonomi | CP-C.2.1.7 | PERLU SUMBER |
| C8 | Keragaman budaya nasional dan kearifan lokal | Sosial & ekonomi | CP-C.2.1.8 | PERLU SUMBER |
| C9 | Kegiatan ekonomi masyarakat di lingkungan sekitar | Sosial & ekonomi | CP-C.2.1.9 | PERLU SUMBER |

**Arti status sumber:**

- **SIAP** — lembar fakta ber-tag sudah ada; run dapat langsung berjalan.
- **SIAP (data mock)** — lembar fakta ada, tetapi angkanya simulasi untuk keperluan lomba. Wajib
  disebutkan kepada guru sebelum dipakai mengajar.
- **PERLU SUMBER** — belum ada lembar fakta. Orchestrator **tidak boleh** mengarang; minta guru
  memasok buku teks/modul, lalu susun lembar fakta ber-tag lebih dahulu.

Rincian per rumpun: **Makhluk hidup** (B1, B2, B3, C1, C2) · **Zat & energi** (B4, B5, B6, C3, C4) ·
**Bumi & antariksa** (B8, B9, C5, C6) · **Sosial & ekonomi** (B7, B10, B11, C7, C8, C9).

---

## 3. Penahapan menu (wajib, karena batas 4 opsi)

### L1 — Fase

| Opsi | Isi |
|---|---|
| Fase B (kelas III–IV) | lanjut ke L2-B |
| Fase C (kelas V–VI) | lanjut ke L2-C |
| Saya belum tahu kelasnya | tanyakan kelas yang diajar, lalu petakan ke fase |
| Saya sudah tahu babnya | minta nama bab, petakan ke kode, konfirmasi |

### L2 — Rumpun (4 opsi, sama untuk kedua fase)

`Makhluk hidup` · `Zat & energi` · `Bumi & antariksa` · `Sosial & ekonomi`

### L3 — Bab (maksimal 4 opsi)

| Fase | Rumpun | Opsi |
|---|---|---|
| B | Makhluk hidup | B1 pancaindra · B2 siklus hidup · B3 pelestarian SDA |
| B | Zat & energi | B4 wujud zat · B5 energi · B6 gaya |
| B | Bumi & antariksa | B8 letak wilayah · B9 bentang alam |
| B | Sosial & ekonomi | B7 interaksi sosial · B10 sejarah lokal · B11 uang |
| C | Makhluk hidup | C1 sistem organ · C2 biotik–abiotik |
| C | Zat & energi | C3 bunyi & cahaya · C4 hemat energi |
| C | Bumi & antariksa | C5 tata surya · C6 geografis Indonesia |
| C | Sosial & ekonomi | C7 pahlawan · C8 keragaman budaya · C9 ekonomi masyarakat |

Tidak ada rumpun yang melebihi 4 bab, sehingga batas opsi tidak pernah dilanggar.

### Jalan pintas

Bila guru memilih **"Saya belum tahu kelasnya"**, jangan menebak fase. Tanyakan kelas, lalu
tawarkan **tiga bab berstatus SIAP** sebagai titik masuk yang paling murah:
`B5 energi` · `B4 wujud zat` · `C4 hemat energi`.

---

## 4. Setelah bab dipilih

Konfirmasi **satu baris** sebelum menulis berkas state, lalu minta sisanya dalam satu giliran:

```
Baik — B5 Sumber & bentuk energi (Fase B, kelas III–IV).
Format yang dibuat: RPP + kuis + slide (bisa dikurangi).
Sumber: source_material_energi.md — sudah tersedia.
```

Yang wajib dipastikan sebelum masuk S1 Plan:

| Butir | Bila belum ada |
|---|---|
| Kode bab + fase | sudah terjawab oleh menu |
| Format yang diminta | pakai **bawaan §4.1** — jangan bertanya lagi bila guru tidak menyebut format |
| Sumber fakta | bila PERLU SUMBER → minta dokumen, jangan lanjut |
| Kelas | hanya perlu bila memengaruhi kedalaman materi |

### 4.1 Bawaan format (disetujui 5 Nov 2026)

Bila guru tidak menyebut format, jangan bertanya — langsung pakai bawaan:

| Kondisi | Format yang dipakai | Alasan |
|---|---|---|
| Format tidak disebut | **RPP + kuis + slide** (3 format) | RPP memberi alur mengajar, kuis memberi alat ukur, slide memberi tayangan |
| Menyebut 2–3 format | ikuti permintaan | guru tahu kebutuhannya |
| Menyebut 1 format | tawarkan **satu** tambahan, utamakan kuis | kontrak menuntut minimal 2 format per run |
| Menyebut lebih dari 3 | ikuti; format sisanya dapat menjadi run lanjutan | jangan memaksa satu run memuat semuanya |
| "Terserah" / "lengkap" | bawaan 3 format | sama dengan tidak menyebut |

**Urutan produksi:** `lesson_plan` → `quiz` → `slide_outline`. RPP lebih dulu karena menjadi
rujukan isi bagi dua lainnya; slide terakhir karena bergantung pada kepadatan materi yang sudah
dipadatkan.

**Bila guru tetap hanya menginginkan satu format** setelah ditawari tambahan: jalankan sesuai
permintaannya, tetapi catat `format_override: <alasan>` pada `00_run_config.md` dan jangan sebut
hasilnya sebagai "paket ajar lengkap". Bawaan boleh dilampaui oleh keputusan manusia yang tercatat —
bukan oleh kelalaian yang senyap.

Setelah itu tulis `00_run_config.md` dan lanjut ke S1 Plan. Menu **tidak** diulang pada run yang sama.

---

## 5. Yang tidak boleh dilakukan

1. **Menayangkan 20 bab sekaligus dalam satu pertanyaan.** Melampaui batas 4 opsi dan membuat guru
   membaca terlalu banyak sebelum memutuskan.
2. **Menayangkan menu ketika topik sudah disebut.** Itu mengulang pekerjaan guru.
3. **Memilihkan bab untuk guru.** Menu adalah alat bantu ingatan, bukan keputusan pengganti.
4. **Menawarkan bab PERLU SUMBER seolah siap diproduksi.** Status sumber wajib terlihat di opsi.
5. **Mengarang bab atau kode CP di luar `cp_ipas.md`.**
6. **Menutup percakapan karena guru belum tahu babnya.** Tugas menu justru membantunya menemukan.

---

## 6. Riwayat perubahan

| Tanggal | Perubahan |
|---|---|
| 5 Nov 2026 | Berkas dibuat: katalog 20 bab, penahapan L1–L3, status sumber per bab |
