from service.error import *


class VerifySessionError(Error):
    def __init__(self, message):
        super().__init__(message)


class VerifySessionErrorInvalidSession(VerifySessionError):
    def __init__(self):
        super().__init__("Invalid session")
