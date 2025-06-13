from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extension import db

from .base import MainModel


class Category(db.Model, MainModel["Category"]):
    _SEARCH_BY = ["name"]
    _ORDER_BY = [{"column": "name"}]

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    recipes: Mapped[list["Recipe"]] = relationship(
        back_populates="category", cascade="all, delete"
    )

    @property
    def recipes_count(self) -> int:
        return len(self.recipes)


from .recipe import Recipe
