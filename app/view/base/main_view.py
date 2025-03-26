from abc import ABC
from flask import request
from flask_classful import route

from app.facade import Flash
from app.form import F
from app.service import MS

from ..mixin import MessageMixin

from .view import View


class MainView(View[MS, F], ABC, MessageMixin):
    _Service: MS

    def index(self):
        search = request.args.get("search", "")
        models = self._Service.get_all(search)
        return self._render_page(
            f"{self._module}/index",
            columns=self._INDEX_COLUMNS,
            models=models,
            search=search,
        )

    def create(self):
        form = self._Form()
        return self._render_page(f"{self._module}/create", form=form)

    def post(self):
        form = self._Form()
        model = self._Service.create(form)
        Flash.append(self._MESSAGE["post"], "success")
        return self._redirect_to(f"{self._module}:edit", id=model.id)

    def edit(self, id: int):
        form = self._Form()
        model = self._Service.fill(id, form)
        return self._render_page(f"{self._module}/edit", form=form, model=model)
    
    @route("/put/<int:id>", methods=["POST"])
    def put(self, id: int):
        form = self._Form(request.form)
        model = self._Service.update(id, form)
        Flash.append(self._MESSAGE["put"], "info")
        return self._redirect_to(f"{self._module}:edit", id=model.id)

    def show(self, id: int):
        model = self._Service.get_one(id)
        return self._render_page(
            f"{self._module}/show",
            columns=self._SHOW_COLUMNS,
            model=model,
        )

    @route("/delete/<int:id>", methods=["GET"])
    def delete(self, id: int):
        self._Service.delete(id)
        Flash.append(self._MESSAGE["delete"], "info")
        return self._redirect_to(f"{self._module}:index")
