from .db import db
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

#saved/liked recipes join table
saved_recipe = db.Table(
    "saved_recipes",
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("recipe_id", db.Integer, db.ForeignKey("recipes.id"), primary_key=True)
)

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    # first_name = db.Column(db.String(100), nullable=False)
    # last_name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    recipes = db.relationship('Recipe', back_populates='user', foreign_keys='[Recipe.user_id]')
    comments = db.relationship('Comment', back_populates='user', foreign_keys='[Comment.user_id]')
    saved_recipes = db.relationship('Recipe', secondary=saved_recipe, back_populates='saves')

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

    def to_dict_with_saves(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'saved_recipes': self.saved_recipes
        }


