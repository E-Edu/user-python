from service.error import *


class SignupError(Error):
    def __init__(self, message):
        super().__init__(message)


class SignupErrorInvalidTeacherToken(SignupError):
    def __init__(self):
        super().__init__("invalid teacher token")


class SignupErrorInvalidEmail(SignupError):
    def __init__(self):
        super().__init__("invalid email")


class SignupErrorInvalidFirstName(SignupError):
    def __init__(self):
        super().__init__("invalid first name")


class SignupErrorInvalidLastName(SignupError):
    def __init__(self):
        super().__init__("invalid last name")


class SignupErrorInvalidWeakPassword(SignupError):
    def __init__(self):
        super().__init__("password too weak")
