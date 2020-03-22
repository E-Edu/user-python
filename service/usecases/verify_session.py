from service.util.jwt import *
from service.response import *
from service.transfer.input import Session as SessionIn
from service.transfer.output import Session as SessionOut
from service.error.error import *


def verify_session(session: SessionIn):
    payload = jwt_decode(session.session)
    try:
        json.loads(payload)
        return SessionOut()
    except ValueError:
        return Error("Invalid session")
