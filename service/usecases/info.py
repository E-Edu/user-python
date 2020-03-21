from service.transfer.out import *
from service.repository.user import *


def info(user_uuid):
    user = get_user(user_uuid)
    error = None
    if user is None:
        error = "User not found"
    return User(user, error)
