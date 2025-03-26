from flask import redirect
from app.facade import Template, URL


class ResponseMixin:
    def _render_page(self, template: str, **context):
        return Template.render(f"page/{template}", **context)

    def _redirect_to(self, endpoint: str, **values):
        return redirect(URL.for_view(endpoint, **values))
