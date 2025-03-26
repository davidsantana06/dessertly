from app.model import PaymentMethod
from app.form import PaymentMethodForm

from .base import MainService
from .mixin import SelectChoicesMixin


class PaymentMethodService(
    MainService[PaymentMethod, PaymentMethodForm], SelectChoicesMixin
):
    _Model = PaymentMethod
