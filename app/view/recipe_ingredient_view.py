from app.form import RecipeIngredientForm
from app.service import RecipeIngredientService

from .base import BridgeView


class RecipeIngredientView(BridgeView[RecipeIngredientService, RecipeIngredientForm]):
    _Service, _Form = RecipeIngredientService, RecipeIngredientForm

    _PRIMARY_MODULE = "recipe"

    _HEADER = {
        "icon": "fas fa-boxes-stacked",
        "title": "Ingredientes da Receita",
    }

    _INDEX_COLUMNS = [
        {
            "icon": "fas fa-boxes-stacked",
            "title": "Ingrediente",
            "attr": "ingredient.name",
        },
        {
            "icon": "fas fa-weight-scale",
            "title": "Quantidade (g/ml)",
            "attr": "quantity_in_grams_or_milliliters",
        },
    ]
    _SHOW_COLUMNS = _INDEX_COLUMNS

    _MESSAGE = {
        "post": "Ingrediente adicionado à receita",
        "put": "Ingrediente atualizado na receita",
        "delete": "Ingrediente excluído da receita",
    }
