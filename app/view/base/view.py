from abc import ABC
from caseconverter import snakecase
from flask import session
from flask_classful import FlaskView
from typing import Generic

from app.form import F
from app.service import S

from ..mixin import ColumnsMixin, HeaderMixin, ResponseMixin


class View(Generic[S, F], ABC, FlaskView, ColumnsMixin, HeaderMixin, ResponseMixin):
    _Service, _Form = S, F

    @property
    def _module(self) -> str:
        class_ = self.__class__.__name__
        return snakecase(class_[:-4])

    def before_request(self, *_, **__):
        session.update({"module": self._module, "header": self._HEADER})
