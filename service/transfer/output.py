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
    def __init__(self, user: User):  # TODO remove unnecessary fields
        self.teacher = user.role == Role.TEACHER,
        self.admin = user.role == Role.ADMIN,
        self.priviliged_student = user.role == Role.PRIVILEGED_STUDENT,
        self.report_spammer = user.status == Status.REPORTED
        self.role = user.role
        self.status = user.status


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
