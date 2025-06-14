from app.model import Ingredient
from app.form import IngredientForm

from .base import MainService
from .mixin import SelectChoicesMixin


class IngredientService(MainService[Ingredient, IngredientForm], SelectChoicesMixin):
    _Model = Ingredient

    @classmethod
    def decrease_quantity(
        cls, ingredient: Ingredient, quantity_in_grams_or_milliliters: int
    ) -> None:
        current_quantity = ingredient.current_quantity
        quantity = (
            quantity_in_grams_or_milliliters
            / ingredient.quantity_in_grams_or_milliliters
        )
        decreased_quantity = round(current_quantity - quantity, 2)
        ingredient.current_quantity = max(0, decreased_quantity)
        Ingredient.save(ingredient)
