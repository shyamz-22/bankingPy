from typing import Optional

from flask_login import UserMixin

from app import login
from app.models import User


class AuthenticatedUser(UserMixin):
    id: str

    def __init__(self, email) -> None:
        super().__init__()
        self.id = email


# the flask-login extension expects that the application will configure a user loader function, that can be called
#  to load a user given the ID
@login.user_loader
def load_user(id) -> Optional[AuthenticatedUser]:
    user = User.find_by_email(id)
    if user is None:
        return None

    return AuthenticatedUser(user.email)


def authenticate(email: str, password: str) -> Optional[AuthenticatedUser]:
    user = User.find_by_email(email)

    if user is None or not user.check_password(password):
        return None

    return AuthenticatedUser(email)
