from .db import db, environment, SCHEMA, add_prefix_for_prod

class MeasurementUnit(db.Model):
    __tablename__ = 'measurement_units'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    unit = db.Column(db.String(50), nullable=False)

    #relationships
    ingredient = db.relationship('Ingredient', back_populates='unit')

    def to_dict(self):
        return {
            'id': self.id,
            'unit': self.unit,
        }
