from sqlalchemy import Column, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.extension import db

from .base import MainModel
from .mixin import StockMixin


class Ingredient(db.Model, MainModel["Ingredient"], StockMixin):
    _SEARCH_BY = ["name", "brand", "supplier"]
    _ORDER_BY = [
        {"column": "name"},
        {"column": "brand"},
        {"column": "supplier"},
        {"column": "value"},
        {"column": "weight_in_grams"},
        {"column": "current_quantity"},
        {"column": "minimum_quantity"},
    ]

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    weight_in_grams = Column(Integer, nullable=False)

    recipe_rels = []


# from .recipe_ingredient import RecipeIngredient
