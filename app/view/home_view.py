from flask import session
from flask_classful import FlaskView

from app.service import UserService

from .mixin import ResponseMixin


class HomeView(FlaskView, ResponseMixin):
    route_base = "/"

    def before_request(self, _):
        if "is_first_acess" not in session:
            session["is_first_acess"] = False
            user = UserService.get()
            return self._redirect_to(user.first_view)

    def index(self): ...
