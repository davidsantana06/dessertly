from abc import ABC
from flask import request
from flask_classful import route

from app.facade import Flash
from app.form import F
from app.service import BS

from ..mixin import MessageMixin

from .view import View


class BridgeView(View[BS, F], ABC, MessageMixin):
    _Service: BS

    _PRIMARY_MODULE: str

    def index(self, primary_id: int):
        models = self._Service.get_all(primary_id)
        return self._render_page(
            f"{self._module}/index",
            columns=self._INDEX_COLUMNS,
            models=models,
            primary_module=self._PRIMARY_MODULE,
            primary_id=primary_id,
        )

    def create(self, primary_id: int):
        form = self._Form()
        self._Service.fill(form)
        return self._render_page(
            f"{self._module}/create",
            form=form,
            primary_id=primary_id,
        )

    def post(self, primary_id: int):
        form = self._Form(request.form)
        model = self._Service.create(form, primary_id)
        Flash.append(self._MESSAGE["post"], "success")
        return self._redirect_to(
            f"{self._module}:edit",
            primary_id=primary_id,
            id=model.id,
        )

    def edit(self, id: int):
        form = self._Form(request.form)
        model = self._Service.get_one(id)
        self._Service.fill(form, model)
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
        model = self._Service.delete(id)
        Flash.append(self._MESSAGE["delete"], "info")
        return self._redirect_to(f"{self._module}:index", primary_id=model.primary_id)
