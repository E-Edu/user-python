import re

def is_strong_password(password) -> bool:
    if len(password) < 8:
        return False
    elif re.search('[0-9]', password) is None:
        return False
    elif re.search('[a-zA-Z]', password) is None:
        return False
    return True


def is_valid_name(name) -> bool:
    if re.match(r"^[a-zA-Z]+$", name) is None:
        return False
    elif len(name) < 0:
        return False
    elif len(name) > 32:
        return False
    return True


def is_valid_email(email) -> bool:
    if re.match(r"[^@]+@[^@]+\.[^@]+", email) is None:
        return False
    elif len(email) > 64:
        return False
    return True