from sqlalchemy import Column, Float, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extension import db

from .base import BridgeModel


class SaleProduct(db.Model, BridgeModel["SaleProduct"]):
    primary_id: Mapped[int] = mapped_column(ForeignKey("sale.id"))
    secondary_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    quantity = Column(Integer(), nullable=False)
    sell_value = Column(Float(), nullable=False)
    balance_value = Column(Float(), nullable=False)

    sale: Mapped["Sale"] = relationship(back_populates="product_rels")
    product: Mapped["Product"] = relationship(back_populates="sale_rels")

    @property
    def total_sell_value(self) -> float:
        return self.sell_value * self.quantity

    @property
    def total_balance_value(self) -> float:
        return self.balance_value * self.quantity


from .sale import Sale
from .product import Product
