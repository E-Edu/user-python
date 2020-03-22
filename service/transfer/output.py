from service.response import *
from service.user import *


class Login:
    def __init__(self, session):
        self.session = session


class Session:
    def __init__(self):
        pass


class User:
    def __init__(self, user: User):
        self.teacher = user.role == 0,
        self.admin = user.role == 2,
        self.priviliged_student = user.role == 3,
        self.report_spammer = user.status == 2


class Modify:
    def __init__(self):
        pass


class VerifyEmail:
    def __init__(self, session):
        self.session = session


class Signup:
    def __init__(self):
        pass
