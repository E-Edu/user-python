from service import User, jwt_encode


def create_session(user: User):
    payload = {
        "uuid": user.uuid,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "role": user.role,
        "status": user.status
    }
    return jwt_encode(payload)
