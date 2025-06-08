from flask import Flask
from models.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.settings.Config")

    db.init_app(app)

    from routes.main_routes import main_bp
    app.register_blueprint(main_bp)

    return app
