from flask import redirect
from app.facade import Template, Url


class ResponseMixin:
    def _render_page(self, template: str, **context):
        return Template.render(f"page/{template}", **context)

    def _redirect_to(self, endpoint: str, **values):
        return redirect(Url.for_view(endpoint, **values))
