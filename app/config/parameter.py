from .path import Path


class Parameter:
    SECRET_KEY = "Dessertly _ by davidsantana06"

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{Path.DATABASE_FILE}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_ENABLED = False
