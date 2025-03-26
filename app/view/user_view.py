from flask import request, session
from flask_classful import FlaskView, route

from app.facade import Flash
from app.form import UserForm
from app.service import UserService

from .mixin import ColumnsMixin, HeaderMixin, ResponseMixin


class UserView(FlaskView, ColumnsMixin, HeaderMixin, ResponseMixin):
    _HEADER = {
        "icon": "fas fa-address-card",
        "title": "Perfil",
    }

    _SHOW_COLUMNS = [
        {
            "icon": "fas fa-address-card",
            "title": "Nome",
            "attr": "name",
        },
        {
            "icon": "fas fa-desktop",
            "title": "Tela inicial",
            "attr": "first_view",
        },
        {
            "icon": "fas fa-palette",
            "title": "Tema",
            "attr": "theme",
        },
        {
            "icon": "fas fa-expand",
            "title": "Escala de visualização",
            "attr": "zoom",
        },
    ]

    def before_request(self, _: str):
        session.update({"header": self._HEADER})

    def edit(self):
        form = UserForm()
        UserService.fill(form)
        return self._render_page("user/edit", form=form)

    @route("/put", methods=["POST"])
    def put(self):
        form = UserForm(request.form)
        UserService.update(form)
        Flash.append("Perfil atualizado", "info")
        return self._redirect_to("user:edit")

    def show(self):
        return self._render_page("user/show", columns=self._SHOW_COLUMNS)
