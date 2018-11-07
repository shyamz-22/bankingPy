import datetime
from enum import Enum


class TransactionType(Enum):
    DEBIT = 'DEBIT'
    CREDIT = 'CREDIT'


class Transaction:
    def __init__(self, amount: float,
                 current_balance: float,
                 txn_type: TransactionType) -> None:
        self.amount = amount
        self.balance = current_balance
        self.type = txn_type
        self.date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")


balance = 1000.00
transactions = []


def record_debit(debit_amt: float) -> Transaction:
    global balance
    balance = balance - debit_amt
    return record(TransactionType.DEBIT, debit_amt, balance)


def record_credit(credit_amt: float) -> Transaction:
    global balance
    balance = balance + credit_amt
    return record(TransactionType.CREDIT, credit_amt, balance)


def record(txn_type: TransactionType, amount: float, current_balance: float):
    txn = Transaction(amount=amount, current_balance=current_balance, txn_type=txn_type)
    transactions.append(txn)
    return txn
