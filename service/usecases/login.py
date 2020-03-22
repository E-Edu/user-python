from service.repository.user import *
from service.error import *
from service.util.jwt import *
from service.transfer import *
import bcrypt


def login(input: LoginIn):

    user = get_user_by_email(input.email)
    if user is None:
        return LoginErrorUserNotFound()

    if not __is_password_matching(input.password, user.password):
        return LoginErrorWrongUsernameOrPassword()

    payload = {
        "uuid": user.uuid,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "role": user.role,
        "status": user.status
    }
    jwt_token = jwt_encode(payload)
    return LoginOut(jwt_token)


def __is_password_matching(password: str, hashed: str) -> bool:
    password_encoded = password.encode("utf8")
    hashed_encoded = hashed.encode("utf8")
    return bcrypt.checkpw(password_encoded, hashed_encoded)
