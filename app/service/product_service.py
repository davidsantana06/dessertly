from app.model import Product
from app.form import ProductForm

from .base import MainService
from .mixin import SelectChoicesMixin

from .employee_service import EmployeeService
from .recipe_service import RecipeService


class ProductService(MainService[Product, ProductForm], SelectChoicesMixin):
    _Model = Product

    @staticmethod
    def fill(form: ProductForm, product: Product | None = None) -> None:
        if product:
            form.process(obj=product)
        form.employee_id.choices += EmployeeService.get_select_choices()
        form.recipe_id.choices += RecipeService.get_select_choices()
