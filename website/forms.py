from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class PseudoLoginForm(FlaskForm):
	id_cliente = StringField('ID do Usuario', validators=[DataRequired(), Length(min=1, max=10)])
	cpf = StringField('CPF', validators=[DataRequired(), Length(min=1, max=14)])
	submit = SubmitField('Entrar')
