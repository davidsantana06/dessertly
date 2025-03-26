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
