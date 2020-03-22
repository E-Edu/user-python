from service.error import *


class VerifyEmailError(Error):
    def __init__(self, message):
        super().__init__(message)


class VerifyEmailErrorTokenNotFound(VerifyEmailError):
    def __init__(self):
        super().__init__("Token not found")
