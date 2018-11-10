from datetime import datetime
from decimal import Decimal, ROUND_UP
from enum import Enum

from flask_login import current_user

from app.models import User, Transaction


class TransactionType(Enum):
    DEBIT = 'DEBIT'
    CREDIT = 'CREDIT'


class TransactionViewObject:
    def __init__(self, amount: Decimal,
                 current_balance: Decimal,
                 txn_type: str,
                 date: datetime) -> None:
        self.amount = amount
        self.balance = current_balance
        self.type = txn_type
        self.date = date.strftime("%d.%m.%Y %H:%M:%S")


def formatted_balance():
    user = User.find_by_email(current_user.email)
    return Decimal(user.balance).quantize(Decimal('.01'), rounding=ROUND_UP)


def transactions():
    txns = Transaction.list(current_user.user_id)

    def to_txn_vo(txn: Transaction) -> TransactionViewObject:
        return TransactionViewObject(amount=txn.txn_amount,
                                     current_balance=txn.current_balance,
                                     txn_type=txn.txn_type,
                                     date=txn.date)

    return list(map(to_txn_vo, txns))


def record_debit(debit_amt: Decimal) -> TransactionViewObject:
    user = User.find_by_email(current_user.email)

    balance = user.balance - debit_amt
    User.update_balance(user.email, balance)

    return __record(TransactionType.DEBIT, debit_amt, user.balance)


def record_credit(credit_amt: Decimal) -> TransactionViewObject:
    user = User.find_by_email(current_user.email)

    balance = user.balance + credit_amt
    User.update_balance(user.email, balance)

    return __record(TransactionType.CREDIT, credit_amt, user.balance)


def __record(txn_type: TransactionType, amount: Decimal, current_balance: Decimal):
    user = User.find_by_email(current_user.email)

    amount = Decimal(amount).quantize(Decimal('.01'), rounding=ROUND_UP)
    current_balance = Decimal(current_balance).quantize(Decimal('.01'), rounding=ROUND_UP)
    txn_date = datetime.utcnow()

    user.add_transaction(txn_type.value, amount, current_balance, txn_date)

    txn = TransactionViewObject(amount=amount,
                                current_balance=current_balance,
                                txn_type=txn_type.value,
                                date=txn_date)

    return txn
