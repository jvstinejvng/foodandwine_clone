from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError, Length
from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('This email address is already exists. Please use another.')


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('This username is already exists. Please use another.')

def password_length(form, field):
    password = field.data
    if len(password) < 6:
        raise ValidationError("Password must be 6 characters or more.")


class SignUpForm(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired(message='Please enter a username'), username_exists])
    email = StringField('email', validators=[DataRequired(message='Please enter your email'), Email(message='* Please enter a valid email address'), user_exists])
    password = StringField('password', validators=[
                           DataRequired('Password is required.'), password_length, Length(max=200, message='Password length cannot exceed 200 characters.')])
