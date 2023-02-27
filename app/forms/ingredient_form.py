from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, FloatField
from wtforms.validators import DataRequired, Length

class IngredientForm(FlaskForm):
    amount = StringField('Amount')
    food_stuff = StringField('Food Stuff', validators=[DataRequired(), Length(min=1, max=50)])
    measurement_unit_id = SelectField('Measurement Unit', validators=[DataRequired()], validate_choice=False)
    recipe_id = IntegerField('Recipe', validators=[DataRequired()])
