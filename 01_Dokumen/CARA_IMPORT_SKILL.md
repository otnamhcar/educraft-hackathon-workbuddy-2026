# Memasang skill EduCraft — panduan singkat

Panduan ini untuk siapa pun yang baru meng-*clone* repo ini dan ingin menjalankannya.
Tidak ada compile, tidak ada build. Skill = folder berisi `SKILL.md`.

---

## Cara tercepat (disarankan)

Dari akar folder repo:

```bash
./tools/install_skills.sh
```

Skrip ini menyalin empat folder dari `05_Bukti_Proses/skills_package/` ke direktori skill
WorkBuddy, lalu memverifikasi jumlahnya. Kalau jumlahnya bukan 4, skrip berhenti dengan pesan error.

Lalu **restart WorkBuddy** — daftar skill dibaca saat sesi dibuka, bukan saat file disalin.

Setelah restart, periksa seluruh clone sekaligus:

```bash
./tools/doctor.sh
```

Enam pemeriksaan: python3, kontrak skill, skill terpasang, knowledge layer, checksum rulebook,
dan cek grounding R001 pada kedua run. Keluar dengan kode 0 hanya kalau semuanya lolos.

### Kalau direktori skill Anda berbeda

Beberapa versi WorkBuddy membaca skill dari lokasi lain. Arahkan sendiri:

```bash
WORKBUDDY_SKILLS_DIR=~/.workbuddy/skills ./tools/install_skills.sh
```

Cek lokasi sebenarnya di **Settings → Skills**.

---

## Empat skill yang dipasang

| Skill | Peran |
|-------|-------|
| `edu-orchestrator` | Pintu masuk. Menahan state, merutekan kerja, menegakkan batas 3 iterasi, berhenti di gerbang approval |
| `edu-planner` | Memecah satu topik menjadi outline untuk format yang diminta |
| `edu-writer` | Menulis draf; setiap klaim fakta wajib bertag `[src:#]` |
| `edu-reviewer` | Memutuskan `APPROVE`/`REJECT`, wajib mengutip ID aturan dan kalimat yang melanggar |

Hanya empat. Pembuatan infografis, video, dan kuis interaktif adalah **fase aset di dalam
`edu-writer`**, bukan skill terpisah.

---

## Cara memakainya

Buka chat baru di WorkBuddy, lalu:

```
Gunakan edu-orchestrator untuk membuat paket materi IPAS topik "Perubahan Wujud Zat",
Fase C (kelas V-VI).
Source: 03_Hasil/referensi/source_material_wujud_zat.md
Konteks aktual: 03_Hasil/referensi/konteks_aktual.md
Rulebook: 03_Hasil/referensi/rulebook_ipas.md
Jangan publish. Berhenti di approval gate.
```

Guru hanya memanggil **satu pintu**: `edu-orchestrator`. Jangan memanggil sub-skill satu per satu —
itu menyembunyikan nilai "asisten".

---

## Kalau gagal

| Gejala | Yang diperiksa |
|--------|----------------|
| `install_skills.sh: ... SKILL.md not found` | Anda menjalankan skrip dari folder yang bukan clone lengkap |
| Skill tidak muncul di daftar | Belum restart WorkBuddy; atau `WORKBUDDY_SKILLS_DIR` menunjuk folder yang salah |
| `doctor.sh` gagal di cek 6 | Jalankan `python3 tools/check_grounding.py --run 03_Hasil/materi_ajar --knowledge 03_Hasil/referensi --out /tmp/r.md` dan baca laporannya |
| `HOME is not set` | Lingkungan tanpa `HOME` (mis. cron/container). Set `WORKBUDDY_SKILLS_DIR` eksplisit |

Kalau masih gagal, buka `README.md` → bagian **Troubleshooting**, atau buat issue dengan
menyertakan keluaran lengkap `./tools/doctor.sh`.
