from werkzeug.exceptions import UnprocessableEntity

from app.model import Recipe, Sale
from app.form import SaleForm

from .base import MainService

from .customer_service import CustomerService
from .ingredient_service import IngredientService
from .material_service import MaterialService
from .payment_method_service import PaymentMethodService


class SaleService(MainService[Sale, SaleForm]):
    _Model = Sale

    @staticmethod
    def fill(form: SaleForm, sale: Sale | None = None) -> None:
        if sale: form.process(obj=sale)
        form.customer_id.choices += CustomerService.get_select_choices()
        form.payment_method_id.choices += PaymentMethodService.get_select_choices()

    @classmethod
    def update(cls, id: int, form: SaleForm) -> Sale:
        sale = cls.get_one(id)

        if sale.is_concluded:
            raise UnprocessableEntity("Não é possível editar uma venda concluída")

        form.populate_obj(sale)
        Sale.save(sale)
        return sale

    @staticmethod
    def __process_ingredients(
        recipe: Recipe,
        saled_quantity: int,
    ) -> None:
        for recipe_ingredient in recipe.ingredient_rels:
            ingredient = recipe_ingredient.ingredient
            weight_in_grams = recipe_ingredient.weight_in_grams * saled_quantity
            IngredientService.decrease_quantity(ingredient, weight_in_grams)

    @staticmethod
    def __process_materials(
        recipe: Recipe,
        saled_quantity: int,
    ) -> None:
        for recipe_material in recipe.material_rels:
            material = recipe_material.material
            quantity = recipe_material.quantity * saled_quantity
            MaterialService.decrease_quantity(material, quantity)

    @classmethod
    def conclude(cls, id: int) -> Sale:
        sale = cls.get_one(id)
        sale.status = "Concluída"

        for product_rel in sale.product_rels:
            saled_quantity = product_rel.quantity
            product = product_rel.product
            recipe = product.recipe
            cls.__process_ingredients(recipe.ingredient_rels, saled_quantity)
            cls.__process_materials(recipe.material_rels, saled_quantity)

        Sale.save(sale)
        return sale
