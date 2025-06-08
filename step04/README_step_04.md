# Schritt 4 – Admin-Oberfläche für Lebenslauf-Abschnitte

## 🎯 Ziel
Erstellung einer Admin-Seite zum Bearbeiten und Speichern aller Lebenslauf-Abschnitte direkt aus der Datenbank.

---

## 🧱 Neue Struktur

```
lebenslauf/
├── routes/
│   └── admin_routes.py       # Admin-Routen
├── templates/
│   └── admin/
│       └── sections.html     # Admin-HTML-Seite zur Bearbeitung
```

---

## 📂 `routes/admin_routes.py`

```python
from flask import Blueprint, render_template, request, redirect, url_for
from models.models import db, Section

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/sections", methods=["GET", "POST"])
def manage_sections():
    if request.method == "POST":
        for section_id, content in request.form.items():
            section = Section.query.get(int(section_id))
            if section:
                section.content = content
        db.session.commit()
        return redirect(url_for("admin.manage_sections"))

    sections = Section.query.all()
    return render_template("admin/sections.html", sections=sections)
```

---

## 🛠️ Registrierung im `__init__.py`

```python
from routes.admin_routes import admin_bp
app.register_blueprint(admin_bp)
```

---

## 🖥️ `templates/admin/sections.html`

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Abschnitte verwalten</title>
</head>
<body>
    <h1>📝 Lebenslauf-Abschnitte bearbeiten</h1>
    <form method="POST">
        {% for section in sections %}
            <h3>{{ section.title }}</h3>
            <textarea name="{{ section.id }}" rows="4" cols="80">{{ section.content }}</textarea>
            <hr>
        {% endfor %}
        <button type="submit">💾 Änderungen speichern</button>
    </form>
</body>
</html>
```

---

## ▶️ Ausführen

```bash
python run.py
```

Im Browser öffnen:

```
http://localhost:4050/admin/sections
```

---

## ✅ Ergebnis

- Alle Abschnitte werden dynamisch geladen.
- Änderungen können direkt gespeichert werden.
- Volle Bearbeitbarkeit über das Admin-Panel.