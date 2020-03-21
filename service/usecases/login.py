from service.response import *
from service.repository.user import *
from service.util.jwt import *
import bcrypt


def login(user_data: dict) -> dict:

    try:
        email = user_data["email"]
        password = user_data["password"]
    except KeyError:
        error = ErrorResponse("json key not found", 404)
        return error.get_json_value(), error.get_code()

    user = get_user_by_email(email)

    if __is_password_matching(password, user.password):
        payload = {
              "uuid": user.uuid,
              "email": user.email,
              "first_name": user.first_name,
              "last_name": user.last_name,
              "role": user.role,
              "status": user.status
            }
        jwt_token = jwt_encode(payload)
        return Response({"session": jwt_token}, 200)

    error = ErrorResponse("wrong username or password", 404)
    return error.get_json_value(), error.get_code()


def __is_password_matching(password: str, hashed: str) -> bool:
    password_encoded = password.encode("utf8")
    hashed_encoded = hashed.encode("utf8")
    return bcrypt.checkpw(password_encoded, hashed_encoded)

