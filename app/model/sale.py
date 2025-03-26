from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extension import db

from .base import MainModel


class Sale(db.Model, MainModel["Sale"]):
    _SEARCH_BY = ["status", "created_at"]
    _ORDER_BY = [{"column": "created_at", "direction": "desc"}]

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"), nullable=False)
    payment_method_id: Mapped[int] = mapped_column(
        ForeignKey("payment_method.id"), nullable=False
    )
    freight = Column(Float, nullable=False)
    discount = Column(Float, nullable=False)
    status = Column(String, nullable=False, default="Pendente")

    customer: Mapped["Customer"] = relationship(back_populates="sales")
    payment_method: Mapped["PaymentMethod"] = relationship(back_populates="sales")
    product_rels: Mapped[list["SaleProduct"]] = relationship(
        back_populates="sale", cascade="all, delete"
    )

    @property
    def code(self) -> str:
        year, month, day = (
            self.created_at.year % 100,
            self.created_at.month,
            self.created_at.day,
        )
        filled_id = str(self.id).zfill(5)
        return f"{year:02}{month:02}{day:02}{filled_id}"

    @property
    def sell_value(self) -> float:
        value = sum(product_rel.total_sell_value for product_rel in self.product_rels)
        return value or 0.0

    @property
    def balance_value(self) -> float:
        value = sum(
            product_rel.total_balance_value for product_rel in self.product_rels
        )
        return value or 0.0

    @property
    def total_sell_value(self) -> float:
        return self.sell_value + self.freight - self.discount

    @property
    def total_balance_value(self) -> float:
        return self.balance_value - self.discount

    @property
    def is_pending(self) -> bool:
        return self.status == "Pendente"

    @property
    def is_concludable(self) -> bool:
        return self.is_pending and self.product_rels

    @property
    def is_concluded(self) -> bool:
        return self.status == "Concluída"


from .customer import Customer
from .payment_method import PaymentMethod
from .sale_product import SaleProduct
