from service.transfer.output import Info as InfoOut
from service.transfer.input import Info as InfoIn
from service.repository.user import *
from service.error.error import *


def info(input: InfoIn):
    user = get_user(input.uuid)
    if user is None:
        return Error("User not found")
    return InfoOut(user)
