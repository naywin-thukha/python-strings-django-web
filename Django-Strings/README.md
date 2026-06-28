# Python Strings — Django Presentation Project

A layered Django web app that demonstrates **Python strings** and **string methods** for presentations and learning.

## Architecture (4 Layers)

```
Presentation  →  strings_app/views/ + templates/
Service       →  strings_app/services/
Repository    →  strings_app/repositories/
Domain        →  strings_app/domain/
```

**Request flow:** Browser → View → Service → Repository → Domain entities → back up the chain.

## Categories Demonstrated

| Category | Methods |
|----------|---------|
| Creation | `+`, `*`, `len()` |
| Case | `upper()`, `lower()`, `capitalize()`, `title()`, `swapcase()`, `casefold()` |
| Search | `find()`, `index()`, `count()`, `startswith()`, `endswith()`, `in` |
| Modify | `replace()`, `split()`, `join()`, `strip()`, `lstrip()`, `rstrip()`, `removeprefix()`, `removesuffix()` |
| Format | `format()`, f-strings, `center()`, `ljust()`, `rjust()`, `zfill()` |
| Validation | `isalpha()`, `isdigit()`, `isalnum()`, `isspace()`, `islower()`, `isupper()`, `isnumeric()` |
| Slicing | `[i]`, `[-1]`, `[start:end]`, `[::n]`, `[::-1]` |

## Quick Start

### macOS / Linux

```bash
cd "/path/to/Python Strings"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Windows (Command Prompt)

```cmd
cd "C:\Users\YourName\Desktop\Python Strings"
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Windows (PowerShell)

```powershell
cd "C:\Users\YourName\Desktop\Python Strings"
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

> **PowerShell note:** If activation is blocked, run once:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

Open **http://127.0.0.1:8000/** in your browser on any platform.

## Pages

- **Home** — Architecture overview and category links
- **Category Demo** — Live results for one category (e.g. `/category/case/`)
- **Playground** — Run all methods on one input string
- **Method Catalog** — Full reference table from the Repository layer
- **API** — `POST /api/demo/` with `text` and `category` for live demos

## Project Structure

```
Python Strings/
├── manage.py
├── requirements.txt
├── string_demo/          # Django project settings
└── strings_app/
    ├── domain/           # Entities & enums
    ├── repositories/     # Sample data & method catalog
    ├── services/         # String operation logic
    ├── views/            # HTTP handlers
    ├── templates/        # HTML UI
    └── static/           # CSS styling
```

## Presentation Tips

1. Start on **Home** to explain the 4-layer architecture
2. Pick a **Category** page and type live strings from the audience
3. Use **Playground** to show all methods at once
4. Show **catalog.html** to explain the Repository layer's role
5. Demo the JSON API:

**macOS / Linux:**
```bash
curl -X POST http://127.0.0.1:8000/api/demo/ \
  -d "text=Hello Python&category=case"
```

**Windows (PowerShell):**
```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/api/demo/ -Method Post `
  -Body @{ text = "Hello Python"; category = "case" }
```
