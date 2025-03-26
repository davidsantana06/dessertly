from sqlalchemy import desc
from sqlalchemy.orm import MappedColumn
from typing import TypeVar

from .model import Model


BM = TypeVar("BM", bound="BridgeModel")


class BridgeModel(Model[BM]):
    __abstract__ = True

    primary_id: MappedColumn[int]
    secondary_id: MappedColumn[int]

    @classmethod
    def find_all(cls, primary_id: int) -> list[BM]:
        return (
            cls.query.filter(cls.primary_id == primary_id)
            .order_by(desc(cls.created_at))
            .all()
        )
