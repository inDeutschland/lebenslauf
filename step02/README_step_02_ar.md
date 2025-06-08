
# الخطوة 2 – تنظيم هيكل المشروع (مستوي + معياري)

## 🎯 الهدف
تنظيم المشروع ضمن هيكل نظيف ومعياري، جاهز للتوسعة، الترجمة، ولوحة تحكم المشرف.

---

## 🧱 الهيكل بعد هذه المرحلة

```
lebenslauf/
│
├── run.py                  # نقطة البداية
├── __init__.py             # مصنع التطبيق (App Factory)
│
├── config/
│   └── settings.py         # إعدادات Flask
│
├── routes/
│   └── main_routes.py      # مسارات الصفحة الرئيسية
│
├── templates/
│   └── home.html           # صفحة HTML ترحيبية
│
├── static/
│   ├── css/
│   └── js/
```

---

## 📂 تفاصيل الملفات

### `config/settings.py`

```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_key')
    DEBUG = True
```

---

### `__init__.py`

```python
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.settings.Config")

    from routes.main_routes import main_bp
    app.register_blueprint(main_bp)

    return app
```

---

### `run.py`

```python
from __init__ import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4050)
```

---

### `routes/main_routes.py`

```python
from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return render_template("home.html")
```

---

### `templates/home.html`

```html
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>مشروع السيرة الذاتية</title>
</head>
<body>
    <h1>✅ تم تشغيل مشروع السيرة الذاتية بنجاح!</h1>
</body>
</html>
```

---

## ▶️ التشغيل

```bash
python run.py
```

ثم افتح المتصفح على:  
[http://localhost:4050](http://localhost:4050)

---

## ✅ النتيجة
تظهر صفحة HTML ترحيبية:

```
✅ تم تشغيل مشروع السيرة الذاتية بنجاح!
```
