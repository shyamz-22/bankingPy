from werkzeug.security import generate_password_hash, check_password_hash

from app import db, log


def dummy_print_for_import_optimization():
    log.info('models imported')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Email {}>'.format(self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def find_by_email(email):
        return db.session.query(User).filter(User.email == email).first()