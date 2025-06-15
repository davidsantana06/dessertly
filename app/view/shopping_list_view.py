from flask_classful import FlaskView
from app.service import ShoppingListService
from .mixin import ResponseMixin


class ShoppingListView(FlaskView, ResponseMixin):
    def export(self):
        buffer, filename = ShoppingListService.export()
        return self._send_file(buffer, filename, "text/csv")
