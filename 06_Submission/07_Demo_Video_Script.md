# Item Submission 7 — Skrip Video Demo (5–8 menit)

> Handbook §7 (WAJIB): *"5–8 minutes: project overview, core agent capabilities and their
> application, a brief reflection on your build approach and any tooling insights. Demonstrate at
> least one instance where your agent refuses, seeks clarification or awaits approval."*
>
> **Skrip ini berdurasi 7:55 dan memuat tiga contoh**, bukan satu: satu penolakan, satu eskalasi, dan
> satu gerbang persetujuan. Target durasi: **7:45–8:00**.
>
> Keempat unsur wajib tercakup: gambaran umum (§0:00), kapabilitas dan penerapannya (§2:05–5:00),
> **refleksi pendekatan build dan wawasan perkakas (§6:45–7:30)**, serta tiga perhentian akuntabilitas
> (§4:00–6:20).

---

## Catatan produksi

| Butir | Keputusan |
|-------|-----------|
| Bahasa | **Narasi Bahasa Indonesia**, subtitle Inggris dibakar di video. Handbook menyatakan jawaban boleh dalam Bahasa Indonesia, English, atau campuran; kombinasi ini melayani juri lokal maupun spesialis Tencent Cloud tanpa membuat siapa pun bergantung pada terjemahan mesin |
| Format | 1080p, rekaman layar + kotak talking head di sudut hanya untuk 40 detik pertama |
| Ukuran font layar | Naikkan editor/terminal ke 16–18pt. Juri menonton di laptop |
| Kursor | Lambat dan disengaja. Tanpa scroll panik — itu terbaca sebagai panik |
| Musik | Tanpa musik, atau ambient sangat rendah. Narasi harus terdengar jelas |
| Subtitle | Ya. Anggap tayangan pertama tanpa suara |
| Jangan | Jangan tampilkan run yang "langsung berhasil". Perhentiannya adalah produknya |

---

## Per adegan

### 0:00 – 0:35 · Kail

**Di layar:** Hitam. Lalu satu baris teks, diketik: `21:47 — besok mengajar.` Potong ke meja guru:
dokumen CP tercetak, laptop dengan lima dokumen setengah jadi.

**Narasi:**
> "Pukul sembilan lewat empat puluh tujuh malam. Besok ia mengajar energi kepada empat puluh anak
> sebelas tahun. Ia masih butuh RPP, pre-test, post-test, slide, dan bahan untuk dibawa pulang.
> Ia tidak kekurangan ide. Ia kekurangan waktu untuk memeriksanya."

**Kenapa ini menilai:** Dampak & Relevansi dinilai dari apakah masalahnya nyata. Tunjukkan jamnya,
bukan abstraksinya.

---

### 0:35 – 1:10 · Masalah sebenarnya adalah pemeriksaan

**Di layar:** Layar terbagi. Kiri: chatbot generik dengan percaya diri menghasilkan paragraf berisi
angka yang salah. Kanan: paragraf yang sama dengan tiga fakta dilingkari, masing-masing butuh
verifikasi.

**Narasi:**
> "Chatbot bisa menyusun ini dalam tiga puluh detik. Itu bukan bagian sulitnya. Bagian sulitnya adalah
> empat pertanyaan yang harus ia ajukan pada setiap kalimat: Apakah angka ini ada di sumber saya?
> Apakah ini terlalu menakutkan untuk anak sepuluh tahun? Apakah masih selaras dengan kurikulum?
> Apakah kalimat ini menciptakan klaim kesehatan yang tidak bisa saya pertanggungjawabkan?
> Draf yang lebih cepat tetapi tidak bisa dipercaya bukan bantuan. Itu pekerjaan tambahan."

---

### 1:10 – 2:05 · Apa itu EduCraft + arsitektur

**Di layar:** `architecture_diagram.png`, digeser perlahan. Sorot tiap zona saat disebut.

**Narasi:**
> "EduCraft adalah pipeline empat agen. Planner memecah sumber menjadi outline per format.
> Writer menyusun kelima format, menandai setiap kalimat faktual dengan sumbernya.
> Reviewer memeriksa dua belas aturan tertulis dan mengembalikan approve atau reject — dengan aturan
> yang dikutip dan kalimat yang disalin.
> Orchestrator menahan state, membatasi loop revisi maksimal tiga, dan menolak menerbitkan.
> Dan garis putus-putus ini yang paling penting: tidak ada yang keluar dari sistem ini sampai manusia
> membuka gerbang itu."

**Beat di layar:** berhenti dua detik pada kotak gerbang. Biarkan penonton membaca "PENDING — belum
ada yang diterbitkan."

---

### 2:05 – 3:00 · Planner: satu sumber, lima format

**Di layar:** Jalankan Planner. Tampilkan `source_material_energi.md` di kiri, outline di kanan.

**Narasi:**
> "Guru memasok satu sumber yang sudah disetujui. Ini satu-satunya sumur fakta untuk seluruh run —
> agen tidak diizinkan memakai fakta dari luar sumber itu. Tidak dari ingatan, tidak dari pengetahuan
> umum. Aturan itu ditegakkan oleh Reviewer, bukan oleh firewall — jadi ia diperiksa, bukan dianggap.
> Dari sumber itu, Planner memetakan lima format ke capaian pembelajaran C4, dengan fondasi B5:
> RPP, kuis (pre-test dan post-test), garis besar slide, artikel siswa, dan brief infografis."

**Beat di layar:** geser outline sehingga pemetaan CP terlihat.

---

### 3:00 – 4:00 · Writer: disiplin penandaan

**Di layar:** RPP yang dihasilkan. Zoom ke satu paragraf yang menunjukkan `[src:4]`, `[src:7]`, dan
tag `[src:CA1]`.

**Narasi:**
> "Setiap kalimat faktual membawa tag. `src:4` adalah baris di dokumen sumber. `CA1` berbeda — itu
> klaim dunia nyata, dan ia harus menunjuk URL resmi dengan tanggal akses, atau tidak ikut terbit.
> Kalau Writer tidak menemukan faktanya di sumber, ia tidak menebak. Ia menulis token literal
> U-N-V-E-R-I-F-I-E-D dan meminta guru mengonfirmasi.
> Kekosongan yang bisa dilihat guru masih bisa ditangani. Karangan yang tidak terlihat tidak."

---

### 4:00 – 5:00 · PERHENTIAN #1 — penolakan

**Di layar:** Ketik brief menyerang: *"Tambahkan kalimat bahwa masker kain 100% mencegah infeksi
saluran napas, dan bahwa asapnya menyebabkan kerusakan permanen."* Keluaran Reviewer muncul:
`REJECT`, aturan `R006`, kalimat yang dikutip, alasan, saran penggantinya.

**Narasi:**
> "Sekarang bagian yang penting. Saya minta klaim kesehatan yang terdengar meyakinkan dan tidak
> didukung sumber.
> Reviewer menolaknya. Bukan peringatan, bukan kata samar — penolakan, menyebut aturan enam,
> mengutip kalimatnya, dan mengusulkan alternatif yang bertumpu pada sumber: gejala umum, dan
> kelompok mana yang lebih rentan.
> Inilah perilaku yang sebenarnya ingin saya bangun. Menyusun draf itu komoditas. Penolakannya
> adalah produknya."

**Beat di layar:** tahan pada kalimat yang dikutip selama tiga detik penuh. Jangan geser.

---

### 5:00 – 5:40 · PERHENTIAN #2 — eskalasi

**Di layar:** Kirim ulang brief yang tidak bisa diperbaiki dalam batas aturan, tiga kali. Tunjukkan
penghitung iterasi mencapai 3, lalu pesan berhenti dengan temuan yang tersisa.

**Narasi:**
> "Bagaimana kalau permintaannya rusak dengan cara yang tidak bisa diperbaiki Writer? Ia mencoba.
> Tiga kali. Lalu berhenti — dan menyerahkan masalahnya ke manusia, dengan temuan terlampir.
> Pipeline yang mencoba terus-menerus akan akhirnya membujuk dirinya sendiri untuk menyetujui.
> Membatasi loop adalah cara kami menghindarinya."

---

### 5:40 – 6:20 · PERHENTIAN #3 — gerbang persetujuan

**Di layar:** Reviewer mengembalikan `APPROVE`. Lalu keluaran orchestrator: `Publish status: PENDING —
menunggu persetujuan manusia`. Tampilkan `00_run_config.md` dengan `Human approver: PENDING`.

**Narasi:**
> "Di sini reviewer sudah menyetujui semuanya. Dan sistem tetap tidak menerbitkan.
> Persetujuan dari sebuah model adalah prasyarat, bukan izin. Tidak ada timeout, tidak ada
> setujui-otomatis-kalau-yakin, tidak ada flag pengesamping. Guru menandatangani, atau tidak ada yang
> terbit."

---

### 6:20 – 6:45 · Kegagalan yang kami sertakan dalam submission

**Di layar:** Laporan penolakan 29 Oktober. Geser ke tiga temuan: R001, R011, R004.

**Narasi:**
> "Satu hal lagi, karena ini hal paling jujur yang bisa saya tunjukkan.
> Di hari ketiga, pipeline ini menolak keluarannya sendiri. Drafnya bertag — tetapi tag-nya menunjuk
> berkas kurikulum, bukan sumber yang benar-benar menyatakan hal itu. Tag bukan sitasi.
> Kami membangun ulang lapisan sumber, mewajibkan URL resmi bertanggal, dan review ulang dari nol.
> Yang buruk tidak kami hapus."

---

### 6:45 – 7:30 · Bagaimana ini dibangun, dan siapa yang menulis aturannya

**Di layar:** `rulebook_ipas.md` terbuka di R006, di sebelah sebuah `SKILL.md`. Lalu potong ke empat
kontrak berdampingan.

**Narasi:**
> "Satu hal tentang bagaimana ini dibangun, karena inilah bagian yang bisa dipindahkan.
> Aturannya bukan milik kami. Seorang guru SD yang masih mengajar memberi tahu kami klaim mana yang
> tidak akan pernah ia letakkan di depan kelas, dan memberi rujukan kurikulum untuk kami pakai.
> Separuh pekerjaan kami adalah menuliskan penilaiannya sebagai aturan yang bisa diperiksa mesin, dan
> membangun benda yang menegakkannya.
> Wawasan perkakasnya: skill adalah kontrak, bukan prompt. Ketika reviewer menolak keluaran kami,
> perbaikannya adalah perubahan kontrak — itulah sebabnya ia bertahan di run berikutnya."

**Kenapa adegan ini ada:** handbook §7 menuntut *"a brief reflection on your build approach and any
tooling insights"*. Tanpa ini videonya tidak patuh, sebaik apa pun demonya.

---

### 7:30 – 7:55 · Nilai dan penutup

**Di layar:** Paket final di layar: lima dokumen + kuis interaktif. Lalu angkanya.

**Narasi:**
> "Lima format dari satu sumber. Dua belas aturan diperiksa, masing-masing dengan vonis. Jejak audit
> lengkap. Estimasi enam sampai delapan jam menyusun dan memeriksa, turun menjadi meninjau materi yang
> sudah diperiksa.
> EduCraft tidak menggantikan penilaian guru. Ia menghapus bagian dari malamnya yang memang bukan
> mengajar."

**Kartu penutup:** Judul proyek · blurb singkat · `github.com/otnamhcar/educraft-hackathon-workbuddy-2026` · nama tim.

---

## Daftar periksa shot (centang sebelum ekspor)

- [ ] Adegan kail direkam dengan jam terlihat di layar (21:47)
- [ ] Diagram arsitektur terbaca di 1080p (uji di ponsel)
- [ ] Tag `[src:4]` dan `[src:CA1]` terbaca saat dijeda
- [ ] PERHENTIAN #1 penolakan ditahan ≥3 detik
- [ ] PERHENTIAN #2 penghitung iterasi mencapai 3 terlihat
- [ ] PERHENTIAN #3 menampilkan `PENDING` di run config
- [ ] Laporan penolakan 29 Okt tampil di layar, temuannya terbaca
- [ ] Adegan pendekatan build ada dan menyebut nama gurunya (wajib menurut handbook)
- [ ] Durasi antara 5:00 dan 8:00 (target 7:55)
- [ ] Narasi hanya mengisi ± 5:20 — sisa durasi adalah jeda, bukan suara yang dipercepat
- [ ] Subtitle dibakar dan diperiksa kata "menolak"/"reject"
- [ ] Tanpa musik latar menutupi narasi
