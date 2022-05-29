from flask import Flask

from lunar.extensions import db
from lunar.extensions import jwt
from lunar.extensions import cors
from lunar.config import ProdConfig
from lunar.game.views import game_bp
from lunar.ticket.views import ticket_bp
from lunar.player.views import player_bp
from lunar.account.views import account_bp


def register_extensions(app):
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)


def register_blueprints(app):
    app.register_blueprint(game_bp)
    app.register_blueprint(ticket_bp)
    app.register_blueprint(player_bp)
    app.register_blueprint(account_bp)


def create_app(config=ProdConfig):
    """Create the Flask app through app factory pattern.
    https://flask.palletsprojects.com/en/2.1.x/patterns/appfactories/
    """
    app = Flask(__name__)
    app.config.from_object(config)

    register_extensions(app)
    register_blueprints(app)

    return app