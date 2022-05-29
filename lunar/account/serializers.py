from marshmallow import fields
from marshmallow import validate
from marshmallow import post_dump

from lunar.utils import BaseSchema


class AccountSchema(BaseSchema):
    name = fields.Str(required=True, validate=validate.Length(6, 32))
    password = fields.Str(
        load_only=True,
        required=True,
        validate=validate.Length(min=8),
    )
    type = fields.Int(dump_only=True)
    premium_ends_at = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    creation = fields.Int(dump_only=True)

    @post_dump
    def dump_account(self, data, **kwargs):
        return {"account": data}


account_schema = AccountSchema()
