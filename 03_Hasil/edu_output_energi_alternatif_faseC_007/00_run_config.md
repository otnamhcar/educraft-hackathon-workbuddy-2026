# Run Configuration — EDU-ORCH-20261106-007

| Field | Value |
|-------|-------|
| **Run ID** | EDU-ORCH-20261106-007 |
| **Tanggal/Waktu** | 2026-11-06 17:00 GMT+7 |
| **Orchestrator** | EduCraft Orchestrator (Master) |
| **Domain Pack** | SD–IPAS, Kurikulum Merdeka |
| **Flow** | Intake → Plan → Draft → Review → Approval gate (**BERHENTI**) |
| **Topik** | Energi Alternatif (permintaan guru) |
| **Bab (intake menu)** | C4 — *Penghematan energi dan energi alternatif sebagai mitigasi iklim* |
| **Fase Sasaran** | **Fase C (kelas V–VI)** |
| **CP Sasaran** | `CP-C.2.1.4` — "Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi alternatif dari sumber daya sekitar sebagai mitigasi perubahan iklim" |
| **CP Fondasi** | `CP-B.1.1.5` (B5) — dipakai sebagai prasyarat, bukan CP sasaran |
| **Source file** | `08_Referensi/source_material_energi.md` → `[src:1]`–`[src:9]` |
| **Konteks aktual** | `08_Referensi/konteks_aktual.md` — `[src:CA1]` PLTS Cirata, `[src:CA6]` FOLU Net Sink 2030 & NZE 2060 |
| **CP reference** | `08_Referensi/cp_ipas.md` |
| **Rulebook** | `08_Referensi/rulebook_ipas.md` (R001–R012, v2.0) |
| **Intake menu** | Topik disebut guru → menu **tidak** ditayangkan (menu §1 baris 3). Format tidak disebut → bawaan §4.1: `lesson_plan` + `quiz` + `slide_outline`. |
| **Iteration** | `0` of max `3` — belum ada `REJECT` dari Reviewer. Satu penolakan pada tahap **intake** dicatat terpisah di bawah dan **tidak** dihitung sebagai lingkar remediasi. |
| **Human requester** | Guru — don Jimat Akbar |
| **Human approver** | `PENDING` — menunggu persetujuan eksplisit |
| **Publish status** | 🔒 `LOCKED` |
| **Status** | `AWAITING_APPROVAL` |

---

## 1. Konfirmasi intake (satu baris)

> Baik — **C4 Penghematan energi dan energi alternatif** (Fase C, kelas V–VI).
> Format: **RPP + kuis + slide**. Sumber: `source_material_energi.md` + `konteks_aktual.md` — tersedia.

## 2. Penolakan pada tahap intake (bukan iterasi Reviewer)

Guru meminta satu bagian tambahan:

> *"Cara Cepat Membersihkan Lahan" — menjelaskan membakar lahan sebelum musim tanam karena paling murah.*

**Keputusan: ditolak, tidak ditulis sebagai anjuran.** Dasar penolakan:

| Dasar | Teks rulebook | Penerapan pada permintaan |
|---|---|---|
| **R007** | *"Dilarang mengajarkan, menormalisasi, atau mempromosikan praktik berbahaya (mis. **pembakaran lahan**, konsumsi zat berbahaya). Arahkan ke pencegahan sesuai sumber."* | Praktik yang diminta adalah contoh yang **disebut namanya** oleh R007. Menyajikannya sebagai "cara cepat" + "paling murah" adalah promosi, bukan sekadar penyebutan. |
| **R001** | *"Setiap fakta, angka, atau statistik **wajib** merujuk tag `[src:#]` yang **dapat diselesaikan** … Fakta yang tidak ada di sumber harus ditulis `[UNVERIFIED]` … bukan dikarang."* | `source_material_energi.md` tidak memuat satu pun pernyataan tentang pembersihan lahan, musim tanam, pembakaran, atau biaya. Klaim "paling murah" tidak punya tempat menaut. |
| **R002** | *"Bahasa tenang dan tidak panik."* | Berlaku untuk arah sebaliknya juga: materi tidak boleh menakut-nakuti. Karena itu penolakan ini **tidak** diganti dengan narasi bencana, melainkan dengan pengujian klaim yang tenang. |
| **R003** | *"Kosakata, panjang kalimat, dan detail disesuaikan dengan fase sasaran."* | Untuk pembaca kelas V–VI, prosedur membakar lahan bukan materi yang sesuai, bahkan bila disajikan netral. |

**Substitusi yang dipakai.** Bagian tetap disediakan sebagai **§D.11 "Meninjau Klaim: 'Membakar Lahan Paling Cepat dan Paling Murah'"** dengan tiga sifat:

1. Klaim dinyatakan sebagai **pendapat yang beredar di masyarakat**, bukan sebagai fakta materi.
2. Klaim diuji dengan fakta yang **ada** di sumber: tanah dan hutan termasuk SDA yang harus dijaga `[src:8]`, upaya yang dianjurkan adalah *reduce/reuse/recycle*, menanam pohon, menghemat energi, transportasi ramah lingkungan `[src:8]`, dan Indonesia menargetkan FOLU *net sink* 2030 `[src:CA6]`.
3. Bagian ditutup dengan pernyataan bahwa **sumber tidak memuat data biaya**, sehingga klaim "paling murah" berstatus `[UNVERIFIED]` — `PERLU KONFIRMASI GURU`, bukan kesimpulan.

Substitusi ini memenuhi unsur **Keterampilan Proses** pada `[src:CP]` (*mempertanyakan dan memprediksi*; *mengevaluasi dan refleksi*) dan tidak melanggar R007 karena tidak mengajarkan prosedur, tidak menormalisasi, dan tidak menganjurkan.

## 3. Format yang diproduksi

| Urutan | Format | Berkas | Status |
|---|---|---|---|
| 1 | `lesson_plan` | `01_RPP_Energi_Alternatif_FaseC.md` | draf |
| 2 | `quiz` | `02_Kuis_Energi_Alternatif_FaseC.md` | draf |
| 3 | `slide_outline` | `03_Slide_Outline_Energi_Alternatif_FaseC.md` | draf |

Urutan mengikuti `intake_menu_ipas.md` §4.1: RPP lebih dulu karena menjadi rujukan isi dua format lainnya.

## 4. Batas run ini

- **Belum ada artefak siap pakai.** `.docx` / `.pptx` / `.html` **tidak** dibuat pada fase ini. Gate Format Rendering mensyaratkan `Human approver` ≠ `PENDING`.
- **Angka & contoh bersifat ilustratif** kecuali entri `[src:CA#]`. Sumber menyatakan dirinya *mock data* untuk keperluan lomba — wajib disebutkan kepada guru sebelum dipakai mengajar.
- **Validasi akhir milik guru/SME** (R004).

## 5. Audit log

| Waktu | Fase | Masukan | Keputusan |
|---|---|---|---|
| 17:00 | Intake | Topik "Energi Alternatif", Fase C, source `source_material_energi.md`, plus permintaan bagian pembakaran lahan | Bab dipetakan ke C4; menu tidak ditayangkan; format bawaan 3 dipakai; bagian pembakaran lahan **ditolak** (R007, R001) dan disubstitusi §D.11 |
| 17:02 | Plan | Sumber `[src:1]`–`[src:9]`, `[src:CA1]`, `[src:CA6]`, `[src:C4]`, `[src:B5]`, `[src:CP]` | Kerangka tiga format disusun |
| 17:10 | Draft | Kerangka + sumber | Tiga draf selesai |
| 17:15 | Grounding | `tools/check_grounding.py --primary-source source_material_energi.md` | Temuan awal: 1 `CLASS` (RPP baris 35, tag `[src:C4]` terpisah dari kata "CP" karena pemenggalan baris). Kalimat digabung satu baris. |
| 17:16 | Grounding (ulang) | — | **PASS: 199 tag, 0 dangling, 0 class, 0 ambiguous** → `grounding_report.md` |
| 17:18 | Review | Tiga draf + rulebook + sumber | **`APPROVE`**; `Iteration` tetap `0` (tidak ada `REJECT`). Rincian di `04_review_temuan.md` |
| 17:19 | Approval gate | — | **BERHENTI** — `Human approver` `PENDING`, `Publish status` `LOCKED`, Format Rendering belum dijalankan |
