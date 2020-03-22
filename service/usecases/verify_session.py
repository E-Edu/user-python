from service.util.jwt import *
from service.response import *
from service.transfer.input import VerifySession as VerifySessionIn
from service.transfer.output import VerifySession as VerifySessionOut
from service.error.error import *


def verify_session(input: VerifySessionIn):
    payload = jwt_decode(input.session)
    try:
        json.loads(payload)
        return VerifySessionOut()
    except ValueError:
        return Error("Invalid session")
