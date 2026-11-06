# Situs demo EduCraft

Halaman statis untuk item submission **#11 Tautan proyek (bonus)**.

**Status: belum dipublikasikan.** Berkas ini ada di disk dan bisa dibuka dengan
`file://`, tetapi belum punya URL publik. Jangan tulis tautannya di formulir sebelum
benar-benar diunggah.

## Isi

| Berkas | Asal | Perubahan |
|--------|------|-----------|
| `index.html` | berkas baru | tidak ada |
| `kuis.html` | `03_Hasil/edu_output_wujud_zat/06_quiz_interaktif.html` | lihat di bawah |
| `infografis.png` | `03_Hasil/edu_output_wujud_zat/03_infografis_wujud_zat.png` | tidak ada, salinan byte-identik |
| `animatik.html` | `03_Hasil/edu_output_wujud_zat/07_video_animatik.html` | tidak ada, salinan byte-identik |

### Satu-satunya penyimpangan dari sumber

`kuis.html` **bukan** salinan persis. Dua hal dihapus, tidak ada yang ditambahkan:

1. Tombol `<button id="key-pre">Kunci (guru)</button>` dan `<button id="key-post">…</button>`.
2. Dua event listener yang membuka kotak kunci saat tombol itu diklik.

Alasannya etik, bukan teknis: halaman ini publik, dan protokol run `-002` menyatakan kunci
jawaban baru boleh diberikan setelah guru menyetujuinya. Membiarkan tombolnya ada berarti
kunci bisa dibuka siapa pun yang mengklik.

Yang **tidak** bisa dihapus: data penilaian di dalam berkas. Kuis ini memeriksa jawaban
sendiri di peramban, jadi kunci benar harus ada di sana. Artinya kunci secara teknis masih
bisa dibaca orang yang membuka kode sumber halaman. `index.html` menyatakan hal ini apa
adanya, tidak menyebut "tanpa kunci jawaban".

### Kenapa infografis berupa PNG, bukan HTML

`03_infografis_wujud_zat.html` menetapkan `html, body { width: 1080px; height: 1350px; }`
dan tidak punya meta viewport. Itu benar untuk poster yang akan diekspor ke PNG, tetapi
salah untuk halaman web: di layar laptop 1280px isinya terpotong, di ponsel tidak terbaca.
Poster tetap bisa dilihat utuh sebagai gambar, jadi yang dipublikasikan PNG-nya.

## Isi halaman

1. **Galeri penolakan.** Lima temuan R001 dari pass 1, lengkap dengan kalimat yang dikutip
   dan alasan penolakannya, lalu hasil pass 2. Sumber: `03_Hasil/edu_output_wujud_zat/05_review.md`.
2. **Tiga artefak** yang bisa dibuka langsung.
3. **Angka yang bisa diperiksa.** Tag grounding 115 dan 121, status 23 kasus uji.
   Sumbernya ditulis di halaman, bukan diketik ulang dari ingatan.

## Yang sengaja tidak ditampilkan

- Run `EDU-ORCH-20261026-001` (Energi Alternatif): disetujui guru 4 Nov 2026 14:49; materi diserahkan dalam format siap pakai, tidak disebarkan ke publik.
- Kunci jawaban sebagai tabel.
- Nama guru, sampai ada persetujuan tertulis untuk mencantumkannya.
- Data siswa apa pun.

## Cara memeriksa sebelum dipublikasikan

```bat
cd 06_Submission\demo_site
python -m http.server 8080
```

Di Linux/macOS sama, hanya `python3` dan garis miring biasa. Tanpa server pun halaman ini terbuka
dengan klik dua kali — server hanya dipakai agar perilakunya sama dengan saat dipublikasikan.

Buka `http://localhost:8080`, lalu klik keempat tautan. Yang harus benar:

- Kuis bisa dijawab dan "Periksa Jawaban" memberi hasil.
- Tombol "Kunci (guru)" **tidak ada** di halaman kuis.
- Infografis terbuka sebagai gambar 1080 x 1350.
- Animatik punya tombol Putar, Sebelumnya, Berikutnya, dan durasinya 04:45.
- Tautan repo di kaki halaman membuka repo yang benar.

## Kalau nanti dipublikasikan

Perbarui tiga tempat sekaligus, jangan hanya satu:

1. `06_Submission/00_SUBMISSION_CHECKLIST.md` baris item 11.
2. `06_Submission/10_Submission_Form_CopyPaste.txt` bagian tautan proyek.
3. `07_Dokumentasi/07_GAP_DAN_REKOMENDASI.md` butir G12.

Lalu buka URL-nya dari perangkat lain, bukan dari mesin yang mengunggah.
