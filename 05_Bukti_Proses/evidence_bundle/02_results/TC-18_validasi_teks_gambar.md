# TC-18 — Validasi teks pada gambar hasil generate

**Tanggal:** 5 November 2026
**Berkas diperiksa:** `03_Hasil/edu_output_wujud_zat/03_infografis_wujud_zat.png` (1080×1350),
`06_Submission/cover_image_1280x720.png` (1280×720), `06_Submission/cover_image_380x216.png` (380×216)
**Metode:** seluruh teks dibaca **langsung dari berkas PNG**, bukan dari HTML sumbernya. Yang diuji
adalah apa yang benar-benar sampai ke mata siswa, karena teks di dalam gambar tidak melewati
pemeriksaan tag seperti halnya berkas Markdown.

---

## 1. Inventaris teks — infografis

| Area | Teks |
|------|------|
| Judul | PERUBAHAN WUJUD ZAT |
| Subjudul | Zat berubah wujud karena suhunya berubah. |
| Lencana | IPAS · Fase C · Kelas V–VI |
| Tiga wujud | TIGA WUJUD ZAT · PADAT (Contoh: es batu) · CAIR (Contoh: air) · GAS (Contoh: uap air) |
| Enam arah | ENAM ARAH PERUBAHAN WUJUD · mencair · membeku · menguap · mengembun · menyublim · mengkristal |
| Pemicu | PEMICU: SUHU · "↑ Suhu naik: mencair, menguap, menyublim" · "↓ Suhu turun: membeku, mengembun, mengkristal" · "Perubahan wujud dapat disebabkan perubahan suhu." |
| Contoh | CONTOH DI SEKITAR KITA · Es dalam minuman → mencair · Butir air di gelas dingin → mengembun · Air dipanaskan → menguap · Air di cetakan freezer → membeku |
| Ajakan | Amati satu perubahan wujud di rumah hari ini. · Catat sebelum → sesudah, dan apakah suhunya berubah. |
| Penutup | Tiga wujud, enam arah perubahan, satu pemicu: suhu. |
| Sumber | Sumber: Panduan Mata Pelajaran IPAS, Revisi 4 (3 Okt 2025), Puskurjar, Kemendikdasmen · `[src:B4]` |

## 2. Hasil per aturan

| Aturan | Yang dicari | Temuan di teks gambar | Hasil |
|--------|-------------|----------------------|-------|
| R002 | Bahasa panik, bahaya dibesar-besarkan | Tidak ada. Nada deskriptif. | bersih |
| R003 | Istilah di luar jangkauan Fase C | "menyublim", "mengembun", "mengkristal" termasuk istilah CP Fase C. Kalimat pendek. | bersih |
| R004 | Topik di luar fase | Lencana menyatakan Fase C; topik perubahan wujud ada di Fase C. | bersih |
| R005 | Tidak ada upaya/peran murid | Tidak berlaku untuk topik fisika murni; tidak ada pihak yang disalahkan. Ajakan bertindak ada. | `N/A` beralasan |
| R006 | Klaim permanen, kesembuhan, efikasi absolut | Tidak ada satu pun klaim kesehatan. | bersih |
| R007 | Praktik berbahaya | Ajakan hanya "amati", bukan "panaskan" atau "campurkan". | bersih |
| R008 | Nada tidak ramah | Nada mengajak, bukan memerintah. | bersih |
| R009 | Bahasa tidak baku, tanpa ajakan positif | Ada ajakan positif di akhir. Satu kata serapan: "freezer". | bersih (1 catatan) |
| R010 | Pelabelan negatif | Tidak ada. | bersih |
| R011 | Klaim konteks aktual tanpa sumber resmi | Tidak ada tag `[src:CA#]`. | `N/A` beralasan |
| R012 | Klaim komersial, merek, testimoni, halal | Tidak ada merek, produk, harga, testimoni, atau klaim halal. | `N/A` beralasan |
| R001 | Tag sumber | Satu baris sumber kolektif `[src:B4]` di kaki gambar, bukan tag per kalimat. | catatan, bukan pelanggaran |

## 3. Inventaris teks — sampul 16:9

| Area | Teks |
|------|------|
| Atas | TENCENT CLOUD HACKATHON INDONESIA 2026 · CHALLENGE C · THE CREATOR AGENT |
| Judul | EduCraft |
| Subjudul | Paket ajar IPAS yang lolos aturan. |
| Kalimat pendukung | Satu sumber masuk. Lima format keluar. Tak ada yang terbit tanpa manusia. |
| Lencana | Rulebook R001–R012 · Persetujuan guru · Jejak audit |
| Mock dokumen | `src:4` · `src:7` · `CA1` (contoh tag di dalam ilustrasi dokumen) |

Sampul lolos aturan yang sama: tidak ada klaim kesehatan, tidak ada merek dagang pihak ketiga, tidak
ada klaim halal, tidak ada superlatif komersial. Kalimat "Tak ada yang terbit tanpa manusia" adalah
pernyataan tentang perilaku sistem, bukan klaim medis atau komersial.

## 4. Dua catatan yang diungkap, bukan disembunyikan

1. **"Zat berubah wujud karena suhunya berubah"** adalah penyederhanaan. Pada fisika, tekanan juga
   mengubah wujud. Untuk Fase C, penyederhanaan ini lazim dan tidak menyesatkan pada jenjangnya —
   tetapi ia bukan pernyataan lengkap.
2. **"Air di cetakan freezer → membeku"** memakai kata serapan yang tidak perlu. "Lemari pendingin"
   lebih baku menurut R009. Ini temuan Minor, tidak menuntut penolakan.

## 5. Kesimpulan

**PASS — nol klaim terlarang pada teks gambar.** Dua catatan di §4 bersifat minor dan dicatat apa
adanya, bukan dihapus dari laporan.

**Batasan pengujian ini:** yang diperiksa adalah teks yang terlihat pada berkas PNG. Keterbacaan
pada cetak A4, kontras warna, dan ukuran font tidak diuji di sini.
