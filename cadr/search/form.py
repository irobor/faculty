from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, ValidationError, DataRequired, Email, EqualTo, Length



class SearchFormIndex(FlaskForm):
    searched = StringField("Searched", validators=[Length(min=3, max=100, message=u'от 3 символов')])