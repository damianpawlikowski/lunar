from flask_cors import CORS
from flask_sqlalchemy import Model
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


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
jwt.user_identity_loader(lambda account: account.id)


# Cross-Origin Resource Sharing
cors = CORS()
