import re


def valid_name(name):
    if re.match(r"^[a-zA-Z]+$", name) is None:
        return False
    return True


def valid_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email) is None:
        return False
    return True

