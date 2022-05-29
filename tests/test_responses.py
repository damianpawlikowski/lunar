from lunar.responses import base_response
from lunar.responses import error_response
from lunar.responses import fail_response
from lunar.responses import success_response


def test_base_response(app):
    data = {}
    data["greeting"] = "Bonjour le monde!"

    with app.app_context():
        response = base_response(200, "test", "Hello World!", data)
        assert response.status_code == 200

        payload = response.get_json()
        assert payload["status"] == "test"
        assert payload["msg"] == "Hello World!"
        assert payload["data"] == data


def test_error_response(app):
    with app.app_context():
        response = error_response(500, "Server error occurred!")
        assert response.json.get("status") == "error"


def test_fail_response(app):
    with app.app_context():
        response = fail_response(422, "You screwed something up!")
        assert response.json.get("status") == "fail"


def test_success_response(app):
    with app.app_context():
        response = success_response(200, "Everything is fine.")
        assert response.json.get("status") == "success"
