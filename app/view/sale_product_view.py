from flask_classful import route
from werkzeug.exceptions import UnprocessableEntity

from app.facade import Flash
from app.form import SaleProductForm
from app.service import SaleProductService

from .base import BridgeView


class SaleProductView(BridgeView[SaleProductService, SaleProductForm]):
    _Service, _Form = SaleProductService, SaleProductForm

    _PRIMARY_MODULE = "sale"

    _HEADER = {
        "icon": "fas fa-box",
        "title": "Produtos da Venda",
    }

    _INDEX_COLUMNS = [
        {
            "icon": "fas fa-box",
            "title": "Produto",
            "attr": "product.name",
        },
        {
            "icon": "fas fa-circle-xmark",
            "title": "Quantidade",
            "attr": "quantity",
        },
        {
            "icon": "fas fa-money-bill",
            "title": "Valor unitário (R$)",
            "attr": "sell_value",
        },
        {
            "icon": "fas fa-scale-balanced",
            "title": "Balanço unitário (R$)",
            "attr": "balance_value",
        },
    ]
    _SHOW_COLUMNS = _INDEX_COLUMNS

    _MESSAGE = {
        "post": "Produto adicionado à venda",
        "put": "Produto atualizado na venda",
        "delete": "Produto excluído da venda",
    }

    def post(self, primary_id: int):
        try:
            response = super().post(primary_id)
        except UnprocessableEntity as e:
            Flash.append(e.description, "danger")
            response = self._redirect_to("sale_product:create", primary_id=primary_id)
        return response

    @route("/put/<int:id>", methods=["POST"])
    def put(self, id: int):
        try:
            response = super().put(id)
        except UnprocessableEntity as e:
            Flash.append(e.description, "danger")
            response = self._redirect_to("sale_product:edit", id=id)
        return response

    @route("/delete/<int:id>", methods=["GET"])
    def delete(self, id: int):
        try:
            response = super().delete(id)
        except UnprocessableEntity as e:
            Flash.append(e.description, "danger")
            response = self._redirect_to("sale_product:show", id=id)
        return response
