import datetime
from sqlalchemy.sql import func
from .db import db, environment, SCHEMA, add_prefix_for_prod
from .user import saved_recipe

class Recipe(db.Model):
    __tablename__ = 'recipes'
    

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String, nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    total_time = db.Column(db.String(50), nullable=False)
    servings = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(10000), nullable=False)
    directions = db.Column(db.String(10000), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow, onupdate=func.now())

    user = db.relationship('User', back_populates='recipes', foreign_keys=[user_id])
    comments = db.relationship('Comment', back_populates='recipe', cascade="all, delete")

    saves = db.relationship('User', secondary=saved_recipe, back_populates='saved_recipes', cascade="all, delete")

    def has_saved_recipe(self, user):
        saved_recipes = [user.id for user in self.saves]
        return user.id in saved_recipes

    def save_recipe(self, user):
        if not self.has_saved_recipe(user):
            self.saves.append(user)

    def unsave_recipe(self, user):
        if self.has_saved_recipe(user):
            self.saves.remove(user)

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
            'saves': [user.to_dict() for user in self.saves]
        }
