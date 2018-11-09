import logging
import os

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app import logger

logger.configure(level=os.getenv('LOG_LEVEL', logging.INFO))
log = logging.getLogger(__name__)
logging.getLogger('werkzeug').setLevel(logging.INFO)
logging.getLogger('botocore').setLevel(logging.INFO)

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    # database and migration
    db.init_app(app)
    migrate.init_app(app, db)
    migration_setup()

    # security
    login.init_app(app)
    login.login_view = 'home.login'
    # Workaround for issue https://github.com/maxcountryman/flask-login/issues/419
    login.login_message_category = 'login.message'

    register_blueprints(app)

    log.info("App Setup complete")

    return app


def migration_setup():
    from app import models
    models.dummy_print_for_import_optimization()


def register_blueprints(app: Flask):
    # BluePrints and models need db, so imports cannot be before creating the db
    from app.account.views import account_view
    from app.home.views import home_view

    app.register_blueprint(account_view)
    app.register_blueprint(home_view)

    log.info("Blueprints registered")
