
# 🎨 الخطوة 8 – تعديل مرئي لتنسيقات CSS داخل لوحة الإدارة

## 🎯 الهدف
استبدال إعدادات CSS بصيغة JSON بعناصر إدخال مرئية مثل القوائم المنسدلة ومنتقي الألوان – دون الحاجة لتعديل JSON يدويًا!

---

## ✅ الحقول المرئية المدعومة

| مفتاح الإعداد              | عناصر الإدخال                        |
|----------------------------|--------------------------------------|
| section_title_css          | حجم الخط، اللون، وزن الخط            |
| paragraph_css              | حجم الخط، اللون                      |
| body_font                  | نوع الخط (قائمة منسدلة)             |

---

## 📁 الملفات المعدّلة

```
step8/
├── routes/
│   └── admin_routes.py        # منطق موسع لمعالجة الحقول المرئية
├── templates/
│   └── admin/
│       └── settings.html      # عناصر إدخال مرئية بدلاً من Textarea
```

---

## 🖼️ مثال: `section_title_css`

```html
<select name="section_title_css_font_size">...</select>
<input type="color" name="section_title_css_color">
<select name="section_title_css_weight">...</select>
```

---

## 🖼️ مثال: `paragraph_css`

```html
<select name="paragraph_css_font_size">...</select>
<input type="color" name="paragraph_css_color">
```

---

## 🖼️ مثال: `body_font`

```html
<select name="body_font">
  <option value="Arial, sans-serif">Arial</option>
  <option value="Verdana, sans-serif">Verdana</option>
  ...
</select>
```

---

## ⚙️ المعالجة في `admin_routes.py`

- عند الإرسال (POST): يتم جمع القيم من الحقول المرئية وتجميعها في صيغة JSON (أو حفظها مباشرة).
- عند العرض (GET): يتم تحليل القيم وتحويلها إلى كائنات بيانات تُمرر إلى القالب.

---

## ▶️ تشغيل التطبيق

```bash
python run.py
```

ثم زيارة:
```
http://localhost:40505/admin/settings
```

---

## ✅ النتيجة

- يمكن للمشرفين الآن تعديل التنسيقات بسهولة من خلال واجهة مرئية.
- لا يوجد خطر ناتج عن JSON غير صحيح.
- التعديلات تنعكس مباشرة على صفحة السيرة الذاتية العامة `/resume`.

---

## 🔜 الخطوة التالية

- عرض مباشر (Live Preview) عند التعديل.
- دمج زر لإعادة القيم إلى الإعدادات الافتراضية.
