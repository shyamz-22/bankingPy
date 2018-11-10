from flask import render_template, flash, redirect, url_for
from flask_login import login_required

from app.account import account, account_view
from app.account.forms import AccountForm


@account_view.route('/debit', methods=['GET', 'POST'])
@login_required
def debit():
    form = AccountForm()
    if form.validate_on_submit():
        transaction = account.record_debit(form.amount.data)
        flash(f'{transaction.amount} debited successfully.')
        return redirect(url_for('account.debit'))
    else:
        return render_debit(form=form)


@account_view.route('/credit', methods=['GET', 'POST'])
@login_required
def credit():
    form = AccountForm()
    if form.validate_on_submit():
        transaction = account.record_credit(form.amount.data)
        flash(f'{transaction.amount} credited successfully.')
        return redirect(url_for('account.credit'))
    else:
        return render_credit(form=form)


def render_credit(form: AccountForm):
    return render_template('credit.html', form=form,
                           currentBalance=account.formatted_balance(),
                           transactions=account.transactions())


def render_debit(form: AccountForm):
    return render_template('debit.html', form=form,
                           currentBalance=account.formatted_balance(),
                           transactions=account.transactions())
