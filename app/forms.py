from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import InputRequired

class UserForm(FlaskForm):
    firstname = StringField('FirstName', validators=[InputRequired()])
    lastname = StringField('LastName', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    age = IntegerField('Age', validators=[InputRequired()])
    gender = StringField('Gender', validators=[InputRequired])
    bio = StringField('Bio')
    dp = StringField('Dp', validators=[InputRequired])
