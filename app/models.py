from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Bakery(db.Model, SerializerMixin):
    pass

class BakedGood(db.Model, SerializerMixin):
    pass
