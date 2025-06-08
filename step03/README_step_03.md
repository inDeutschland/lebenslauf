# Schritt 3 – Datenbank und Grundmodelle einrichten (SQLAlchemy)

## 🎯 Ziel
Einrichtung der SQLite-Datenbank mit SQLAlchemy und Definition der Grundtabellen:
- `Section`: Lebenslauf-Bereiche
- `Setting`: Formatierungseinstellungen

---

## 🧱 Neue Struktur

```
lebenslauf/
├── models/
│   └── models.py          # Datenbankmodelle
├── tools/
│   └── init_db.py         # Initialisierungsskript
├── config/
│   └── settings.py        # Datenbank-Konfiguration
├── __init__.py            # App-Factory mit DB-Integration
```

---

## 💾 Abhängigkeit installieren

```bash
pip install flask_sqlalchemy
```

---

## 🧪 Konfiguration in `config/settings.py`

```python
class Config:
    SECRET_KEY = 'dev_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///lebenslauf.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
```

---

## 🧩 Inhalt von `models/models.py`

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=True)

class Setting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), unique=True, nullable=False)
    value = db.Column(db.Text, nullable=False)
```

---

## 🔗 App-Integration in `__init__.py`

```python
from flask import Flask
from models.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.settings.Config")

    db.init_app(app)

    from routes.main_routes import main_bp
    app.register_blueprint(main_bp)

    return app
```

---

## 🛠️ Datenbank initialisieren – `tools/init_db.py`

```python
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from __init__ import create_app
from models.models import db, Section, Setting

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    sections = [
        "Profil", "Karriereziel", "Bevorzugte Bereiche",
        "Berufserfahrung", "Qualifikationen", "Technische Fähigkeiten",
        "Sprachen", "Projekte", "Links", "Interessen"
    ]

    for title in sections:
        db.session.add(Section(title=title, content=""))

    db.session.add(Setting(key="section_title_css", value="{'font-size': '18px', 'color': '#000'}"))
    db.session.commit()

    print("✅ Datenbank initialisiert und mit Beispieldaten gefüllt.")
```

---

## ▶️ Ausführen

```bash
python tools/init_db.py
```

Dann:

```bash
python run.py
```

Und im Browser öffnen:
[http://localhost:4050](http://localhost:4050)

---

## ✅ Ergebnis
- Datenbankdatei `lebenslauf.db` wurde erstellt.
- Grunddaten sind vorhanden.