from flask import Blueprint

home_view = Blueprint('home', __name__,
                      url_prefix='/home')

from app.home import views
