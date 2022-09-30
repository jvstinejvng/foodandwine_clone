from .db import db
from datetime import datetime


class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(1500), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user = db.relationship('User', back_populates='reviews')
    recipes = db.relationship('Recipe', back_populates='reviews')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'recipe_id': self.recipe_id,
            'stars': self.stars,
            'comment': self.comment,
            'updated_at': self.updated_at,
            'created_at': self.created_at,
            'user': self.user.to_dict()
        }
