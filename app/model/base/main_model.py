from sqlalchemy import ColumnElement, asc, desc, or_
from typing import Literal, NotRequired, TypedDict, TypeVar

from .model import Model


MM = TypeVar("MM", bound="MainModel")


class _Ordering(TypedDict):
    column: str
    direction: NotRequired[Literal["asc", "desc"]]


class MainModel(Model[MM]):
    __abstract__ = True

    _SEARCH_BY: list[str]
    _ORDER_BY: list[_Ordering]

    @classmethod
    def __mount_filters(cls, search: str) -> list[ColumnElement[bool]]:
        return [
            getattr(cls, column).icontains(search)  # ~ cls.{column}.icontains({search})
            for column in cls._SEARCH_BY
        ]

    @classmethod
    def __mount_orderings(cls) -> list[ColumnElement]:
        return [
            globals()[ordering.get("direction", "asc")](  # ~ asc(...) or desc(...)
                getattr(cls, ordering["column"])  # ~ cls.{column}
            )
            for ordering in cls._ORDER_BY
        ]

    @classmethod
    def find_all(cls, search: str = "") -> list[MM]:
        filters = cls.__mount_filters(search) if search else []
        orderings = cls.__mount_orderings()
        return (
            cls.query.filter(or_(*filters))
            .order_by(*orderings, asc(cls.created_at))
            .all()
        )
