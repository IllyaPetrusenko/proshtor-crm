from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class NewUser(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    user_phone = StringField('User phone')
    user_email = StringField('User email')
    submit = SubmitField('Create')

