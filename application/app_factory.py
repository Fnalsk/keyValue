from flask import Flask

from application.features.views import register_base_routes


def create_base_app() -> Flask:
    """
    Base Flask app factory.
    """
    app = Flask(__name__)

    return app


def create_web_app() -> Flask:
    """
    Create a version of the app suitable for serving the website locally or in production.
    """
    app = create_base_app()

    register_base_routes(app)

    return app
