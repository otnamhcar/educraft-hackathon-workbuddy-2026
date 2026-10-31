# Panduan Demo & Pengambilan Testimoni — Agent Asisten Guru (EduCraft)

**Tujuan:** Menjelaskan cara menjalankan sistem di depan guru nyata untuk keperluan submission Tencent Hackathon 2026 (Kategori C — Creator Agent), sekaligus mengambil testimoni guru yang akan menggunakan `edu-orchestrator` di masa depan.

---

## 1. Pertanyaan Kunci: Panggil Orchestrator saja atau Satu-satu?

**Jawabannya: CUKUP PANGGIL `edu-orchestrator`.**

- Guru **hanya berinteraksi dengan satu pintu masuk**: `edu-orchestrator`.
- `edu-planner`, `edu-writer`, `edu-reviewer`, `edu-quiz`, `edu-assessor`, `edu-infographic`, `edu-video` adalah **agent internal** — orchestrator yang mendelegasikan pekerjaan ke mereka di balik layar.
- Guru **tidak perlu** dan **tidak disarankan** memanggil agent-agent tersebut satu per satu. Itu justru menyembunyikan nilai "asisten" (guru ingin kemudahan, bukan mengatur pipeline).

> **Catatan jujur soal mekanisme (untuk tim, bukan guru):**
> Skill di WorkBuddy berbentuk instruksi (SKILL.md), bukan proses terpisah. Saat `edu-orchestrator` dijalankan, agent utama memegang instruksi orchestrator lalu — sesuai Pipeline — **memanggil/me-load skill sub-agent** untuk menjalankan peran masing-masing (plan → draft → review → generate). Dua cara implementasi:
> - **(a) Role-play (saat ini):** agent utama "menjelma" tiap peran bergiliran mengikuti instruksi sub-skill. Berfungsi penuh, sederhana.
> - **(b) Sub-agent nyata:** orchestrator meluncurkan sub-agent terisolasi (via Agent tool) yang masing-masing load skill-nya. Lebih "otentik multi-agent", lebih meyakinkan untuk juri & testimoni.
> Dua-duanya menghasilkan **pengalaman guru yang sama**: hanya lihat orchestrator + gate persetujuan.

---

## 2. Alur Pengalaman Guru (Teacher Journey)

```
[Guru] ──▶ edu-orchestrator (SATU pintu)
                │
                ├─▶ edu-planner      (buat outline)
                ├─▶ edu-writer       (draf artikel/kuis/naskah)
                ├─▶ edu-reviewer     (cek aturan R001–R010)
                │       └─ bila REJECT → kembali ke writer (maks 3x) → escalate
                ├─▶ edu-quiz / edu-infographic / edu-video (generator)
                │
                └─▶ ⛔ GATE PERSETUJUAN GURU (HITL) ◀── Guru melihat & menyetujui
                        │
                        └─▶ Publikasikan ke siswa / tabel nilai
```
Guru **hanya diminta ikut campur di dua titik**: (1) memberi topik/sumber di awal, (2) **menyetujui sebelum dipublikasikan** (akuntabilitas #3: *asks before acting*).

---

## 3. Runbook Demo (langkah demi langkah)

1. **Buka chat baru** di WorkBuddy (agar 8 skill termuat di menu).
2. **Panggil orchestrator**, contoh prompt:
   > "Gunakan edu-orchestrator untuk membuat materi IPAS tentang *sistem organ tubuh manusia* untuk kelas 5: artikel singkat + infografis + pre-test (7 soal) & post-test (20 soal), patuhi rulebook R001–R010."
3. **Orchestrator berjalan** di balik layar (planner→writer→reviewer→generator). Guru menunggu.
4. **Sistem berhenti & minta approval**: guru melihat draf + kunci jawaban + (opsional) `quiz_interaktif.html`. Guru bisa:
   - Setuju → lanjut.
   - Minta revisi → orchestrator perbaiki (loop remediation).
5. **Setelah approval**, hasil diserahkan ke siswa.
6. **Siswa kerjakan pre-test → materi → post-test**.
7. **Guru input jawaban** → orchestrator (`edu-assessor`) mengisi **tabel nilai** + ringkasan ketercapaian per siswa.
8. **`audit_log.md` otomatis tercatat** sebagai bukti akuntabilitas (MUST-HAVE #7).

---

## 4. Mengambil Testimoni Guru (untuk submission)

Agar testimoni **otentik**, guru sungguhan harus mencoba alur di atas (langkah 2–7). Rekomendasi:

- **Rekam layar** sesi demo (screen record) — ini bukti penggunaan nyata.
- **Form singkat testimoni** (isi setelah mencoba):
  1. Apa yang Bapak/Ibu rasakan saat pertama kali memanggil asisten ini?
  2. Apakah kemudahan membuat materi (artikel/infografis/kuis) terbantu? Sebutkan waktu yang dihemat.
  3. Apakah fitur "persetujuan sebelum dipublikasikan" membuat Bapak/Ibu merasa kontrol tetap di tangan guru?
  4. Apakah penjelasan sumber (`[src:#]`) membuat Bapak/Ibu percaya materi tidak asal comot?
  5. Apakah tabel nilai pre/post-test membantu melihat ketercapaian tiap siswa?
  6. Apa yang ingin diperbaiki ke depan?
- **Catat consent** (izin publikasi testimoni untuk lomba).

> Tips: ambil 1–2 guru beda jenjang (SD untuk IPAS, atau SMP untuk IPA) agar testimoni cover Domain Pack berbeda.

---

## 5. Catatan untuk Submission

- **Bukti TC-12/TC-13**: `evidence_demo_karhutla.md` + `audit_log.md` (sudah dibuat, berupa simulasi ber-grounding). Untuk bukti *nyata*, jalankan Runbook di atas di chat baru lalu simpan screenshot/rekaman.
- **Upgrade opsional**: ubah orchestrator ke mode **(b) sub-agent nyata** agar multi-agent-ness terlihat eksplisit di demo.
- **Jangan** suruh guru memanggil agent sub-agent — cukup orchestrator.
