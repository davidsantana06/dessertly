from app.model import Material
from app.form import MaterialForm

from .base import MainService
from .mixin import SelectChoicesMixin


class MaterialService(MainService[Material, MaterialForm], SelectChoicesMixin):
    _Model = Material

    @classmethod
    def decrease_quantity(cls, material: Material, quantity: float) -> None:
        current_quantity = material.current_quantity
        decreased_quantity = round(current_quantity - quantity, 2)
        material.current_quantity = max(0, decreased_quantity)
        Material.save(material)
