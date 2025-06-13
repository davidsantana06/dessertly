from app.model import Category
from app.form import CategoryForm

from .base import MainService
from .mixin import SelectChoicesMixin


class CategoryService(MainService[Category, CategoryForm], SelectChoicesMixin):
    _Model = Category
