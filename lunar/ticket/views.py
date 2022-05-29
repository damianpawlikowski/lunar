from flask import Blueprint
from flask_apispec import use_kwargs
from flask_apispec import marshal_with
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from lunar.responses import success_response

from lunar.ticket.models import Ticket
from lunar.ticket.constants import STATUSES
from lunar.ticket.constants import TYPES
from lunar.ticket.serializers import TicketSchema

ticket_bp = Blueprint("ticket_bp", __name__, url_prefix="/api/ticket")


@ticket_bp.get("/constants")
def get_ticket_constants():
    output = {}
    output["statuses"] = STATUSES
    output["types"] = TYPES

    return success_response(200, data=output)


@ticket_bp.post("/create")
@use_kwargs(TicketSchema(only=("title", "body", "type")))
@marshal_with(TicketSchema(only=("title", "body", "type")))
@jwt_required()
def create_ticket(title, body, type):
    account_id = get_jwt_identity()
    Ticket.create(
            title=title,
            body=body,
            type=type,
            account_id=account_id,
    )
    return success_response(201, "Ticket has been created.")
