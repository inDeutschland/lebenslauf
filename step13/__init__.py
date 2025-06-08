from flask import Flask
from .models.models import db, Section
from .routes.admin_routes import admin_bp
from .routes.public_routes import public_bp
from .routes.main_routes import main_bp
from .extensions import babel  # هذا يجب أن يأتي بعد Flask
from .i18n_runtime import init_i18n
import os
from flask_babel import get_locale
from flask_babel import _


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("step13.config.settings.Config")
    app.config['LANGUAGES'] = ['de', 'en', 'ar']
    app.debug = True

    import logging
    logging.basicConfig(level=logging.DEBUG)
    app.logger.setLevel(logging.DEBUG)

    # تأكد من وجود مجلد instance
    os.makedirs(app.instance_path, exist_ok=True)

    # تهيئة قواعد البيانات والإضافات
    db.init_app(app)

    translations_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'translations'))
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = translations_path
    babel.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(public_bp)

    init_i18n(app)

    # ✅ إنشاء قاعدة البيانات تلقائيًا
    with app.app_context():
        db_path = os.path.join(app.instance_path, 'lebenslauf.db')
        if not os.path.exists(db_path):
            db.create_all()
            insert_initial_sections()

    @app.before_request
    def log_locale_info():
        print("🌐 Requested locale:", get_locale())
        print("📦 Babel directory:", app.config.get('BABEL_TRANSLATION_DIRECTORIES'))

    return app


def insert_initial_sections():
    """إدخال الأقسام الأساسية تلقائيًا"""
    default_sections = [
        "Summary", "Career Objective", "Experience", "Qualifications",
        "Skills", "Languages", "Projects", "Links", "Interests"
    ]
    for idx, title in enumerate(default_sections, start=1):
        print(f"➕ Adding section: {title}")
        section = Section(order=idx, title=title, content="")
        db.session.add(section)
    db.session.commit()
    print("✅ Sections inserted.")

