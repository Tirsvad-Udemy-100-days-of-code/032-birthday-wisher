# Seni Bina

🌐 [English](Architecture) · [Dansk](Architecture-da) · **Bahasa Melayu**

Kod mengikut seni bina bersih yang kecil. Import menuju ke dalam.

| Lapisan | Folder | Mengandungi |
| --- | --- | --- |
| Domain | `src/birthday_wisher/domain/` | `Person` dan ralat |
| Aplikasi | `src/birthday_wisher/application/` | Kes guna `send_birthday_wishes` dan port (`BirthdayRepository`, `LetterSource`, `MailSender`) |
| Infrastruktur | `src/birthday_wisher/infrastructure/` | Pembaca CSV, fail surat, penghantar SMTP, tetapan |
| Pembentangan | `src/birthday_wisher/presentation/` | Baris arahan dan composition root |

Ujian mencerminkan lapisan: `tests/unit`, `tests/integration`, `tests/e2e`. Petunjuk kursus tentang kamus berkunci `(month, day)` ialah `birthdays_by_day`.
