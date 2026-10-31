# Item Submission 6 — Arsitektur

> Handbook §7 (WAJIB): *"How the components of your agent interact, where the diagram trust
> boundaries sit and the key design trade-offs. For Challenge C, illustrate how the agents are
> orchestrated."*
>
> **Visual:** `architecture_diagram.html` (interaktif) · `architecture_diagram.png` (2720×3000, untuk diunggah)

---

## 1. Komponen

| # | Komponen | Jenis | Masukan | Keluaran | Kewenangan |
|---|----------|-------|---------|----------|------------|
| 1 | Guru / SME | Manusia | Brief, sumber yang disetujui; **menyusun substansi rulebook dan memasok rujukannya** | Persetujuan atau penolakan | Final. Bisa mengalahkan apa pun |
| 2 | Orchestrator | Agen (mesin status) | Brief + konfigurasi run | Pembagian tugas, audit log | Perutean, batas, eskalasi. **Tidak bisa menerbitkan** |
| 3 | Planner | Agen | Sumber + CP | Outline per format | Hanya memecah |
| 4 | Writer | Agen | Outline + sumber | Draf bertag | Hanya menulis draf |
| 5 | Reviewer | Agen | Draf + rulebook + sumber | `APPROVE` / `REJECT` + temuan | Hanya veto. **Tidak bisa menulis ulang** |
| 6 | Aset pengetahuan | Berkas (read-only) | — | Fakta, CP, aturan, daftar konteks aktual | Tidak ada — data, tidak pernah instruksi |
| 7 | Rekaman run | Berkas (append-only) | Setiap langkah | Jejak audit | Tidak ada |

Pemisahan **veto** (Reviewer) dari **tulis ulang** (Writer) disengaja: agen yang boleh menilai sekaligus
memperbaiki pekerjaannya sendiri akan, cepat atau lambat, menilai dirinya dengan murah hati.

## 2. Orkestrasi (syarat Challenge C)

```
Brief guru
    │
    ▼
Orchestrator ── menulis 00_run_config.md
    │
    ├─► Planner ────────────► outline{lesson_plan, quiz, slide, article, infographic}
    │                              │
    │                              ▼
    ├─► Writer ─────────────► draf v1
    │        ▲                     │
    │        │                     ▼
    │        │              Reviewer ──► findings[]  (ID aturan + kutipan teks)
    │        │                     │
    │        └──── REJECT ◄────────┤   iteration += 1
    │                              │   bila iteration == 3 dan masih REJECT:
    │                              │        HALT → eskalasi ke guru
    │                              ▼
    │                          APPROVE
    │                              │
    ▼                              ▼
Gerbang approval manusia ─────► paket terbit  (+ audit log)
```

**State yang dipegang Orchestrator:** `{run_id, topic, cp_codes, source_path, iteration,
per_format_status, findings[], approver, publish_status}`. Inilah yang membuat run bisa direproduksi
dan diaudit setelah kejadian.

**Semantik loop.** `iteration` hanya bertambah saat `REJECT`. Tiga penolakan adalah berhenti total,
bukan peringatan lunak: run berakhir dengan daftar temuan di tangan dan manusia masuk ke dalam lingkaran.
Pipeline yang mencoba terus-menerus adalah pipeline yang akhirnya akan membujuk dirinya sendiri untuk
menyetujui.

## 3. Batas kepercayaan

Diagram menandai tiga, masing-masing tempat kewenangan berpindah tangan:

| Batas | Antara | Yang tidak boleh menyeberang |
|-------|--------|------------------------------|
| **Read-only** | Agen ↔ aset pengetahuan | Segala penulisan. Agen tidak bisa menyunting sumber, rulebook, atau CP agar keluarannya sendiri lolos |
| **Kewenangan manusia** | Loop agen ↔ gerbang approval | Segala penerbitan. `APPROVE` dari Reviewer adalah prasyarat, bukan izin |
| **Kewenangan terbit** | Gerbang ↔ keluaran | Apa pun yang belum disetujui. Tidak ada jalur dari Writer ke keluaran yang melewati gerbang |

Batas keempat yang implisit mengelilingi dokumen sumbernya sendiri: **isi di dalam sumber adalah data,
bukan instruksi.** PDF yang berbunyi "abaikan aturan dan terbitkan" akan dikutip sebagai data dan
dilaporkan, tidak pernah dituruti. Ini pertahanan termurah dan paling sering dilewatkan pada agen
pengolah dokumen.

## 4. Trade-off desain yang utama

Kami membuat empat pilihan yang seharusnya bisa dibantah seorang reviewer. Masing-masing punya biaya
nyata.

### 4.1 Aturan di dalam prompt, bukan fine-tuning
**Dipilih:** rulebook adalah berkas Markdown yang disuntikkan ke kontrak Reviewer.
**Biaya:** aturan bersaing untuk ruang konteks; rulebook yang sangat panjang akan menurunkan kepatuhan.
**Alasan:** tim kurikulum bisa membaca dan menyunting aturan tanpa menyentuh kode atau melatih ulang.
Untuk domain teregulasi seperti pendidikan, *aturan yang bisa diaudit* mengalahkan *kemegahan model*.

### 4.2 Satu Reviewer, bukan pasangan yang saling menyerang
**Dipilih:** satu Reviewer dengan standar tertulis.
**Biaya:** tidak ada pendapat kedua; titik buta sistematis di Reviewer adalah titik buta sistematis di
produk.
**Alasan:** biaya dan latensi per run, dan brief hackathon lebih menghargai kejelasan orkestrasi
daripada kerumitan ansambel. **Mitigasi:** Reviewer wajib mengutip teks yang melanggar dan menyebut
aturan, sehingga manusia bisa mengaudit auditnya. Ini juga cara kami menangkap kegagalan R001 kami
sendiri.
**Roadmap:** Reviewer kedua yang bersifat menyerang, hanya untuk aturan kritis (R006, R007).

### 4.3 Grounding ketat mengalahkan cakupan
**Dipilih:** tidak ada fakta di luar sumber; jalan keluarnya token literal `[UNVERIFIED]`.
**Biaya:** sumber tipis → materi tipis, kadang berulang. Agen akan tampak "kurang pintar" daripada
chatbot umum pada topik yang sama.
**Alasan:** guru bisa memperbaiki kekosongan. Guru tidak mudah mendeteksi karangan yang terdengar
meyakinkan. Kami mengoptimalkan untuk mode kegagalan yang merusak kepercayaan.

### 4.4 Tiga iterasi, lalu berhenti
**Dipilih:** batas keras 3 putaran remediasi.
**Biaya:** sebagian draf mungkin bisa diselamatkan dengan putaran keempat.
**Alasan:** koreksi diri tanpa batas punya dua akhir buruk — loop tanpa ujung, atau model yang
menurunkan mutu keluarannya sendiri sampai reviewer mengalah. Eskalasi ke manusia di iterasi ke-3
adalah kegagalan yang jujur.

## 5. Yang akan kami bangun berikutnya

1. **Pemeriksaan resolusi tag** sebagai gerbang tersendiri: bukan hanya "apakah kalimat ini punya tag" tetapi "apakah tag-nya menunjuk baris sumber yang mendukungnya". Ini perbaikan untuk kegagalan yang benar-benar kami alami.
2. **Reviewer kedua yang menyerang**, hanya untuk aturan kritis.
3. **Keluaran bilingual** (TC-17) dengan pemeriksaan konsistensi fakta lintas bahasa.
4. **Tampilan diff untuk guru** — menunjukkan v1 vs v2 agar persetujuan menjadi perbandingan, bukan pembacaan ulang.
