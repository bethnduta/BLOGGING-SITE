from app import db
from app import bcrypt


class Blog(db.Model):
    id = db.Column(db.Integer(), primay_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)