from dotenv import load_dotenv
from flask import Flask, session

from app.model import *
from app.extension import db
from app.facade import Flash, Url
from app.jinja import *
from app.service import UserService
from app.view import (
    CategoryView,
    CustomerView,
    EmployeeView,
    HomeView,
    IngredientView,
    MaterialView,
    MonthlyFeeView,
    PaymentMethodView,
    ProductView,
    RecipeIngredientView,
    RecipeMaterialView,
    RecipeView,
    SaleProductView,
    SaleView,
    UserView,
)

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
    def create_default_user(app: Flask) -> None:
        with app.app_context():
            UserService.get() or UserService.create()

    @staticmethod
    def register_views(app: Flask) -> None:
        CategoryView.register(app)
        CustomerView.register(app)
        EmployeeView.register(app)
        HomeView.register(app, route_base="/")
        IngredientView.register(app)
        MaterialView.register(app)
        MonthlyFeeView.register(app)
        PaymentMethodView.register(app)
        RecipeView.register(app)
        RecipeIngredientView.register(app)
        RecipeMaterialView.register(app)
        ProductView.register(app)
        SaleProductView.register(app)
        SaleView.register(app)
        UserView.register(app)

    @staticmethod
    def inject_jinja_globals(app: Flask) -> None:
        app.jinja_env.filters.update({"format": format, "get": get})
        app.context_processor(
            lambda: {
                "layout": resolve_layout,
                "macro": resolve_macro,
                "partial": resolve_partial,
                "static": Url.for_static,
                "view": Url.for_view,
                "flashes": Flash.pop_all(),
                "header": session.get("header"),
                "module": session.get("module"),
                "user": UserService.get(),
            }
        )
