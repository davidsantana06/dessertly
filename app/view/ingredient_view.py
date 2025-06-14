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
            "icon": "fas fa-circle-chevron-up",
            "title": "Quantidade atual em estoque",
            "attr": "current_quantity",
        },
    ]
    _SHOW_COLUMNS = [
        _INDEX_COLUMNS[0],
        _INDEX_COLUMNS[1],
        _INDEX_COLUMNS[2],
        _INDEX_COLUMNS[3],
        {
            "icon": "fas fa-wrench",
            "title": "Fator de correção",
            "attr": "correction_factor",
        },
        {
            "icon": "fas fa-money-bill-wave",
            "title": "Valor unitário corrigido (R$)",
            "attr": "corrected_value",
        },
        {
            "icon": "fas fa-weight-scale",
            "title": "Quantidade por unidade (g/ml)",
            "attr": "quantity_in_grams_or_milliliters",
        },
        {
            "icon": "fas fa-weight-scale",
            "title": "Quantidade por unidade (kg/l)",
            "attr": "quantity_in_kilograms_or_liters",
        },
        {
            "icon": "fas fa-circle-chevron-down",
            "title": "Quantidade mínima em estoque",
            "attr": "minimum_quantity",
        },
        _INDEX_COLUMNS[4],
    ]

    _MESSAGE = {
        "post": "Ingrediente adicionado",
        "put": "Ingrediente atualizado",
        "delete": "Ingrediente excluído",
    }
