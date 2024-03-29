from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length

class InstructionForm(FlaskForm):
    recipe_id = IntegerField('Recipe', validators=[DataRequired()])
    specification = StringField('Specification', validators=[DataRequired(), Length(min=1, max=10000)])
