from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models import User


def user_exists(form, field):
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')

def username_exists(form, field):
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('Username is already in use.')

class SignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField(
        'username', validators=[
            DataRequired(message='Please enter a username.'),
            username_exists,
            Length(max=50, message='Username must be less than 50 characters.'),
            Length(min=5, message='Username must be at least 5 characters long.')
            ])
    email = StringField('email', validators=[DataRequired(), user_exists])
    password = StringField('password', validators=[
        DataRequired(message='Please enter a password.'),
        Length(min=5, message='Password must be at least 5 characters long.'),
        Length(max=30, message='Password must be less than 30 characters.')
        ])
