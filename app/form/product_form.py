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
    loss_margin = FloatField(
        label="Margem de perda (%)",
        description="Margem de perda, em porcentagem",
        render_kw={
            "placeholder": "5",
            "data-mask": "0" * 2,  # ~ 2 numbers
        },
        validators=[DataRequired(), NumberRange(0, 100)],
        default=0,
    )
    contribuition_margin = FloatField(
        label="Margem de contribuição (%)",
        description="Margem de contribuição, em porcentagem",
        render_kw={
            "placeholder": "100",
            "data-mask": "0" * 4,  # ~ 4 numbers
        },
        validators=[DataRequired(), NumberRange(0, 10_000)],
        default=0,
    )
