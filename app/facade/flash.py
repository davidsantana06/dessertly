from flask import flash, get_flashed_messages
from typing import Literal


class Flash:
    @staticmethod
    def append(message: str, category: Literal["danger", "info", "success"]) -> None:
        flash(message, category)

    @classmethod
    def pop_all(cls) -> list[tuple[str, str]]:
        return get_flashed_messages(with_categories=True)
