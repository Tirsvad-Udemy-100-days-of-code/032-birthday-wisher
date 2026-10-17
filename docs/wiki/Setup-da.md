# Opsætning

🌐 [English](Setup) · **Dansk** · [Bahasa Melayu](Setup-ms)

Du skal bruge Python 3.13 eller nyere.

```bash
python -m venv .venv
```

Aktivér miljøet. Windows PowerShell: `.venv\Scripts\Activate.ps1`. Windows cmd: `.venv\Scripts\activate`. Linux og macOS: `source .venv/bin/activate`.

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

![Oprettelse af .venv](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-birthday-wisher/raw/branch/main/docs/images/venv-setup.png)

Tilvalget `dev` installerer pytest, ruff og mypy. Selve programmet kræver intet.
