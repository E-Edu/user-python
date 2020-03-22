from service.repository.user import *
from service.util.jwt import *
from service.util.check_data import *
from service.transfer import *
from service.error import *


def modify(user_data: ModifyIn):
    jwt_paylaod = jwt_decode(user_data["session"])
    user = get_user(jwt_paylaod["uuid"])
    if user is None:
        return ModifyErrorUserNotFound()

    if "last_name" in user_data:
        if not is_valid_name(user_data.last_name):
            return ModifyErrorInvalidLastName()
        user.last_name = user_data["last_name"]

    if "first_name" in user_data:
        if not is_valid_name(user_data.first_name):
            return ModifyErrorInvalidFirstName()
        user.first_name = user_data["first_name"]

    if "email" in user_data:
        if not is_valid_email(user_data.email):
            return ModifyErrorInvalidEmail()
        user.email = user_data["email"]

    if "status" in user_data:
        if user_data["status"] == Status.UNVERIFIED:
            user.status = Status.UNVERIFIED
        elif user_data["status"] == Status.VERIFIED:
            user.status = Status.VERIFIED
        elif user_data["status"] == Status.REPORTED:
            user.status = Status.REPORTED
        elif user_data["status"] == Status.BANNED:
            user.status = Status.BANNED
        else:
            return ModifyErrorInvalidStatus()

    if "role" in user_data:
        if user_data["role"] == Status.USER:
            user.role = Status.USER
        elif user_data["role"] == Status.TEACHER:
            user.role = Status.TEACHER
        elif user_data["role"] == Status.ADMIN:
            user.role = Status.ADMIN
        elif user_data["role"] == Status.PRIVILEGED_STUDENT:
            user.role = Status.PRIVILEGED_STUDENT
        else:
            return ModifyErrorInvalidRole()

    update_user(user)
    return ModifyOut()
