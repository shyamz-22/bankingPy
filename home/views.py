from flask import Blueprint, render_template, redirect, url_for

from home.forms import LoginForm

home_view = Blueprint('home', __name__, url_prefix='/home')


@home_view.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print('before_validate')
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print('after_validate')
        print(url_for('account.debit'))
        return redirect(url_for('account.debit'))
    return render_template('login.html', title='Login', form=form)
