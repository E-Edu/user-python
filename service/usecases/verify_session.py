from service.util.jwt import *
from service.transfer import *
from service.error import *
import jwt


def verify_session(input: VerifySessionIn):
    try:
        jwt_decode(input.session)
        return VerifySessionOut()
    except jwt.exceptions.PyJWTError:
        return VerifySessionErrorInvalidSession()
