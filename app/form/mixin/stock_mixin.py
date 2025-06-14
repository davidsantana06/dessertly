from wtforms import FloatField, StringField
from wtforms.validators import DataRequired, Length, NumberRange


class StockMixin:
    name = StringField(label="Nome", validators=[DataRequired(), Length(1, 100)])
    brand = StringField(label="Marca", validators=[Length(0, 100)])
    supplier = StringField(label="Fornecedor", validators=[Length(0, 100)])
    value = FloatField(
        label="Valor unitário (R$)",
        render_kw={
            "placeholder": "9.99",
            "data-regex": "^[0-9]{1,4}([.][0-9]{0,2})?$",  # ~ 4 numbers and 2 decimals
        },
        validators=[DataRequired(), NumberRange(0, 9_999.99)],
    )
    minimum_quantity = FloatField(
        label="Quantidade mínima em estoque",
        render_kw={
            "placeholder": "1",
            "data-mask": "0" * 4,  # ~ 4 numbers
        },
        validators=[DataRequired(), NumberRange(0, 9999)],
        default=0,
    )
    current_quantity = FloatField(
        label="Quantidade atual em estoque",
        render_kw={
            "placeholder": "10",
            "data-regex": "^[0-9]{1,4}([.][0-9]{0,1})?$",  # ~ 4 numbers and 1 decimal
        },
        validators=[DataRequired(), NumberRange(0, 9_999.9)],
        default=0,
    )
