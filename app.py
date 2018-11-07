import os

from flask import Flask, request, session, abort

from account.views import account_view
from security.csrf import generate_csrf_token

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.jinja_env.globals['csrf_token'] = generate_csrf_token

app.register_blueprint(account_view)


@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)


if __name__ == '__main__':
    app.run()
