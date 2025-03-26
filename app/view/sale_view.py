from flask_classful import route
from werkzeug.exceptions import UnprocessableEntity

from app.facade import Flash
from app.form import SaleForm
from app.service import SaleService

from .base import MainView


class SaleView(MainView[SaleService, SaleForm]):
    _Service, _Form = SaleService, SaleForm

    _HEADER = {
        "icon": "fas fa-money-bill-transfer",
        "title": "Vendas",
    }

    _INDEX_COLUMNS = [
        {
            "icon": "fas fa-hashtag",
            "title": "Código",
            "attr": "code",
        },
        {
            "icon": "fas fa-calendar-days",
            "title": "Data/hora",
            "attr": "created_at",
        },
        {
            "icon": "fas fa-user",
            "title": "Cliente",
            "attr": "customer.name",
        },
        {
            "icon": "fas fa-credit-card",
            "title": "Método de pagamento",
            "attr": "payment_method.name",
        },
        {
            "icon": "fas fa-dollar-sign",
            "title": "Valor total (R$)",
            "attr": "total_sell_value",
        },
    ]
    _SHOW_COLUMNS = [
        _INDEX_COLUMNS[0],
        {
            "icon": "fas fa-circle",
            "title": "Status",
            "attr": "status",
        },
        _INDEX_COLUMNS[1],
        _INDEX_COLUMNS[2],
        _INDEX_COLUMNS[3],
        {
            "icon": "fas fa-dollar-sign",
            "title": "~ Valor dos produtos (R$)",
            "attr": "sell_value",
        },
        {
            "icon": "fas fa-dollar-sign",
            "title": "~ Valor do frete (R$)",
            "attr": "freight",
        },
        {
            "icon": "fas fa-dollar-sign",
            "title": "~ Desconto (R$)",
            "attr": "discount",
        },
        _INDEX_COLUMNS[4],
        {
            "icon": "fas fa-scale-balanced",
            "title": "Saldo (R$)",
            "attr": "total_balance_value",
        },
    ]

    _MESSAGE = {
        "post": "Venda adicionada",
        "put": "Venda atualizada",
        "delete": "Venda excluída",
    }

    def create(self):
        form = SaleForm()
        SaleService.fill(form)
        return self._render_page("sale/create", form=form)

    def edit(self, id: int):
        form = SaleForm()
        sale = SaleService.get_one(id)
        SaleService.fill(form, sale)
        return self._render_page("sale/edit", form=form, model=sale)

    @route("/put/<int:id>", methods=["POST"])
    def put(self, id: int):
        try:
            response = super().put(id)
        except UnprocessableEntity as e:
            Flash.append(e.description, "danger")
            response = self._redirect_to("sale:edit", id=id)
        return response

    def conclude(self, id: int):
        SaleService.conclude(id)
        Flash.append("Venda concluída", "success")
        return self._redirect_to("sale:show", id=id)
