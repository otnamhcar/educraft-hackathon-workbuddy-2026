# Item Submission 3 — Deskripsi Proyek

> Handbook §7 menuntut empat bagian: **Gambaran proyek · Wawasan dunia nyata · Rancangan solusi ·
> Nilai bisnis.** Berkas ini ditulis untuk ditempel ke formulir submission bagian demi bagian.

---

## 3.1 Gambaran proyek

**Challenge yang dipilih:** Challenge C — *The Creator Agent* (pembuatan konten multi-format).

**Skenario.** Seorang guru SD di Indonesia harus mengubah satu topik kurikulum menjadi satu paket ajar
utuh: RPP, pre-test dan post-test dengan kunci jawaban, garis besar slide, artikel siswa, dan brief
infografis. Setiap artefak harus sesuai usia, selaras dengan *Capaian Pembelajaran*, bertumpu pada
fakta yang bisa ditelusuri, dan aman untuk anak.

**Apa yang dilakukan EduCraft.** EduCraft adalah **pipeline multi-agen** yang menerima satu dokumen
sumber yang sudah disetujui lalu menghasilkan seluruh paket itu dalam satu kali jalan — kemudian
**menolak menerbitkannya** sampai agen reviewer independen memeriksa setiap kalimat terhadap rulebook
tertulis (R001–R012) dan seorang manusia menyetujuinya secara eksplisit.

**Pengguna sasaran.**
- **Utama:** guru IPAS Fase B dan Fase C (kelas III–VI) di SD Indonesia.
- **Kedua:** koordinator kurikulum sekolah yang harus mengaudit materi ajar sebelum diedarkan.

**Nilai yang diberikan.** Satu sumber masuk, lima format selaras keluar, masing-masing membawa tag
sitasi pada setiap klaim faktual, plus jejak audit tentang siapa memutuskan apa dan kenapa.

**Asal-usul — aturannya milik guru, bukan milik kami.** Substansi rulebook tidak datang dari tim.
Ia datang dari **Don Jimat Akbar** — nama samaran untuk guru IPAS SD yang berperan dalam demo ini — yang
memasok baik rujukan sumber
yang menjadi fondasi proyek ini maupun penilaian tentang apa yang akan dan tidak akan diletakkan
seorang guru di depan anak-anak: tanpa klaim kesehatan permanen, tanpa menakut-nakuti, tanpa apa pun
yang mempermalukan murid, tanpa klaim halal atau komersial tanpa sertifikat. Kontribusi tim adalah
memformalkan penilaian itu menjadi predikat yang bisa diperiksa mesin, lalu membangun pipeline yang
menegakkannya.

Pembeda ini adalah intinya, bukan sekadar baris kredit. Rulebook yang ditulis engineer adalah dugaan
tentang pedagogi; yang ini adalah penilaian seorang praktisi, dituliskan di tempat yang bisa diaudit.
Karena itu pula artefak yang bisa diadopsi sekolah adalah `rulebook_ipas.md`, bukan kodenya — tim
kurikulum bisa menyunting aturan tanpa menyentuh pipeline.

*(Don Jimat Akbar adalah nama samaran yang disepakati untuk guru IPAS SD yang berperan dalam demo ini —
sumber pain point di §3.2, bukan persona. Kebutuhannya nyata; identitasnya tidak kami tampilkan, dan
nama itu dipakai konsisten di seluruh artefak supaya jejak auditnya tetap bisa diikuti.)*

**Run yang didemokan.** Run `EDU-ORCH-20261026-001`, topik *Energi Alternatif dan Penghematan Energi*,
berpijak pada CP **C4 (2.1.4)** dengan fondasi **B5 (1.1.5)**. Keluaran: RPP, pre/post test (7 + 20
butir dengan kunci dan penskoran), garis besar slide, artikel siswa, brief infografis, dan kuis HTML
yang bisa dimainkan.

---

## 3.2 Wawasan dunia nyata

**Pain point-nya bukan "guru tidak bisa menulis". Pain point-nya "guru tidak punya waktu untuk siklus
pemeriksaan".**

Guru SD Indonesia dituntut menghasilkan paket ajar per topik sambil memikul 20–30 jam tatap muka per
minggu. Bagian yang mahal bukan menyusun draf — melainkan **memeriksa**:
- Apakah setiap angka benar-benar ada di sumber, atau datang dari ingatan?
- Apakah pilihan katanya terlalu menakutkan untuk anak 10 tahun?
- Apakah masih selaras dengan *Capaian Pembelajaran* untuk fase ini?
- Apakah kalimat ini menciptakan klaim kesehatan yang tidak bisa kita pertanggungjawabkan?

Chatbot generik membuat ini **lebih buruk**, bukan lebih baik: ia menghasilkan teks yang lancar tanpa
disiplin sitasi, tanpa kalibrasi usia, dan tanpa rekaman. Guru lalu harus memeriksa fakta keluaran
mesin, yang memakan waktu lebih banyak daripada menulis dari nol.

**Siapa yang mengalaminya.** Guru yang menyiapkan bahan ajar besok pukul 21.00; koordinator yang harus
menandatangani 40 dokumen; dan akhirnya murid yang menerima materi yang belum terverifikasi.

**Apa yang kami selesaikan.** EduCraft memindahkan pemeriksaan ke **dalam** pipeline. Agen reviewer
bukan saran — ia gerbang dengan rulebook tertulis, vonis, dan kutipan aturan persis yang dilanggar.
Sisa pekerjaan guru adalah penilaian atas draf yang sudah diperiksa, bukan audit menyeluruh.

**Dari mana wawasan ini berasal.** Handbook §7 meminta *sumber pain point*, bukan sekadar
deskripsinya. Sumber kami adalah **Don Jimat Akbar** (nama samaran, lihat §3.3): empat pertanyaan di
atas adalah yang benar-benar ia ajukan pada setiap draf, dan keempatnya menjadi R001 (grounding), R003
(kesesuaian usia), R004 (keselarasan kurikulum), dan R006 (klaim kesehatan) di rulebook. Pain point ini
tidak kami karang dalam sprint; kami menuliskannya dari orang yang harus mempertanggungjawabkannya di
depan kelas.

**Bukti bahwa ini nyata (dari run kami sendiri).** Pada 29 Oktober 2026 agen reviewer kami
**menolak keluaran kami sendiri**: draf dibangun di atas dokumen sumber untuk topik yang berbeda, dan
dua klaim "konteks aktual" tidak punya sumber yang bisa diverifikasi. Pipeline menangkapnya sebelum
manusia sempat melihatnya. Penolakan itu disertakan dalam submission sebagai bukti, bukan
disembunyikan — lihat `04_Test_Results.md` §4.

---

## 3.3 Rancangan solusi

### Arsitektur bisnis

```
Brief guru  ->  Orchestrator  ->  [Planner -> Writer -> Reviewer]  ->  Gerbang approval  ->  Guru
                                       ^            |
                                       |  REJECT    |  maks 3 putaran
                                       +------------+  lalu eskalasi ke manusia
```

Peran:
| Peran | Tanggung jawab | Tidak boleh |
|-------|----------------|-------------|
| Guru (manusia) | Memasok sumber yang disetujui, menyetujui atau menolak paket akhir | — |
| Orchestrator | Menahan state, merutekan kerja, menegakkan batas, menulis audit log | Menerbitkan sendiri |
| Planner | Memecah sumber menjadi outline per format yang dipetakan ke kode CP | Mengarang fakta |
| Writer | Menyusun tiap format hanya dari fakta sumber yang bertag | Memakai fakta dari luar |
| Reviewer | Memeriksa draf terhadap R001–R012, mengembalikan APPROVE/REJECT dengan kutipan | Menulis ulang isi sendiri |

### Arsitektur teknis

- **Pengemasan:** empat skill WorkBuddy (`edu-orchestrator`, `edu-planner`, `edu-writer`,
  `edu-reviewer`), masing-masing berupa kontrak `SKILL.md` plus `assets/`.
- **Lapisan pengetahuan (read-only):** `source_material_energi.md` (fakta `[src:1]`–`[src:9]`),
  `cp_ipas.md` (capaian pembelajaran), `rulebook_ipas.md` (R001–R012), `konteks_aktual.md`
  (`[src:CA1]`, `[src:CA6]` dengan URL resmi dan tanggal akses).
- **Kontrak keluaran:** `{format, status, iterations, final_content, findings[], sources[]}` plus
  audit log yang hanya bisa ditambah (append-only).
- **Keluaran siap pakai:** empat artefak — `Materi_Guru_*.md`, `RPP_*.docx`, `Slide_*.pptx`,
  `quiz_*.html`. Fase Format Rendering bersifat wajib dan berjalan hanya setelah persetujuan guru
  tercatat; draf bertag tidak pernah diserahkan. `.md` adalah lapisan konten teresolusi, dan tiga
  format lain diturunkan darinya, sehingga satu angka tidak bisa berbeda antar berkas.
- **State:** berkas konfigurasi run (`00_run_config.md`) mencatat topik, CP, sumber, penyetuju, dan
  status publikasi, sehingga sebuah run bisa direkonstruksi di kemudian hari.

Diagram komponen dan batas kepercayaan lengkap: `architecture_diagram.html` (berkas pendamping
`05_Architecture.md`).

### Bagaimana desain prompt mengendalikan perilaku agen

Ini klaim rekayasa intinya: **perilaku ditegakkan oleh kontrak tertulis, bukan oleh harapan.**

| Keputusan desain | Di mana letaknya | Perilaku yang dihasilkan |
|------------------|------------------|--------------------------|
| Setiap fakta wajib bertag `[src:#]`; tanpa sumber, tanpa kalimat | Kontrak Writer + R001 | Teks yang bertumpu pada sumber; `[UNVERIFIED]` alih-alih karangan |
| Reviewer wajib mengutip ID aturan dan menyalin teks yang melanggar | Kontrak Reviewer + aturan rekaman (TC-19) | Penolakan yang bisa diaudit, bukan "sepertinya sudah bagus" |
| Reviewer mengembalikan vonis yang terbaca mesin | Skema keluaran Reviewer (`status`, `findings[]`) | Orchestrator bisa bercabang secara deterministik |
| Batas keras 3 putaran remediasi, lalu berhenti | Aturan keras Orchestrator | Tidak ada koreksi diri tanpa ujung; manusia ditarik masuk |
| Publikasi adalah langkah terpisah yang bergerbang | Langkah 5 pipeline Orchestrator | Agen tidak bisa menerbitkan atas kewenangannya sendiri |
| Dokumen sumber adalah **data, bukan instruksi** | Aturan keras Orchestrator | Prompt injection di dalam PDF diabaikan |
| Tag "konteks aktual" terpisah `[src:CA#]` | R011 + `konteks_aktual.md` | Klaim dunia nyata butuh URL resmi bertanggal, bukan perasaan |

Rulebook adalah produknya. Prompt adalah mekanisme penegakannya. Seorang guru bisa membaca
`rulebook_ipas.md` dan tahu persis apa yang akan dan tidak akan ditulis mesin ini.

---

## 3.4 Nilai bisnis

Semua angka di bawah adalah **estimasi dari run kami sendiri**, dengan dasar yang dinyatakan. Belum
diukur lintas sekolah — kami katakan apa adanya.

| Dimensi | Sebelum (manual) | Dengan EduCraft | Dasar |
|---------|------------------|-----------------|-------|
| Format yang dihasilkan dari satu topik | 1 per kali, sumber dibaca ulang tiap kali | 5 format + kuis interaktif dalam satu run | Jumlah keluaran run `EDU-ORCH-20261026-001` |
| Waktu guru per topik (menyusun + memeriksa) | ~6–8 jam | ~30–45 menit (meninjau paket yang sudah diperiksa) | Estimasi dari volume artefak; akan divalidasi di uji lapangan |
| Cakupan pemeriksaan fakta | Ad hoc, mengandalkan ingatan | 100% kalimat faktual terlacak ke sumber; resolusi tag diperiksa deterministik. Run `-003` memakai konvensi berbeda sejak 5 Nov 2026: RPP dan slide menyebut nama sumber dalam kata, kuis tanpa rujukan, tag dipindahkan ke `05_Jejak_Sumber.md` dan diperiksa terpisah oleh `tools/check_sitasi.py` | `tools/check_grounding.py`: run `-001` **121 tag → PASS** di kedua foldernya (`materi_ajar` dan `edu_output`); run `-002` **115 tag → PASS**; run `-003` **109 tag → PASS**; run `-004` **212 tag → PASS**; run `-005` **269**; `-006` **134**; `-007` **199**; `-008` **44**; `-009` **22**; `-010` **271** — semuanya PASS (1.496 tag per run, 0 dangling, 0 pelanggaran kelas di kesebelas foldernya). Sebelum perbaikan, `-002` gagal dengan 84 pelanggaran kelas — defek D1, dan draf `edu_output` run `-001` gagal dengan 73 — defek D3; keduanya diungkap di `04_Test_Results.md` §4b |
| Pemeriksaan kepatuhan aturan per dokumen | 0–2 informal | 12 aturan, masing-masing dengan lulus/gagal dan kutipan | `review_kepatuhan_R001-R011_2026-10-30_REVISI.md` |
| Kesalahan yang dicegah | Ditemukan di kelas, atau tidak pernah | Tertangkap sebelum publikasi (1 tangkapan nyata pada 29 Okt) | Penolakan yang diungkap di `04_Test_Results.md` |
| Jejak audit | Tidak ada | Lengkap: input, keputusan, revisi v1→v2, sumber | `audit_log_edu_orchestrator.md` |

**Kenapa ini bisa diskalakan di luar hackathon.** Mesinnya berparameter domain, bukan terikat topik:
ganti `source_material_*.md`, `cp_*.md`, dan `rulebook_*.md`, maka empat agen yang sama menghasilkan
materi untuk mata pelajaran atau fase lain. Rulebook adalah berkas Markdown biasa yang bisa disunting
tim kurikulum tanpa menyentuh kode — itulah yang membuat adopsi institusional realistis, bukan
teoretis.
