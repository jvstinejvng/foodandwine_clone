from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length

class RecipeForm(FlaskForm):
    user_id = IntegerField('User Id', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired(), Length(min=5, max=244)])
    description = StringField('Description', validators=[DataRequired(), Length(min=5, max=2000)])
    image_url = StringField("Image")
    total_time = StringField('Total Time', validators=[DataRequired(), Length(min=2, max=50)])
    servings = StringField('Servings', validators=[DataRequired(), Length(min=5, max=50)])
    ingredients = StringField('Description', validators=[DataRequired(), Length(min=5, max=10000)])
    directions = StringField('Description', validators=[DataRequired(), Length(min=5, max=10000)])


