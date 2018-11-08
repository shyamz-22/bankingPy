from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.html5 import DecimalField
from wtforms.validators import DataRequired


class AccountForm(FlaskForm):
    amount = DecimalField(places=2, validators=[DataRequired()])
    submit = SubmitField(label='Submit')
