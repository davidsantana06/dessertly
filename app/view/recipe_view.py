from app.form import RecipeForm
from app.service import RecipeService


from .base import MainView


class RecipeView(MainView[RecipeService, RecipeForm]):
    _Service, _Form = RecipeService, RecipeForm

    _HEADER = {
        "icon": "fas fa-receipt",
        "title": "Receitas",
    }

    _INDEX_COLUMNS = [
        {
            "icon": "fas fa-receipt",
            "title": "Nome",
            "attr": "name",
        },
        {
            "icon": "fas fa-clock",
            "title": "Tempo de preparo (min)",
            "attr": "preparation_time_in_minutes",
        },
        {
            "icon": "fas fa-align-right",
            "title": "Descrição",
            "attr": "description",
        },
    ]
    _SHOW_COLUMNS = _INDEX_COLUMNS + [
        {
            "icon": "fas fas fa-dollar-sign",
            "title": "Valor dos ingredientes (R$)",
            "attr": "ingredients_value",
        },
        {
            "icon": "fas fas fa-dollar-sign",
            "title": "Valor dos materiais (R$)",
            "attr": "materials_value",
        },
    ]

    _MESSAGE = {
        "post": "Receita adicionada",
        "put": "Receita atualizada",
        "delete": "Receita excluída",
    }
