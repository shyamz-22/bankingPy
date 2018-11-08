import os

from flask import Flask

from account.views import account_view

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

app.register_blueprint(account_view)

if __name__ == '__main__':
    app.run()
