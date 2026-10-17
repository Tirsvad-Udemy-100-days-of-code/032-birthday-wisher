# Penggunaan

🌐 [English](Usage) · [Dansk](Usage-da) · **Bahasa Melayu**

Cetak surat tanpa menghantarnya. `--today` berpura-pura hari ini ialah tarikh lain:

```bash
python -m birthday_wisher --dry-run --today 2000-10-17
```

![Larian percubaan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-birthday-wisher/raw/branch/main/docs/images/dry-run.png)

Hantar surat untuk hari jadi hari ini (memerlukan [tetapan penghantar](Configuration-ms)):

```bash
python -m birthday_wisher
```

| Pilihan | Maksud |
| --- | --- |
| `--dry-run` | Cetak e-mel tanpa menghantarnya |
| `--today YYYY-MM-DD` | Berpura-pura hari ini ialah tarikh ini |
| `--csv FILE` | Guna fail hari jadi lain |
| `--letters FOLDER` | Guna folder templat surat lain |

Status keluar 0 bermaksud berjaya. Status 1 bermaksud persediaan salah (fail atau tetapan tiada) atau satu surat gagal dihantar. Hari jadi pada 29 Februari disambut pada 28 Februari dalam tahun yang bukan tahun lompat.
