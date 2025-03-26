from app.model import Employee
from app.form import EmployeeForm

from .base import MainService
from .mixin import SelectChoicesMixin


class EmployeeService(MainService[Employee, EmployeeForm], SelectChoicesMixin):
    _Model = Employee
