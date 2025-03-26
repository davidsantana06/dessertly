from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms.validators import DataRequired, NumberRange

from .mixin import StockMixin


class IngredientForm(FlaskForm, StockMixin):
    weight_in_grams = FloatField(
        label="Peso unitário (g)",
        description="Peso por unidade, em gramas",
        render_kw={
            "placeholder": "50",
            "data-mask": "0" * 4,  # ~ 4 numbers
        },
        validators=[DataRequired(), NumberRange(0, 10_000)],
    )
