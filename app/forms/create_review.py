from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class CreateReview(FlaskForm):
    stars = IntegerField("stars", validators=[DataRequired()])
    review = StringField("review")
    user_id = IntegerField("user", validators=[DataRequired()])
    recipe_id = IntegerField("recipe id", validators=[DataRequired()])
