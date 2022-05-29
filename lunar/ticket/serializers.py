from marshmallow import fields
from marshmallow import validate
from marshmallow import validates
from marshmallow import post_dump
from marshmallow import ValidationError

from lunar.utils import BaseSchema
from lunar.ticket.constants import TYPES
from lunar.ticket.constants import STATUSES


class TicketSchema(BaseSchema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(max=64))
    body = fields.Str(required=True)
    status = fields.Int(dump_only=True)
    type = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)

    @validates("status")
    def validate_status(self, status):
        if status not in STATUSES:
            raise ValidationError("Not a valid ticket status.")
        return None

    @validates("type")
    def validate_type(self, type):
        if type not in TYPES:
            raise ValidationError("Not a valid ticket type.")
        return None

    @post_dump(pass_many=True)
    def dump_tickets(self, data, **kwargs):
        return {"tickets": data}


ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)
