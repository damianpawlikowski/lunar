from flask import Blueprint
from flask_apispec import use_kwargs
from flask_apispec import marshal_with
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from lunar.extensions import db
from lunar.player.models import Player
from lunar.game.constants import SKILLS
from lunar.responses import fail_response
from lunar.game.constants import VOCATIONS
from lunar.responses import success_response
from lunar.player.serializers import PlayerSchema
from lunar.player.serializers import players_schema


player_bp = Blueprint("player_bp", __name__, url_prefix="/api/player")


@player_bp.post("/create")
@use_kwargs(PlayerSchema(only=("name", "vocation", "sex")))
@marshal_with(PlayerSchema(only=("name", "vocation", "sex")))
@jwt_required()
def create_player(name, vocation, sex):
    account_id = get_jwt_identity()
    try:
        Player.create(
            name=name,
            vocation=vocation,
            sex=sex,
            account_id=account_id,
        )
    except IntegrityError:
        db.session.rollback()
        return fail_response(422, "Player name is taken.")
    return success_response(201, "Player has been created.")


@player_bp.get("/highscores/<int:skill_id>/<int:count>")
def get_highscores(skill_id, count):
    if skill_id not in SKILLS:
        return fail_response(422, "Not a valid skill.")
    column = getattr(Player, SKILLS[skill_id])
    query = Player.query.with_entities(
        Player.name,
        Player.vocation,
        column,
    ).order_by(column.desc()).limit(count).all()

    output = players_schema.dump(query)
    output["skill"] = SKILLS[skill_id]

    return success_response(200, data=output)


@player_bp.get("/highscores/<int:vocation_id>/<int:skill_id>/<int:count>")
def get_highscores_by_vocation(vocation_id, skill_id, count):
    if vocation_id not in VOCATIONS:
        return fail_response(422, "Not a valid vocation.")
    if skill_id not in SKILLS:
        return fail_response(422, "Not a valid skill.")
    column = getattr(Player, SKILLS[skill_id])
    query = Player.query.with_entities(
        Player.name,
        Player.vocation,
        column,
    ).filter(Player.vocation == vocation_id).order_by(column.desc()).limit(
        count).all()

    output = players_schema.dump(query)
    output["skill"] = SKILLS[skill_id]
    output["vocation"] = VOCATIONS[vocation_id]["name"]

    return success_response(200, data=output)
