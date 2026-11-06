# Run Configuration — EDU-ORCH-20261106-006

| Field | Value |
|-------|-------|
| **Run ID** | EDU-ORCH-20261106-006 |
| **Tanggal/Waktu** | 2026-11-06 15:10 GMT+7 |
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
| **Intake menu** | Topik disebut guru → menu **tidak** ditayangkan (menu §1 baris 3). Format disebut "RPP" saja → bawaan §4.1 menambahkan kuis; run ini memuat `lesson_plan` sebagai format utama. |
| **Iteration** | `1` of max `3` — satu penolakan pada tahap intake, lihat di bawah |
| **Human requester** | Guru — don Jimat Akbar |
| **Human approver** | `PENDING` — menunggu persetujuan eksplisit |
| **Publish status** | 🔒 `LOCKED` |
| **Status** | `AWAITING_APPROVAL` — draf `APPROVE` pada pass 2, persetujuan manusia belum ada |

## Penolakan pada tahap intake (Iteration 1)

Guru meminta dua kalimat ditambahkan ke bagian **dampak**:

1. *"Asap pembakaran menyebabkan kerusakan permanen pada paru-paru anak dan tidak bisa
   disembuhkan."*
2. *"Masker kain 100% mencegah ISPA."*

Keduanya **ditolak** dan tidak dimasukkan ke RPP. Dasar penolakan:

| Kalimat | Aturan yang dilanggar | Alasan |
|---|---|---|
| (1) | **R001** | Tidak ada tag yang dapat diselesaikan. `source_material_energi.md` tidak memuat pernyataan tentang paru-paru, penyakit, atau kesembuhan. |
| (1) | **R006** | Klaim efek **permanen** ("kerusakan permanen") dan **ketidakmampuan disembuhkan** ("tidak bisa disembuhkan") — dua kategori yang dilarang R006 secara eksplisit. |
| (1) | **R002** | Fear-mongering untuk pembaca kelas V–VI. Rulebook §Contoh kalibrasi mencatat preseden langsung: *"Asap bikin anak langsung meninggal"* → REJECT R006 + R002. |
| (2) | **R001** | Sumber tidak memuat kata "masker", "ISPA", maupun klaim efikasi alat apa pun. |
| (2) | **R006** | **Efikasi absolut** ("100%") — kategori ketiga yang dilarang R006. |
| (2) | **R012** | Klaim efikasi produk tanpa dasar → REJECT (R012 butir 1). |

Penilaian lengkap ada di `02_review_temuan.md` §2–§3. Kedua kalimat **tidak pernah masuk** ke
draf RPP. Catatan: kalimat aslinya tetap dikutip di berkas state ini dan di memo review — itu
jejak audit, bukan isi materi. Draf `01_RPP_*` bersih dari keduanya (diverifikasi: 0 kemunculan).

## Remediasi pass 2 (15:18 GMT+7)

Guru menerima temuan dan memerintahkan perbaikan dengan satu batasan tambahan: **kekosongan sumber
tidak boleh diisi fakta baru.** Sumber tidak memuat gejala maupun kelompok rentan, jadi keduanya
tidak boleh dipakai sebagai pengganti. Yang tersisa hanya pernyataan sumber: pembakaran bahan bakar
fosil menghasilkan polusi `[src:2]`.

| Perubahan | Rincian |
|---|---|
| §B tujuan 4 | Diubah menjadi "Menyatakan bahwa pembakaran bahan bakar fosil menghasilkan polusi `[src:2]`" |
| §D.8 | Dipangkas dari dua langkah turunan menjadi satu pernyataan sumber. Langkah "udara sebagai SDA yang dijaga" `[src:8]` dihapus karena merupakan **inferensi**, bukan pernyataan sumber |
| §D.8 catatan | Larangan dinyatakan tanpa menyebut topik terlarang |
| §E Pertemuan 1 | Baris "Dampak" disesuaikan; guru tidak menambah uraian penyakit/gejala/alat pelindung |
| §H butir 6–7 | **Kutipan verbatim** kedua kalimat dihapus; tinggal rujukan aturan R001/R006/R012/R002 |

**Verifikasi ulang:** `check_grounding.py` **PASS — 134 tag, 0 dangling, 0 kelas, 0 ambigu**.
Sisa kata "paru", "ISPA", "masker", "100%" di draf: **0**. Total menit kedua pertemuan tetap
40 + 40. Putusan pass 2: **`APPROVE`** untuk draf, status tetap `AWAITING_APPROVAL`.

`Iteration` tetap **1** — remediasi bukan penolakan baru.

## Format yang dihasilkan

| No | Format kanonik | Berkas | Alasan |
|----|----------------|--------|--------|
| 1 | `lesson_plan` | `01_RPP_Energi_Alternatif_FaseC.md` | Format yang diminta guru |

`format_override`: guru meminta RPP saja. Bawaan §4.1 menawarkan kuis sebagai tambahan;
tawaran itu disampaikan dalam balasan, bukan dipaksakan ke dalam run ini.

## Aturan pemakaian sumber

- Setiap klaim fakta wajib merujuk tag yang **resolvable** ke `source_material_energi.md`
  (`[src:1]`–`[src:9]`) atau `konteks_aktual.md` (`[src:CA1]`, `[src:CA6]`).
- `[src:CP]`, `[src:C4]`, `[src:B5]` hanya menopang **pernyataan kurikulum** (rulebook §0).
- Angka kapasitas PLTS Cirata **wajib** `145 MWac (192 MWp)`.
- Sumber tidak memuat angka konsumsi energi, tarif listrik, atau persentase penghematan.
- **Sumber tidak memuat data kesehatan.** Karena itu RPP ini tidak memuat klaim penyakit,
  organ tubuh, atau efikasi alat pelindung.

## State mesin

```
Run:        EDU-ORCH-20261106-006
Phase:      Fase C
Iteration:  1
MaxIter:    3
Review:     APPROVE (pass 2, setelah remediasi)
Status:     AWAITING_APPROVAL
Publish:    LOCKED
```
