from flask import Blueprint

albuns_bp = Blueprint("albuns", __name__, template_folder="templates", static_folder='static', static_url_path='/albuns/static')

from controllers.albuns import routes