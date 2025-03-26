from abc import ABC, abstractmethod
from app.model import MainModel


class SelectChoicesMixin(ABC):
    @classmethod
    @abstractmethod
    def get_all(cls, search: str = "") -> list[MainModel]: ...

    @classmethod
    def get_select_choices(cls) -> list[tuple[int, str]]:
        models = cls.get_all()
        return [(model.id, model.name) for model in models]
