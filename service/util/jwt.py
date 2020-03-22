import os
import jwt
ALGORITHM = "HS256"


def jwt_encode(payload):
    return (jwt.encode(payload, os.environ["JWT_SECRET"], algorithm=ALGORITHM)).decode("utf-8")


def jwt_decode(encoded):
    return jwt.decode(encoded.encode("utf-8"), os.environ["JWT_SECRET"], algorithms=ALGORITHM)
