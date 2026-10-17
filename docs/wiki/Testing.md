# Testing

🌐 **English** · [Dansk](Testing-da) · [Bahasa Melayu](Testing-ms)

```bash
python -m pytest
```

![The test run](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-birthday-wisher/raw/branch/main/docs/images/tests.png)

The tests use a fake SMTP connection and temporary files. They need no network, no `.env` and no credentials. Optional checks:

```bash
python -m ruff check src tests
python -m mypy src tests
```

API documentation from the Doxygen comments: `doxygen Doxyfile` (output in `docs/doxygen/`).
