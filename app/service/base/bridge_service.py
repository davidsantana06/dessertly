from abc import ABC, abstractmethod
from typing import TypeVar

from app.form import F
from app.model import BM

from .service import Service


BS = TypeVar("BS", bound="BridgeService")


class BridgeService(Service[BM, F], ABC):
    _Model: BM

    @classmethod
    def create(cls, form: F, primary_id: int) -> BM:
        model = cls._Model()
        model.primary_id = primary_id
        form.populate_obj(model)
        cls._Model.save(model)
        return model

    @classmethod
    def get_all(cls, primary_id: int) -> list[BM]:
        return cls._Model.find_all(primary_id)

    @staticmethod
    @abstractmethod
    def fill(form: F, model: BM | None = None) -> None: ...
