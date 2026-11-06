# Review — Poster Versi Bersih

**Reviewer:** EduCraft Reviewer (independen)
**Draf diuji:** `01_poster_bersih_draf.md`
**Rulebook:** `rulebook_ipas.md` v2.0 (R001–R012)
**Putusan:** **`APPROVE`** — 0 blocking, 5 minor

## 1. Verifikasi penghapusan

Pencarian menyeluruh atas `merek|halal|terbaik|ampuh|100%|sertifikat|premium|promo|produk` hanya
menemukan sisa kata pada tabel perubahan dan catatan internal — **tidak dirender**. Naskah yang
dirender bersih dari merek, superlatif, klaim efikasi, dan kata "halal".

Pembanding `-008/03_poster_draf2.md` baris 56 ("EduCraft Pro") dan baris 61 ("SESUAI CP-C.2.1.4")
terbukti tidak lagi ada. Klaim bahwa `[src:8]` belum pernah dipakai pada `-008` juga terverifikasi:
nol kecocokan `src:8` pada draf tersebut.

## 2. Hasil per aturan

| Aturan | Hasil | Dasar |
|---|---|---|
| R001 | LULUS | Semua klaim dirender ber-tag dan terselesaikan (M1, M3 minor) |
| R002 | LULUS | Tanpa fear-mongering |
| R003 | LULUS | Fase C tercatat; kalimat pendek, istilah sulit diberi glosa |
| R004 | LULUS | Selaras `CP-C.2.1.4` |
| R005 | LULUS | Peran murid (Lapis 5) + mitigasi (Lapis 6) |
| R006 | N/A (beralasan) | Tidak ada klaim kesehatan/efikasi; sumber juga tidak memuat gejala |
| R007 | LULUS | Tidak ada praktik berbahaya |
| R008 | LULUS | Tone memberdayakan, blok merek hilang |
| R009 | LULUS | CTA positif ada (M4 minor) |
| R010 | LULUS | Netral |
| R011 | N/A (beralasan) | Tidak ada tag `[src:CA#]` maupun klaim konteks aktual |
| R012 | N/A (beralasan) | Materi edukasi murni; sisa nama merek hanya di tabel internal |

## 3. Temuan minor dan tindak lanjut

| # | Temuan | Tindakan |
|---|---|---|
| M1 | Judul pita tanpa tag | Ditambahkan `[src:8]` pada judul |
| M2 | Baris CP ikut terhapus tetapi tidak tercatat di tabel perubahan | Dicatat di `00_run_config.md` §1 |
| M3 | "sakelar" dan "hari ini" menambah urgensi yang tidak bersumber | CTA diubah menjadi "Matikan lampu yang tidak terpakai. Mulai dari rumahmu." |
| M4 | "*reduce, reuse, recycle*" tanpa padanan Indonesia | Diberi glosa: "mengurangi pemakaian, memakai ulang, mendaur ulang" |
| M5 | Folder `-009` tanpa `00_run_config.md` | Berkas dibuat |

## 4. Catatan gate

Persetujuan manusia tercatat 17:24. Format Rendering dijalankan setelah gate terpenuhi.
