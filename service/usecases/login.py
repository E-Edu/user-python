from service.response import *
from service.repository.user import *
from service.error.error import *
from service.util.jwt import *
from service.transfer.input import Login as LoginIn
from service.transfer.output import Login as LoginOut
import bcrypt


def login(input: LoginIn):

    user = get_user_by_email(input.email)

    if not __is_password_matching(input.password, user.password):
        return Error("Wrong username or password")

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
