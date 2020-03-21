from service.util.jwt import *
from service.response import *


def verify_session(session: str):
    payload = jwt_decode(session)
    try:
        json.loads(payload)
        return Response({}, 200)
    except ValueError:
        return ErrorResponse("Invalid session", 401)
