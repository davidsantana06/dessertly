from datetime import datetime
from io import BytesIO, StringIO
from typing import BinaryIO
import csv

from app.model import StockMixin

from .ingredient_service import IngredientService
from .material_service import MaterialService


class ShoppingListService:
    @staticmethod
    def __filter_missing(stock_items: list[StockMixin]) -> list[StockMixin]:
        return [item for item in stock_items if item.is_missing]

    @staticmethod
    def __sort(stock_items: list[StockMixin]) -> list[StockMixin]:
        def key(item: StockMixin):
            return (
                item.name,
                item.brand,
                item.supplier,
                item.current_quantity,
                item.minimum_quantity,
            )

        return sorted(stock_items, key=key)

    @classmethod
    def __get_missing(cls) -> list[StockMixin]:
        ingredients = IngredientService.get_all()
        materials = MaterialService.get_all()
        stock_items = cls.__filter_missing(ingredients + materials)
        return cls.__sort(stock_items)

    @classmethod
    def export(cls) -> tuple[BytesIO, str]:
        def compose_header(writer):
            header = [
                "Nome",
                "Marca",
                "Fornecedor",
                "Quantidade atual",
                "Comprar",
            ]
            writer.writerow(header)

        def compose_rows(writer, stock_items: list[StockMixin]):
            for item in stock_items:
                row = [
                    item.name,
                    item.brand,
                    item.supplier,
                    item.current_quantity,
                    item.quantity_to_restock,
                ]
                writer.writerow(row)

        def generate_filename():
            current_date = datetime.now().strftime("%Y.%m.%d")
            return f"Dessertly — Lista de Compras {current_date}.csv"

        stock_items = cls.__get_missing()

        text_stream = StringIO()
        writer = csv.writer(text_stream, delimiter=";")

        compose_header(writer)
        compose_rows(writer, stock_items)

        text_stream.seek(0)
        content = text_stream.getvalue().encode("utf-8-sig")

        buffer = BytesIO(content)
        buffer.seek(0)

        return buffer, generate_filename()
