from random import choice
from sqlalchemy import Column, Integer, String

from app.extension import db

from .mixin import TimestampMixin


class User(db.Model, TimestampMixin):
    id = Column(Integer, primary_key=True, default=1)
    name = Column(
        String,
        nullable=False,
        default=choice(
            [
                "Águia Majestosa",
                "Cervo Ágil",
                "Gavião Desbravador",
                "Lobo Astuto",
                "Onça Veloz",
                "Puma Destemido",
                "Tigre Sereno",
            ]
        ),
    )
    first_view = Column(String, nullable=False, default="home:index")
    theme = Column(String, nullable=False, default="light")
    zoom = Column(Integer, nullable=False, default=0)

    @classmethod
    def save(cls, user: "User") -> None:
        db.session.add(user)
        db.session.commit()

    @classmethod
    def find_first(cls) -> "User":
        return cls.query.filter(cls.id == 1).first()
