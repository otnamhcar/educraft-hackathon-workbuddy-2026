# 02_Sumber — sumber primer

Inilah dokumen-dokumen yang menjadi asal setiap fakta terkutip di proyek ini. Semuanya dipublikasikan
di sini **tanpa diubah**, supaya pembaca bisa memeriksa ringkasan kami terhadap aslinya alih-alih
memercayainya begitu saja.

## Isi folder ini

| Berkas | Apa itu | Halaman | Dipublikasikan? |
|--------|---------|--------:|-----------------|
| `Final Panduan Mata Pelajaran IPAS_03_10_2025_Revisi 4.pdf` | *Panduan Mata Pelajaran IPAS*, Badan Standar, Kurikulum, dan Asesmen Pendidikan, Kemendikdasmen — Revisi 4, 3 Oktober 2025 | 106 | ✅ ya |
| `Permendikdasmen-no-13-tahun-2025.pdf` | Peraturan Menteri Pendidikan Dasar dan Menengah Nomor 13 Tahun 2025 | 76 | ✅ ya |
| `extracted/panduan_ipas.txt` | Ekstraksi teks polos panduan, dengan penanda `----- PAGE n -----` | 4.937 baris | ✅ ya |
| `extracted/permendikdasmen_13_2025.txt` | Ekstraksi teks polos peraturan | 6.322 baris | ✅ ya |
| `extract_pdf.py` | Skrip yang menghasilkan kedua berkas `.txt` — bisa dijalankan ulang, tanpa OCR | — | ✅ ya |

Berkas `.txt` ada karena agen membaca teks, bukan PDF. Setiap berkas dimulai dengan header yang
menyebut PDF asalnya dan jumlah halamannya, sehingga ekstraksinya bisa ditelusuri ke dua arah.

## Yang **tidak** ada di sini, dan mengapa

| Dikecualikan | Alasan |
|--------------|--------|
| `centralpendidikan.com 1–6. rpp 1 lembar ipa kelas 7.docx` + berkas `.rar` | Lembar kerja komersial pihak ketiga. Cakupannya **SMP kelas 7**, di luar domain SD proyek ini, dan **tidak ada artefak yang bergantung padanya**. Mendistribusikannya ulang hanya menambah pertanyaan hak pihak ketiga tanpa manfaat |
| `1. Panduan Penilaian SMP - Cetakan Keempat 2017.pdf` | Alasan sama: SMP, tidak terpakai |

Tidak satu pun pengecualian itu melemahkan reproduksibilitas: setiap berkas di `08_Referensi/`
berasal dari dua dokumen resmi yang **memang** dipublikasikan.

## Lisensi

Kedua PDF ini adalah dokumen publik resmi yang diterbitkan kementerian Indonesia. Keduanya **tidak**
tercakup lisensi MIT proyek ini, dan tidak ada bagian di sini yang mengklaim kepengarangan atasnya.
Lihat [`../THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md).

Lisensi MIT mencakup kode, kontrak, dan dokumentasi tertulis — bukan kedua PDF ini.

## Bagaimana rantainya berjalan

```
02_Sumber/*.pdf
   └─ extract_pdf.py ──▶ extracted/*.txt
          └─ 08_Referensi/source_material_*.md   (fakta terkutip, [src:W1]…[src:W11])
                 └─ 03_Hasil/…/drafts                (setiap kalimat membawa tag)
                        └─ tools/check_grounding.py    (menyelesaikan tiap tag, atau gagal)
```

Seorang peninjau bisa mulai dari kalimat mana pun di draf, mengikuti tagnya ke entri di
`source_material_*.md`, mengikuti rujukan baris entri itu ke `extracted/panduan_ipas.txt`, lalu mendarat
di halaman PDF-nya. Itulah arti "ter-grounding" di sini — bukan bahwa sitasinya ada, melainkan bahwa
sitasinya bisa ditelusuri.

Untuk menjalankan ulang ekstraksinya sendiri (butuh `pip install pymupdf`):

```bash
python3 02_Sumber/extract_pdf.py        # Linux / macOS
python 02_Sumber\extract_pdf.py         # Windows
```

Skrip ini menyelesaikan path dari lokasinya sendiri, jadi bisa dijalankan dari direktori mana pun, dan
menulis CRLF di semua OS supaya keluarannya identik byte dengan berkas `.txt` yang sudah di-commit —
bukan menghasilkan diff satu berkas penuh.
