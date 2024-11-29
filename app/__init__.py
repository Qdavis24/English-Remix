import flask
from .config import Config
from .views import index_bp


def create_app():
    app = flask.Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(index_bp)
    return app
