import pytest

from lunar.extensions import db
from lunar.app import create_app
from lunar.config import TestConfig
from lunar.account.models import Account


@pytest.fixture
def app():
    """The Flask app instance for tests."""
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
    return app


@pytest.fixture
def client(app):
    """The Flask test client."""
    return app.test_client()


class Auth:
    def __init__(self, client):
        self.client = client

    def login(self, name="tester", password="secret?@"):
        return self.client.post(
            "/api/account/login",
            json={
                "name": name,
                "password": password,
            }
        )

    def logout(self):
        return self.client.post("/api/account/logout")


@pytest.fixture
def auth(app, client):
    with app.app_context():
        db.session.add(
            Account(
                name="tester",
                password="secret?@",
                email="tester@email.com"
            )
        )
        db.session.commit()
    return Auth(client)
