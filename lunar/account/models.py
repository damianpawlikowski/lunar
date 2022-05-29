from datetime import datetime

from lunar.extensions import db
from lunar.utils import text_to_sha1
from lunar.player.models import Player
from lunar.ticket.models import Ticket
from lunar.utils import IdentifierMixin


class Account(db.Model, IdentifierMixin):
    __tablename__ = "accounts"

    name = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.CHAR(40), nullable=False)
    secret = db.Column(db.CHAR(16))
    type = db.Column(db.Integer, nullable=False, default=1)
    premium_ends_at = db.Column(db.Integer, nullable=False, default=0)
    email = db.Column(db.String(255), nullable=False)
    creation = db.Column(
        db.Integer,
        nullable=False,
        default=datetime.timestamp(datetime.utcnow()),
    )

    players = db.relationship(
        Player,
        cascade="all, delete-orphan",
        backref="account",
        lazy="dynamic",
    )
    tickets = db.relationship(
        Ticket,
        cascade="all, delete-orphan",
        backref="requester",
        lazy="dynamic",
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_password(self.password)  # Ugly hack.

    def set_password(self, password):
        """Hash and set password."""
        self.password = text_to_sha1(password)

    def check_password(self, password):
        """Return True if the passed password matches stored hash, otherwise
        return False.
        """
        return self.password == text_to_sha1(password)
