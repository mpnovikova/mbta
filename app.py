from flask import Flask


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config)

    register_blueprints(app)

    return app


def register_blueprints(app):
    from services.api.subway import subway_api
    app.register_blueprint(subway_api)


