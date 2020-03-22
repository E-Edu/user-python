from service.error import *


class InfoError(Error):
    def __init__(self, message):
        super().__init__(message)


class InfoErrorUserNotFound(InfoError):
    def __init__(self):
        super().__init__("User not found")
