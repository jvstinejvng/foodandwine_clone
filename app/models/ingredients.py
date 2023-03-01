from .db import db, environment, SCHEMA, add_prefix_for_prod

class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.String, nullable=False)
    food_stuff = db.Column(db.String(100), nullable=False)
    measurement_unit_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('measurement_units.id')), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)

    #relationships
    recipe = db.relationship('Recipe', back_populates='ingredients')
    unit = db.relationship('MeasurementUnit', back_populates='ingredient')

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'food_stuff': self.food_stuff,
            'measurement_unit': self.unit.to_dict(),
        }
