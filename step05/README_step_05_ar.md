
# الخطوة 5 – عرض صفحة السيرة الذاتية العامة (`/resume`)

## 🎯 الهدف
إنشاء صفحة عامة لعرض السيرة الذاتية الكاملة باستخدام البيانات من قاعدة البيانات.

---

## 🧱 الهيكل الجديد

```
lebenslauf/
├── routes/
│   └── public_routes.py         # المسارات العامة
├── templates/
│   └── public/
│       └── resume.html          # قالب العرض للسيرة الذاتية
```

---

## 📂 `routes/public_routes.py`

```python
from flask import Blueprint, render_template
from models.models import Section

public_bp = Blueprint("public", __name__)

@public_bp.route("/resume")
def resume():
    sections = Section.query.all()
    return render_template("public/resume.html", sections=sections)
```

---

## 🛠️ تسجيل المسار في `__init__.py`

```python
from routes.public_routes import public_bp
app.register_blueprint(public_bp)
```

---

## 🖥️ `templates/public/resume.html`

```html
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>السيرة الذاتية</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
        }
        h2 {
            border-bottom: 1px solid #ccc;
            margin-top: 40px;
            color: #333;
        }
        .section-content {
            white-space: pre-wrap;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <h1>📄 سيرتي الذاتية</h1>

    {% for section in sections %}
        <h2>{{ section.title }}</h2>
        <div class="section-content">{{ section.content }}</div>
    {% endfor %}
</body>
</html>
```

---

## ▶️ التشغيل

```bash
python run.py
```

ثم افتح في المتصفح:

```
http://localhost:4050/resume
```

---

## ✅ النتيجة

- يتم عرض جميع الأقسام بشكل ديناميكي.
- المحتوى يأتي مباشرة من قاعدة بيانات SQLite.
- الصفحة بسيطة، نظيفة، وجاهزة للتنسيق.
