from app.facade import Flash
from app.form import RecipeForm
from app.service import RecipeService

from .base import MainView


class RecipeView(MainView[RecipeService, RecipeForm]):
    _Service, _Form = RecipeService, RecipeForm

    _HEADER = {
        "icon": "fas fa-receipt",
        "title": "Receitas",
    }

    _INDEX_COLUMNS = [
        {
            "icon": "fas fa-receipt",
            "title": "Nome",
            "attr": "name",
        },
        {
            "icon": "fas fa-align-right",
            "title": "Descrição",
            "attr": "description",
        },
        {
            "icon": "fas fa-clock",
            "title": "Tempo de preparo (min)",
            "attr": "preparation_time_in_minutes",
        },
    ]
    _SHOW_COLUMNS = [
        _INDEX_COLUMNS[0],
        {
            "icon": "fas fa-tags",
            "title": "Categoria",
            "attr": "category.name",
        },
        _INDEX_COLUMNS[1],
        _INDEX_COLUMNS[2],
        {
            "icon": "fas fas fa-dollar-sign",
            "title": "Valor dos ingredientes (R$)",
            "attr": "ingredients_value",
        },
        {
            "icon": "fas fas fa-dollar-sign",
            "title": "Valor dos materiais (R$)",
            "attr": "materials_value",
        },
        {
            "icon": "fas fa-weight-scale",
            "title": "Rendimento (g/ml)",
            "attr": "yield_in_grams_or_milliliters",
        },
        {
            "icon": "fas fa-weight-scale",
            "title": "Rendimento (kg/l)",
            "attr": "yield_in_kilograms_or_liters",
        },
        {
            "icon": "fas fa-utensils",
            "title": "Porção(ões)",
            "attr": "yield_in_units",
        },
        {
            "icon": "fas fa-weight-scale",
            "title": "Quantidade por unidade (g/ml)",
            "attr": "quantity_per_unit_in_grams_or_milliliters",
        },
    ]

    _MESSAGE = {
        "post": "Receita adicionada",
        "put": "Receita atualizada",
        "delete": "Receita excluída",
    }

    def create(self):
        form = RecipeForm()
        RecipeService.fill(form)
        return self._render_page("recipe/create", form=form)

    def edit(self, id: int):
        form = RecipeForm()
        recipe = RecipeService.get_one(id)
        RecipeService.fill(form, recipe)
        return self._render_page("recipe/edit", form=form, model=recipe)

    def clone(self, id: int):
        recipe = RecipeService.clone(id)
        Flash.append("Receita clonada", "success")
        return self._redirect_to("recipe:edit", id=recipe.id)
