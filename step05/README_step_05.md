# Schritt 5 – Öffentliche Lebenslauf-Seite anzeigen (`/resume`)

## 🎯 Ziel
Erstellung einer öffentlichen Seite zur Anzeige des vollständigen Lebenslaufs mit Daten aus der Datenbank.

---

## 🧱 Neue Struktur

```
lebenslauf/
├── routes/
│   └── public_routes.py         # Öffentliche Routen
├── templates/
│   └── public/
│       └── resume.html          # Anzeigevorlage für den Lebenslauf
```

---

## 📂 `routes/public_routes.py`

```python
from flask import Blueprint, render_template
from models.models import Section

public_bp = Blueprint("public", __name__)

@public_bp.route("/resume")
def resume():
    sections = Section.query.all()
    return render_template("public/resume.html", sections=sections)
```

---

## 🛠️ Registrierung im `__init__.py`

```python
from routes.public_routes import public_bp
app.register_blueprint(public_bp)
```

---

## 🖥️ `templates/public/resume.html`

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Lebenslauf</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
        }
        h2 {
            border-bottom: 1px solid #ccc;
            margin-top: 40px;
            color: #333;
        }
        .section-content {
            white-space: pre-wrap;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <h1>📄 Mein Lebenslauf</h1>

    {% for section in sections %}
        <h2>{{ section.title }}</h2>
        <div class="section-content">{{ section.content }}</div>
    {% endfor %}
</body>
</html>
```

---

## ▶️ Ausführen

```bash
python run.py
```

Dann im Browser öffnen:

```
http://localhost:4050/resume
```

---

## ✅ Ergebnis

- Alle Abschnitte werden dynamisch dargestellt.
- Inhalt stammt direkt aus der SQLite-Datenbank.
- Die Seite ist einfach, sauber und bereit zur Formatierung.