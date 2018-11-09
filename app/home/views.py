from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_user, logout_user

from app.home import user
from app.home.forms import LoginForm
from app.url_util import is_safe_url

home_view = Blueprint('home', __name__, url_prefix='/home')


@home_view.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('account.debit'))

    form = LoginForm(next_page='')

    if request.method == 'GET':
        form.next_page.data = request.args.get('next')

    if form.validate_on_submit():
        authenticated_user = user.authenticate(form.username.data, form.password.data)

        if authenticated_user:
            next_page = form.next_page.data

            if not is_safe_url(next_page):
                next_page = None

            login_user(authenticated_user)
            return redirect(next_page or url_for('account.debit'))

        else:
            return _render_login(LoginForm(next_page=''), error='Please check your username and password')

    return _render_login(form)


@home_view.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.login'))


def _render_login(form: LoginForm, error: str = None):
    return render_template('login.html',
                           title='Login',
                           form=form,
                           error=error)
