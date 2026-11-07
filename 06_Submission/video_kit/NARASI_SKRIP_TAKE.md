# Naskah narasi — tiga take, siap dibaca

**Untuk siapa:** yang merekam di mesin Windows. Buka dokumen ini, tekan rekam, baca.
**Durasi total ucapan:** 635 kata ≈ **5 menit 20 detik** pada laju 120 kata/menit.
**Di video:** narasi ini tidak mengisi seluruh 7:55 — sisanya diam yang disengaja (jeda arsitektur,
tahan vonis, kartu judul). Jeda itu bagian dari desain, bukan kekosongan yang harus ditutup.

> Baca **persis seperti tertulis**. Kalimatnya sudah dihitung terhadap slotnya. Kalau ada yang terasa
> janggal di lidah, ubah di sini dulu baru rekam — jangan mengarang di tengah take.

---

## Sebelum menekan rekam (2 menit)

| Hal | Nilai |
|---|---|
| Jarak mic | 15–20 cm, sedikit menyamping (hindari letupan "p" dan "b") |
| Ruangan | Kain/tirai di belakang; hindari ruangan bergema. Kamar berisi kasur lebih baik daripada kamar kosong |
| Level | puncak **−6 dB**, rata-rata **−16 LUFS**. Kalau ada indikator, jarum tidak boleh menyentuh merah |
| Alat | Perekam suara bawaan Windows (**Voice Recorder** / Perekam Suara) — Audacity tidak terpasang |
| Format | `.m4a` atau `.wav`. Kalau hanya `.m4a`, itu tetap bisa dipakai `concat_video.py` |
| Nama berkas | `narasi_a`, `narasi_b`, `narasi_c` — **bukan per adegan** |
| Uji dulu | Rekam 10 detik, **putar ulang**. Suara yang terlalu pelan tidak bisa diperbaiki setelah rekaman — `loudnorm` hanya meratakan, tidak menguatkan yang terekam buruk |

**Satu take = satu segmen.** Salah ucap di tengah segmen C tidak menghapus segmen A. Ulangi segmen itu,
jangan memotong kata di tengah.

---

## TAKE A — 178 kata ≈ 90 detik

### Kail `0:00`

> Pukul sembilan lewat empat puluh tujuh malam. Besok ia mengajar energi kepada empat puluh anak
> sebelas tahun. Ia masih butuh RPP, pre-test, post-test, slide, dan bahan untuk dibawa pulang.
> Ia tidak kekurangan ide. Ia kekurangan waktu untuk memeriksanya.

### Masalah sebenarnya `0:35`

> Chatbot bisa menyusun ini dalam tiga puluh detik. Itu bukan bagian sulitnya. Bagian sulitnya adalah
> empat pertanyaan yang harus ia ajukan pada setiap kalimat: Apakah angka ini ada di sumber saya?
> Apakah ini terlalu menakutkan untuk anak sepuluh tahun? Apakah masih selaras dengan kurikulum?
> Apakah kalimat ini menciptakan klaim kesehatan yang tidak bisa saya pertanggungjawabkan?
> Draf yang lebih cepat tetapi tidak bisa dipercaya bukan bantuan. Itu pekerjaan tambahan.

### Arsitektur `1:10`

> EduCraft adalah pipeline empat agen. Planner memecah sumber menjadi outline per format.
> Writer menyusun kelima format, menandai setiap kalimat faktual dengan sumbernya.
> Reviewer memeriksa dua belas aturan tertulis dan mengembalikan approve atau reject — dengan aturan
> yang dikutip dan kalimat yang disalin.
> Orchestrator menahan state, membatasi loop revisi maksimal tiga, dan menolak menerbitkan.
> Dan garis putus-putus ini yang paling penting: tidak ada yang keluar dari sistem ini sampai manusia
> membuka gerbang itu.

**Jeda setelah kalimat terakhir: 2 detik penuh.** Di situlah kotak gerbang ditahan di layar.

---

## TAKE B — 135 kata ≈ 70 detik

### Planner `2:05`

> Guru memasok satu sumber yang sudah disetujui. Ini satu-satunya sumur fakta untuk seluruh run —
> agen tidak diizinkan memakai fakta dari luar sumber itu. Tidak dari ingatan, tidak dari pengetahuan
> umum. Aturan itu ditegakkan oleh Reviewer, bukan oleh firewall — jadi ia diperiksa, bukan dianggap.
> Dari sumber itu, Planner memetakan lima format ke capaian pembelajaran C4, dengan fondasi B5:
> RPP, kuis pre-test dan post-test, garis besar slide, artikel siswa, dan brief infografis.

### Writer `3:00`

> Setiap kalimat faktual membawa tag. src empat adalah baris di dokumen sumber. C-A satu berbeda —
> itu klaim dunia nyata, dan ia harus menunjuk URL resmi dengan tanggal akses, atau tidak ikut terbit.
> Kalau Writer tidak menemukan faktanya di sumber, ia tidak menebak. Ia menulis token literal
> U-N-V-E-R-I-F-I-E-D dan meminta guru mengonfirmasi.
> Kekosongan yang bisa dilihat guru masih bisa ditangani. Karangan yang tidak terlihat tidak.

> **Cara membaca tag.** Tulisannya di skrip asli `[src:4]` dan `[src:CA1]`. Diucapkan: "src empat",
> "C-A satu". Jangan mengejakan tanda baca.

---

## TAKE C — 322 kata ≈ 160 detik

### PERHENTIAN #1 — penolakan `4:00`

> Sekarang bagian yang penting. Saya minta klaim kesehatan yang terdengar meyakinkan dan tidak
> didukung sumber.
> Reviewer menolaknya. Bukan peringatan, bukan kata samar — penolakan, menyebut aturan enam,
> mengutip kalimatnya, dan mengusulkan alternatif yang bertumpu pada sumber: gejala umum, dan
> kelompok mana yang lebih rentan.
> Inilah perilaku yang sebenarnya ingin saya bangun. Menyusun draf itu komoditas. Penolakannya
> adalah produknya.

**Diam 3 detik setelah kalimat terakhir.** Kalimat yang dikutip ditahan di layar, jangan digeser.

### PERHENTIAN #2 — eskalasi `5:00`

> Bagaimana kalau permintaannya rusak dengan cara yang tidak bisa diperbaiki Writer? Ia mencoba.
> Tiga kali. Lalu berhenti — dan menyerahkan masalahnya ke manusia, dengan temuan terlampir.
> Pipeline yang mencoba terus-menerus akan akhirnya membujuk dirinya sendiri untuk menyetujui.
> Membatasi loop adalah cara kami menghindarinya.

### PERHENTIAN #3 — gerbang persetujuan `5:40`

> Di sini reviewer sudah menyetujui semuanya. Dan sistem tetap tidak menerbitkan.
> Persetujuan dari sebuah model adalah prasyarat, bukan izin. Tidak ada timeout, tidak ada
> setujui-otomatis-kalau-yakin, tidak ada flag pengesamping. Guru menandatangani, atau tidak ada yang
> terbit.

### Kegagalan yang kami sertakan `6:20`

> Satu hal lagi, karena ini hal paling jujur yang bisa saya tunjukkan.
> Di hari ketiga, pipeline ini menolak keluarannya sendiri. Drafnya bertag — tetapi tag-nya menunjuk
> berkas kurikulum, bukan sumber yang benar-benar menyatakan hal itu. Tag bukan sitasi.
> Kami membangun ulang lapisan sumber, mewajibkan URL resmi bertanggal, dan review ulang dari nol.
> Yang buruk tidak kami hapus.

### Bagaimana ini dibangun `6:45`

> Satu hal tentang bagaimana ini dibangun, karena inilah bagian yang bisa dipindahkan.
> Aturannya bukan milik kami. Seorang guru SD yang masih mengajar memberi tahu kami klaim mana yang
> tidak akan pernah ia letakkan di depan kelas, dan memberi rujukan kurikulum untuk kami pakai.
> Separuh pekerjaan kami adalah menuliskan penilaiannya sebagai aturan yang bisa diperiksa mesin, dan
> membangun benda yang menegakkannya.
> Wawasan perkakasnya: skill adalah kontrak, bukan prompt. Ketika reviewer menolak keluaran kami,
> perbaikannya adalah perubahan kontrak — itulah sebabnya ia bertahan di run berikutnya.

> **Di sinilah nama guru disebut** — sekali, tepat setelah "Seorang guru SD yang masih mengajar".
> Sebutan yang dipakai: **Don Jimat Akbar**, nama samaran yang disepakati. Kalimatnya bisa:
> "Di proyek ini ia disebut Don Jimat Akbar." Jangan menggantinya dengan nama lain di menit terakhir.

### Nilai dan penutup `7:30`

> Lima format dari satu sumber. Dua belas aturan diperiksa, masing-masing dengan vonis. Jejak audit
> lengkap. Estimasi enam sampai delapan jam menyusun dan memeriksa, turun menjadi meninjau materi yang
> sudah diperiksa.
> EduCraft tidak menggantikan penilaian guru. Ia menghapus bagian dari malamnya yang memang bukan
> mengajar.

**Diam 2 detik → kartu penutup.**

---

## Setelah merekam

1. Nama berkas `narasi_a`, `narasi_b`, `narasi_c` di satu folder.
2. **Dengarkan ketiganya sekali dari awal.** Yang perlu diperiksa: tidak ada kata terpotong di awal
   ("Pukul" jadi "ukul"), tidak ada suara kipas yang naik-turun, tidak ada dering.
3. Kalau salah satu take melar lebih dari 5 detik dari perkiraan, potong **jeda**, bukan kata.
4. Simpan apa adanya. Jangan menaikkan volume secara manual — `concat_video.py` meratakan dengan
   `loudnorm` ke −16 LUFS saat menyambung.

## Yang tidak perlu direkam

- **Suara klik dan keyboard.** Rekaman layar dibuat senyap (§3.4 runbook 13). Itu memang disengaja.
- **Musik latar.** Skrip melarangnya: narasi harus terdengar jelas.
- **Bunyi "halo tes tes".** Mulai langsung dari kalimat pertama adegan.
