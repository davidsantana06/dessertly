from app.model import Customer
from app.form import CustomerForm

from .base import MainService
from .mixin import SelectChoicesMixin


class CustomerService(MainService[Customer, CustomerForm], SelectChoicesMixin):
    _Model = Customer
