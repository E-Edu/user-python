from service.repository.user import *
from service.error import *
from service.util.create_session import create_session
from service.transfer import *
import bcrypt


def login(input: LoginIn):

    user = get_user_by_email(input.email)
    if user is None:
        return LoginErrorUserNotFound()

    if not __is_password_matching(input.password, user.password):
        return LoginErrorWrongUsernameOrPassword()

    return LoginOut(create_session(user))


def __is_password_matching(password: str, hashed: str) -> bool:
    password_encoded = password.encode("utf8")
    hashed_encoded = hashed.encode("utf8")
    return bcrypt.checkpw(password_encoded, hashed_encoded)
