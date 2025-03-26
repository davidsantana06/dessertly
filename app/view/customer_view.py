from app.form import CustomerForm
from app.service import CustomerService

from .base import MainView


class CustomerView(MainView[CustomerService, CustomerForm]):
    _Service, _Form = CustomerService, CustomerForm

    _HEADER = {
        "icon": "fas fa-user",
        "title": "Clientes",
    }

    _INDEX_COLUMNS = [
        {
            "icon": "fas fa-user",
            "title": "Nome",
            "attr": "name",
        },
        {
            "icon": "fas fa-phone",
            "title": "Celular",
            "attr": "cellphone",
        },
        {
            "icon": "fas fa-mobile",
            "title": "Telefone",
            "attr": "telephone",
        },
        {
            "icon": "fas fa-camera",
            "title": "Instagram",
            "attr": "instagram",
        },
    ]
    _SHOW_COLUMNS = _INDEX_COLUMNS + [
        {
            "icon": "fas fa-note-sticky",
            "title": "Notas",
            "attr": "notes",
        },
        {
            "icon": "fas fa-cart-shopping",
            "title": "Quantidade de compras",
            "attr": "sales_count",
        },
    ]

    _MESSAGE = {
        "post": "Cliente adicionado",
        "put": "Cliente atualizado",
        "delete": "Cliente excluído",
    }
