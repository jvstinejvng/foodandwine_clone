from .db import db
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    # first_name = db.Column(db.String(100), nullable=False)
    # last_name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
 
    recipes = db.relationship('Recipe', back_populates='user', foreign_keys='[Recipe.user_id]')
    comments = db.relationship('Comment', back_populates='user', foreign_keys='[Comment.user_id]')

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }

