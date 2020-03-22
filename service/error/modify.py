from service.error import *


class ModifyError(Error):
    def __init__(self, message):
        super().__init__(message)


class ModifyErrorUserNotFound(ModifyError):
    def __init__(self):
        super().__init__("User not found")
