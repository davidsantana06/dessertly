from app.form import MonthlyFeeForm
from app.service import MonthlyFeeService

from .base import MainView


class MonthlyFeeView(MainView[MonthlyFeeService, MonthlyFeeForm]):
    _Service, _Form = MonthlyFeeService, MonthlyFeeForm

    _HEADER = {
        "icon": "fas fa-money-check-dollar",
        "title": "Mensalidades",
    }

    _INDEX_COLUMNS = [
        {
            "icon": "fas fa-money-check-dollar",
            "title": "Nome",
            "attr": "name",
        },
        {
            "icon": "fas fa-dollar-sign",
            "title": "Valor (R$)",
            "attr": "value",
        },
        {
            "icon": "fas fa-align-right",
            "title": "Descrição",
            "attr": "description",
        },
    ]
    _SHOW_COLUMNS = _INDEX_COLUMNS + [
        {
            "icon": "fas fa-info-circle",
            "title": "Taxa diária (R$)",
            "attr": "daily_rate",
        },
        {
            "icon": "fas fa-info-circle",
            "title": "Taxa horária (R$)",
            "attr": "hourly_rate",
        },
    ]

    _MESSAGE = {
        "post": "Mensalidade adicionada",
        "put": "Mensalidade atualizada",
        "delete": "Mensalidade excluída",
    }
