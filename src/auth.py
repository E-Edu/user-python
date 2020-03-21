import bcrypt

def hash_password(plain):
    salt = bcrypt.gensalt(rounds=10)
    hashed_password = bcrypt.hashpw(plain.encode('utf-8'), salt)
    return hashed_password

def sanitize_user_input(email, first_name, last_name, teacher_token):
    pass

def verify_teacher(teacher_token):
    pass

def create_session(email):
    pass

def create_database_user(email, password, first_name, last_name, hashed_password, teacher_token):
    pass

def verify_password(teacher_token):
    pass