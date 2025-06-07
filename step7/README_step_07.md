# 🛠️ Schritt 7 – Admin-Oberfläche für dynamische CSS-Einstellungen

## 🎯 Ziel
Erstellung einer Admin-Seite zur Bearbeitung der Lebenslauf-Stile direkt aus der Datenbank via `/admin/settings`.

---

## ⚙️ Neue Funktionen

- ✅ Neue Admin-Route zur Bearbeitung von CSS-Stileinstellungen.
- ✅ Speichern von Änderungen direkt in der Tabelle `Setting`.
- ✅ Sofortige Wirkung der Änderungen auf die öffentliche Lebenslaufseite `/resume`.
- ✅ Fehlerprüfung für ungültige JSON-Werte.

---

## 📂 Neue/aktualisierte Dateien

```
step7/
├── routes/
│   └── admin_routes.py        # Neue Route: /admin/settings
├── templates/
│   └── admin/
│       └── settings.html      # Formular zur Bearbeitung der CSS-Einstellungen
```

---

## 🌐 Neue Route: `/admin/settings`

```python
@admin_bp.route("/settings", methods=["GET", "POST"])
def manage_settings():
    error = None

    if request.method == "POST":
        try:
            for key, value in request.form.items():
                import json
                json.loads(value.replace("'", '"'))
                setting = Setting.query.filter_by(key=key).first()
                if setting:
                    setting.value = value
            db.session.commit()
            return redirect(url_for("admin.manage_settings"))
        except Exception as e:
            error = f"❌ Fehler im JSON-Format: {str(e)}"

    settings = Setting.query.all()
    return render_template("admin/settings.html", settings=settings, error=error)
```

---

## 🖼️ Template: `settings.html`

```html
{% if error %}
    <p style="color: red;">{{ error }}</p>
{% endif %}

<form method="POST">
    {% for setting in settings %}
        <h3>{{ setting.key }}</h3>
        <textarea name="{{ setting.key }}" rows="4" cols="80">{{ setting.value }}</textarea>
        <hr>
    {% endfor %}
    <button type="submit">💾 Änderungen speichern</button>
</form>
```

---

## ▶️ Testen

1. Starte die App:
```bash
python run.py
```

2. Besuche im Browser:
```
http://localhost:40505/admin/settings
```

3. Bearbeite z. B. den Wert:
```json
{"font-size": "20px", "color": "#444", "font-weight": "bold"}
```

---

## ✅ Ergebnis

- Admins können jetzt CSS-Einstellungen sicher und einfach verwalten.
- Fehlerhafte Eingaben werden erkannt und nicht gespeichert.
- Die Resume-Seite `/resume` reflektiert jede Änderung sofort.

---

## 🔜 Nächster Schritt (Schritt 8)

- Verbesserung der Oberfläche mit visuellen Eingabeelementen (Color Picker, Dropdowns, Vorschau).