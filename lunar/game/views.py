from flask import Blueprint

from lunar.game.constants import SEX
from lunar.game.constants import VOCATIONS
from lunar.responses import success_response


game_bp = Blueprint("game_bp", __name__, url_prefix="/api/game")


@game_bp.get("/constants")
def get_game_constants():
    output = {}
    output["vocations"] = VOCATIONS
    output["sex"] = SEX

    return success_response(200, data=output)
