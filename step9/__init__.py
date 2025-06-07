from flask import Flask
from models.models import db
from routes.admin_routes import admin_bp
from routes.public_routes import public_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.settings.Config")

    db.init_app(app)

    from routes.main_routes import main_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(public_bp)

    return app
