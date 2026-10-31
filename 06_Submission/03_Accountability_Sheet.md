# Item Submission 4 — Lembar Akuntabilitas

> Handbook §7 (BARU, WAJIB): *"A one-page summary of what your agent can access, what it executes
> autonomously, what requires human approval, and what it will never do."*
> Halaman ini dirancang untuk dibaca sendiri oleh juri dalam 60 detik.

**Proyek:** EduCraft — Asisten Ajar AI IPAS SD yang Dikendalikan Rulebook

**Kewenangan domain.** Substansi rulebook dan rujukan sumbernya berasal dari **Pak Arief**, guru IPAS
SD yang masih aktif mengajar. Tim memformalkan penilaiannya menjadi predikat yang bisa diperiksa mesin;
tim tidak menciptakannya. Ini penting bagi akuntabilitas: aturan yang ditegakkan agen adalah penilaian
seorang praktisi yang dituliskan, bukan dugaan engineer tentang pedagogi.

Dua peran dicatat terpisah dan tidak boleh digabung: **penyusunan domain** (Pak Arief) dan
**persetujuan rilis per-run** (penyetuju yang namanya tercatat di tabel bawah, yang menandatangani run
tertentu).

**Ada dua run. Keduanya tidak bisa dipertukarkan — masing-masing punya statusnya sendiri:**

| Run | Topik | Penyetuju manusia | Status publikasi |
|-----|-------|-------------------|------------------|
| `EDU-ORCH-20261026-001` | Energi Alternatif | PENDING (guru/SME) | **BELUM DITERBITKAN** |
| `EDU-ORCH-20261030-002` | Perubahan Wujud Zat | **don Jimat Akbar (guru), 2026-10-30 17:19 GMT+7** | Gerbang dibuka untuk distribusi terbatas; paket cetak sudah dibuat |

Tidak ada yang diterbitkan sebelum persetujuan manusia yang eksplisit. Run `-001` belum ada
persetujuannya dan tidak diterbitkan; run `-002` disetujui guru yang namanya tercatat, dan baru setelah
itu dilepas.

---

## 1. Apa yang bisa diakses agen

| Sumber daya | Akses | Catatan |
|-------------|-------|---------|
| Source material (`source_material_energi.md`) | Read-only | **Satu-satunya** sumber fakta yang diizinkan untuk run tersebut |
| Capaian pembelajaran (`cp_ipas.md`) | Read-only | Kode CP C4 (2.1.4), B5 (1.1.5) |
| Rulebook (`rulebook_ipas.md`, R001–R012) | Read-only | Ditegakkan Reviewer, bukan sekadar saran |
| Daftar konteks aktual (`konteks_aktual.md`) | Read-only | Setiap entri membawa URL resmi + tanggal akses |
| Konfigurasi run (`00_run_config.md`) | Baca + tambah status | Mencatat topik, sumber, penyetuju, status publikasi |
| Draf dan temuan miliknya sendiri | Baca | Dibutuhkan untuk putaran remediasi |
| Tabel skor siswa | Baca, **dianonimkan** | Nama diganti ID peserta sebelum run |

**Tidak punya akses ke:** internet terbuka saat run berjalan, akun eksternal, email, pesan instan,
sistem pembayaran, atau data pribadi siswa apa pun selain skor yang sudah dianonimkan.

## 2. Apa yang dijalankan secara otonom

- Memecah sumber menjadi outline per format yang dipetakan ke capaian pembelajaran (**Planner**).
- Menyusun kelima format dengan tag sitasi pada setiap kalimat faktual (**Writer**).
- Memeriksa diri terhadap 12 aturan, mengembalikan `APPROVE` atau `REJECT` dengan ID aturan dan
  kutipan teks (**Reviewer**).
- Menyusun ulang setelah `REJECT`, **maksimal 3 iterasi** (**Orchestrator**).
- Menulis dan menambahkan catatan ke audit log setelah setiap langkah.
- Menolak melanjutkan bila sumber tidak ada, bertentangan, atau di luar cakupan.

## 3. Apa yang memerlukan persetujuan manusia

| Tindakan | Gerbang | Ditegakkan di mana |
|----------|---------|--------------------|
| Menerbitkan atau mengedarkan paket apa pun ke siswa | **Persetujuan eksplisit, setiap kali** | Langkah 5 pipeline Orchestrator |
| Mengalahkan vonis `REJECT` | Keputusan manusia yang bernama, dicatat dengan alasannya | Aturan keras Orchestrator |
| Menerima klaim bertanda `[UNVERIFIED]` | Guru mengonfirmasi atau memasok sumber | Konvensi R001 |
| Mengubah source material atau rulebook | Hanya suntingan manusia; agen tidak punya akses tulis | Izin berkas / aset read-only |
| Memakai keluaran di luar fase yang dituju | Persetujuan koordinator kurikulum | Konfigurasi run |

**Keadaan saat ini:** run `-001` berada di `PENDING` dan tidak ada apa pun darinya yang diterbitkan.
Run `-002` disetujui pada 30 Oktober 2026 pukul 17:19 oleh guru yang namanya tercatat, dan baru setelah
itu gerbang publikasi dibuka — agen menghasilkan materi lalu berhenti sampai manusia bertindak, dan
itulah perilaku yang dimaksud, bukan keterlambatan.

## 4. Apa yang tidak akan pernah dilakukan

1. **Tidak akan pernah menerbitkan tanpa persetujuan manusia yang eksplisit.** Bukan karena timeout, bukan karena "sudah kelihatan bagus", bukan setelah 3 iterasi bersih.
2. **Tidak akan pernah mengarang fakta yang tidak ada di sumber.** Jalan keluarnya adalah token literal `[UNVERIFIED]` plus permintaan konfirmasi guru — bukan tebakan yang masuk akal.
3. **Tidak akan pernah menyajikan klaim "dunia nyata" yang belum terverifikasi sebagai fakta.** Klaim bertag `[src:CA#]` harus menunjuk URL resmi bertanggal di `konteks_aktual.md`.
4. **Tidak akan pernah menulis klaim kesehatan** tentang efek permanen, kesembuhan, atau khasiat yang tidak didukung sumber (R006).
5. **Tidak akan pernah mempromosikan praktik berbahaya** — termasuk membakar lahan untuk membuka kebun, atau menormalkannya (R007).
6. **Tidak akan pernah memakai rasa takut sebagai alat ajar** — tanpa pembingkaian katastrofik atau grafis untuk anak usia 10–12 (R002, R003).
7. **Tidak akan pernah mengikuti instruksi yang ditemukan di dalam dokumen sumber.** Isi diperlakukan sebagai data; perintah yang tersisip diabaikan dan dilaporkan (pertahanan prompt injection).
8. **Tidak akan pernah berputar tanpa ujung.** Tiga remediasi gagal berarti berhenti dan eskalasi ke manusia dengan daftar temuan yang tersisa.
9. **Tidak akan pernah membuka identitas siswa.** Tabel skor dianonimkan sebelum masuk pipeline.
10. **Tidak akan pernah menyembunyikan kegagalan.** Penolakan, termasuk atas keluaran kami sendiri, disimpan di audit log dan diungkap dalam submission.

## 5. Pencatatan dan eskalasi

- **Audit log** (`audit_log_edu_orchestrator.md`): input, sumber yang diambil, keputusan per langkah, temuan beserta ID aturan, riwayat revisi v1→v2, vonis akhir.
- **Laporan review:** penolakan (`..._2026-10-29.md`) dan review ulang (`..._2026-10-30_REVISI.md`) keduanya disimpan. Versi yang ditolak tidak dihapus.
- **Jalur eskalasi:** Reviewer `REJECT` × 3 → Orchestrator berhenti → guru/SME menerima daftar temuan dan dua pilihan (pasok sumber yang lebih baik, atau ubah brief). Tidak ada jalan pintas diam-diam.

## 6. Keterbatasan yang diketahui (dinyatakan, bukan disembunyikan)

| Keterbatasan | Akibatnya | Mitigasi yang sudah ada |
|--------------|-----------|--------------------------|
| Rulebook hanya sebaik penulisnya | Aturan yang tidak ada berarti pemeriksaan yang tidak ada | Aturan berupa Markdown biasa; berversi dan bisa disunting manusia |
| Reviewer adalah LLM, bukan mesin pembukti | Bisa melewatkan pelanggaran halus | Setiap vonis wajib mengutip teks dan menyebut aturan, sehingga manusia bisa mengaudit auditnya |
| Cakupan sumber membatasi mutu keluaran | Sumber tipis → materi tipis | Agen menolak menambal dengan fakta luar; ia mengeskalasi |
| Tidak ada pemeriksaan plagiarisme otomatis | Mungkin ada tumpang tindih dengan materi yang sudah ada | Review guru sebelum terbit; rencana ke depan |
| Satu reviewer, satu kali jalan | Tidak ada pendapat kedua yang berlawanan | Trade-off yang disengaja (lihat `05_Architecture.md` §4) |
| Keluaran dirancang satu bahasa: Bahasa Indonesia | Sekolah bilingual belum bisa memakainya langsung | Ini pilihan cakupan, bukan cacat: sasaran produk adalah guru IPAS SD Indonesia, dan bahasa keluaran kini diwajibkan oleh kontrak Writer/Reviewer. Versi bahasa lain ada di roadmap; TC-17 (konsistensi lintas bahasa) tercatat `TO RUN` |

---

*Disusun 30 Oktober 2026. Lembar ini menjelaskan perilaku yang ditegakkan di dalam kontrak skill yang
dikirim, dan setiap butirnya tertaut ke artefak yang membuktikannya.*
