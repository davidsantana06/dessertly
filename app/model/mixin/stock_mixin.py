from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declared_attr


class StockMixin:
    @declared_attr
    def name(cls):
        return Column(String, nullable=False)

    @declared_attr
    def brand(cls):
        return Column(String)

    @declared_attr
    def supplier(cls):
        return Column(String)

    @declared_attr
    def value(cls):
        return Column(Float, nullable=False)

    @declared_attr
    def minimum_quantity(cls):
        return Column(Integer, nullable=False)

    @declared_attr
    def current_quantity(cls):
        return Column(Float, nullable=False)

    @property
    def is_missing(self) -> bool:
        return self.current_quantity < self.minimum_quantity

    @property
    def quantity_to_restock(self) -> int:
        if not self.is_missing:
            return 0
        return self.minimum_quantity - self.current_quantity
