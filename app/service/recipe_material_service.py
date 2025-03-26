from app.model import RecipeMaterial
from app.form import RecipeMaterialForm

from .base import BridgeService

from .material_service import MaterialService


class RecipeMaterialService(BridgeService[RecipeMaterial, RecipeMaterialForm]):
    _Model = RecipeMaterial

    @staticmethod
    def fill(
        form: RecipeMaterialForm,
        recipe_material: RecipeMaterial | None = None,
    ) -> None:
        if recipe_material: form.process(obj=recipe_material)
        form.secondary_id.choices += MaterialService.get_select_choices()
