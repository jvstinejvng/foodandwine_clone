from .db import db
from datetime import datetime

class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True,  nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(3000), nullable=False)
    image_url = db.Column(db.String, nullable=False)
    total_time = db.Column(db.String(100), nullable=False)
    servings = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(9000), nullable=False)
    directions = db.Column(db.String(9000), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user = db.relationship('User',back_populates='recipes',  foreign_keys=[user_id])
    reviews = db.relationship('Review', back_populates='recipes',cascade='all, delete')

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "description": self.description,
            "image_url": self.image_url,
            "total_time": self.total_time,
            "servings": self.servings,
            "ingredients": self.ingredients,
            "directions": self.directions,
            'updated_at': self.updated_at,
            'created_at': self.created_at,
        }