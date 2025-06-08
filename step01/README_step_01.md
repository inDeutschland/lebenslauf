# Schritt 1 – Einfaches Flask-Projekt starten (Port 4050)

## 🎯 Ziel
Ein minimales Flask-Projekt starten, das auf dem Port `4050` läuft und eine Willkommensnachricht anzeigt.

---

## 🧱 Struktur

```
lebenslauf/
└── run.py
```

---

## 🧪 Inhalt von `run.py`

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Lebenslauf Projekt gestartet erfolgreich!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4050, debug=True)
```

---

## ▶️ Ausführen

```bash
pip install flask
python run.py
```

Dann im Browser öffnen:

```
http://localhost:4050
```

---

## ✅ Ergebnis
Im Browser sollte folgende Nachricht erscheinen:

```
Lebenslauf Projekt gestartet erfolgreich!
```