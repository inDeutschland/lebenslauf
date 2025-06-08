
# 🧩 الخطوة 11 – الترجمة (i18n) + التنسيقات الديناميكية

هذه هي الخطوة الحادية عشرة من مشروع **السيرة الذاتية (lebenslauf)**، حيث تم دمج دعم التعدد اللغوي (i18n) بالإضافة إلى تنسيقات CSS الديناميكية بنجاح.

---

## ✅ الميزات في هذه الخطوة

### 🌍 الترجمة (i18n)
- دعم اللغات: **الألمانية 🇩🇪**، **الإنجليزية 🇬🇧**، **العربية 🇸🇦**
- تغيير اللغة عبر معامل URL مثل: `?lang=de` أو `?lang=en` أو `?lang=ar`
- لغة افتراضية يتم تحديدها تلقائيًا بناءً على `Accept-Language`
- دمج مكتبة Flask-Babel 4.0
- استخدام `force_locale()` لتحديد اللغة يدويًا
- استخدام `gettext` و `_()` و `{{ _('النص') }}` داخل القوالب

### 🎨 تنسيقات CSS ديناميكية
- تحميل إعدادات CSS (`section_title_css`، `paragraph_css`) من قاعدة البيانات
- معاينة حية داخل صفحة `settings.html` في لوحة الإدارة
- تعديل مرئي للإعدادات عبر حقول إدخال مثل: حجم الخط، اللون، الوزن

---

## 🛠️ البنية

```bash
step11/
├── config/
├── logic/
├── models/
├── routes/
│   ├── admin_routes.py
│   ├── main_routes.py   # يحتوي على force_locale و gettext
│   └── public_routes.py
├── static/css/resume.css
├── templates/
│   ├── home.html
│   ├── admin/sections.html
│   └── admin/settings.html
├── translations/
│   ├── de/LC_MESSAGES/messages.po
│   ├── ar/LC_MESSAGES/messages.po
├── i18n_runtime.py
├── extensions.py
├── run.py
```

---

## 🚀 التشغيل السريع

```bash
# تفعيل البيئة الافتراضية
.\env\Scripts\Activate

# تشغيل Flask
$env:FLASK_APP = "step11:create_app"
flask run
```

ثم افتح المتصفح:

```
http://127.0.0.1:5000/?lang=de
```

---

## 📁 تعديل الترجمات

```bash
pybabel extract -F babel.cfg -o messages.pot .
pybabel update -i messages.pot -d translations -l ar
pybabel compile -d translations
```

---

## 🔮 الخطوات التالية (مقترحة)

- [ ] حفظ اللغة المختارة داخل `session` بدلاً من URL
- [ ] إضافة قائمة منسدلة لاختيار اللغة داخل الشريط العلوي
- [ ] ترجمة كاملة لجميع صفحات الإدارة
- [ ] تحديث فوري للمعاينة عبر JavaScript

---

## 🧠 المؤلف
**TamerOnLine** – [github.com/TamerOnLine](https://github.com/TamerOnLine)
