from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange


class RecipeForm(FlaskForm):
    name = StringField(label="Nome", validators=[DataRequired(), Length(1, 100)])
    category_id = SelectField(
        label="Categoria",
        choices=[("", "Selecione uma categoria")],
        validators=[DataRequired()],
        default="",
    )
    description = TextAreaField(label="Descrição", validators=[Length(0, 1_000)])
    preparation_time_in_minutes = FloatField(
        label="Tempo de preparo (min)",
        description="Tempo de preparo, em minutos",
        render_kw={
            "placeholder": "10",
            "data-mask": "0" * 4,  # ~ 4 numbers
        },
        validators=[DataRequired(), NumberRange(0, 9_999)],
    )
