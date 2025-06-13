from sqlalchemy import ColumnElement, UnaryExpression, asc, desc, or_
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
        filters = []
        for column in cls._SEARCH_BY:
            attr = getattr(cls, column)
            filters.append(attr.icontains(search))
        return filters

    @classmethod
    def __mount_orderings(cls) -> list[UnaryExpression]:
        orderings = []
        for ordering in cls._ORDER_BY:
            column = ordering["column"]
            direction = ordering.get("direction", "asc")
            attr = getattr(cls, column)
            direction_func = globals()[direction]
            orderings.append(direction_func(attr))
        return orderings

    @classmethod
    def find_all(cls, search: str = "") -> list[MM]:
        filters = cls.__mount_filters(search) if search else []
        orderings = cls.__mount_orderings()
        return (
            cls.query.filter(or_(*filters))
            .order_by(*orderings, asc(cls.created_at))
            .all()
        )
