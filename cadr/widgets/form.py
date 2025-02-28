from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField
from wtforms.validators import InputRequired, ValidationError, DataRequired,Regexp, Email, EqualTo, Length



class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[InputRequired(u'Поиск'),
        Regexp('[а-яА-я]+', message=u'Имя курса должно содержать только буквы'),
        Length(min=3, max=100, message=u'от 3 символов')])
        
class AskForm(FlaskForm):
    name = StringField(u"Name", validators=[InputRequired(u'Поиск'),
        Regexp('[а-яА-я]+', message=u'Имя должно содержать только буквы'),
        Length(min=2, max=100, message=u'от 2 символов')])
    phone = StringField(u'Phone', validators=[InputRequired(u'Поиск'),
        Length(min=2, max=100, message=u'от 2 символов')])
    textArea = TextAreaField(u'Text', validators=[Length( max=30, message=u'максимум 100 символов')])    
    submit = SubmitField(u"Отправить заявку")
    


    