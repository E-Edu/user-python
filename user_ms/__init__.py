from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from sentry_sdk.integrations.flask import FlaskIntegration
from user_ms.config import ProductionConfig, TestingConfig
import os, sentry_sdk

SENTRY_KEY = os.environ.get("SENTRY_KEY")
SENTRY_ORGANIZATION = os.environ.get("SENTRY_ORGANIZATION")
SENTRY_PROJECT = os.environ.get("SENTRY_PROJECT")
ALL_SENTRY_VALUES_SET = os.environ.get("ALL_SENTRY_VALUES_SET")
if ALL_SENTRY_VALUES_SET == "added":
    sentry_sdk.init(
        dsn=f"https://{SENTRY_KEY}@{SENTRY_ORGANIZATION}.ingest.sentry.io/{SENTRY_PROJECT}",
        integrations=[FlaskIntegration()]
    )

api = Api()
db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()

def init_app():
    app = Flask(__name__)

    conf = os.environ.get("conf_mode")
    if conf == "deploy":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(TestingConfig)

    #from user_ms
    #app.register_blueprint(app_error)

    db.init_app(app)
    @app.before_first_request
    def init_tables():
        db.create_all()

    api.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    return app