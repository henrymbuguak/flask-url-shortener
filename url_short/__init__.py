from flask import Flask
from url_short import url_short


def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'clpoazwvPnBmQW9uOVRGVHJ0N0M4X3owdg=='

    app.register_blueprint(url_short.bp)

    return app
