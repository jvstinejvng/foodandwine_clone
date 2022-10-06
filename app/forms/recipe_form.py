from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length

class RecipeForm(FlaskForm):
    user_id = IntegerField('User Id', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired(), Length(min=5, max=50)])
    description = StringField('Description', validators=[DataRequired(), Length(min=5, max=2000)])
    image_url = StringField("Image")
    total_time = StringField('Total Time', validators=[DataRequired()])
    servings = StringField('Servings', validators=[DataRequired()])
    ingredients = StringField('Description', validators=[DataRequired(), Length(min=5, max=10000)])
    directions = StringField('Description', validators=[DataRequired(), Length(min=5, max=10000)])


