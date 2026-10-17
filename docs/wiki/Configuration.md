# Configuration

🌐 **English** · [Dansk](Configuration-da) · [Bahasa Melayu](Configuration-ms)

**People.** `birthdays.csv` has the header `name,email,year,month,day`. The file in the repository holds dummy data. Replace it with your own, and keep real addresses out of git.

**Letters.** `letter_templates/letter_1.txt` to `letter_3.txt`. The text `[NAME]` is replaced by the person's name. One letter is chosen at random.

**Sender.** Two environment variables:

| Variable | Meaning |
| --- | --- |
| `GMAIL_ADDRESS` | Address the e-mail is sent from |
| `GMAIL_TOKEN` | Gmail app password |

`.env.example` shows the names. Never commit a real `.env`; it is ignored by git. The program reads the environment only and never prints the token.

**Constants.** Server, port, subject and file names are in `src/birthday_wisher/constants.py`.
