from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length

class CreateRecipe(FlaskForm):
    user_id = IntegerField('User Id', validators=[DataRequired()])
    title = StringField('title', validators=[DataRequired(), Length(
        min=3, max=255, message='You have exceeded the maximum number of characters allowed.')])
    description = StringField('description', validators=[DataRequired(), Length(
        min=5, max=5000, message='You have exceeded the maximum number of characters allowed.')])
    img_url = StringField('img_url', validators=[DataRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'tiff'])])
    total_time = StringField('total_time', validators=[DataRequired(), Length(min=1, max=20)])
    servings = IntegerField('servings', validators=[DataRequired(), Length(
        min=1, max=50, message='You have exceeded the maximum number of characters allowed.')])
    ingredients = StringField('ingredients', validators=[DataRequired(), Length(
        min=2, max=9000, message='You have exceeded the maximum number of characters allowed.')])
    directions = StringField('directions', validators=[DataRequired(), Length(
        min=2, max=9000, message='You have exceeded the maximum number of characters allowed.')])
  