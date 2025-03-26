from flask import Flask
from .config import Setup


app = Flask(__name__)
Setup.apply_parameters(app)
Setup.init_db(app)
Setup.create_default_user(app)
Setup.register_views(app)
Setup.inject_jinja_globals(app)
