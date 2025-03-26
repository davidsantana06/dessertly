from sqlalchemy.orm import Mapped, mapped_column

from app.extension import db

from .base import MainModel
from .mixin import StockMixin


class Material(db.Model, MainModel["Material"], StockMixin):
    _SEARCH_BY = ["name", "brand", "supplier"]
    _ORDER_BY = [
        {"column": "name"},
        {"column": "brand"},
        {"column": "supplier"},
        {"column": "value"},
        {"column": "current_quantity"},
        {"column": "minimum_quantity"},
    ]

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    recipe_rels = []


# from .recipe_material import RecipeMaterial
