from lunar.extensions import db
from lunar.utils import IdentifierMixin


class Player(db.Model, IdentifierMixin):
    __tablename__ = "players"

    name = db.Column(db.String(16), nullable=False, unique=True)
    group_id = db.Column(db.Integer, nullable=False, default=1)
    vocation = db.Column(db.Integer, nullable=False, default=0, index=True)
    sex = db.Column(db.Integer, nullable=False, default=0)

    max_health = db.Column(
        "healthmax",
        db.Integer,
        nullable=False,
        default=150,
    )
    max_mana = db.Column("manamax", db.Integer, nullable=False, default=150)

    town_id = db.Column(db.Integer, nullable=False, default=1)

    last_login = db.Column("lastlogin", db.Integer, nullable=False, default=0)
    last_ip = db.Column("lastip", db.Integer, nullable=False, default=0)
    last_logout = db.Column(
        "lastlogout",
        db.Integer,
        nullable=False,
        default=0,
    )
    online_time = db.Column(
        "onlinetime",
        db.Integer,
        nullable=False,
        default=0,
    )

    level = db.Column(db.Integer, nullable=False, default=1)
    experience = db.Column(db.Integer, nullable=False, default=0)
    magic = db.Column("maglevel", db.Integer, nullable=False, default=0)
    fist = db.Column(
        "skill_fist",
        db.Integer,
        nullable=False,
        default=10,
    )
    club = db.Column(
        "skill_club",
        db.Integer,
        nullable=False,
        default=10,
    )
    sword = db.Column(
        "skill_sword",
        db.Integer,
        nullable=False,
        default=10,
    )
    axe = db.Column("skill_axe", db.Integer, nullable=False, default=10)
    dist = db.Column(
        "skill_dist",
        db.Integer,
        nullable=False,
        default=10,
    )
    shielding = db.Column(
        "skill_shielding",
        db.Integer,
        nullable=False,
        default=10,
    )
    fishing = db.Column(
        "skill_fishing",
        db.Integer,
        nullable=False,
        default=10,
    )

    account_id = db.Column(
        db.Integer,
        db.ForeignKey("accounts.id"),
        nullable=False,
    )
