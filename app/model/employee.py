from sqlalchemy import Column, Float, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extension import db

from .base import MainModel


class Employee(db.Model, MainModel["Employee"]):
    _SEARCH_BY = ["name", "notes"]
    _ORDER_BY = [{"column": "name"}, {"column": "hourly_rate"}, {"column": "notes"}]

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    hourly_rate = Column(Float, nullable=False)
    notes = Column(String)

    products: Mapped[list["Product"]] = relationship(
        back_populates="employee", cascade="all, delete"
    )


from .product import Product
