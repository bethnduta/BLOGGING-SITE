from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,PasswordField,validators

class RegisterForm(FlaskForm):
    name = StringField('name',[validators.Length(min=1, max=50)])
    username = StringField('username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6,max=50)])
    password = PasswordField('password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('confirm Password')
    
    class