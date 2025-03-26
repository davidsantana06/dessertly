from sqlalchemy import Column, Float, String
from app.extension import db
from .base import MainModel


class MonthlyFee(db.Model, MainModel["MonthlyFee"]):
    _SEARCH_BY = ["name", "description"]
    _ORDER_BY = [{"column": "name"}, {"column": "value"}, {"column": "description"}]

    name = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    description = Column(String)

    @property
    def daily_rate(self) -> float:
        days_per_month = 30.44
        return self.value / days_per_month

    @property
    def hourly_rate(self) -> float:
        hours_per_day = 24
        return self.daily_rate / hours_per_day
