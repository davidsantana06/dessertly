from datetime import datetime
from functools import reduce

from app.facade import Template


def _format_datetime(value: datetime) -> str:
    return value.strftime("%d/%m/%Y %H:%M")


def _format_float(value: float) -> str:
    return f"{value:,.2f}".translate(str.maketrans(",.", ".,"))


def _format_int(value: int) -> str:
    return f"{value}"


def format(value: datetime | float | int | str) -> str:
    formatter = {
        "datetime": _format_datetime,
        "float": _format_float,
        "int": _format_int,
    }
    type_ = type(value).__name__
    is_str = type_ == "str"
    return value if is_str else formatter[type_](value)


def get(obj: object, attr: str) -> object:
    parts = attr.split(".")
    return reduce(getattr, parts, obj)


def resolve_layout(template: str) -> str:
    return Template.resolve(f"layout/{template}")


def resolve_macro(template: str) -> str:
    return Template.resolve(f"macro/{template}")


def resolve_partial(template: str) -> str:
    return Template.resolve(f"partial/{template}")
