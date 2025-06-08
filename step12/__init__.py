from flask import Flask
from .models.models import db
from .routes.admin_routes import admin_bp
from .routes.public_routes import public_bp
from .routes.main_routes import main_bp
from .extensions import babel  # هذا يجب أن يأتي بعد Flask
from .i18n_runtime import init_i18n
import os
from flask_babel import get_locale
from flask_babel import _


def create_app():
    app = Flask(__name__)
    app.config.from_object("step11.config.settings.Config")
    app.config['LANGUAGES'] = ['de', 'en', 'ar']
    app.debug = True

    import logging
    logging.basicConfig(level=logging.DEBUG)
    app.logger.setLevel(logging.DEBUG)

    db.init_app(app)

    # ✅ التهيئة اليدوية للمسار
    translations_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'translations'))
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = translations_path
    babel.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(public_bp)

    init_i18n(app)

    @app.before_request
    def log_locale_info():
        print("🌐 Requested locale:", get_locale())
        print("📦 Babel directory:", app.config.get('BABEL_TRANSLATION_DIRECTORIES'))

    return app
