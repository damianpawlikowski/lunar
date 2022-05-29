from marshmallow import fields
from marshmallow import validate
from marshmallow import post_dump
from marshmallow import validates
from marshmallow import ValidationError

from lunar.utils import BaseSchema
from lunar.game.constants import SEX
from lunar.game.constants import VOCATIONS


class PlayerSchema(BaseSchema):
    name = fields.Str(required=True, validate=validate.Length(min=3))
    group_id = fields.Int(dump_only=True)
    vocation = fields.Int(required=True)
    sex = fields.Int(required=True)

    max_health = fields.Int(dump_only=True)
    max_mana = fields.Int(dump_only=True)

    town_id = fields.Int(dump_only=True)

    last_login = fields.Int(dump_only=True)
    last_ip = fields.Int(dump_only=True)
    last_logout = fields.Int(dump_only=True)
    online_time = fields.Int(dump_only=True)

    level = fields.Int(dump_only=True)
    experience = fields.Int(dump_only=True)
    magic = fields.Int(dump_only=True)
    fist = fields.Int(dump_only=True)
    club = fields.Int(dump_only=True)
    sword = fields.Int(dump_only=True)
    axe = fields.Int(dump_only=True)
    dist = fields.Int(dump_only=True)
    shielding = fields.Int(dump_only=True)
    fishing = fields.Int(dump_only=True)

    @validates("vocation")
    def validate_vocation(self, vocation):
        if vocation not in VOCATIONS:
            raise ValidationError("Not a valid player vocation.")
        return None

    @validates("sex")
    def validate_sex(self, sex):
        if sex not in SEX:
            raise ValidationError("Not a valid player sex.")
        return None

    @post_dump(pass_many=True)
    def dump_players(self, data, **kwargs):
        return {"players": data}


player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)
