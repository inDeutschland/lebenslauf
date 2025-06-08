# 📘 Schritt 6 – Dynamisches Styling & öffentliche Lebenslaufseite

## 🎯 Ziel  
Integration eines dynamischen CSS-Stylings basierend auf Daten aus der Datenbank, und Verbesserung der öffentlichen Lebenslaufseite `/resume`.

---

## ⚙️ Neue Funktionen

- 📄 Öffentliche Lebenslaufseite mit dynamisch gerenderten Abschnitten.
- 🎨 Dynamisches Styling über das `Setting`-Modell.
- 📁 Separates Stylesheet (`resume.css`) für globale Standard-Stile.
- 🧠 Unterstützung für individuelle Stildefinitionen je Bereich über die Datenbank.

---

## 📂 Neue/aktualisierte Dateien

```
step6/
├── logic/
│   └── builder.py                # Hilfsfunktion zum Laden von CSS-Einstellungen
├── static/
│   └── css/
│       └── resume.css            # Globales CSS für die Resume-Seite
├── templates/
│   └── public/
│       └── resume.html.j2        # Dynamisch formatierte Lebenslaufseite
├── routes/
│   └── public_routes.py          # Route für /resume mit dynamischem Styling
```

---

## 🧠 `get_css_setting` – Hilfsfunktion

```python
def get_css_setting(key, default=""):
    setting = Setting.query.filter_by(key=key).first()
    if setting:
        try:
            css_dict = json.loads(setting.value.replace("'", '"'))
            return "; ".join(f"{k}: {v}" for k, v in css_dict.items())
        except:
            return default
    return default
```

> Diese Funktion holt ein CSS-Objekt (z. B. `{'font-size': '18px', 'color': '#000'}`) und wandelt es in einen gültigen Style-String um.

---

## 🌐 `routes/public_routes.py`

```python
@public_bp.route("/resume")
def resume():
    sections = Section.query.all()
    section_title_css = get_css_setting("section_title_css", "font-size: 20px; color: #000")
    paragraph_css = get_css_setting("paragraph_css", "font-size: 14px; color: #444")
    body_font = get_css_setting("body_font", "font-family: Arial, sans-serif")

    return render_template(
        "public/resume.html.j2",
        sections=sections,
        section_title_css=section_title_css,
        paragraph_css=paragraph_css,
        body_font=body_font
    )
```

---

## 🖼️ `resume.html.j2`

```html
<body style="{{ body_font }}">
    <h1>📄 Mein Lebenslauf</h1>
    {% for section in sections %}
        <h2 class="section-title" style="{{ section_title_css }}">{{ section.title }}</h2>
        <div class="section-content" style="{{ paragraph_css }}">{{ section.content }}</div>
    {% endfor %}
</body>
```

---

## 🎨 `resume.css`

```css
body {
    margin: 40px;
    font-family: Arial, sans-serif;
}
.section-title {
    border-bottom: 1px solid #ccc;
    margin-top: 40px;
}
.section-content {
    white-space: pre-wrap;
    margin-top: 10px;
}
```

---

## 🛠️ Initialisierung der Datenbank

```bash
python tools/init_db.py
```

> Erstellt die Tabellen `Section` und `Setting` mit Startwerten.

---

## ▶️ Anwendung starten

```bash
python run.py
```

Dann öffnen:

```
http://localhost:40505/resume
```

---

## ✅ Ergebnis

- Lebenslauf-Abschnitte werden korrekt aus der Datenbank geladen.
- Formatierung ist dynamisch über Datenbank-Settings steuerbar.
- Seite ist bereit für erweitertes Layout, Druck-Ansicht, etc.