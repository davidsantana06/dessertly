from sqlalchemy.orm import Mapped, mapped_column, relationship

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

    recipe_rels: Mapped[list["RecipeMaterial"]] = relationship(
        back_populates="material", cascade="all, delete"
    )


from .recipe_material import RecipeMaterial
