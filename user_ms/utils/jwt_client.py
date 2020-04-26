import os
import jwt

from user_ms.config import JWT

from datetime import datetime
ALGORITHM = "HS256"


def jwt_encode(payload):
    return (jwt.encode(payload, os.environ["JWT_SECRET"], algorithm=ALGORITHM)).decode("utf-8")


def jwt_decode(encoded):
    return jwt.decode(encoded.encode("utf-8"), os.environ["JWT_SECRET"], algorithms=ALGORITHM)

def create_session(user):
    return jwt.encode({
        'exp': datetime.utcnow() + 900,
        'iat': datetime.utcnow(),
        'iss': 'e-edu',

        'id': user.id,
        'email': user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "role": user.role
         }, JWT.JWT_SEC, algorithm=JWT.JWT_ALGORITHMS)