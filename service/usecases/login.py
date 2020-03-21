from service.response import *
import bcrypt

def user_is_valid(user_data: dict) -> dict:
    """
    takes:
    {
    'email': str,
    'password': str
    }

    checks if:
    - input keys are existing
    - user exists
    - password correct

    then returns as dict:
    {
    'error': str,
    'session': str|Null
    }
    """

    response = {
        "error": "",
        "session": None
    }

    try:
        email = user_data["email"]
        password = user_data["password"]
    except KeyError:
        error = ErrorResponse("json key not found")
        response.update(error.get_value())

    else:
        if _get_user_existing_by_email(email):
            hashed = _get_password_hash_by_email(email)

            try:
                if _is_password_matching(password, hashed):
                    response["session"] = _get_guid_by_email(email)
                else:
                    error = ErrorResponse("incorrect password")
                    response.update(error.get_value())
            except ValueError:  # raised by bcrypt if hash is invalid
                error = ErrorResponse("invalid hash from database")
                response.update(error.get_value()())

    return response


def _is_password_matching(password: str, hashed: str) -> bool:
    password_encoded = password.encode("utf8")
    hashed_encoded = hashed.encode("utf8")
    return bcrypt.checkpw(password_encoded, hashed_encoded)


def _get_user_existing_by_email(email: str) -> bool:
    # TODO get from db
    return False


def _get_password_hash_by_email(email: str) -> str:
    # TODO get from db
    return ""


def _get_guid_by_email(email: str) -> str:
    # TODO get from db
    return ""
