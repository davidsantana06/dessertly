from typing import TypedDict


class _Header(TypedDict):
    icon: str
    title: str


class HeaderMixin:
    _HEADER: _Header
