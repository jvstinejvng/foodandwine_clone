import datetime
from sqlalchemy.sql import func
from .db import db

class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    total_time = db.Column(db.String(50), nullable=False)
    servings = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(10000), nullable=False)
    directions = db.Column(db.String(10000), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow, onupdate=func.now())

    user = db.relationship('User', back_populates='recipes', foreign_keys=[user_id])
    comments = db.relationship('Comment', back_populates='recipe', cascade="all, delete")

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user.to_dict(),
            'title': self.title,
            'image_url': self.image_url,
            'description': self.description,
            'total_time': self.total_time,
            'servings': self.servings,
            'ingredients': self.ingredients,
            'directions': self.directions,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
    
            'comments': [comment.to_dict() for comment in self.comments],
        }
