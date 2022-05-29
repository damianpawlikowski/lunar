import os


class Config:
    SECRET_KEY = os.environ.get("LUNAR_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("LUNAR_DATABASE_URI")

    # Deprecated SQLA feature.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_TOKEN_LOCATION = "cookies"
    JWT_ACCESS_TOKEN_EXPIRES = 900
    JWT_ACCESS_COOKIE_NAME = "Access-Token"
    JWT_COOKIE_CSRF_PROTECT = False

    CORS_SUPPORTS_CREDENTIALS = True


class DevConfig(Config):
    DEBUG = True
    ENV = "development"


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class ProdConfig(Config):
    ENV = "production"
