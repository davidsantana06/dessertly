from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import DataRequired, Length


class UserForm(FlaskForm):
    name = StringField(label="Nome", validators=[DataRequired(), Length(1, 25)])
    first_view = SelectField(
        label="Tela de abertura",
        choices=[
            ("customer:index", "Clientes (customer:index)"),
            ("employee:index", "Funcionários (employee:index)"),
            ("monthly_fee:index", "Mensalidades (monthly_fee:index)"),
            ("ingredient:index", "Ingredientes (ingredient:index)"),
            ("material:index", "Materiais (material:index)"),
            ("recipe:index", "Receitas (recipe:index)"),
            ("product:index", "Produtos (product:index)"),
            ("payment_method:index", "Métodos de Pagamento (payment_method:index)"),
            ("sale:index", "Vendas (sale:index)"),
        ],
        validators=[DataRequired()],
    )
    theme = SelectField(
        label="Tema",
        choices=[("light", "Claro (light)"), ("dark", "Escuro (dark)")],
        validators=[DataRequired()],
    )
    zoom = SelectField(
        label="Escala de visualização",
        choices=[
            (0, "Padrão (0)"),
            (1, "Levemente ampliado (1)"),
            (2, "Ampliado (2)"),
            (3, "Bem ampliado (3)"),
            (4, "Grande (4)"),
            (5, "Muito grande (5)"),
        ],
        validators=[DataRequired()],
    )
