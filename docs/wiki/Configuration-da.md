# Konfiguration

🌐 [English](Configuration) · **Dansk** · [Bahasa Melayu](Configuration-ms)

**Personer.** `birthdays.csv` har overskriften `name,email,year,month,day`. Filen i repositoryet indeholder opdigtede data. Erstat den med dine egne, og hold rigtige adresser ude af git.

**Breve.** `letter_templates/letter_1.txt` til `letter_3.txt`. Teksten `[NAME]` erstattes af personens navn. Ét brev vælges tilfældigt.

**Afsender.** To miljøvariabler:

| Variabel | Betydning |
| --- | --- |
| `GMAIL_ADDRESS` | Adressen, e-mailen sendes fra |
| `GMAIL_TOKEN` | Gmail-app-adgangskode |

`.env.example` viser navnene. Læg aldrig en rigtig `.env` i git; den ignoreres af git. Programmet læser kun miljøet og udskriver aldrig tokenet.

**Konstanter.** Server, port, emne og filnavne står i `src/birthday_wisher/constants.py`.
