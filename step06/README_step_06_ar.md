
# 📘 الخطوة 6 – تنسيق ديناميكي وصفحة السيرة الذاتية العامة

## 🎯 الهدف  
دمج تنسيق CSS ديناميكي بناءً على البيانات من قاعدة البيانات، وتحسين صفحة السيرة الذاتية العامة `/resume`.

---

## ⚙️ الميزات الجديدة

- 📄 صفحة السيرة الذاتية العامة تعرض الأقسام ديناميكيًا.
- 🎨 تنسيق CSS ديناميكي عبر نموذج `Setting`.
- 📁 ملف CSS مستقل (`resume.css`) للتنسيق العام.
- 🧠 دعم تخصيص التنسيق لكل قسم من قاعدة البيانات.

---

## 📂 الملفات الجديدة/المحدّثة

```
step6/
├── logic/
│   └── builder.py                # دالة مساعدة لتحميل إعدادات CSS
├── static/
│   └── css/
│       └── resume.css            # تنسيق CSS عام لصفحة السيرة الذاتية
├── templates/
│   └── public/
│       └── resume.html.j2        # صفحة السيرة الذاتية بتنسيق ديناميكي
├── routes/
│   └── public_routes.py          # مسار /resume مع تنسيق ديناميكي
```

---

## 🧠 `get_css_setting` – دالة مساعدة

```python
def get_css_setting(key, default=""):
    setting = Setting.query.filter_by(key=key).first()
    if setting:
        try:
            css_dict = json.loads(setting.value.replace("'", '"'))
            return "; ".join(f"{k}: {v}" for k, v in css_dict.items())
        except:
            return default
    return default
```

> تقوم هذه الدالة بجلب كائن CSS (مثل `{'font-size': '18px', 'color': '#000'}`) وتحويله إلى سلسلة تنسيق صالحة.

---

## 🌐 `routes/public_routes.py`

```python
@public_bp.route("/resume")
def resume():
    sections = Section.query.all()
    section_title_css = get_css_setting("section_title_css", "font-size: 20px; color: #000")
    paragraph_css = get_css_setting("paragraph_css", "font-size: 14px; color: #444")
    body_font = get_css_setting("body_font", "font-family: Arial, sans-serif")

    return render_template(
        "public/resume.html.j2",
        sections=sections,
        section_title_css=section_title_css,
        paragraph_css=paragraph_css,
        body_font=body_font
    )
```

---

## 🖼️ `resume.html.j2`

```html
<body style="{{ body_font }}">
    <h1>📄 سيرتي الذاتية</h1>
    {% for section in sections %}
        <h2 class="section-title" style="{{ section_title_css }}">{{ section.title }}</h2>
        <div class="section-content" style="{{ paragraph_css }}">{{ section.content }}</div>
    {% endfor %}
</body>
```

---

## 🎨 `resume.css`

```css
body {
    margin: 40px;
    font-family: Arial, sans-serif;
}
.section-title {
    border-bottom: 1px solid #ccc;
    margin-top: 40px;
}
.section-content {
    white-space: pre-wrap;
    margin-top: 10px;
}
```

---

## 🛠️ تهيئة قاعدة البيانات

```bash
python tools/init_db.py
```

> ينشئ الجداول `Section` و`Setting` مع بيانات افتراضية.

---

## ▶️ تشغيل التطبيق

```bash
python run.py
```

ثم افتح المتصفح على:

```
http://localhost:40505/resume
```

---

## ✅ النتيجة

- يتم تحميل أقسام السيرة الذاتية من قاعدة البيانات.
- التنسيق يمكن التحكم فيه ديناميكيًا من خلال الإعدادات.
- الصفحة جاهزة لتنسيقات موسعة، عرض للطباعة، وغيرها.
