# ✅ Schritt 10 – "Speichern + Vorschau"-Button (Live Preview Button)

In diesem Schritt wurde ein zusätzlicher Button integriert, um die aktuelle CSS-Konfiguration zu speichern **und gleichzeitig eine Vorschau der Änderungen anzuzeigen**.

## 🔧 Änderungen im Template (`settings.html`)
Ein neuer Button wurde eingefügt:
```html
<button type="submit" name="action" value="save_and_preview">💾 Speichern + Vorschau anzeigen</button>
```

## 🧠 Logik im Python-Code (`admin_routes.py`)
Im POST-Abschnitt wurde geprüft, ob der Name des Buttons `"save_and_preview"` ist:

```python
if request.form.get("action") == "save_and_preview":
    return redirect(url_for("public.resume"))
```

Dadurch wird der Benutzer nach dem Speichern automatisch auf die Seite `/resume` weitergeleitet, um die neue Darstellung live zu sehen.

## ✅ Vorteil:
- Bessere Benutzererfahrung für Administratoren.
- Spart Zeit beim Anpassen und Testen des Designs.