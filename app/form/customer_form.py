from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, TelField
from wtforms.validators import DataRequired, Length, Optional


class CustomerForm(FlaskForm):
    name = StringField(
        label="Nome",
        validators=[DataRequired(), Length(0, 100)],
    )
    cellphone = TelField(
        label="Celular",
        render_kw={"placeholder": "(00) 90000-0000", "data-mask": "(00) 90000-0000"},
        validators=[Optional(), Length(min=15, max=15)],
    )
    telephone = TelField(
        label="Telefone",
        render_kw={"placeholder": "(00) 0000-0000", "data-mask": "(00) 0000-0000"},
        validators=[Optional(), Length(min=14, max=14)],
    )
    instagram = StringField(
        label="Instagram",
        render_kw={
            "placeholder": "@instagram",
            "data-mask": ("@" + "*" * 29),  # ~ 1 @ and 29 characters,
        },
        validators=[Length(0, 30)],
    )
    notes = TextAreaField(label="Notas", validators=[Length(0, 1_000)])
