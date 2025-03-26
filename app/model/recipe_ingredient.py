from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extension import db

from .base import BridgeModel


class RecipeIngredient(db.Model, BridgeModel["RecipeIngredient"]):
    primary_id: Mapped[int] = mapped_column(ForeignKey("recipe.id"))
    secondary_id: Mapped[int] = mapped_column(ForeignKey("ingredient.id"))
    weight_in_grams = Column(Integer, nullable=False)

    recipe: Mapped["Recipe"] = relationship(back_populates="ingredient_rels")
    ingredient: Mapped["Ingredient"] = relationship(back_populates="recipe_rels")


from .ingredient import Ingredient
from .recipe import Recipe
