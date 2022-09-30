from flask_wtf import FlaskForm
from wtforms.fields import ( TextAreaField, DateTimeField, IntegerField)
from wtforms.validators import DataRequired
from datetime import datetime


class CreateReview(FlaskForm):
    user_id = IntegerField("User Id", validators=[DataRequired()])
    recipe_id = IntegerField("Recipe Id", validators=[DataRequired()])
    stars = IntegerField("Stars", validators=[DataRequired()])
    comment = TextAreaField("Comment", validators=[DataRequired()])
    created_at = DateTimeField("Created At", default=datetime.utcnow, validators=[DataRequired()])
    updated_at = DateTimeField("Updated At", default=datetime.utcnow, validators=[DataRequired()])
