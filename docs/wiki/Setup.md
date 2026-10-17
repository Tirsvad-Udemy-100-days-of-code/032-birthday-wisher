# Setup

🌐 **English** · [Dansk](Setup-da) · [Bahasa Melayu](Setup-ms)

You need Python 3.13 or newer.

```bash
python -m venv .venv
```

Activate the environment. Windows PowerShell: `.venv\Scripts\Activate.ps1`. Windows cmd: `.venv\Scripts\activate`. Linux and macOS: `source .venv/bin/activate`.

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

![Creating the .venv](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-birthday-wisher/raw/branch/main/docs/images/venv-setup.png)

The `dev` extra installs pytest, ruff and mypy. Nothing is needed to run the program itself.
