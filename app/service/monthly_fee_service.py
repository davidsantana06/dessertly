from app.model import MonthlyFee
from app.form import MonthlyFeeForm

from .base import MainService
from .mixin import SelectChoicesMixin


class MonthlyFeeService(MainService[MonthlyFee, MonthlyFeeForm], SelectChoicesMixin):
    _Model = MonthlyFee
