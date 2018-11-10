from typing import Optional

from flask_login import UserMixin

from app import login
from app.models import User


class AuthenticatedUser(UserMixin):
    email: str
    user_id: int

    def __init__(self, user_id, email) -> None:
        super().__init__()
        self.email = email
        self.user_id = user_id

    def get_id(self):
        return self.email


# the flask-login extension expects that the application will configure a user loader function, that can be called
#  to load a user given the ID
@login.user_loader
def load_user(email: str) -> Optional[AuthenticatedUser]:
    user = User.find_by_email(email)
    if not user:
        return None

    return AuthenticatedUser(user.id, user.email)


def authenticate(email: str, password: str) -> Optional[AuthenticatedUser]:
    user = User.find_by_email(email)

    if user is None or not user.check_password(password):
        return None

    return AuthenticatedUser(user.id, email)
