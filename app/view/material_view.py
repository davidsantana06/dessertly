from app.form import MaterialForm
from app.service import MaterialService

from .base import MainView


class MaterialView(MainView[MaterialService, MaterialForm]):
    _Service, _Form = MaterialService, MaterialForm

    _HEADER = {
        "icon": "fas fa-boxes-stacked",
        "title": "Materiais",
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
    _SHOW_COLUMNS = _INDEX_COLUMNS

    _MESSAGE = {
        "post": "Material adicionado",
        "put": "Material atualizado",
        "delete": "Material excluído",
    }
