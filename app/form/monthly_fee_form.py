from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange


class MonthlyFeeForm(FlaskForm):
    name = StringField(
        label="Nome",
        validators=[DataRequired(), Length(1, 100)],
    )
    value = FloatField(
        label="Valor (R$)",
        render_kw={
            "placeholder": "99.99",
            "data-regex": "^[0-9]{1,4}([.][0-9]{0,2})?$",  # ~ 4 numbers and 2 decimals
        },
        validators=[DataRequired(), NumberRange(0, 9_999.99)],
    )
    description = TextAreaField(
        label="Descrição",
        validators=[Length(0, 1_000)],
    )
