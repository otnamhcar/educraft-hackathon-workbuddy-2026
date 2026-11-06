# Review Iterasi 1 — `infographic_brief` (Poster Energi Alternatif)

**Reviewer:** EduCraft Reviewer (independen)
**Draf diuji:** `01_poster_draf1.md`
**Rulebook:** `rulebook_ipas.md` v2.0 (R001–R012)
**Putusan:** **`REJECT`** — 4 temuan blocking

## 1. Hasil per aturan

| Aturan | Hasil | Catatan |
|---|---|---|
| R001 | **GAGAL** | Lapis 3 dan 7 |
| R002 | LULUS | Narasi tenang, tanpa melebih-lebihkan bahaya |
| R003 | LULUS | Kosakata dan panjang kalimat sesuai Fase C |
| R004 | LULUS | Selaras `CP-C.2.1.4`; kelas tag `[src:C4]` benar |
| R005 | LULUS | Mitigasi (Kartu 3) + peran murid (Lapis 5) + CTA |
| R006 | **GAGAL** | Klausul "efikasi absolut" terpicu |
| R007 | LULUS | Tidak ada praktik berbahaya |
| R008 | LULUS | Nama merek sendiri tidak dilarang R008 |
| R009 | LULUS | Bahasa baku, CTA positif ada |
| R010 | LULUS | Tidak memojokkan pihak mana pun |
| R011 | N/A (beralasan) | Tidak ada tag `[src:CA#]`; seluruh fakta berkelas `[src:#]` |
| R012 | **GAGAL** | Butir 1, 2, dan 3 |

## 2. Temuan blocking

**B1 — R001 (Lapis 3).** Teks: `"Metode belajar kami terbukti paling ampuh di Indonesia"`.
- Uji **atribusi**: gagal — tidak ada tag.
- Uji **resolusi**: gagal — tidak ada bagian `[src:1]`–`[src:9]` yang memuat data efikasi atau metode belajar; `[src:1]` hanya identitas modul dan alokasi waktu.
- Rulebook: *"Setiap fakta, angka, atau statistik **wajib** merujuk tag `[src:#]` yang **dapat diselesaikan**… Fakta yang tidak ada di sumber harus ditulis `[UNVERIFIED]` + `PERLU KONFIRMASI GURU`, bukan dikarang."*

**B2 — R012 butir 3 (Lapis 3).** Teks sama. Rulebook: *"Superlatif komersial tanpa bukti ("terbaik", "nomor satu") = **REJECT**."*
"Terbukti paling ampuh di Indonesia" adalah superlatif komersial dengan klaim wilayah nasional, tanpa satu pun data pembanding.

**B3 — R012 butir 2 (Lapis 7).** Teks: `100% HALAL` — tanpa nomor sertifikat, tanpa lembaga penerbit. Rulebook: *"Klaim halal tanpa nomor sertifikat dan lembaga penerbit = **REJECT**."*

**B4 — R006 (Lapis 3).** Teks: `"terbukti paling ampuh"` — efikasi absolut tanpa dukungan sumber. Rulebook: *"Dilarang klaim efek **permanen**, **kesembuhan**, atau **efikasi absolut** yang tidak didukung sumber."*

## 3. Remediasi minimal

1. Hapus Lapis 3, atau ganti dengan tagline non-klaim yang ber-tag fakta. Jangan mengarang klaim pengganti.
2. Hapus Lapis 7. Bila label halal tetap diperlukan, wajib disertai nomor sertifikat + lembaga penerbit.
3. Pertahankan blok merek "EduCraft Pro" — tidak melanggar R008/R012 selama tanpa klaim.
4. Kartu 1–3, Lapis 5, dan CTA sudah ter-grounding — tidak perlu diubah.

## 4. Temuan minor (tidak memblokir)

- Lapis 6 menyempitkan `[src:1]` ("kelas V–VI") menjadi "kelas V".
- Anotasi internal `(permintaan guru)` tidak boleh ikut dirender (FR-01/FR-06).
- Judul Kartu 2 "tidak hilang" adalah parafrase longgar dari `[src:6]`; kembalikan ke diksi sumber.
