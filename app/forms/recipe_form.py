from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length

class CreateRecipe(FlaskForm):
    user_id = IntegerField('User Id', validators=[DataRequired()])
    title = StringField('title', validators=[DataRequired(), Length(min=5, max=100)])
    description = TextAreaField('description', validators=[DataRequired(), Length(min=10, max=3000)])
    image_url = StringField('image_url', validators=[DataRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'tiff'])])
    total_time = StringField('total_time', validators=[DataRequired(), Length(min=1, max=100)])
    servings = StringField('servings', validators=[DataRequired(), Length(min=1, max=100)])
    ingredients = TextAreaField('ingredients', validators=[DataRequired(), Length(min=2, max=9000)])
    directions = TextAreaField('directions', validators=[DataRequired(), Length(min=2, max=9000)])
  