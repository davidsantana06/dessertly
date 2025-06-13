from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField
from wtforms.validators import DataRequired, NumberRange


class RecipeMaterialForm(FlaskForm):
    secondary_id = SelectField(
        label="Material",
        choices=[("", "Selecione um material")],
        validators=[DataRequired()],
        default="",
    )
    quantity = FloatField(
        label="Quantidade",
        render_kw={
            "placeholder": "1",
            "data-regex": "^[0-9]{1,4}([.][0-9]{0,1})?$",  # ~ 4 numbers and 1 decimal
        },
        validators=[DataRequired(), NumberRange(0, 9_999.9)],
    )
