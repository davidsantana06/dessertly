from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange


class EmployeeForm(FlaskForm):
    name = StringField(label="Nome", validators=[DataRequired(), Length(1, 100)])
    hourly_rate = FloatField(
        label="Taxa horária (R$)",
        description="Valor por hora trabalhada, em reais",
        render_kw={
            "placeholder": "9.99",
            "data-regex": "^[0-9]{1,4}([.][0-9]{0,2})?$",  # ~ 4 numbers and 2 decimals
        },
        validators=[DataRequired(), NumberRange(0, 10_000)],
    )
    notes = TextAreaField(label="Notas", validators=[Length(0, 1_000)])
