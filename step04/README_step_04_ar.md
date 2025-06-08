
# الخطوة 4 – واجهة الإدارة لأقسام السيرة الذاتية

## 🎯 الهدف
إنشاء صفحة إدارة لتعديل وحفظ جميع أقسام السيرة الذاتية مباشرة من قاعدة البيانات.

---

## 🧱 الهيكل الجديد

```
lebenslauf/
├── routes/
│   └── admin_routes.py       # مسارات الإدارة
├── templates/
│   └── admin/
│       └── sections.html     # صفحة HTML للإدارة والتعديل
```

---

## 📂 `routes/admin_routes.py`

```python
from flask import Blueprint, render_template, request, redirect, url_for
from models.models import db, Section

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/sections", methods=["GET", "POST"])
def manage_sections():
    if request.method == "POST":
        for section_id, content in request.form.items():
            section = Section.query.get(int(section_id))
            if section:
                section.content = content
        db.session.commit()
        return redirect(url_for("admin.manage_sections"))

    sections = Section.query.all()
    return render_template("admin/sections.html", sections=sections)
```

---

## 🛠️ تسجيل المسارات في `__init__.py`

```python
from routes.admin_routes import admin_bp
app.register_blueprint(admin_bp)
```

---

## 🖥️ `templates/admin/sections.html`

```html
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>إدارة الأقسام</title>
</head>
<body>
    <h1>📝 تعديل أقسام السيرة الذاتية</h1>
    <form method="POST">
        {% for section in sections %}
            <h3>{{ section.title }}</h3>
            <textarea name="{{ section.id }}" rows="4" cols="80">{{ section.content }}</textarea>
            <hr>
        {% endfor %}
        <button type="submit">💾 حفظ التعديلات</button>
    </form>
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
http://localhost:4050/admin/sections
```

---

## ✅ النتيجة

- يتم تحميل جميع الأقسام بشكل ديناميكي.
- يمكن تعديلها وحفظها مباشرة.
- تحكم كامل من خلال لوحة الإدارة.
