from app.form import RecipeMaterialForm
from app.service import RecipeMaterialService

from .base import BridgeView


class RecipeMaterialView(BridgeView[RecipeMaterialService, RecipeMaterialForm]):
    _Service, _Form = RecipeMaterialService, RecipeMaterialForm

    _PRIMARY_MODULE = "recipe"

    _HEADER = {
        "icon": "fas fa-boxes-stacked",
        "title": "Materiais da Receita",
    }

    _INDEX_COLUMNS = [
        {
            "icon": "fas fa-boxes-stacked",
            "title": "Material",
            "attr": "material.name",
        },
        {
            "icon": "fas fa-circle-xmark",
            "title": "Quantidade",
            "attr": "quantity",
        },
    ]
    _SHOW_COLUMNS = _INDEX_COLUMNS

    _MESSAGE = {
        "post": "Material adicionado à receita",
        "put": "Material atualizado na receita",
        "delete": "Material excluído da receita",
    }
