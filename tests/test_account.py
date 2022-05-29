import pytest

from lunar.account.models import Account
from lunar.account.serializers import account_schema


def test_account_set_password(app):
    """Testing both scenario, initializer way and set_password() method way.
    Hashing word "secret" should return following SHA1:
    "e5e9fa1ba31ecd1ae84f75caaa474f3a663f05f4", while setting it as "password"
    should give us: "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"
    """
    with app.app_context():
        account = Account(name="tester", password="secret")
        assert account.password == "e5e9fa1ba31ecd1ae84f75caaa474f3a663f05f4"

        account.set_password("password")
        assert account.password == "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"


@pytest.mark.parametrize(
    "password, expected",
    [
        ("secret", True),
        ("invalid", False),
    ]
)
def test_account_check_password(app, password, expected):
    with app.app_context():
        account = Account(name="tester", password="secret")
        assert account.check_password(password) is expected


def test_account_schema_load(app):
    data = {}
    data["name"] = "tester"
    data["password"] = "secret?@"
    data["email"] = "tester@email.com"

    with app.app_context():
        account = account_schema.load(data)
        assert account["name"] == "tester"
        assert account["email"] == "tester@email.com"


def test_account_schema_dump(app):
    with app.app_context():
        account = Account(
            name="tester",
            password="secret?@",
            email="tester@email.com"
        )
        serialized_account = account_schema.dump(account)["account"]
        assert serialized_account["name"] == "tester"
        assert "password" not in serialized_account


def test_create_account(app, client):
    response = client.post(
        "/api/account/create",
        json={
            "name": "tester",
            "password": "secret?@",
            "email": "tester@email.com",
        }
    )
    assert response.status_code == 201

    with app.app_context():
        assert Account.query.filter_by(name="tester").first() is not None


def test_login(auth):
    response = auth.login()
    data = response.json.get("data")
    assert response.status_code == 200
    assert "account" in data
    assert "Access-Token" in response.headers.get("Set-Cookie")


def test_logout(auth):
    response = auth.logout()
    assert response.status_code == 200
    assert "Access-Token=;" in response.headers.get("Set-Cookie")


def test_get_account(auth, client):
    auth.login()
    response = client.get("/api/account/get")
    data = response.json.get("data")
    assert response.status_code == 200
    assert "account" in data
