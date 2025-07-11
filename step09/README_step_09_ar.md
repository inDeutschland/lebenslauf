
# الخطوة 9 – المعاينة الحية لإعدادات تنسيق السيرة الذاتية

## 🎯 الهدف
دمج ميزة **المعاينة الحية (Live Preview)** لتجربة تغييرات CSS مباشرة في المتصفح قبل حفظها.

---

## 🆕 البنية

```
templates/
└── admin/
    └── settings.html               # تحتوي على المعاينة المضمنة
```

---

## 🖥️ `templates/admin/settings.html`

تظهر المعاينة أعلى نموذج الإعدادات:

```html
<h2>🔍 المعاينة الحية</h2>
<div id="preview-box" style="padding: 20px; border: 1px dashed #aaa;">
    <h2 id="preview-title">عنوان تجريبي</h2>
    <p id="preview-paragraph">هذا مثال لمقطع نصي تجريبي داخل المعاينة.</p>
</div>
```

مع تضمين سكربت JavaScript:

```js
function updatePreview() {
    ...
}
document.addEventListener("DOMContentLoaded", () => {
    ...
});
```

تقوم الدالة JS بقراءة القيم من القوائم المنسدلة ومنتقيات الألوان وتحديث CSS في صندوق المعاينة مباشرة.

---

## 📜 الإعدادات المدعومة في المعاينة

| مفتاح الإعداد              | النوع                | المعاينة |
|---------------------------|----------------------|----------|
| `section_title_css`       | حجم الخط، اللون، الوزن | ✅       |
| `paragraph_css`           | حجم الخط، اللون        | ✅       |
| `body_font`               | نوع الخط              | ✅       |

---

## ▶️ النتيجة

- يمكن للمستخدم تعديل إعدادات CSS ومشاهدة التأثير مباشرة على العناوين والمقاطع.
- بدون الحاجة لإعادة تحميل الصفحة.
- تجربة استخدام محسّنة، خاصة لغير المبرمجين.

---

## 📦 مثال للاختبار

ابدأ المشروع:

```bash
python run.py
```

ثم افتح في المتصفح:

```
http://localhost:40505/admin/settings
```

الآن يمكنك تعديل الألوان، الأحجام، وأنواع الخطوط ومعاينتها بشكل مباشر.

---

✅ **المعاينة تظهر التغييرات فورًا – يمكنك حفظها عندما تكون راضيًا عنها.**
