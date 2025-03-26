from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, mapped_column

from app.extension import db

from .base import MainModel


class PaymentMethod(db.Model, MainModel["PaymentMethod"]):
    _SEARCH_BY = ["name"]
    _ORDER_BY = [{"column": "name"}]

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    sales = []

    @property
    def sales_count(self) -> int:
        return len(self.sales)


# from .sale import Sale
