# DESIGN.md — EduCraft

> Arah desain untuk halaman yang dilihat publik (situs demo, halaman bukti).
> **Sumbernya bukan selera baru.** Semua nilai di bawah diekstrak dari artefak yang sudah
> dikirim ke guru dan juri: `03_Hasil/edu_output_wujud_zat/06_quiz_interaktif.html`,
> `06_Submission/cover_image.svg`, `06_Submission/architecture_diagram.html`.
> Tujuannya satu: halaman demo harus terlihat seperti produk yang sama dengan paket cetak
> dan kuis yang dibuka juri dari tautan itu.

## Identity

EduCraft adalah alat kerja guru, bukan aplikasi konsumen. Halaman publiknya adalah **halaman
bukti**: yang dinilai juri adalah jejak keputusan agen (aturan mana yang menolak, kalimat mana
yang dikutip, sumber mana yang menopang), bukan kesan modern.

Karena itu identitasnya **kertas dan tinta**, bukan layar dan glow. Latar krem seperti lembar
fotokopi buku pelajaran; indigo sebagai warna tinta judul; teal sebagai tanda "lolos"; amber
sebagai tanda "perlu perhatian".

## Personality

- Tenang. Tidak menjual.
- Menunjukkan, bukan mengklaim. Setiap angka di halaman harus bisa dibuka sumbernya.
- Sedikit kaku, dan itu disengaja: ini dokumen, bukan kampanye.

## Palette

| Peran | Nilai | Alasan |
|-------|-------|--------|
| Latar | `#FFF8F0` | Krem, sama dengan latar kuis dan paket cetak |
| Permukaan | `#FFFFFF` | Kartu bukti harus terbaca sebagai lembar terpisah |
| Tinta | `#1F2937` | Netral gelap, kontras 12,6:1 di atas krem |
| Tinta muda | `#6B7280` | Keterangan; dipakai hanya pada 14px+ dan tetap ≥ 4,5:1 |
| Indigo | `#4338CA` | Judul dan tautan, dari kuis |
| Indigo terang | `#5B6CFF` | Aksen tunggal: garis atas, penanda bagian |
| Teal | `#0F766E` | Status lolos, dari sampul dan diagram |
| Amber | `#B45309` | Status perlu perhatian, dari kuis |
| Garis | `#E5D9C9` | Pemisah, dari kuis |

Inti: dua warna (indigo, teal) + satu aksen (amber). Krem dan tinta netral tidak dihitung.

## Typography

- Teks: `"Segoe UI", "Trebuchet MS", Arial, sans-serif` — **sama persis dengan kuis dan paket
  cetak**. Alasan: guru dan juri membuka halaman ini dari tautan di dokumen yang hurufnya sudah
  ini; mengganti huruf akan membuatnya terasa produk lain.
- Angka dan ID aturan: `"Consolas", "SF Mono", monospace`. Alasan fungsional, bukan estetika:
  `R001` dan `121` harus sejajar saat dibandingkan antar baris.
- Skala: 34 / 22 / 17 / 15 / 13. Tanpa huruf di bawah 13px.

## Mood

Rapi seperti lembar kerja yang sudah diperiksa. Ruang kosong dipakai untuk memisahkan bukti
yang berbeda tingkat, bukan untuk mengisi.

## Dial

Dial: ENERGY 2 / RHYTHM 2 / MOTION 1

- **ENERGY 2** — ada satu titik fokus (galeri penolakan), sisanya melayani.
- **RHYTHM 2** — bagian-bagian berbeda komposisi, tetapi tidak lompat-lompat.
- **MOTION 1** — hanya keadaan hover dan focus. Tidak ada animasi masuk, tidak ada loop.

## Larangan yang mengikat halaman ini

- Tidak ada gradien, glow, atau bayangan lembut. Kedalaman hanya lewat garis 1px.
- Tidak ada ikon dekoratif. Penanda status memakai teks (`LOLOS`, `DITOLAK`), bukan glyph.
- Tidak ada angka tanpa sumber. Angka yang tampil hanya yang bisa dibuka di berkas laporan.
- Tidak ada testimoni, logo mitra, atau foto orang.
- Tidak ada nama guru di halaman ini sampai persetujuan tertulis ada.
