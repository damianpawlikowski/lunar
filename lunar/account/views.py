from flask import Blueprint
from flask_apispec import use_kwargs
from flask_apispec import marshal_with
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import unset_jwt_cookies
from flask_jwt_extended import create_access_token
from flask_jwt_extended import set_access_cookies

from lunar.extensions import db
from lunar.account.models import Account
from lunar.responses import fail_response
from lunar.responses import success_response
from lunar.ticket.serializers import tickets_schema
from lunar.account.serializers import AccountSchema
from lunar.player.serializers import players_schema
from lunar.account.serializers import account_schema


account_bp = Blueprint("account_bp", __name__, url_prefix="/api/account")


@account_bp.post("/create")
@use_kwargs(AccountSchema(only=("name", "password", "email")))
@marshal_with(AccountSchema(only=("name", "password", "email")))
def create_account(name, password, email):
    try:
        Account.create(name=name, password=password, email=email)
    except IntegrityError:
        db.session.rollback()
        return fail_response(422, "Account name is taken.")
    return success_response(201, "Account has been created.")


@account_bp.post("/login")
@use_kwargs(AccountSchema(only=("name", "password")))
@marshal_with(AccountSchema(only=("name", "password")))
def login_account(name, password):
    account = Account.query.filter(Account.name == name).first()
    if account is None or not account.check_password(password):
        return fail_response(422, "Not a valid account name or password.")

    response = success_response(
        200,
        data=account_schema.dump(account)
    )
    access_token = create_access_token(account)
    set_access_cookies(response, access_token)
    return response


@account_bp.post("/logout")
def logout_account():
    response = success_response(200)
    unset_jwt_cookies(response)
    return response


@account_bp.get("/get")
@jwt_required()
def get_account():
    account = Account.get_by_id(get_jwt_identity())
    return success_response(200, data=account_schema.dump(account))


@account_bp.get("/players")
@jwt_required()
def get_account_players():
    account = Account.get_by_id(get_jwt_identity())
    return success_response(
        200,
        data=players_schema.dump(account.players.all())
    )


@account_bp.get("/tickets")
@jwt_required()
def get_account_tickets():
    account = Account.get_by_id(get_jwt_identity())
    return success_response(
        200,
        data=tickets_schema.dump(account.tickets.all())
    )
