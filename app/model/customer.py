from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, mapped_column

from app.extension import db

from .base import MainModel


class Customer(db.Model, MainModel["Customer"]):
    _SEARCH_BY = ["name", "telephone", "cellphone", "instagram", "notes"]
    _ORDER_BY = [
        {"column": "name"},
        {"column": "telephone"},
        {"column": "cellphone"},
        {"column": "instagram"},
        {"column": "notes"},
    ]

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    cellphone = Column(String)
    telephone = Column(String)
    instagram = Column(String)
    notes = Column(String)

    sales = []

    @property
    def sales_count(self) -> int:
        return len(self.sales)


# from .sale import Sale
