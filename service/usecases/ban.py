from service.error import *
from service.transfer import *
from service.repository.user import *


def ban(user_uuid: BanIn):
    user = get_user(user_uuid.uuid)
    if user is None:
        return BanErrorUserNotFound()
    user.status = Status.BANNED
    update_user(user)
    return BanOut()
