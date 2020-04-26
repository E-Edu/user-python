import os, psycopg2

class Config(object):
    SECRET_KEY = os.environ.get("MS_Secret")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USE_TLS  = os.environ.get("MAIL_USE_TLS")
    MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL")
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    DEFAULT_MAIL_SENDER = os.environ.get("DEFAULT_MAIL_SENDER")

class ProductionConfig(Config):
    username = os.environ.get('DB_USERNAME')
    password = os.environ.get('DB_PASSWORD')
    hostname = os.environ.get('DB_HOSTNAME')
    port = 5432
    database = os.environ.get('DB_DATABASE')
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{database}'

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///"
    DEBUG = True

class JWT:
    JWT_SEC = os.environ.get("JWT_Secret")
    JWT_ALGORITHMS = algorithms=['HS512']