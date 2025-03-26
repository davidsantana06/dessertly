from werkzeug.exceptions import UnprocessableEntity

from app.model import SaleProduct
from app.form import SaleProductForm

from .base import BridgeService

from .product_service import ProductService
from .sale_service import SaleService


class SaleProductService(BridgeService[SaleProduct, SaleProductForm]):
    _Model = SaleProduct

    @classmethod
    def create(cls, form: SaleProductForm, primary_id: int) -> SaleProduct:
        sale = SaleService.get_one(primary_id)
        product = ProductService.get_one(form.secondary_id.data)
        sale_product = SaleProduct()

        if sale.is_concluded:
            raise UnprocessableEntity(
                "Não é possível adicionar produtos à uma venda concluída"
            )

        sale_product.primary_id = primary_id
        sale_product.sell_value = product.sell_value
        sale_product.balance_value = product.balance_value
        form.populate_obj(sale_product)

        SaleProduct.save(sale_product)
        return sale_product

    @staticmethod
    def fill(form: SaleProductForm, sale_product: SaleProduct | None = None) -> None:
        if sale_product: form.process(obj=sale_product)
        form.secondary_id.choices += ProductService.get_select_choices()

    @classmethod
    def update(cls, id: int, form: SaleProductForm) -> SaleProduct:
        sale_product = cls.get_one(id)
        sale = sale_product.sale
        product = sale_product.product

        if sale.is_concluded:
            raise UnprocessableEntity(
                "Não é possível editar produtos de uma venda concluída"
            )

        sale_product.sell_value = product.sell_value
        sale_product.balance_value = product.balance_value
        form.populate_obj(sale_product)

        SaleProduct.save(sale_product)
        return sale_product

    @classmethod
    def delete(cls, id: int) -> SaleProduct:
        sale_product = cls.get_one(id)
        sale = sale_product.sale

        if sale.is_concluded:
            raise UnprocessableEntity(
                "Não é possível excluir produtos de uma venda concluída"
            )

        SaleProduct.delete(sale_product)
        return sale_product
