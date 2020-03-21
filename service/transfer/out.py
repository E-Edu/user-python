from service.response import *
from service.user import *


class Login(Response):
    def __init__(self, session, error):
        if error is not None:
            super().__init__({"error": error}, 400)
        else:
            super().__init__({"session": session}, 200)


class User(Response):
    def __init__(self, user: User, error):
        if error is not None:
            super().__init__({"error": error}, 400)
        else:
            super().__init__({
                "teacher": user.role == 0,
                "admin": user.role == 2,
                "priviliged_student": user.role == 3,
                "report_spammer": user.status == 2
            }, 201)


class Verify(Response):
    def __init__(self, session, error):
        if error is not None:
            super().__init__({"error": error}, 400)
        else:
            super().__init__({"session": session}, 200)
