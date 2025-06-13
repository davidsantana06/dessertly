from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CategoryForm(FlaskForm):
    name = StringField(
        label="Nome",
        validators=[DataRequired(), Length(1, 100)],
        render_kw={"placeholder": "Nome"},
    )
