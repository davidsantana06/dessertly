from dotenv import load_dotenv
from flask import Flask

from app.model import *
from app.extension import db

from .parameter import Parameter
from .path import Path


class Setup:
    @staticmethod
    def apply_parameters(app: Flask) -> None:
        load_dotenv(Path.ENV_FILE)
        app.config.from_object(Parameter)
        app.static_folder = Path.STATIC_FOLDER
        app.template_folder = Path.TEMPLATE_FOLDER

    @staticmethod
    def init_db(app: Flask) -> None:
        db.init_app(app)
        with app.app_context():
            db.create_all()

    @staticmethod
    def create_default_user(app: Flask) -> None: ...

    @staticmethod
    def register_views(app: Flask) -> None: ...

    @staticmethod
    def inject_jinja_globals(app: Flask) -> None: ...
