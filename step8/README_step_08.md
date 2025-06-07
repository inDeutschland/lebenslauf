# 🎨 Schritt 8 – Visuelle Bearbeitung von CSS-Stilen in der Admin-Oberfläche

## 🎯 Ziel
Die bisherigen JSON-basierten CSS-Einstellungen werden nun über visuelle Bedienelemente (Dropdowns, Farbwähler) bearbeitet – ganz ohne manuelles JSON!

---

## ✅ Unterstützte visuelle Felder

| Einstellungsschlüssel     | Eingabefelder                         |
|---------------------------|----------------------------------------|
| section_title_css         | Font Size, Color, Font Weight         |
| paragraph_css             | Font Size, Color                      |
| body_font                 | Font Family (Dropdown)                |

---

## 📁 Geänderte Dateien

```
step8/
├── routes/
│   └── admin_routes.py        # Erweiterte Logik zum Parsen visueller Felder
├── templates/
│   └── admin/
│       └── settings.html      # Visuelle Eingabeelemente statt Textarea für JSON
```

---

## 🖼️ Beispiel: `section_title_css`

```html
<select name="section_title_css_font_size">...</select>
<input type="color" name="section_title_css_color">
<select name="section_title_css_weight">...</select>
```

---

## 🖼️ Beispiel: `paragraph_css`

```html
<select name="paragraph_css_font_size">...</select>
<input type="color" name="paragraph_css_color">
```

---

## 🖼️ Beispiel: `body_font`

```html
<select name="body_font">
  <option value="Arial, sans-serif">Arial</option>
  <option value="Verdana, sans-serif">Verdana</option>
  ...
</select>
```

---

## ⚙️ Verarbeitung in `admin_routes.py`

- POST: Werte werden aus einzelnen Feldern gesammelt und in JSON umgewandelt (bzw. direkt gespeichert).
- GET: Werte werden geparsed und als Datenobjekte an das Template übergeben.

---

## ▶️ Anwendung starten

```bash
python run.py
```

Dann besuchen:
```
http://localhost:40505/admin/settings
```

---

## ✅ Ergebnis

- Admins können alle Stile bequem visuell konfigurieren.
- Kein Risiko durch fehlerhaftes JSON.
- Änderungen wirken sich direkt auf die öffentliche Lebenslaufseite `/resume` aus.

---

## 🔜 Nächster Schritt

- Live-Vorschau beim Bearbeiten.
- Integration eines Reset-Buttons für Standardwerte.