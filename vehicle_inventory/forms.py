from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email

#email, password, submit_button
class UserLoginForm(FlaskForm):
    first_name = StringField('First Name', validators= [DataRequired()])    #First name showing up in email column of postgres
    last_name = StringField('Last Name', validators=[DataRequired()])       #Last name not showing up at all
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()