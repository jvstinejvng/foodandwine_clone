from .db import db
from datetime import datetime

class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True,  nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(5000), nullable=False)
    img_url = db.Column(db.String(2000), nullable=False)
    total_time = db.Column(db.String(50), nullable=False)
    servings = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(9000), nullable=False)
    directions = db.Column(db.String(9000), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user = db.relationship('User',back_populates='recipes')
    reviews = db.relationship('Review', back_populates='recipes',cascade='all, delete')

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "description": self.description,
            "img_url": self.img_url,
            "total_time": self.total_time,
            "servings": self.servings,
            "ingredients": self.ingredients,
            "directions": self.directions,
            'updated_at': self.updated_at,
            'created_at': self.created_at,
        }