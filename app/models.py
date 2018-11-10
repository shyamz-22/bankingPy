from datetime import datetime
from decimal import Decimal

from sqlalchemy import String, Numeric, DateTime, Integer
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(String(120), index=True, unique=True)
    password_hash = db.Column(String(128))
    balance = db.Column(Numeric(6, 2))
    created_date = db.Column(DateTime)
    updated_date = db.Column(DateTime)

    def __repr__(self):
        return '<Email {}>'.format(self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password_hash, password)

    def add_transaction(self,
                        txn_type: str,
                        txn_amount: Decimal,
                        current_balance: Decimal,
                        date=datetime.utcnow()):
        txn = Transaction(user_id=self.id,
                          txn_amount=txn_amount,
                          current_balance=current_balance,
                          txn_type=txn_type,
                          date=date)

        txn.add()

    @staticmethod
    def find_by_email(email):
        return db.session.query(User).filter(User.email == email).one()

    @staticmethod
    def update_balance(email, balance):
        user = db.session.query(User).with_lockmode('update').filter(User.email == email).one()
        user.balance = balance
        user.updated_date = datetime.utcnow()
        db.session.commit()


class Transaction(db.Model):
    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(Integer, nullable=False)
    txn_amount = db.Column(Numeric(6, 2), nullable=False)
    current_balance = db.Column(Numeric(6, 2), nullable=False)
    txn_type = db.Column(String(20), nullable=False)
    date = db.Column(DateTime, nullable=False)

    def add(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def list(user_id: Integer, limit: int = 10):
        return (Transaction.query
                .filter_by(user_id=user_id)
                .order_by(Transaction.date.desc())
                .limit(limit)
                .all())
