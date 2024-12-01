import flask
from .extensions import db
from .config import Config
from .views import main_bp



def create_app():
    app = flask.Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(main_bp)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
