# Schritt 2 – Projektstruktur organisieren (Flat + Modular)

## 🎯 Ziel
Das Projekt in eine saubere, modulare Struktur organisieren, bereit für Erweiterung, Übersetzung und Admin-Panel.

---

## 🧱 Struktur nach dieser Phase

```
lebenslauf/
│
├── run.py                  # Einstiegspunkt
├── __init__.py             # App-Factory
│
├── config/
│   └── settings.py         # Flask-Konfiguration
│
├── routes/
│   └── main_routes.py      # Homepage-Routen
│
├── templates/
│   └── home.html           # HTML-Begrüßungsseite
│
├── static/
│   ├── css/
│   └── js/
```

---

## 📂 Dateien im Detail

### `config/settings.py`

```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_key')
    DEBUG = True
```

---

### `__init__.py`

```python
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.settings.Config")

    from routes.main_routes import main_bp
    app.register_blueprint(main_bp)

    return app
```

---

### `run.py`

```python
from __init__ import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4050)
```

---

### `routes/main_routes.py`

```python
from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return render_template("home.html")
```

---

### `templates/home.html`

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Lebenslauf Projekt</title>
</head>
<body>
    <h1>✅ Lebenslauf Projekt gestartet erfolgreich!</h1>
</body>
</html>
```

---

## ▶️ Ausführen

```bash
python run.py
```

Dann im Browser öffnen:  
[http://localhost:4050](http://localhost:4050)

---

## ✅ Ergebnis
Eine HTML-Seite mit Begrüßung erscheint:

```
✅ Lebenslauf Projekt gestartet erfolgreich!
```