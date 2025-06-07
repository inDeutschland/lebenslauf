from flask import Flask
from flask_babel import Babel
from models.models import db
from routes.admin_routes import admin_bp
from routes.public_routes import public_bp
from i18n import init_i18n

babel = Babel()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.settings.Config")

    # إعداد Flask-Babel
    app.config['LANGUAGES'] = ['de', 'en', 'ar']  # اللغات المدعومة
    app.config['BABEL_DEFAULT_LOCALE'] = 'de'     # اللغة الافتراضية

    db.init_app(app)
    babel.init_app(app)

    from routes.main_routes import main_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(public_bp)
    init_i18n(app)

    return app
