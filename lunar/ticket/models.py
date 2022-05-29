from datetime import datetime

from lunar.extensions import db
from lunar.utils import IdentifierMixin


class Ticket(db.Model, IdentifierMixin):
    __tablename__ = "tickets"

    title = db.Column(db.String(64), nullable=False)
    body = db.Column(db.Text, nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)
    type = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow(),
    )

    account_id = db.Column(
        db.Integer,
        db.ForeignKey("accounts.id"),
        nullable=False,
    )
