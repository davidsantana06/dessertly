from app.model import Recipe, RecipeIngredient, RecipeMaterial
from app.form import RecipeForm

from .base import MainService
from .mixin import SelectChoicesMixin

from .category_service import CategoryService


class RecipeService(MainService[Recipe, RecipeForm], SelectChoicesMixin):
    _Model = Recipe

    @staticmethod
    def fill(form: RecipeForm, recipe: Recipe | None = None) -> None:
        if recipe:
            form.process(obj=recipe)
        form.category_id.choices += CategoryService.get_select_choices()

    @staticmethod
    def __clone_attrs(original_recipe: Recipe) -> Recipe:
        clone_recipe = Recipe()

        clone_recipe.category_id = original_recipe.category_id
        clone_recipe.name = f"Clone de {original_recipe.name}"
        clone_recipe.description = original_recipe.description
        clone_recipe.preparation_time_in_minutes = (
            original_recipe.preparation_time_in_minutes
        )
        clone_recipe.yield_in_grams_or_milliliters = (
            original_recipe.yield_in_grams_or_milliliters
        )
        clone_recipe.yield_in_units = original_recipe.yield_in_units

        Recipe.save(clone_recipe)
        return clone_recipe

    @staticmethod
    def __clone_ingredients(original_recipe: Recipe, clone_recipe: Recipe) -> None:
        for original_recipe_ingredient in original_recipe.ingredient_rels:
            clone_recipe_ingredient = RecipeIngredient()

            clone_recipe_ingredient.primary_id = clone_recipe.id
            clone_recipe_ingredient.secondary_id = (
                original_recipe_ingredient.secondary_id
            )
            clone_recipe_ingredient.quantity_in_grams_or_milliliters = (
                original_recipe_ingredient.quantity_in_grams_or_milliliters
            )

            RecipeIngredient.save(clone_recipe_ingredient)

    @staticmethod
    def __clone_materials(original_recipe: Recipe, clone_recipe: Recipe) -> None:
        for original_recipe_material in original_recipe.material_rels:
            clone_recipe_material = RecipeMaterial()

            clone_recipe_material.primary_id = clone_recipe.id
            clone_recipe_material.secondary_id = original_recipe_material.secondary_id
            clone_recipe_material.quantity = original_recipe_material.quantity

            RecipeMaterial.save(clone_recipe_material)

    @classmethod
    def clone(cls, id: int) -> Recipe:
        original_recipe = cls.get_one(id)
        clone_recipe = cls.__clone_attrs(original_recipe)
        cls.__clone_ingredients(original_recipe, clone_recipe)
        cls.__clone_materials(original_recipe, clone_recipe)
        return clone_recipe
