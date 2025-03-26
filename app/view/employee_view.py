from app.form import EmployeeForm
from app.service import EmployeeService

from .base import MainView


class EmployeeView(MainView[EmployeeService, EmployeeForm]):
    _Service, _Form = EmployeeService, EmployeeForm

    _HEADER = {
        "icon": "fas fa-user-tie",
        "title": "Funcionários",
    }

    _INDEX_COLUMNS = [
        {
            "icon": "fas fa-user-tie",
            "title": "Nome",
            "attr": "name",
        },
        {
            "icon": "fas fa-dollar-sign",
            "title": "Taxa horária (R$)",
            "attr": "hourly_rate",
        },
    ]
    _SHOW_COLUMNS = _INDEX_COLUMNS + [
        {
            "icon": "fas fa-note-sticky",
            "title": "Notas",
            "attr": "notes",
        },
    ]

    _MESSAGE = {
        "post": "Funcionário adicionado",
        "put": "Funcionário atualizado",
        "delete": "Funcionário excluído",
    }
