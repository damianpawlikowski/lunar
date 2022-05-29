from lunar.app import create_app
from lunar.config import Config
from lunar.config import DevConfig
from lunar.config import TestConfig
from lunar.config import ProdConfig


def test_base_config():
    app = create_app(Config)
    assert app.config["SECRET_KEY"] is not None
    assert app.config["SQLALCHEMY_DATABASE_URI"] is not None


def test_development_config():
    app = create_app(DevConfig)
    assert app.config["DEBUG"] is True
    assert app.config["ENV"] == "development"


def test_testing_config():
    app = create_app(TestConfig)
    assert app.config["TESTING"] is True
    assert app.config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///:memory:"


def test_production_config():
    app = create_app(ProdConfig)
    assert app.config["ENV"] == "production"
    assert app.config["DEBUG"] is False
    assert app.config["TESTING"] is False
