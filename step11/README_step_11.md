# 🧩 Schritt 11 – Internationalisierung (i18n) + Dynamische Styles

Dies ist der elfte Schritt des Projekts **lebenslauf**, in dem wir die mehrsprachige Unterstützung (i18n) sowie dynamische CSS-Stile erfolgreich integriert haben.

---

## ✅ Funktionen in diesem Schritt

### 🌍 Mehrsprachigkeit (i18n)
- Unterstützung für **Deutsch 🇩🇪**, **Englisch 🇬🇧**, **Arabisch 🇸🇦**
- Wechsel der Sprache über URL-Parameter: `?lang=de`, `?lang=en`, `?lang=ar`
- Automatische Fallback-Sprache basierend auf `Accept-Language`
- Integration von Flask-Babel 4.0
- Verwendung von `force_locale()` zur erzwungenen Sprachumschaltung
- Übersetzbare Templates mit `gettext`, `_()` und `{{ _('Text') }}`

### 🎨 Dynamische CSS-Stile
- CSS-Konfigurationen (`section_title_css`, `paragraph_css`) aus der Datenbank
- Live-Vorschau in `settings.html` (Adminbereich)
- Visual CSS Editing via Input-Felder (z. B. Font Size, Color, Weight)

---

## 🛠️ Struktur

```bash
step11/
├── config/
├── logic/
├── models/
├── routes/
│   ├── admin_routes.py
│   ├── main_routes.py   # enthält force_locale + gettext
│   └── public_routes.py
├── static/css/resume.css
├── templates/
│   ├── home.html
│   ├── admin/sections.html
│   └── admin/settings.html
├── translations/
│   ├── de/LC_MESSAGES/messages.po
│   ├── ar/LC_MESSAGES/messages.po
├── i18n_runtime.py
├── extensions.py
├── run.py
```

---

## 🚀 Schnellstart

```bash
# Virtuelle Umgebung aktivieren
.env\Scripts\Activate

# Flask starten
$env:FLASK_APP = "step11:create_app"
flask run
```

Dann öffne deinen Browser:

```
http://127.0.0.1:5000/?lang=de
```

---

## 📁 Übersetzungen bearbeiten

```bash
pybabel extract -F babel.cfg -o messages.pot .
pybabel update -i messages.pot -d translations -l ar
pybabel compile -d translations
```

---

## 🔮 Nächste Schritte (Empfohlen)

- [ ] Sprache in `session` speichern statt in `?lang=`
- [ ] Dropdown für Sprachauswahl in Navbar
- [ ] Vollständige Übersetzung von Adminseiten
- [ ] Live-Aktualisierung der CSS-Vorschau (JavaScript)

---

## 🧠 Autor
**TamerOnLine** – [github.com/TamerOnLine](https://github.com/TamerOnLine)