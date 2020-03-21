import bcrypt
import re


def hash_password(plain):
    salt = bcrypt.gensalt(rounds=10)
    hashed_password = bcrypt.hashpw(plain.encode('utf-8'), salt)
    return hashed_password


def sanitize_user_input(email, first_name, last_name, teacher_token):
    errors = []
    if not valid_email(email): errors.append("invalid email")
    if not valid_name(first_name): errors.append("invalid first name")
    if not valid_name(last_name): errors.append("invalid last name")
    return errors


def verify_teacher(teacher_token):
    pass


def create_session(email):
    pass


def create_database_user(email, password, first_name, last_name, hashed_password, teacher_token):
    pass


def verify_password(teacher_token):
    pass


def valid_name(name):
    if re.match(r"^[a-zA-Z]+$", name) is None:
        return False
    return True


def valid_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email) is None:
        return False
    return True


