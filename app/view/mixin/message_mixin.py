from typing import TypedDict


class _Message(TypedDict):
    post: str
    put: str
    delete: str


class MessageMixin:
    _MESSAGE: _Message
