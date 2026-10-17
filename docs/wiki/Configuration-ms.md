# Konfigurasi

🌐 [English](Configuration) · [Dansk](Configuration-da) · **Bahasa Melayu**

**Orang.** `birthdays.csv` mempunyai pengepala `name,email,year,month,day`. Fail dalam repositori mengandungi data rekaan. Gantikan dengan data anda sendiri, dan jauhkan alamat sebenar daripada git.

**Surat.** `letter_templates/letter_1.txt` hingga `letter_3.txt`. Teks `[NAME]` diganti dengan nama orang itu. Satu surat dipilih secara rawak.

**Penghantar.** Dua pemboleh ubah persekitaran:

| Pemboleh ubah | Maksud |
| --- | --- |
| `GMAIL_ADDRESS` | Alamat e-mel dihantar daripadanya |
| `GMAIL_TOKEN` | Kata laluan aplikasi Gmail |

`.env.example` menunjukkan namanya. Jangan sekali-kali komit `.env` sebenar; git mengabaikannya. Program hanya membaca persekitaran dan tidak pernah mencetak token.

**Pemalar.** Pelayan, port, subjek dan nama fail ada dalam `src/birthday_wisher/constants.py`.
