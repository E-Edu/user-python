from service.response import *
from service.repository.teacher import *
from service.repository.user import *
from service.usecases.send_verify_email import *
from service.role import *
from service.status import *
from service.transfer.input import Signup as SignupIn
from service.transfer.output import Signup as SignupOut
from service.error.error import *
from uuid import uuid4
import re


def signup(data: SignupIn) -> ErrorResponse:
    is_teacher = False
    # key only exists if user wants to register as teacher
    if "teacher_token" in data.keys():
        teacher_token = data["teacher_token"]
        if not _is_valid_teacher_token(teacher_token):
            return Error("invalid teacher token")
        is_teacher = True

    if not _is_valid_email(data.email):
        return Error("invalid email")
    if not _is_valid_name(data.first_name):
        return Error("invalid first name")
    if not _is_valid_name(data.last_name):
        return Error("invalid last name")
    if not _is_strong_password(data.password):
        return Error("password too weak")

    uuid = uuid4()

    while get_user(uuid) is not None:
        uuid = uuid4()

    if is_teacher:
        role = Role.TEACHER
    else:
        role = Role.USER
    user = User(uuid, data.email, data.password, data.first_name, data.last_name, Status.UNVERIFIED, role, None)
    create_user(user)

    send_verify_email(data.email)

    if is_teacher:
        asign_teacher_token_to_user(user, teacher_token)

    return SignupOut()


def _is_valid_teacher_token(teacher_token) -> bool:
    if len(teacher_token) != 32:
        return False
    elif re.search('[a-zA-Z0-9\\-]', teacher_token):
        return search_teacher_token(teacher_token)  # TODO Teacher Repository
    return False


def _is_strong_password(self, password) -> bool:
    if len(password) < 8:
        return False
    elif re.search('[0-9]', password) is None:
        return False
    elif re.search('[a-zA-Z]', password) is None:
        return False
    return True


def _is_valid_name(self, name) -> bool:
    if re.match(r"^[a-zA-Z]+$", name) is None:
        return False
    elif len(name) < 0:
        return False
    elif len(name) > 32:
        return False
    return True


def _is_valid_email(self, email) -> bool:
    if re.match(r"[^@]+@[^@]+\.[^@]+", email) is None:
        return False
    elif len(email) > 64:
        return False
    return True
