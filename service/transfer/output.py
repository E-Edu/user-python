from service.user import *
from service.status import *
from service.role import *


class Login:
    def __init__(self, session):
        self.session = session


class Signup:
    def __init__(self):
        pass


class Info:
    def __init__(self, user: User):
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.email = user.email
        self.role = user.role
        self.status = user.status
        self.created_at = user.created


class Ban:
    def __init__(self):
        pass


class Modify:
    def __init__(self):
        pass


class VerifyEmail:
    def __init__(self, session):
        self.session = session


class VerifySession:
    def __init__(self):
        pass
