import hashlib

from marshmallow import Schema
from marshmallow import EXCLUDE

from lunar.extensions import db


class IdentifierMixin:
    """Mixin that adds integer "id" column declared as primary key to any
    SQLA declarative-mapped class.
    """
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def get_by_id(cls, id):
        """Get a record by id from the session identity map. If not present,
        SELECT will be performed in order to locate it.

        ``record = Model.get_by_id(43)``
        """
        return db.session.get(cls, id)

    @classmethod
    def filter_by_ids(cls, ids):
        """Filter records by identifiers and return them as a list of tuples.
        Identifiers can be passed as list, tuple or set of ints.

        ``records = Model.filter_by_ids([12, 71, 43])``
        """
        return cls.query.filter(cls.id.in_(ids)).all()


def text_to_sha1(text):
    if not isinstance(text, str):
        return None
    return hashlib.sha1(text.encode()).hexdigest()


class BaseSchema(Schema):
    """Base schema to avoid constant repeating."""
    class Meta:
        strict = True
        unknown = EXCLUDE
