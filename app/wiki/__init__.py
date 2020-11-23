from flask import Blueprint

from config import DIR_TEMPLATES, DIR_STATIC

wiki = Blueprint('wiki', __name__, template_folder=DIR_TEMPLATES, static_folder=DIR_STATIC)

from app.wiki import views
