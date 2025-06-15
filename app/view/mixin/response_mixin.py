from flask import redirect, send_file
from io import BytesIO

from app.facade import Template, Url


class ResponseMixin:
    def _redirect_to(self, endpoint: str, **values):
        return redirect(Url.for_view(endpoint, **values))

    def _render_page(self, template: str, **context):
        return Template.render(f"page/{template}", **context)

    def _send_file(self, buffer: BytesIO, filename: str, mimetype: str):
        return send_file(
            buffer,
            mimetype,
            as_attachment=True,
            download_name=filename,
        )
