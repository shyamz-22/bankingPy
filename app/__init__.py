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

    register_error_handler(app)
    register_blueprints(app)

    log.info("App Setup complete")

    return app


def migration_setup():
    from app import models


def register_error_handler(app: Flask):
    from app.errors import errors_view
    app.register_blueprint(errors_view)


def register_blueprints(app: Flask):
    # BluePrints and models need db, so imports cannot be before creating the db
    from app.home import home_view
    from app.account import account_view

    app.register_blueprint(home_view)
    app.register_blueprint(account_view)

    log.info("Blueprints registered")
