from abc import ABC
from typing import TypeVar

from app.form import F
from app.model import MM

from .service import Service


MS = TypeVar("MS", bound="MainService")


class MainService(Service[MM, F], ABC):
    _Model: MM

    @classmethod
    def create(cls, form: F) -> MM:
        model = cls._Model()
        form.populate_obj(model)
        cls._Model.save(model)
        return model

    @classmethod
    def get_all(cls, search: str = "") -> list[MM]:
        return cls._Model.find_all(search)

    @classmethod
    def fill(cls, id: int, form: F) -> MM:
        model = cls.get_one(id)
        form.process(obj=model)
        return model
