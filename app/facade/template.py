from flask import render_template


class Template:
    @staticmethod
    def resolve(template: str) -> str:
        return f"{template}.html.j2"

    @classmethod
    def render(cls, template: str, **context) -> str:
        return render_template(cls.resolve(template), **context)
