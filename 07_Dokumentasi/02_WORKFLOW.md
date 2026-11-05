# 02 — Alur kerja (kanonik)

> **Cakupan:** bagaimana sebuah run dieksekusi, dalam urutan apa, siapa menulis berkas apa, dan
> seperti apa bentuk berhenti yang sah. Arsitektur (komponen, batas) ada di `01_ARSITEKTUR.md` —
> tidak diulang di sini.

---

## 1. Satu run dalam satu tabel

| Langkah | Pelaku | Masukan | Artefak yang ditulis (path) | Penjaga sebelum lanjut | Bila gagal |
|---------|--------|---------|------------------------------|------------------------|------------|
| S0 Intake | Orchestrator | brief guru + `intake_menu_ipas.md` | `00_run_config.md` | Berkas sumber ada dan bisa dibaca; kode bab + fase + format + sumber sudah pasti | Berhenti; minta sumber |
| S1 Plan | Planner | sumber + CP | `00_plan.md` | Setiap format terpetakan ke kode CP, atau `PERLU KONFIRMASI GURU` | Tandai celah, lanjut dengan peringatan |
| S2 Draft | Writer | rencana + sumber | `01_artikel.md`, `02_*brief.md`, `03_*storyboard.md`, `04_kuis*.md` | Setiap kalimat faktual membawa tag | Keluarkan `[UNVERIFIED]`, jangan mengarang |
| S3 Ground | Orchestrator | draf + sumber | `grounding_report.md` | 0 tag menggantung, 0 ketidakcocokan kelas | Kembali ke S2 dengan laporan |
| S4 Review | Reviewer | draf + rulebook + sumber | `05_review.md` | Vonis + temuan dengan ID aturan dan teks kutipan | `REJECT` → S2, `iteration += 1` |
| S4b Limit | Orchestrator | penghitung iterasi | entri audit log | `iteration < 3` | Di angka 3 → S6 (eskalasi, jangan terbitkan) |
| S5 Approve | Manusia | seluruh paket | baris persetujuan di `00_run_config.md` | Persetujuan eksplisit, nama + stempel waktu | Tanpa persetujuan → berhenti |
| S6 Release | Orchestrator | paket yang disetujui | paket cetak, kuis HTML, penutupan audit | Persetujuan tercatat sebelum distribusi apa pun | Menolak |
| S6b Format Rendering | Orchestrator | paket yang disetujui + `format_rendering_spec.md` | `RPP_*.docx`, `Slide_*/`, `quiz_*.html` | Checklist verifikasi 10 butir lulus; Source Resolution Map tercatat | Kembali ke S6b; tidak menyerahkan artefak yang gagal verifikasi |

**Status S6b:** ditetapkan 4 Nov 2026 sebagai Stage 6 pada `edu-orchestrator/SKILL.md` (pipeline menjadi
7 langkah). Kontrak operasionalnya `edu-orchestrator/assets/format_rendering_spec.md` — aturan FR-01…FR-08
dan checklist §5. Langkah ini **tidak menggantikan** S0–S6; ia berjalan hanya setelah persetujuan manusia
tercatat, dan mengubah paket yang disetujui menjadi artefak siap pakai.

**Status S0:** sejak 5 Nov 2026, S0 tidak lagi sekadar menerima brief. Bila brief hanya memuat niat
tanpa topik ("bantu saya", "tolong buatkan materi"), Orchestrator **wajib menayangkan menu bab** dari
`edu-orchestrator/assets/intake_menu_ipas.md` secara bertahap: L1 fase → L2 rumpun → L3 bab, maksimal
4 opsi per pertanyaan. Tujuannya menutup kegagalan yang paling sering terjadi di ruang guru: niat sudah
ada, nomor bab tidak diingat. Bab berstatus `PERLU SUMBER` menghentikan S0 sampai guru memasok dokumen —
mengarang bab atau fakta dilarang. Bila topik sudah disebut, menu **tidak** ditayangkan.
Bila format tidak disebut, bawaan yang dipakai adalah **RPP + kuis + slide** dengan urutan produksi
`lesson_plan` → `quiz` → `slide_outline`, dan minimal dua format per run (disetujui 5 Nov 2026;
rincian di `intake_menu_ipas.md` §4.1).

**Status S3:** pemeriksanya sudah ada (`tools/check_grounding.py`); menjadikannya gerbang wajib masih
**GAP** — kontrak orchestrator belum mewajibkannya. Lihat `07_GAP_DAN_REKOMENDASI.md` G1.

---

## 2. State dan transisi

```
S0 ──► S1 ──► S2 ──► S3 ──► S4 ──APPROVE──► S5 ──disetujui──► S6 ──► S6b ──► RELEASED
                    ▲         │
                    └──REJECT─┤
                              └──iteration==3──► S6-ESCALATE (tanpa penerbitan)
```

**S6b hanya boleh dijalankan bila `approved_at` terisi.** Artefak hasil S6b tidak pernah menjadi
masukan bagi S2–S4: format berubah, isi tidak. Bila verifikasi S6b menemukan cacat isi, jalur yang
benar adalah kembali ke S2 dengan iterasi baru — bukan menambal artefak.

| Transisi | Syarat | Dicatat di mana |
|----------|--------|-----------------|
| S2→S3 | draf selesai untuk format yang diminta | audit log §pertukaran agen |
| S3→S2 | ≥1 tag menggantung atau salah kelas | `grounding_report.md` |
| S3→S4 | 0 temuan | audit log |
| S4→S2 | `REJECT` | daftar temuan + kenaikan iterasi |
| S4→S5 | `APPROVE` | vonis JSON |
| S5→S6 | persetujuan manusia yang eksplisit | `approver`, `approved_at` |
| S6→S6b | paket disetujui tersedia dan `format_rendering_spec.md` terbaca | audit log §Format Rendering |
| S6b→RELEASED | checklist 10 butir lulus; 0 tag internal tersisa | tabel verifikasi di audit log |
| S4→S6 | `REJECT` ketiga | entri eskalasi dengan temuan yang belum tertangani |

**State terminal:** `RELEASED` (disetujui dan didistribusikan) dan `ESCALATED` (berhenti dengan
temuan). Tidak ada jalur dari `S4` ke `RELEASED`.

---

## 3. Buku besar artefak

Setiap run memiliki tepat satu folder. Tidak ada yang ditulis di luarnya kecuali audit log.

| Berkas | Penghasil | Tidak boleh diubah setelah? | Kegunaan |
|--------|-----------|-----------------------------|----------|
| `00_run_config.md` | Orchestrator | Tidak (hanya field status) | State of record |
| `00_plan.md` | Planner | Tidak | Ketertelusuran ke CP, celah yang dinyatakan |
| draf `0N_*.md` | Writer | Digantikan, bukan disunting di tempat | Isi yang berversi |
| `05_review.md` | Reviewer | **Ya** — tambahkan pass baru, jangan tulis ulang yang lama | Riwayat vonis |
| `grounding_report.md` | Orchestrator | Ya, per pass | Keluaran cek tag deterministik |
| `audit_log.md` | Orchestrator | Append-only | Siapa memutuskan apa, kapan |
| PDF cetak / PNG / HTML | Writer (fase aset) | Dibuat ulang dari HTML sumber | Deliverable |

**Aturan:** draf yang ditolak tidak pernah dihapus atau ditambal diam-diam. Draf itu digantikan dan
alasannya dicatat. Inilah yang membuat penolakan 29 Oktober bisa dipakai sebagai bukti.

---

## 4. Semantik iterasi

- `iteration` menghitung **penolakan**, bukan draf. `iteration = 1` berarti sudah terjadi satu penolakan.
- Kenaikan terjadi **sekali per vonis `REJECT`**, pada seluruh paket, bukan per format.
- Pada `iteration == 3` run **berhenti**: tidak ada draf keempat, tidak ada "coba sekali lagi". Guru
  menerima temuan yang belum tertangani dan dua pilihan: berikan sumber yang lebih baik, atau ubah brief.
- Alasannya: koreksi diri tanpa batas punya dua akhir — perulangan tak berujung, atau model yang
  menurunkan mutu keluarannya sendiri sampai reviewer menyerah.

**Status:** penghitung ini sekarang **IMPLEMENTED sebagai field** (31 Okt 2026). Kedua run config
membawa baris `Iteration`:

| Run | `iteration` | Arti |
|-----|-------------|------|
| `-001` | `1` | Satu penolakan (29 Okt). Disetujui pada draf v2, 30 Okt. |
| `-002` | `1` | Satu penolakan (Reviewer pass 1, 5 Major). Disetujui pada pass 2. |

**Field vs prosa — konvensi yang pernah menimbulkan kebingungan, jadi dinyatakan sekali di sini.**
Field `iteration` menghitung **penolakan**. Audit log yang ditulis sebelum 31 Okt mencatat
"iterasi terpakai: 2/3" untuk `-002` karena yang dihitung adalah **pass review**. Kedua angka benar
dan menggambarkan peristiwa yang sama: pass 1 `REJECT`, pass 2 `APPROVE` ⇒ satu penolakan, dua pass.
Saat mengutip sebuah run, kutip field-nya dan sebutkan semantiknya.

**Yang masih belum bisa diperiksa mesin:** tidak ada yang menulis ulang field itu secara otomatis.
Field ini baris manual dalam tabel Markdown, jadi run yang lupa memperbaruinya akan melenceng.
Deskripsi yang jujur adalah "tercatat, belum ditegakkan" — `tools/check_grounding.py` hanya mencakup R001.

---

## 5. Protokol persetujuan (apa yang dihitung sebagai bukti)

Sebuah persetujuan sah hanya bila keempatnya ada:

1. **Manusia yang disebut namanya** — bukan "tim", bukan "guru" secara generik.
2. **Stempel waktu** — tanggal dan jam beserta zona waktunya.
3. **Cakupan** — artefak mana saja, dan secara eksplisit apakah kunci jawaban serta keringanan celah CP termasuk.
4. **Pernyataan verbatim** — kalimat persetujuannya, dikutip persis.

Dicatat sebagai, misalnya:

```markdown
- Human approver: <nama>, <peran>
- Approved at: 2026-10-30 17:19 GMT+7
- Scope: seluruh artefak pada run ini, termasuk penempatan topik Fase B di kelas V–VI,
         kuis 27 butir beserta kunci, infografis final
- Statement: "<kalimat persetujuan, dikutip persis>"
```

**Run `-002` memenuhi keempat bagian**, tetapi tidak semuanya di satu berkas. `00_run_config.md` memuat
nama penyetuju ✓, stempel waktu ✓, dan cakupan ✓ lewat baris `Publish status`. Bagian 4 — pernyataan
verbatim — ada di `03_Hasil/edu_output_wujud_zat/audit_log.md` §3.7: **"ok saya setujui"**, dengan
cakupan yang menyebut **kunci jawaban 27 butir** secara eksplisit.

G16 semula ditulis dengan membaca `00_run_config.md` saja, sehingga terlihat 3/4. Setelah audit log run
yang sama diperiksa pada 5 November 2026, celahnya bersifat dokumenter, bukan substantif, dan G16
ditutup. Yang tetap harus disebut jujur: kutipan itu tercatat oleh tim di log run, bukan tangkapan pesan
asli.

Run `-001` disetujui 4 November 2026 pukul 14:49 GMT+7, tercatat di `03_Hasil/edu_output/00_run_config.md`
dan `audit_log.md` §3.7. Sebelum tanggal itu, dokumen mana pun yang menyebutnya disetujui adalah salah;
sesudahnya, dokumen yang masih menulis `PENDING` yang salah.

---

## 6. Eskalasi

| Pemicu | Yang diterima manusia | Yang tidak boleh dilakukan sistem |
|--------|----------------------|-----------------------------------|
| `REJECT` ketiga | Daftar temuan dengan ID aturan dan teks kutipan; dua pilihan (sumber lebih baik, brief diubah) | Menghasilkan draf keempat |
| Sumber tidak ada | Permintaan yang menyebut apa yang kurang | Mengarang sumber yang masuk akal |
| Topik di luar fase | `PERLU KONFIRMASI GURU` pada kerangka | Diam-diam memindahkan jenjang kelas |
| Tag tak terselesaikan | Tag persisnya dan berkas tempat ia gagal diselesaikan | Membuang kalimatnya diam-diam |

---

## 7. Dua run, dua tujuan (jangan dicampur)

| | Run `-001` Energi | Run `-002` Wujud Zat |
|---|---|---|
| Tujuan | Mendemonstrasikan siklus tolak → remediasi → setujui | Mendemonstrasikan paket lengkap yang disetujui dan dicetak |
| Jalur vonis | REJECT (29 Okt) → remediasi → APPROVE (30 Okt) | REJECT (5 major) → remediasi → APPROVE (iterasi 2) |
| Persetujuan manusia | **tidak ada — PENDING** | **ada — 30 Okt 17:19** |
| Penerbitan | tidak ada | gerbang dibuka, paket cetak didistribusikan |
| Dipakai di submission | bukti adanya lingkar perulangan dan pengungkapan kegagalan | bukti gerbang persetujuan dan deliverable nyata |

Pernyataan apa pun tentang "run yang jadi acuan" harus menyebut yang mana. Mencampur keduanya adalah
inkonsistensi paling mudah ditemukan juri (lihat `07_GAP_DAN_REKOMENDASI.md` G2).

---

## 8. Yang tidak boleh pernah terjadi (level alur kerja)

1. Draf mencapai `RELEASED` tanpa persetujuan manusia yang tercatat.
2. Jumlah iterasi di atas 3.
3. Laporan review disunting setelah kejadian, bukan dengan menambahkan pass baru.
4. Artefak yang ditolak dihapus.
5. Status publikasi diubah oleh apa pun selain keputusan manusia.
