from service.error import *


class LoginError(Error):
    def __init__(self, message):
        super().__init__(message)


class LoginErrorUserNotFound(LoginError):
    def __init__(self):
        super().__init__("User not found")


class LoginErrorWrongUsernameOrPassword(LoginError):
    def __init__(self):
        super().__init__("Wrong username or password")
