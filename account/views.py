from flask import Blueprint, render_template, flash, redirect, url_for

from account import account
from account.forms import AccountForm

account_view = Blueprint('account', __name__,
                         url_prefix='/account')


@account_view.route('/debit', methods=['GET', 'POST'])
def debit():
    form = AccountForm()
    if form.validate_on_submit():
        debit_amt = form.amount.data
        transaction = account.record_debit(debit_amt)
        flash(f'{transaction.amount} debited successfully.')
        return redirect(url_for('account.debit'))
    else:
        return render_debit(form=form)


@account_view.route('/credit', methods=['GET', 'POST'])
def credit():
    form = AccountForm()
    if form.validate_on_submit():
        credit_amt = form.amount.data
        transaction = account.record_credit(credit_amt)
        flash(f'{transaction.amount} credited successfully.')
        return redirect(url_for('account.credit'))
    else:
        return render_credit(form=form)


def render_credit(form: AccountForm):
    return render_template('credit.html', form=form,
                           currentBalance=account.formatted_balance(),
                           transactions=account.transactions)


def render_debit(form: AccountForm):
    return render_template('debit.html', form=form,
                           currentBalance=account.formatted_balance(),
                           transactions=account.transactions)
