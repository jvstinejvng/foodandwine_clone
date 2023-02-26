import datetime
from sqlalchemy.sql import func
from .db import db, environment, SCHEMA, add_prefix_for_prod

class Comment(db.Model):
    __tablename__ = 'comments'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    body = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('recipes.id')), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow, onupdate=func.now())

    recipe = db.relationship('Recipe', back_populates='comments')
    user = db.relationship('User', back_populates='comments', foreign_keys=[user_id])

    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'body': self.body,
            'user': self.user.to_dict(),
            'recipe_id': self.recipe_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
