
# 🛠️ الخطوة 7 – واجهة إدارة إعدادات CSS الديناميكية

## 🎯 الهدف
إنشاء صفحة إدارة لتعديل تنسيقات السيرة الذاتية مباشرة من قاعدة البيانات عبر `/admin/settings`.

---

## ⚙️ الميزات الجديدة

- ✅ مسار جديد للإدارة لتعديل إعدادات تنسيق CSS.
- ✅ حفظ التغييرات مباشرة داخل جدول `Setting`.
- ✅ ظهور التغييرات مباشرة على صفحة السيرة الذاتية `/resume`.
- ✅ التحقق من صحة تنسيقات JSON قبل الحفظ.

---

## 📂 الملفات الجديدة / المعدّلة

```
step7/
├── routes/
│   └── admin_routes.py        # مسار جديد: /admin/settings
├── templates/
│   └── admin/
│       └── settings.html      # نموذج لتعديل إعدادات CSS
```

---

## 🌐 المسار الجديد: `/admin/settings`

```python
@admin_bp.route("/settings", methods=["GET", "POST"])
def manage_settings():
    error = None

    if request.method == "POST":
        try:
            for key, value in request.form.items():
                import json
                json.loads(value.replace("'", '"'))
                setting = Setting.query.filter_by(key=key).first()
                if setting:
                    setting.value = value
            db.session.commit()
            return redirect(url_for("admin.manage_settings"))
        except Exception as e:
            error = f"❌ خطأ في تنسيق JSON: {str(e)}"

    settings = Setting.query.all()
    return render_template("admin/settings.html", settings=settings, error=error)
```

---

## 🖼️ القالب: `settings.html`

```html
{% if error %}
    <p style="color: red;">{{ error }}</p>
{% endif %}

<form method="POST">
    {% for setting in settings %}
        <h3>{{ setting.key }}</h3>
        <textarea name="{{ setting.key }}" rows="4" cols="80">{{ setting.value }}</textarea>
        <hr>
    {% endfor %}
    <button type="submit">💾 حفظ التعديلات</button>
</form>
```

---

## ▶️ التجربة

1. تشغيل التطبيق:
```bash
python run.py
```

2. افتح في المتصفح:
```
http://localhost:40505/admin/settings
```

3. قم بتعديل قيمة مثل:
```json
{"font-size": "20px", "color": "#444", "font-weight": "bold"}
```

---

## ✅ النتيجة

- يمكن للمشرفين الآن تعديل إعدادات CSS بسهولة وأمان.
- يتم كشف التنسيقات غير الصحيحة وعدم حفظها.
- صفحة السيرة الذاتية `/resume` تعكس التعديلات فورًا.

---

## 🔜 الخطوة التالية (الخطوة 8)

- تحسين الواجهة بعناصر إدخال مرئية (مثل منتقي الألوان، القوائم المنسدلة، والمعاينة).
