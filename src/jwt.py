import os
import jwt
ALGORITHM = "ES256"

def encode(payload):
    return jwt.encode(payload, os.environ["JWT_SECRET"], algorithm=ALGORITHM)


def decode(encoded):
    return jwt.decode(encoded, os.environ["JWT_SECRET"], algorithms=ALGORITHM)
