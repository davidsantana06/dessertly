from abc import ABC
from typing import Generic, TypeVar

from app.form import F
from app.model import M


S = TypeVar("S", bound="Service")


class Service(Generic[M, F], ABC):
    _Model: M

    @classmethod
    def get_one(cls, id: int) -> M:
        return cls._Model.find_first(id)

    @classmethod
    def update(cls, id: int, form: F) -> M:
        model = cls.get_one(id)
        form.populate_obj(model)
        cls._Model.save(model)
        return model

    @classmethod
    def delete(cls, id: int) -> M:
        model = cls.get_one(id)
        cls._Model.delete(model)
        return model
