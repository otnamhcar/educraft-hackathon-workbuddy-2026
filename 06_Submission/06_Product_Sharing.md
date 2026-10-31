# Item Submission 8 — Berbagi Produk

> Handbook §7 (WAJIB): *"Where WorkBuddy added value in your build, plus your key insights
> and learnings."*

---

## 0. Dari mana ini berasal

Ide, rujukan sumber, dan substansi aturannya berasal dari **Pak Arief**, guru IPAS SD yang masih aktif
mengajar. Ia bukan persona di slide: ia orang yang menyebut klaim mana yang tidak akan pernah ia
letakkan di depan kelas, dan yang memasok materi kurikulum yang dipakai pipeline ini.

Peran kami adalah separuh lainnya: mengubah penilaiannya menjadi predikat yang bisa diperiksa mesin,
dan membangun pipeline yang menegakkannya. Semua di bawah ini tentang separuh itu — rekayasanya — dan
hanya masuk akal bila dibaca bersama separuh pertama. **Rulebook yang ditulis engineer adalah dugaan
tentang pedagogi.**

---

## 1. Di mana WorkBuddy menambah nilai

### 1.1 Skill sebagai unit rekayasa
Gagasan paling berguna dalam build ini: **skill adalah kontrak, bukan prompt.** Keempat agen adalah
`SKILL.md` dengan peran yang dinyatakan, masukan yang dinyatakan, pipeline, dan daftar aturan keras
yang tidak boleh dilanggarnya. Itu mengubah sifat pekerjaannya — kami berhenti menyetel paragraf dan
mulai menulis spesifikasi yang bisa dijadikan pegangan untuk menagih agen.

Efek praktisnya: ketika reviewer menolak keluaran kami pada 29 Oktober, perbaikannya adalah
**perubahan kontrak** (tambahkan R011, tuntut URL bertanggal), bukan prompt ulang yang kebetulan
berhasil. Perbaikan itu bertahan di run berikutnya karena dituliskan.

### 1.2 Orkestrasi multi-agen tanpa framework
Tanpa LangChain, tanpa pustaka orkestrasi. Skill Orchestrator *adalah* mesin statusnya: ia memegang
penghitung iterasi, merutekan ke Planner/Writer/Reviewer, dan berhenti di angka tiga. Untuk pipeline
empat agen ini pilihan yang tepat — setiap serah-terima adalah berkas yang bisa dibaca, dan juri bisa
menelusuri seluruh run dengan membuka empat berkas Markdown.

### 1.3 Berkas sebagai state
`00_run_config.md` plus audit log append-only memberi kami reproduksibilitas gratis. Saat kami perlu
menjelaskan *kenapa* draf berubah antara v1 dan v2, jawabannya sudah ada di disk. Tanpa basis data,
tanpa UI tracing, tanpa rekonstruksi dari ingatan.

### 1.4 Isolasi proyek untuk build yang berantakan
Build ini membentang sembilan sesi kerja terpisah selama dua minggu. Mengonsolidasikannya ke satu
folder proyek dengan memori sendiri membuat agen berhenti memperdebatkan ulang keputusan yang sudah
kami ambil — dan, yang lebih penting, artefak yang *ditolak* tetap berada di sebelah yang diterima
alih-alih menghilang ke dalam percakapan lama.

### 1.5 Di mana ia tidak membantu
Jujur saja: konsistensi konteks panjang lintas lima format keluaran masih manual. Agen dengan senang
hati memperbaiki satu fakta di RPP dan meninggalkan fakta yang sama kedaluwarsa di garis besar slide. Kami
menangkapnya dengan `grep` untuk string lama (`145 MWp`), bukan dengan penalaran agen. **Konsistensi
lintas dokumen butuh gerbangnya sendiri; kami belum punya.**

---

## 2. Wawasan kunci

### Wawasan 1 — Grounding punya dua separuh, dan semua orang hanya membangun satu
Atribusi: *apakah kalimat ini membawa sitasi?* Resolusi: *apakah sitasi itu menunjuk sumber yang
benar-benar mengatakan ini?* Versi pertama kami hanya punya atribusi, dan ia lolos review-nya sendiri
sambil tetap salah. Tag bukan sitasi. **Ini pelajaran paling bisa dipindahkan dari build ini**, dan
berlaku untuk setiap demo RAG yang menunjukkan superskrip `[1]` kecil.

### Wawasan 2 — Rulebook adalah artefak produk, bukan dokumentasi
Guru memberi kami aturannya sebagai penilaian, bukan sebagai spesifikasi: *"jangan bilang ke anak bahwa
kerusakan akibat asap itu permanen"*, *"jangan menakut-nakuti mereka agar peduli"*, *"jangan klaim
produk halal tanpa sertifikat"*. Kami menuliskan versi pertama sebagai R001–R008 lalu lanjut bekerja.

Lalu audit log mulai mengutip R009–R011, yang tidak ada di mana pun. Reviewer sedang menegakkan aturan
yang sudah disepakati dalam percakapan tetapi belum pernah ditulis. **Celahnya bukan invensi — celahnya
transkripsi.** Aturan yang hidup di kepala seseorang, atau di dalam chat, tidak bisa diaudit, dan
reviewer yang mengutip aturan yang tidak bisa Anda buka tidak bisa dibedakan dari reviewer yang
mengarangnya.

Menuliskannya secara formal, lengkap dengan predikat dan satu contoh kerja untuk masing-masing, bukan
administrasi. Itu perbedaan antara pagar dan perasaan — dan itu juga yang memungkinkan guru memeriksa
transkripsi penilaiannya sendiri.

### Wawasan 3 — Reviewer tidak boleh bisa memperbaiki
Memisahkan veto dari tulis ulang menjaga reviewer tetap jujur. Begitu reviewer bisa ikut menyunting,
ia mulai menyetujui suntingannya sendiri.

### Wawasan 4 — "Menolak dan mengeskalasi" adalah fitur yang bisa dilihat juri
Tiga puluh detik paling meyakinkan dalam demo mana pun adalah saat agen berhenti. Punya kami berhenti
karena tiga alasan berbeda — sumber tidak ada, pelanggaran aturan, dan menunggu persetujuan — dan
setiap perhentian tercatat. Merancang untuk perhentian, bukan hanya untuk keluaran, itulah yang
membuat benda ini bisa dipercaya.

### Wawasan 5 — Mengungkap kegagalan membuat ceritanya lebih kuat
Kami sempat tergoda hanya mengirim review ulang yang bersih. Menyertakan penolakan, diagnosis, dan
perbaikannya itulah yang mengubah "agen yang menulis RPP" menjadi "agen dengan proses mutu yang
bekerja". Handbook secara eksplisit menghargai ini; yang lebih penting, itu benar.

---

## 3. Yang akan kami sampaikan ke tim berikutnya

1. **Tulis rulebook sebelum prompt.** Kalau Anda tidak bisa menyatakan aturannya dalam kalimat yang mau ditandatangani guru, Anda belum punya produk — Anda punya demo.
2. **Buat reviewer mengutip.** Vonis tanpa baris yang dikutip tidak bisa dibantah.
3. **Beri batas pada loop.** Pilih satu angka, tulis di kontrak, eskalasi saat mencapainya.
4. **Uji keluaran Anda sendiri secara menyerang, sejak awal.** Penolakan kami datang di hari ke-3 dan memakan waktu satu hari. Penolakan yang sama di hari submission akan memakan submission-nya.
5. **Simpan versi yang ditolak.** Itu artefak paling kredibel yang Anda punya.

---

## 4. Catatan perkakas

| Kebutuhan | Yang kami pakai | Catatan |
|-----------|-----------------|---------|
| Kontrak agen | Skill WorkBuddy (`SKILL.md` + `assets/`) | Bisa diberi versi, bisa di-diff, tanpa framework |
| Lapisan pengetahuan | Berkas Markdown dengan disiplin tag | Bisa di-grep; manusia bisa mengauditnya |
| Artefak interaktif | Kuis HTML satu berkas | Tanpa build, terbuka offline |
| Dokumentasi | Markdown → bundel ini | Semuanya teks, semuanya bisa ditinjau |
| Verifikasi | `grep` untuk string kedaluwarsa, rekonsiliasi jumlah berkas | Murah, menangkap kesalahan nyata |
