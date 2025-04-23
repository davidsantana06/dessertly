from app.form import PaymentMethodForm
from app.service import PaymentMethodService

from .base import MainView


class PaymentMethodView(MainView[PaymentMethodService, PaymentMethodForm]):
    _Service, _Form = PaymentMethodService, PaymentMethodForm

    _HEADER = {
        "icon": "fas fa-credit-card",
        "title": "Métodos de Pagamento",
    }

    _INDEX_COLUMNS = [
        {
            "icon": "fas fa-credit-card",
            "title": "Nome",
            "attr": "name",
        },
        {
            "icon": "fas fa-cart-shopping",
            "title": "Quantidade de vendas",
            "attr": "sales_count",
        },
    ]
    _SHOW_COLUMNS = _INDEX_COLUMNS

    _MESSAGE = {
        "post": "Método de pagamento adicionado",
        "put": "Método de pagamento atualizado",
        "delete": "Método de pagamento excluído",
    }
