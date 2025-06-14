from sqlalchemy import Column, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

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
        {"column": "quantity_in_grams_or_milliliters"},
        {"column": "current_quantity"},
        {"column": "minimum_quantity"},
    ]

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    quantity_in_grams_or_milliliters = Column(Integer, nullable=False)
    correction_factor = Column(Float, nullable=False)

    recipe_rels: Mapped[list["RecipeIngredient"]] = relationship(
        back_populates="ingredient", cascade="all, delete"
    )

    @property
    def corrected_value(self) -> Float:
        return self.value * self.correction_factor

    @property
    def quantity_in_kilograms_or_liters(self) -> Float:
        return self.quantity_in_grams_or_milliliters / 1000


from .recipe_ingredient import RecipeIngredient
