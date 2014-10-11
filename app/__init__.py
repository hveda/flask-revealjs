from flask import Flask
from flask.ext.bootstrap import Bootstrap


def bootstrap_app():
    """
    Simple bootstrap function that intialises the app and any config
    """
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    from .web import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app