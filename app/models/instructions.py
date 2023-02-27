from .db import db, environment, SCHEMA, add_prefix_for_prod

class Instruction(db.Model):
    __tablename__ = 'instructions'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('recipes.id')), nullable=False)
    specification = db.Column(db.String(10000), nullable=False)


    #relationships
    recipe = db.relationship('Recipe', back_populates='instructions')

    def to_dict(self):
        return {
            'id': self.id,
            'specification': self.specification,
        }
