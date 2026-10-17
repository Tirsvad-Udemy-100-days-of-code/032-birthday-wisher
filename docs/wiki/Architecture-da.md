# Arkitektur

🌐 [English](Architecture) · **Dansk** · [Bahasa Melayu](Architecture-ms)

Koden følger en lille clean architecture. Imports peger indad.

| Lag | Mappe | Indeholder |
| --- | --- | --- |
| Domæne | `src/birthday_wisher/domain/` | `Person` og fejlene |
| Applikation | `src/birthday_wisher/application/` | Use casen `send_birthday_wishes` og portene (`BirthdayRepository`, `LetterSource`, `MailSender`) |
| Infrastruktur | `src/birthday_wisher/infrastructure/` | CSV-læser, brevfiler, SMTP-afsender, indstillinger |
| Præsentation | `src/birthday_wisher/presentation/` | Kommandolinjen og composition root |

Testene afspejler lagene: `tests/unit`, `tests/integration`, `tests/e2e`. Kursets hint om en ordbog med `(month, day)` som nøgle er `birthdays_by_day`.
