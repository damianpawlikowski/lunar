from flask import Flask
from flask_wtf.csrf import CSRFError

from lunar.extensions import db
from lunar.extensions import jwt
from lunar.extensions import cors
from lunar.extensions import csrf
from lunar.extensions import docs
from lunar.config import ProdConfig
from lunar.game.views import game_bp
from lunar.ticket.views import ticket_bp
from lunar.player.views import player_bp
from lunar.account.views import account_bp
from lunar.errors import handle_csrf_error
from lunar.account.views import create_account
from lunar.utils import set_csrf_token_cookie
from lunar.extensions import refresh_expiring_jwt


def register_swagger_docs(docs):
    docs.register(create_account, blueprint="account_bp")


def register_extensions(app):
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
    csrf.init_app(app)

    if app.config["ENV"] == "development":
        docs.init_app(app)
        register_swagger_docs(docs)


def register_blueprints(app):
    app.register_blueprint(game_bp)
    app.register_blueprint(ticket_bp)
    app.register_blueprint(player_bp)
    app.register_blueprint(account_bp)


def register_error_handlers(app):
    app.register_error_handler(CSRFError, handle_csrf_error)


def create_app(config=ProdConfig):
    """Create the Flask app through app factory pattern.
    https://flask.palletsprojects.com/en/2.1.x/patterns/appfactories/
    """
    app = Flask(__name__)
    app.config.from_object(config)

    register_blueprints(app)
    register_extensions(app)
    register_error_handlers(app)

    app.after_request(refresh_expiring_jwt)
    app.after_request(set_csrf_token_cookie)

    return app
