from service.repository.teacher import *
from service.repository.user import *
from service.role import *
from service.status import *
from service.transfer import *
from service.error import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from uuid import uuid4
import re
import os


def signup(input: SignupIn):

    is_teacher = False

    # key only exists if user wants to register as teacher
    if not __is_valid_teacher_token(input.teacher_token):
        return SignupErrorInvalidTeacherToken()
    else:
        is_teacher = True

    if not __is_valid_email(input.email):
        return SignupErrorInvalidEmail()
    if not __is_valid_name(input.first_name):
        return SignupErrorInvalidFirstName()
    if not __is_valid_name(input.last_name):
        return SignupErrorInvalidLastName()
    if not __is_strong_password(input.password):
        return SignupErrorInvalidWeakPassword()

    if is_teacher:
        role = Role.TEACHER
    else:
        role = Role.USER

    uuid = uuid4()
    while get_user(uuid) is not None:
        uuid = uuid4()

    user = User(uuid, input.email, input.password, input.first_name, input.last_name, Status.UNVERIFIED, role, None)
    create_user(user)

    __send_verify_email(input.email)

    if is_teacher:
        asign_teacher_token_to_user(user, input.teacher_token)

    return SignupOut()


def __is_valid_teacher_token(teacher_token) -> bool:
    if len(teacher_token) != 32:
        return False
    elif re.search('[a-zA-Z0-9\\-]', teacher_token):
        return search_teacher_token(teacher_token)  # TODO Teacher Repository
    return False


def __is_strong_password(password) -> bool:
    if len(password) < 8:
        return False
    elif re.search('[0-9]', password) is None:
        return False
    elif re.search('[a-zA-Z]', password) is None:
        return False
    return True


def __is_valid_name(name) -> bool:
    if re.match(r"^[a-zA-Z]+$", name) is None:
        return False
    elif len(name) < 0:
        return False
    elif len(name) > 32:
        return False
    return True


def __is_valid_email(email) -> bool:
    if re.match(r"[^@]+@[^@]+\.[^@]+", email) is None:
        return False
    elif len(email) > 64:
        return False
    return True


def __send_verify_email(email):

    # TODO: add Token from Database to mail

    port = os.environ["SMTP_PORT"] # ssl port
    password = os.environ["SMTP_PASSWORD"]
    host = os.environ["SMTP_HOST"]
    sender_mail = os.environ["SMTP_USERNAME"]
    receiver_mail = email
    subject = "Verify Email"
    body = open('resources/verify_email_template.html')  # TODO check path
    message = body.read()

    msg = MIMEMultipart()  # message of mail
    msg["From"] = sender_mail
    msg["To"] = receiver_mail
    msg["Subject"] = subject
    msg.attach(MIMEText(message, 'html'))

    server = smtplib.SMTP_SSL(host, port)
    server.connect(host, port)
    server.login(sender_mail, password)

    server.sendmail(sender_mail, receiver_mail, msg.as_string())
    server.close()
