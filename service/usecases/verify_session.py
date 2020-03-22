from service.util.jwt import *
from service.response import *
from service.transfer import *
from service.error import *


def verify_session(input: VerifySessionIn):
    payload = jwt_decode(input.session)
    try:
        json.loads(payload)
        return VerifySessionOut()
    except ValueError:
        return VerifySessionErrorInvalidSession()
