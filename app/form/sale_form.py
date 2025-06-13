from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField
from wtforms.validators import DataRequired, NumberRange


class SaleForm(FlaskForm):
    customer_id = SelectField(
        label="Cliente",
        choices=[("", "Selecione um cliente")],
        validators=[DataRequired()],
        default="",
    )
    payment_method_id = SelectField(
        label="Método de pagamento",
        choices=[("", "Selecione um método de pagamento")],
        validators=[DataRequired()],
        default="",
    )
    freight = FloatField(
        label="Valor do frete (R$)",
        render_kw={
            "placeholder": "9.99",
            "data-regex": "^[0-9]{1,4}([.][0-9]{0,2})?$",  # ~ 4 numbers and 2 decimals}
        },
        validators=[DataRequired(), NumberRange(0, 9_999.99)],
        default=0,
    )
    discount = FloatField(
        label="Desconto (R$)",
        render_kw={
            "placeholder": "9.99",
            "data-regex": "^[0-9]{1,4}([.][0-9]{0,2})?$",  # ~ 4 numbers and 2 decimals}
        },
        validators=[DataRequired(), NumberRange(0, 9_999.99)],
        default=0,
    )
