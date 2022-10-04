from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class CreateRecipe(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(min=5, max=50)])
    description = StringField('description', validators=[DataRequired(), Length(min=10)])
    image_url = StringField('image_url', validators=[DataRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'tiff'])])
    total_time = StringField('total_time', validators=[DataRequired(), Length(min=1, max=50)])
    servings = StringField('servings', validators=[DataRequired(), Length(min=1)])
    ingredients = StringField('ingredients', validators=[DataRequired(), Length(min=2)])
    directions = StringField('directions', validators=[DataRequired(), Length(min=10)])
  