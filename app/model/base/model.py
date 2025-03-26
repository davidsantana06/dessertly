from flask_sqlalchemy.model import Model as SQLAlchemyModel
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declared_attr
from typing import TypeVar, Generic

from app.extension import db

from ..mixin import TimestampMixin


M = TypeVar("M", bound="Model")


class Model(Generic[M], SQLAlchemyModel, TimestampMixin):
    __abstract__ = True

    @declared_attr
    def id(cls):
        return Column(Integer, primary_key=True, autoincrement=True)

    @classmethod
    def save(cls, model: M) -> None:
        db.session.add(model)
        db.session.commit()

    @staticmethod
    def delete(model: M) -> None:
        db.session.delete(model)
        db.session.commit()

    @classmethod
    def find_first(cls, id: int) -> M:
        return cls.query.filter(cls.id == id).first()
