# Usage

🌐 **English** · [Dansk](Usage-da) · [Bahasa Melayu](Usage-ms)

Print the letters instead of sending them. `--today` pretends it is another day:

```bash
python -m birthday_wisher --dry-run --today 2000-10-17
```

![A dry run](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-birthday-wisher/raw/branch/main/docs/images/dry-run.png)

Send the letters for today's birthdays (needs the [sender settings](Configuration)):

```bash
python -m birthday_wisher
```

| Option | Meaning |
| --- | --- |
| `--dry-run` | Print the e-mails instead of sending them |
| `--today YYYY-MM-DD` | Pretend today is this date |
| `--csv FILE` | Use another birthdays file |
| `--letters FOLDER` | Use another folder of letter templates |

Exit status 0 means success. Status 1 means the setup is wrong (missing file or setting) or a letter could not be sent. A birthday on 29 February is celebrated on 28 February in years that are not leap years.
