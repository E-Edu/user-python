from service.error import *
from service.transfer import *
from service.repository.user import *


def info(input: InfoIn):
    user = get_user(input.uuid)
    if user is None:
        return InfoErrorUserNotFound()
    return InfoOut(user)
