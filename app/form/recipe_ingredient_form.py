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
    quantity_in_grams_or_milliliters = FloatField(
        label="Quantidade (g/ml)",
        description="Quantidade, em gramas ou mililitros",
        render_kw={
            "placeholder": "50",
            "data-mask": "0" * 5,  # ~ 5 numbers
        },
        validators=[DataRequired(), NumberRange(0, 99_999)],
    )
