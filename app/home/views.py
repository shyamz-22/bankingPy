from flask import Blueprint, render_template, redirect, url_for

from app.home import user
from app.home.forms import LoginForm

home_view = Blueprint('home', __name__, url_prefix='/home')


@home_view.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if user.authenticate(form.username.data, form.password.data).authenticated:
            return redirect(url_for('account.debit'))
        else:
            return render_template('login.html',
                                   title='Login',
                                   form=LoginForm(),
                                   error='Please check your username and password')

    return render_template('login.html', title='Login', form=form)
