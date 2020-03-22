import bcrypt

from service.repository.email_verification import *
from service.repository.teacher import *
from service.repository.user import *
from service.role import *
from service.status import *
from service.transfer import *
from service.error import *
from service.util.check_data import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from uuid import uuid4
import os


def signup(input: SignupIn):

    if get_user_by_email(input.email) is not None:
        return SignupErrorUserExist()

    # key only exists if user wants to register as teacher
    if input.teacher_token is None:
        is_teacher = False
    elif not is_valid_teacher_token(input.teacher_token):
        return SignupErrorInvalidTeacherToken()
    else:
        is_teacher = True

    if not is_valid_email(input.email):
        return SignupErrorInvalidEmail()
    if not is_valid_name(input.first_name):
        return SignupErrorInvalidFirstName()
    if not is_valid_name(input.last_name):
        return SignupErrorInvalidLastName()
    if not is_strong_password(input.password):
        return SignupErrorInvalidWeakPassword()

    if is_teacher:
        role = Role.TEACHER
    else:
        role = Role.USER

    uuid = str(uuid4())
    while get_user(uuid) is not None:
        uuid = str(uuid4())

    password = input.password.encode("utf8")

    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(12))

    user = User(uuid, input.email, hashed_password, input.first_name, input.last_name, Status.UNVERIFIED, role, None)
    create_user(user)

    # TODO __send_verify_email(user)

    if is_teacher:
        asign_teacher_token_to_user(user, input.teacher_token)

    return SignupOut()


def __send_verify_email(user: User):
    token = str(uuid4())
    create_user_verification(user, token)

    port = os.environ["SMTP_PORT"]
    password = os.environ["SMTP_PASSWORD"]
    host = os.environ["SMTP_HOST"]
    sender_mail = os.environ["SMTP_USERNAME"]
    receiver_mail = user.email
    subject = "Verify Email"
    body = open('resources/verify_email_template.html')  # TODO check path
    message = body.read()  # TODO add token to template

    msg = MIMEMultipart()
    msg["From"] = sender_mail
    msg["To"] = receiver_mail
    msg["Subject"] = subject
    msg["X-Token"] = token
    msg.attach(MIMEText(message, 'html'))

    server = smtplib.SMTP_SSL(host, port)
    server.connect(host, port)
    server.login(sender_mail, password)

    server.sendmail(sender_mail, receiver_mail, msg.as_string())
    server.close()
