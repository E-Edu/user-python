from service.teacher import *
from service.user import *
from service import database


def search_teacher_token(token: str) -> bool:
    database.checkConnection()
    if not database.isConnected():
        return None
    database.execute('SELECT * FROM User_Teachers WHERE token = ?', token)
    result = database.cursor.fetchone()
    if result is None:
        return False
    return True


def asign_teacher_token_to_user(user: User, token: str) -> bool:
    database.checkConnection()
    if not database.isConnected():
        return None
    if not search_teacher_token(token):
        return False
    database.execute('UPDATE FROM User_Teachers SET user_uuid = ? WHERE token = ?', user.uuid, token)
    database.connection.commit()
    return True


def create_teacher(teacher: Teacher):
    database.checkConnection()
    if not database.isConnected():
        return None
    database.execute(
        'INSERT INTO User_Teachers (user_uuid, schoolDomain, token) VALUES (?, ?, ?)',
        (teacher.user_uuid, teacher.school_domain, teacher.token))
    database.connection.commit()


def delete_teacher(teacher: Teacher):
    database.checkConnection()
    if not database.isConnected():
        return None
    database.execute('DELETE FROM User_Teachers WHERE token = ?', str(teacher.token))
    database.connection.commit()
