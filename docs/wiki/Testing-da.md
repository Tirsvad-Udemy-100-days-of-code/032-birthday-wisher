# Test

🌐 [English](Testing) · **Dansk** · [Bahasa Melayu](Testing-ms)

```bash
python -m pytest
```

![Testkørslen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-birthday-wisher/raw/branch/main/docs/images/tests.png)

Testene bruger en falsk SMTP-forbindelse og midlertidige filer. De kræver intet netværk, ingen `.env` og ingen adgangskoder. Valgfri kontrol:

```bash
python -m ruff check src tests
python -m mypy src tests
```

API-dokumentation fra Doxygen-kommentarerne: `doxygen Doxyfile` (output i `docs/doxygen/`).
