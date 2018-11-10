from flask import Blueprint

account_view = Blueprint('account', __name__,
                         url_prefix='/account')

from app.account import views
