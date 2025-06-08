
# الخطوة 3 – إعداد قاعدة البيانات والنماذج الأساسية (SQLAlchemy)

## 🎯 الهدف
إعداد قاعدة بيانات SQLite باستخدام SQLAlchemy وتعريف الجداول الأساسية:
- `Section`: أقسام السيرة الذاتية
- `Setting`: إعدادات التنسيق

---

## 🧱 الهيكل الجديد

```
lebenslauf/
├── models/
│   └── models.py          # نماذج قاعدة البيانات
├── tools/
│   └── init_db.py         # سكربت التهيئة
├── config/
│   └── settings.py        # إعدادات قاعدة البيانات
├── __init__.py            # مصنع التطبيق مع تكامل قاعدة البيانات
```

---

## 💾 تثبيت الاعتماد

```bash
pip install flask_sqlalchemy
```

---

## 🧪 الإعداد في `config/settings.py`

```python
class Config:
    SECRET_KEY = 'dev_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///lebenslauf.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
```

---

## 🧩 محتوى `models/models.py`

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=True)

class Setting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), unique=True, nullable=False)
    value = db.Column(db.Text, nullable=False)
```

---

## 🔗 التكامل داخل `__init__.py`

```python
from flask import Flask
from models.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.settings.Config")

    db.init_app(app)

    from routes.main_routes import main_bp
    app.register_blueprint(main_bp)

    return app
```

---

## 🛠️ تهيئة قاعدة البيانات – `tools/init_db.py`

```python
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from __init__ import create_app
from models.models import db, Section, Setting

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    sections = [
        "الملف الشخصي", "الهدف المهني", "المجالات المفضلة",
        "الخبرات العملية", "المؤهلات", "المهارات التقنية",
        "اللغات", "المشاريع", "الروابط", "الاهتمامات"
    ]

    for title in sections:
        db.session.add(Section(title=title, content=""))

    db.session.add(Setting(key="section_title_css", value="{'font-size': '18px', 'color': '#000'}"))
    db.session.commit()

    print("✅ تم تهيئة قاعدة البيانات وإدخال بيانات تجريبية.")
```

---

## ▶️ التشغيل

```bash
python tools/init_db.py
```

ثم:

```bash
python run.py
```

ثم فتح المتصفح على:  
[http://localhost:4050](http://localhost:4050)

---

## ✅ النتيجة
- تم إنشاء ملف قاعدة البيانات `lebenslauf.db`.
- البيانات الأساسية أصبحت جاهزة.
