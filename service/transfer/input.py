class Login:
    def __init__(self, obj: dict):
        self.email = obj["email"]
        self.password = obj["password"]


class Signup:
    def __init__(self, obj: dict):
        self.email = obj["email"]
        self.password = obj["password"]
        self.first_name = obj["first_name"]
        self.last_name = obj["last_name"]
        self.teacher_token = obj["teacher_token"]


class Info:
    def __init__(self, uuid):
        self.uuid = uuid


class Ban:
    def __init__(self, uuid):
        self.uuid = uuid


class Modify:
    def __init__(self, obj: dict):
        self.session = obj["session"]
        self.user = obj["user"]
        self.teacher = obj["teacher"]
        self.admin = obj["admin"]
        self.priviliged_student = obj["priviliged_student"]
        self.report_spammer = obj["report_spammer"]


class VerifyEmail:
    def __init__(self, obj: dict):
        self.token = obj["token"]


class VerifySession:
    def __init__(self, obj: dict):
        self.session = obj["session"]