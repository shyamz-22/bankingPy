from typing import Optional

from flask_login import UserMixin

from app import login
from app.models import User


class AuthenticatedUser(UserMixin):
    user_id: str

    def __init__(self, email) -> None:
        super().__init__()
        self.user_id = email

    def get_id(self):
        return self.user_id


# the flask-login extension expects that the application will configure a user loader function, that can be called
#  to load a user given the ID
@login.user_loader
def load_user(user_id: str) -> Optional[AuthenticatedUser]:
    user = User.find_by_email(user_id)
    if not user:
        return None

    return AuthenticatedUser(user.email)


def authenticate(email: str, password: str) -> Optional[AuthenticatedUser]:
    user = User.find_by_email(email)

    if user is None or not user.check_password(password):
        return None

    return AuthenticatedUser(email)
