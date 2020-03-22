from service.repository.email_verification import *
from service.repository.user import *
from service.error import *
from service.transfer import *


def verify_email(input: VerifyEmailIn):
    email_verification = get_user_verification(input.token)
    if email_verification is None:
        return Error("Token not found")
    activate_user(email_verification.user_uuid)
    delete_user_verification(email_verification)
    return VerifyEmailOut()  # TODO add session
