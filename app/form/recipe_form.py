from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange


class RecipeForm(FlaskForm):
    name = StringField(label="Nome", validators=[DataRequired(), Length(1, 100)])
    preparation_time_in_minutes = FloatField(
        label="Tempo de preparo (min)",
        description="Tempo de preparo, em minutos",
        render_kw={
            "placeholder": "10",
            "data-mask": "0" * 4,  # ~ 4 numbers
        },
        validators=[DataRequired(), NumberRange(0, 10_000)],
    )
    description = TextAreaField(label="Descrição", validators=[Length(0, 1_000)])
