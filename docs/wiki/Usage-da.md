# Brug

🌐 [English](Usage) · **Dansk** · [Bahasa Melayu](Usage-ms)

Udskriv brevene i stedet for at sende dem. `--today` lader som om, det er en anden dag:

```bash
python -m birthday_wisher --dry-run --today 2000-10-17
```

![En prøvekørsel](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-birthday-wisher/raw/branch/main/docs/images/dry-run.png)

Send brevene til dagens fødselsdage (kræver [afsenderindstillingerne](Configuration-da)):

```bash
python -m birthday_wisher
```

| Valgmulighed | Betydning |
| --- | --- |
| `--dry-run` | Udskriv e-mailene i stedet for at sende dem |
| `--today YYYY-MM-DD` | Lad som om, det er denne dato |
| `--csv FILE` | Brug en anden fødselsdagsfil |
| `--letters FOLDER` | Brug en anden mappe med brevskabeloner |

Slutstatus 0 betyder succes. Status 1 betyder, at opsætningen er forkert (manglende fil eller indstilling), eller at et brev ikke kunne sendes. En fødselsdag den 29. februar fejres den 28. februar i år, der ikke er skudår.
