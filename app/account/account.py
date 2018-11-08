import datetime
from decimal import Decimal, ROUND_UP
from enum import Enum


class TransactionType(Enum):
    DEBIT = 'DEBIT'
    CREDIT = 'CREDIT'


class Transaction:
    def __init__(self, amount: Decimal,
                 current_balance: Decimal,
                 txn_type: TransactionType) -> None:
        self.amount = amount
        self.balance = current_balance
        self.type = txn_type
        self.date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")


__balance = Decimal(1000.00)
transactions = []


def formatted_balance():
    global __balance
    return Decimal(__balance).quantize(Decimal('.01'), rounding=ROUND_UP)


def record_debit(debit_amt: Decimal) -> Transaction:
    global __balance
    __balance = __balance - debit_amt
    return __record(TransactionType.DEBIT, debit_amt, __balance)


def record_credit(credit_amt: Decimal) -> Transaction:
    global __balance
    __balance = __balance + credit_amt
    return __record(TransactionType.CREDIT, credit_amt, __balance)


def __record(txn_type: TransactionType, amount: Decimal, current_balance: Decimal):
    txn = Transaction(amount=amount,
                      current_balance=Decimal(current_balance).quantize(Decimal('.01'), rounding=ROUND_UP),
                      txn_type=txn_type)
    transactions.append(txn)
    return txn
