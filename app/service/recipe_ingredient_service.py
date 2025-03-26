from app.model import RecipeIngredient
from app.form import RecipeIngredientForm

from .base import BridgeService

from .ingredient_service import IngredientService


class RecipeIngredientService(BridgeService[RecipeIngredient, RecipeIngredientForm]):
    _Model = RecipeIngredient

    @staticmethod
    def fill(
        form: RecipeIngredientForm,
        recipe_ingredient: RecipeIngredient | None = None,
    ) -> None:
        if recipe_ingredient: form.process(obj=recipe_ingredient)
        form.secondary_id.choices += IngredientService.get_select_choices()
