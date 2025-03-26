from sqlalchemy import Column, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extension import db

from .base import BridgeModel


class RecipeMaterial(db.Model, BridgeModel["RecipeMaterial"]):
    primary_id: Mapped[int] = mapped_column(ForeignKey("recipe.id"))
    secondary_id: Mapped[int] = mapped_column(ForeignKey("material.id"))
    quantity = Column(Float, nullable=False)

    recipe: Mapped["Recipe"] = relationship(back_populates="material_rels")
    material: Mapped["Material"] = relationship(back_populates="recipe_rels")


from .recipe import Recipe
from .material import Material
