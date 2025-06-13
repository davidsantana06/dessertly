from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extension import db

from .base import MainModel


class Recipe(db.Model, MainModel["Recipe"]):
    _SEARCH_BY = ["name", "description"]
    _ORDER_BY = [
        {"column": "name"},
        {"column": "preparation_time_in_minutes"},
        {"column": "description"},
    ]

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"), nullable=False)
    name = Column(String, nullable=False)
    preparation_time_in_minutes = Column(Integer, nullable=False)
    description = Column(String)

    category: Mapped["Category"] = relationship(back_populates="recipes")
    ingredient_rels: Mapped[list["RecipeIngredient"]] = relationship(
        back_populates="recipe", cascade="all, delete"
    )
    material_rels: Mapped[list["RecipeMaterial"]] = relationship(
        back_populates="recipe", cascade="all, delete"
    )
    products: Mapped[list["Product"]] = relationship(
        back_populates="recipe", cascade="all, delete"
    )

    @property
    def preparation_time_in_hours(self) -> float:
        minutes_per_hour = 60
        return self.preparation_time_in_minutes / minutes_per_hour

    @property
    def ingredients_value(self) -> float:
        value = sum(
            (
                ingredient_rel.weight_in_grams
                / ingredient_rel.ingredient.weight_in_grams
                * ingredient_rel.ingredient.corrected_value
            )
            for ingredient_rel in self.ingredient_rels
        )
        return value or 0.0

    @property
    def materials_value(self) -> float:
        value = sum(
            (material_rel.material.value * material_rel.quantity)
            for material_rel in self.material_rels
        )
        return value or 0.0


from .category import Category
from .product import Product
from .recipe_ingredient import RecipeIngredient
from .recipe_material import RecipeMaterial
