from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extension import db

from .base import MainModel


class Product(db.Model, MainModel["Product"]):
    _SEARCH_BY = ["name"]
    _ORDER_BY = [
        {"column": "name"},
        {"column": "loss_margin"}, 
        {"column": "contribuition_margin"},
    ]

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipe.id"), nullable=False)
    employee_id: Mapped[int] = mapped_column(ForeignKey("employee.id"), nullable=False)
    name = Column(String, nullable=False)
    loss_margin = Column(Integer, nullable=False)
    contribuition_margin = Column(Integer, nullable=False)

    recipe: Mapped["Recipe"] = relationship(back_populates="products")
    employee: Mapped["Employee"] = relationship(back_populates="products")
    sale_rels = []

    @property
    def monthly_fees_value(self) -> float:
        monthly_fees = MonthlyFee.find_all()
        value = sum(
            (monthly_fee.hourly_rate * self.recipe.preparation_time_in_hours)
            for monthly_fee in monthly_fees
        )
        return value or 0.0

    @property
    def employee_value(self) -> float:
        return self.employee.hourly_rate * self.recipe.preparation_time_in_hours

    @property
    def cost_value(self) -> float:
        return (
            self.monthly_fees_value
            + self.recipe.ingredients_value
            + self.recipe.materials_value
            + self.employee_value
        )

    @property
    def loss_value(self) -> float:
        return self.cost_value * (self.loss_margin / 100)

    @property
    def contribuition_value(self) -> float:
        return self.cost_value * (self.contribuition_margin / 100)

    @property
    def sell_value(self) -> float:
        return self.cost_value + self.contribuition_value - self.loss_value

    @property
    def balance_value(self) -> float:
        return self.sell_value - self.cost_value


from .employee import Employee
from .monthly_fee import MonthlyFee
from .recipe import Recipe
# from .sale_product import SaleProduct
