from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember_me = BooleanField('Recuerdame')
    submit = SubmitField('Ingresar')


class PostForm(FlaskForm):
	title = StringField('Título', validators=[DataRequired(), Length(min=10, max=32)])
	text = TextAreaField('Publica una actualización', validators=[DataRequired(), Length(min=10, max=255)])
	type = SelectField('Tipo', choices=[('info', 'Informativo'), ('danger', 'Falla o avería'),\
	                      ('success', 'Chequeos y/o reparaciones'), ('warning', 'Avisos y previsiones')])
	submit = SubmitField('<i class="material-icons"></i>check')	