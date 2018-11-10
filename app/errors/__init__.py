from flask import Blueprint

errors_view = Blueprint('error', __name__)

from app.errors import views
