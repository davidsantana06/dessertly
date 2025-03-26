from app.model import Recipe
from app.form import RecipeForm

from .base import MainService
from .mixin import SelectChoicesMixin


class RecipeService(MainService[Recipe, RecipeForm], SelectChoicesMixin):
    _Model = Recipe
