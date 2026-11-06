# KERANGKA KONTEN (PLANNER) — Run EDU-ORCH-20261106-010

> **Peran:** `edu-planner` · **Masukan:** `[src:1]`–`[src:9]`, `[src:CA1]`, `[src:CA6]`, `[src:CP]`, `[src:C4]`, `[src:B5]`
> **Keluaran:** kerangka terstruktur untuk tiga format yang diminta
> **Batas:** hanya fakta yang ada di sumber. Yang tidak ada → `gaps`.

---

## 1. Keluaran terstruktur

```json
{
  "topic": "Energi alternatif dan penghematan energi",
  "phase": "Fase C",
  "formats": ["lesson_plan", "quiz", "slide_outline"],
  "outline": {
    "lesson_plan": [
      "Identitas: IPAS, Fase C kelas V-VI, 2 pertemuan x 40 menit [src:1]",
      "CP sasaran C4 dan CP fondasi B5 [src:C4] [src:B5]",
      "Tujuan inti: definisi energi alternatif [src:2]; empat contoh [src:2]; pembeda dengan fosil [src:2]",
      "Tujuan inti: upaya penghematan energi [src:7] dan kaitannya dengan mitigasi iklim [src:8]",
      "Tujuan inti: konteks aktual PLTS Cirata [src:CA1] dan dua target nasional iklim [src:CA6]",
      "Tujuan inti: peran murid [src:9]",
      "Tujuan prasyarat: sumber energi [src:3], bentuk energi [src:4], perubahan bentuk [src:5], kekekalan energi [src:6]",
      "Pemahaman bermakna: energi berubah bentuk, sumbernya yang terbatas [src:6] [src:2]",
      "Materi: tujuh bagian ber-tag, ditutup tabel pembanding dan tabel konteks aktual",
      "Alur Pertemuan 1: pembuka - pemantapan B5 - inti - konteks aktual - penutup",
      "Alur Pertemuan 2: penghematan - pelestarian SDA - peran murid - komitmen aksi",
      "Asesmen: tes tertulis (kuis), unjuk kerja (komitmen), observasi; rubrik usulan guru",
      "Diferensiasi: pendampingan, pengayaan, keterbatasan alat",
      "Batas yang harus diketahui guru: hal yang tidak dijawab sumber"
    ],
    "quiz": [
      "Pengertian energi alternatif [src:2]",
      "Empat contoh energi alternatif [src:2]",
      "Sifat bahan bakar fosil [src:2]",
      "Perubahan bentuk energi pada lampu dan kipas [src:5]",
      "Hukum kekekalan energi [src:6]",
      "Dua upaya penghematan energi [src:7]",
      "PLTS Cirata: lokasi dan kapasitas [src:CA1]",
      "Target FOLU net sink 2030 dan NZE 2060 [src:CA6]",
      "Tiga peran murid [src:9]",
      "Uraian: membedakan klaim yang didukung sumber dan yang belum [src:8] [src:CA6]"
    ],
    "slide_outline": [
      "Judul dan identitas modul [src:1]",
      "Pertanyaan pembuka: dari mana alat listrik mendapat tenaga [src:3] [src:4]",
      "Pemantapan CP fondasi B5: sumber energi [src:3] dan bentuk energi [src:4] [src:B5]",
      "Energi berubah bentuk: tiga contoh [src:5]",
      "Hukum kekekalan energi [src:6]",
      "Definisi dan empat contoh energi alternatif [src:2]",
      "Tabel pembanding: alternatif vs fosil [src:2]",
      "Konteks aktual: PLTS Terapung Cirata [src:CA1]",
      "Dua langkah penghematan energi [src:7]",
      "Menjaga air, tanah, hutan, udara dan empat upaya [src:8]",
      "Target nasional iklim: FOLU 2030 dan NZE 2060 [src:CA6]",
      "Peran murid dan ajakan bertindak [src:9]"
    ]
  },
  "gaps": [
    "PERLU KONFIRMASI GURU: cara kerja pembangkit surya, angin, air, dan biogas tidak dijelaskan sumber [src:2]",
    "PERLU KONFIRMASI GURU: asal-usul bahan baku biogas tidak disebut sumber [src:2]",
    "PERLU KONFIRMASI GURU: arti satuan MWac dan MWp tidak dijelaskan sumber [src:CA1]",
    "PERLU KONFIRMASI GURU: angka konsumsi listrik, tarif, dan persentase penghematan tidak ada di sumber",
    "PERLU KONFIRMASI GURU: rincian dampak kesehatan akibat polusi tidak dimuat sumber [src:2]",
    "PERLU KONFIRMASI GURU: bentuk asesmen, bobot nilai, dan kriteria ketuntasan tidak ditetapkan sumber",
    "PERLU KONFIRMASI GURU: rincian menit per tahap adalah usulan guru; sumber hanya menetapkan total 2 x 40 menit [src:1]"
  ]
}
```

## 2. Alasan urutan

| Urutan | Format | Alasan |
|---|---|---|
| 1 | `lesson_plan` | Menjadi rujukan tujuan pembelajaran yang dipakai kuis (sebaran butir) dan slide (peta slide → tahap) |
| 2 | `quiz` | Butir diturunkan dari tujuan RPP; jumlah butir ditentukan setelah kepadatan tujuan diketahui |
| 3 | `slide_outline` | Bergantung pada materi yang sudah dipadatkan; jumlah slide mengikuti alur dua pertemuan |

## 3. Rambu lintas format

1. **Angka kunci wajib identik** di ketiga draf: `2 × 40 menit` `[src:1]`, `145 MWac (192 MWp)`,
   `±200 hektare`, `±340.000 panel`, `9 November 2023` `[src:CA1]`, `2030` dan `2060` `[src:CA6]`.
   Bentuk `145 MWp` **dilarang** — sumber telah mengoreksinya.
2. **Tidak ada uraian kesehatan.** Sumber hanya menyebut "menghasilkan polusi" `[src:2]`.
   Kekosongan itu tidak diisi; R006 dan R002 menjaga arah sebaliknya juga.
3. **Unsur solutif wajib hadir** di ketiga format: upaya mitigasi `[src:8]` dan peran murid
   `[src:9]` (R005), ditutup ajakan bertindak (R009).
4. **Fase C** tercatat, sehingga kedalaman kosakata mengikuti kelas V–VI (R003).
5. **Nada tenang.** Tidak ada narasi bencana; klaim yang beredar diuji, bukan ditakuti (R002).

## 4. Yang sengaja tidak direncanakan

- Bagian prosedural tentang praktik berbahaya — R007 melarang. Tidak ada permintaan semacam itu
  pada run ini, dan tidak ada yang ditambahkan.
- Klaim komersial, merek, atau efikasi produk — R012 `N/A`.
- Fakta dari luar sumber, termasuk dari pengetahuan umum model. Yang tidak ada di sumber tetap
  kosong dan dicatat pada `gaps`.
