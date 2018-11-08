from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user

from app.home import user
from app.home.forms import LoginForm

home_view = Blueprint('home', __name__, url_prefix='/home')


@home_view.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('account.debit'))

    form = LoginForm()

    if form.validate_on_submit():
        authenticated_user = user.authenticate(form.username.data, form.password.data)

        if authenticated_user:
            login_user(authenticated_user)
            return redirect(url_for('account.debit'))
        else:
            return render_template('login.html',
                                   title='Login',
                                   form=LoginForm(),
                                   error='Please check your username and password')

    return render_template('login.html', title='Login', form=form)


@home_view.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.login'))
