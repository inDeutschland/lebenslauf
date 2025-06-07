
# Schritt 9 – Live-Vorschau der Lebenslauf-Stileinstellungen

## 🎯 Ziel
Integration einer **Live Preview**-Funktion, um Stiländerungen (CSS) direkt im Browser visuell zu testen, bevor sie gespeichert werden.

---

## 🆕 Struktur

```
templates/
└── admin/
    └── settings.html               # Mit eingebetteter Vorschau
```

---

## 🖥️ `templates/admin/settings.html`

Die Vorschau erscheint oberhalb des Einstellungsformulars:

```html
<h2>🔍 Live-Vorschau</h2>
<div id="preview-box" style="padding: 20px; border: 1px dashed #aaa;">
    <h2 id="preview-title">Beispiel-Titel</h2>
    <p id="preview-paragraph">Dies ist ein Beispielabschnitt mit Beispielinhalt für die Vorschau.</p>
</div>
```

Dazu ein eingebettetes `<script>` mit JavaScript:

```js
function updatePreview() {
    ...
}
document.addEventListener("DOMContentLoaded", () => {
    ...
});
```

Die JS-Funktion greift auf die Werte der Dropdowns und Farbwähler zu und passt die CSS-Stile des Vorschaukastens dynamisch an.

---

## 📜 Unterstützte Einstellungen mit Vorschau

| Einstellungsschlüssel   | Typ           | Visualisierung im Preview |
|-------------------------|----------------|-----------------------------|
| `section_title_css`     | Font Size, Color, Weight | ✅ |
| `paragraph_css`         | Font Size, Color         | ✅ |
| `body_font`             | Font Family              | ✅ |

---

## ▶️ Ergebnis

- Benutzer kann CSS-Werte direkt anpassen **und live sehen**, wie sich dies auf Titel und Absätze auswirkt.
- Funktioniert ohne Neuladen der Seite.
- Verbesserte Benutzerfreundlichkeit für Nicht-Programmierer.

---

## 📦 Beispiel zum Testen

Starte das Projekt:

```bash
python run.py
```

Rufe im Browser auf:

```
http://localhost:40505/admin/settings
```

Jetzt kannst du Farben, Größen und Schriftarten live ändern und visuell prüfen.

---

✅ **Die Vorschau zeigt sofortige Änderungen – speichere sie, wenn du zufrieden bist.**
