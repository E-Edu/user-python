from service.transfer.output import *
from service.repository.user import *
from service.error.error import *


def info(user_uuid):
    user = get_user(user_uuid)
    if user is None:
        return Error("User not found")
    return User(user)
