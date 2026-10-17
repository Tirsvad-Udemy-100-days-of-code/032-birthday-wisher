# Architecture

🌐 **English** · [Dansk](Architecture-da) · [Bahasa Melayu](Architecture-ms)

The code follows a small clean architecture. Imports point inward.

| Layer | Folder | Holds |
| --- | --- | --- |
| Domain | `src/birthday_wisher/domain/` | `Person` and the errors |
| Application | `src/birthday_wisher/application/` | The use case `send_birthday_wishes` and the ports (`BirthdayRepository`, `LetterSource`, `MailSender`) |
| Infrastructure | `src/birthday_wisher/infrastructure/` | CSV reader, letter files, SMTP mailer, settings |
| Presentation | `src/birthday_wisher/presentation/` | The command line and the composition root |

The tests mirror the layers: `tests/unit`, `tests/integration`, `tests/e2e`. The course hint of a dictionary keyed by `(month, day)` is `birthdays_by_day`.
