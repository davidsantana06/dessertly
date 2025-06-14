from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms.validators import DataRequired, NumberRange

from .mixin import StockMixin


class IngredientForm(FlaskForm, StockMixin):
    quantity_in_grams_or_milliliters = FloatField(
        label="Quantidade por unidade (g/ml)",
        description="Quantidade por unidade, em gramas ou mililitros",
        render_kw={
            "placeholder": "50",
            "data-mask": "0" * 5,  # ~ 5 numbers
        },
        validators=[DataRequired(), NumberRange(0, 99_999)],
    )
    correction_factor = FloatField(
        label="Fator de correção",
        render_kw={
            "placeholder": "1.00",
            "data-regex": "^[0-9]{1,4}([.][0-9]{0,2})?$",  # ~ 4 numbers and 2 decimals
        },
        validators=[DataRequired(), NumberRange(0, 9_999.99)],
        default=1.00,
    )
