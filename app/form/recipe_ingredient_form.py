from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField
from wtforms.validators import DataRequired, NumberRange


class RecipeIngredientForm(FlaskForm):
    secondary_id = SelectField(
        label="Ingrediente",
        choices=[("", "Selecione um ingrediente")],
        validators=[DataRequired()],
        default="",
    )
    weight_in_grams = FloatField(
        label="Peso (g)",
        description="Peso em gramas",
        render_kw={
            "placeholder": "50",
            "data-mask": "0" * 4,  # ~ 4 numbers
        },
        validators=[DataRequired(), NumberRange(0, 10_000)],
    )
