from flask import session
from flask_classful import FlaskView

from app.service import UserService

from .mixin import ResponseMixin


class HomeView(FlaskView, ResponseMixin):
    def before_request(self, _):
        if "is_first_access" not in session:
            session["is_first_access"] = False
            user = UserService.get()
            return self._redirect_to(user.first_view)

    def index(self):
        return self._render_page("home/index")
