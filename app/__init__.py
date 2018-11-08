import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# BluePrints and models need db, so imports cannot be before creating the db
from app import models  # this import is for flask migrate tasks
from app.account.views import account_view
from app.home.views import home_view

app.register_blueprint(account_view)
app.register_blueprint(home_view)

models.dummy_print_for_import_optimization()
