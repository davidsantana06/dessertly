from app.form import ProductForm
from app.service import ProductService

from .base import MainView


class ProductView(MainView[ProductService, ProductForm]):
    _Service, _Form = ProductService, ProductForm

    _HEADER = {
        "icon": "fas fa-box",
        "title": "Produtos",
    }

    _INDEX_COLUMNS = [
        {
            "icon": "fas fa-box",
            "title": "Nome",
            "attr": "name",
        },
        {
            "icon": "fas fa-dollar-sign",
            "title": "Valor de venda (R$)",
            "attr": "sell_value",
        },
        {
            "icon": "fas fa-circle-up",
            "title": "Margem de contribuição (%)",
            "attr": "contribuition_margin",
        },
    ]
    _SHOW_COLUMNS = [
        _INDEX_COLUMNS[0],
        {
            "icon": "fas fa-receipt",
            "title": "Receita",
            "attr": "recipe.name",
        },
        {
            "icon": "fas fa-user-tie",
            "title": "Funcionário",
            "attr": "employee.name",
        },
        {
            "icon": "fas fa-dollar-sign",
            "title": "~ Valor dos ingredientes (R$)",
            "attr": "recipe.ingredients_value",
        },
        {
            "icon": "fas fa-dollar-sign",
            "title": "~ Valor dos materiais (R$)",
            "attr": "recipe.materials_value",
        },
        {
            "icon": "fas fa-dollar-sign",
            "title": "~ Valor das mensalidades (R$)",
            "attr": "monthly_fees_value",
        },
        {
            "icon": "fas fa-dollar-sign",
            "title": "~ Valor do funcionário (R$)",
            "attr": "employee_value",
        },
        {
            "icon": "fas fa-dollar-sign",
            "title": "Custo total (R$)",
            "attr": "cost_value",
        },
        {
            "icon": "fas fa-circle-down",
            "title": "Margem de perda (%)",
            "attr": "loss_margin",
        },
        {
            "icon": "fas fa-dollar-sign",
            "title": "Valor de perda (R$)",
            "attr": "loss_value",
        },
        _INDEX_COLUMNS[2],
        {
            "icon": "fas fa-dollar-sign",
            "title": "Valor de contribuição (R$)",
            "attr": "contribuition_value",
        },
        _INDEX_COLUMNS[1],
        {
            "icon": "fas fa-scale-balanced",
            "title": "Saldo (R$)",
            "attr": "balance_value",
        },
    ]

    _MESSAGE = {
        "post": "Produto adicionado",
        "put": "Produto atualizado",
        "delete": "Produto excluído",
    }

    def create(self):
        form = ProductForm()
        ProductService.fill(form)
        return self._render_page("product/create", form=form)

    def edit(self, id: int):
        form = ProductForm()
        product = ProductService.get_one(id)
        ProductService.fill(form, product)
        return self._render_page("product/edit", form=form, model=product)
