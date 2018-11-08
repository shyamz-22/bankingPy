from dataclasses import dataclass
from enum import Enum

from app.models import User


class UserStatus(Enum):
    FOUND = 'DEBIT'
    NOT_FOUND = 'CREDIT'


@dataclass
class AuthenticationStatus:
    user_status: UserStatus
    authenticated: bool


def authenticate(email: str, password: str) -> AuthenticationStatus:
    user = User.find_by_email(email)
    if user is None:
        return AuthenticationStatus(UserStatus.NOT_FOUND, False)

    return AuthenticationStatus(UserStatus.NOT_FOUND, user.check_password(password))
