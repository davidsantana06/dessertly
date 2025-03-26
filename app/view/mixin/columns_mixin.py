from typing import TypedDict


class _Column(TypedDict):
    icon: str
    title: str
    attr: str


class ColumnsMixin:
    _INDEX_COLUMNS: list[_Column] | None
    _SHOW_COLUMNS: list[_Column]
