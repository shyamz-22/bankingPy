from flask import Blueprint, render_template, request, flash, redirect, url_for

from account import account

account_view = Blueprint('account', __name__,
                         url_prefix='/account',
                         template_folder='templates',
                         static_folder='static')


@account_view.route('/debit', methods=['GET', 'POST'])
def debit():
    if request.method == 'POST':
        debit_amt = float(request.form['amount'])
        transaction = account.record_debit(debit_amt)
        flash(f'{transaction.amount} debited successfully.')
        return redirect(url_for('account.debit'))
    else:
        return render_debit()


@account_view.route('/credit', methods=['GET', 'POST'])
def credit():
    if request.method == 'POST':
        credit_amt = float(request.form['amount'])
        transaction = account.record_credit(credit_amt)
        flash(f'{transaction.amount} credited successfully.')
        return redirect(url_for('account.credit'))
    else:
        return render_credit()


def render_credit():
    return render_template('credit.html', currentBalance=account.balance, transactions=account.transactions)


def render_debit():
    return render_template('debit.html', currentBalance=account.balance, transactions=account.transactions)
