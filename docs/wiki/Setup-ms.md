# Persediaan

🌐 [English](Setup) · [Dansk](Setup-da) · **Bahasa Melayu**

Anda memerlukan Python 3.13 atau lebih baharu.

```bash
python -m venv .venv
```

Aktifkan persekitaran. Windows PowerShell: `.venv\Scripts\Activate.ps1`. Windows cmd: `.venv\Scripts\activate`. Linux dan macOS: `source .venv/bin/activate`.

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

![Mencipta .venv](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-birthday-wisher/raw/branch/main/docs/images/venv-setup.png)

Tambahan `dev` memasang pytest, ruff dan mypy. Program itu sendiri tidak memerlukan apa-apa.
