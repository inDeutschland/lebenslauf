
# الخطوة 1 – بدء مشروع Flask بسيط (المنفذ 4050)

## 🎯 الهدف  
تشغيل مشروع Flask بسيط جدًا يعمل على المنفذ `4050` ويعرض رسالة ترحيبية.

---

## 🧱 الهيكل

```
lebenslauf/
└── run.py
```

---

## 🧪 محتوى الملف `run.py`

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "تم تشغيل مشروع السيرة الذاتية بنجاح!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4050, debug=True)
```

---

## ▶️ التشغيل

```bash
pip install flask
python run.py
```

ثم افتح المتصفح على:

```
http://localhost:4050
```

---

## ✅ النتيجة  
يجب أن تظهر الرسالة التالية في المتصفح:

```
تم تشغيل مشروع السيرة الذاتية بنجاح!
```
