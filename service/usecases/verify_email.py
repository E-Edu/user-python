from service.repository.email_verification import *
from service.repository.user import *
from service.error.error import *
from service.transfer.output import VerifyEmail as VerifyEmailOut
from service.transfer.input import VerifyEmail as VerifyEmailIn


def verify_email(token: VerifyEmailIn):
    email_verification = get_user_verification(token)
    if email_verification is None:
        return Error("Token not found")
    activate_user(email_verification.user_uuid)
    delete_user_verification(email_verification)
    return VerifyEmailOut()
