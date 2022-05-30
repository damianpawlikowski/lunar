from datetime import datetime
from datetime import timezone
from datetime import timedelta

from flask_cors import CORS
from flask_wtf import CSRFProtect
from flask_sqlalchemy import Model
from flask_apispec import FlaskApiSpec
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import get_jwt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import create_access_token


# SQLA Object-Relational Mapping
class BaseModel(Model):
    """Base that adds conveience methods for the database operations."""
    @classmethod
    def create(cls, commit=True, **kwargs):
        """Create a new record and save it to the database."""
        instance = cls(**kwargs)
        return instance.save(commit)

    def update(self, commit=True, **kwargs):
        """Update specific fields of the record."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def delete(self, commit=True):
        """Delete the record from the database."""
        db.session.delete(self)
        return commit and db.session.commit()

    def save(self, commit=True):
        """Save the record to the database."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self


db = SQLAlchemy(model_class=BaseModel)


# JSON Web Tokens
jwt = JWTManager()


def refresh_expiring_jwt(response):
    """Instead of refresh token stored in the cookie, JWT is refreshed
    implicitly after every request if it is close to expire. This solution
    is much more secure.
    """
    try:
        expire_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=5))
        if target_timestamp > expire_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        return response


# Cross-Origin Resource Sharing
cors = CORS()


# Cross-site Request Forgery
csrf = CSRFProtect()

# Swagger Docs
docs = FlaskApiSpec()
