from app.form import CategoryForm
from app.service import CategoryService

from .base import MainView


class CategoryView(MainView[CategoryService, CategoryForm]):
    _Service, _Form = CategoryService, CategoryForm

    _HEADER = {
        "icon": "fas fa-tags",
        "title": "Categorias",
    }

    _INDEX_COLUMNS = [
        {
            "icon": "fas fa-tags",
            "title": "Nome",
            "attr": "name",
        },
    ]
    _SHOW_COLUMNS = _INDEX_COLUMNS + [
        {
            "icon": "fas fa-receipt",
            "title": "Quantidade de receitas",
            "attr": "recipes_count",
        },
    ]

    _MESSAGE = {
        "post": "Categoria adicionada",
        "put": "Categoria atualizada",
        "delete": "Categoria excluída",
    }
