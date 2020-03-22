class Error:
    def __init__(self, message):
        self.message = message


class InfoError(Error):
    def __init__(self, message):
        super().__init__(message)


class BanError(Error):
    def __init__(self, message):
        super().__init__(message)


class InfoErrorUserNotFound(InfoError):
    def __init__(self):
        super().__init__("User not found")


class BanErrorUserNotFound(BanError):
    def __init__(self):
        super().__init__("User not found")


class ModifyError(Error):
    def __init__(self, message):
        super().__init__(message)


class ModifyErrorUserNotFound(ModifyError):
    def __init__(self):
        super().__init__("User not found")


class ModifyErrorInvalidEmail(ModifyError):
    def __init__(self):
        super().__init__("invalid email")


class ModifyErrorInvalidFirstName(ModifyError):
    def __init__(self):
        super().__init__("invalid first name")


class ModifyErrorInvalidStatus(ModifyError):
    def __init__(self):
        super().__init__("invalid status id")


class ModifyErrorInvalidRole(ModifyError):
    def __init__(self):
        super().__init__("invalid role id")


class ModifyErrorInvalidLastName(ModifyError):
    def __init__(self):
        super().__init__("invalid last name")


class LoginError(Error):
    def __init__(self, message):
        super().__init__(message)


class LoginErrorUserNotFound(LoginError):
    def __init__(self):
        super().__init__("User not found")


class LoginErrorWrongUsernameOrPassword(LoginError):
    def __init__(self):
        super().__init__("Wrong username or password")


class SignupError(Error):
    def __init__(self, message):
        super().__init__(message)


class SignupErrorInvalidTeacherToken(SignupError):
    def __init__(self):
        super().__init__("invalid teacher token")


class SignupErrorInvalidEmail(SignupError):
    def __init__(self):
        super().__init__("invalid email")


class SignupErrorUserExist(SignupError):
    def __init__(self):
        super().__init__("user already exist")


class SignupErrorInvalidFirstName(SignupError):
    def __init__(self):
        super().__init__("invalid first name")


class SignupErrorInvalidLastName(SignupError):
    def __init__(self):
        super().__init__("invalid last name")


class SignupErrorInvalidWeakPassword(SignupError):
    def __init__(self):
        super().__init__("password too weak")


class VerifyEmailError(Error):
    def __init__(self, message):
        super().__init__(message)


class VerifyEmailErrorUserNotFound(VerifyEmailError):
    def __init__(self):
        super().__init__("User not found")


class VerifyEmailErrorTokenNotFound(VerifyEmailError):
    def __init__(self):
        super().__init__("Token not found")


class VerifySessionError(Error):
    def __init__(self, message):
        super().__init__(message)


class VerifySessionErrorInvalidSession(VerifySessionError):
    def __init__(self):
        super().__init__("Invalid session")
