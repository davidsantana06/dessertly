from app.form import IngredientForm
from app.service import IngredientService

from .base import MainView


class IngredientView(MainView[IngredientService, IngredientForm]):
    _Service, _Form = IngredientService, IngredientForm

    _HEADER = {
        "icon": "fas fa-boxes-stacked",
        "title": "Ingredientes",
    }

    _INDEX_COLUMNS = [
        {
            "icon": "fas fa-boxes-stacked",
            "title": "Nome",
            "attr": "name",
        },
        {
            "icon": "fas fa-tag",
            "title": "Marca",
            "attr": "brand",
        },
        {
            "icon": "fas fa-store",
            "title": "Fornecedor",
            "attr": "supplier",
        },
        {
            "icon": "fas fa-money-bill-wave",
            "title": "Valor unitário (R$)",
            "attr": "value",
        },
        {
            "icon": "fas fa-circle-chevron-down",
            "title": "Quantidade mínima",
            "attr": "minimum_quantity",
        },
        {
            "icon": "fas fa-circle-chevron-up",
            "title": "Quantidade atual",
            "attr": "current_quantity",
        },
    ]
    _SHOW_COLUMNS = _INDEX_COLUMNS + [
        {
            "icon": "fas fa-weight-hanging",
            "title": "Peso unitário (g)",
            "attr": "weight_in_grams",
        },
    ]

    _MESSAGE = {
        "post": "Ingrediente adicionado",
        "put": "Ingrediente atualizado",
        "delete": "Ingrediente excluído",
    }
