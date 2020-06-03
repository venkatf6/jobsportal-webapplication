# project/server/user/forms.py


from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms import TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(Form):
    email = StringField('Email Address', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])


class RegisterForm(Form):
    email = StringField('Email Address',validators=[DataRequired(), Email(message=None), Length(min=6, max=40)])
    password = PasswordField('Password',validators=[DataRequired(), Length(min=6, max=25)])
    confirm = PasswordField('Confirm password',validators=[DataRequired(),EqualTo('password', message='Passwords needs match.')])

class ProfileForm(Form):
    email = StringField('Email Address',validators=[DataRequired(), Email(message=None), Length(min=6, max=40)])
    phonenumber = StringField('Phone number', validators=[DataRequired(),Length(min=6,max=10)])
    skillset  = TextAreaField('Skills',validators=[DataRequired()])
    zipcode = StringField('Zip Code', validators=[DataRequired(),Length(min=3, max=5)])
    notifications = StringField('Notification Yes/No',validators=[DataRequired()])
    
    