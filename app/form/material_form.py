from flask_wtf import FlaskForm
from .mixin import StockMixin


class MaterialForm(FlaskForm, StockMixin): ...
