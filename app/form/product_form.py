from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, StringField
from wtforms.validators import DataRequired, Length, NumberRange


class ProductForm(FlaskForm):
    name = StringField(
        label="Nome",
        validators=[DataRequired(), Length(1, 100)],
    )
    recipe_id = SelectField(
        label="Receita",
        choices=[("", "Selecione uma receita")],
        validators=[DataRequired()],
        default="",
    )
    employee_id = SelectField(
        label="Funcionário",
        choices=[("", "Selecione um funcionário")],
        validators=[DataRequired()],
        default="",
    )
    contribuition_margin = FloatField(
        label="Margem de contribuição (%)",
        description="Margem de contribuição, em porcentagem",
        render_kw={
            "placeholder": "100",
            "data-mask": "0" * 4,  # ~ 4 numbers
        },
        validators=[DataRequired(), NumberRange(0, 9_999)],
        default=0,
    )
