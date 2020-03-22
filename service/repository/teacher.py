from service.teacher import *
from service.user import *
from service import db


def search_teacher_token(token: str) -> bool:
    db.checkConnection()
    if not db.isConnected():
        return None
    db.execute('SELECT * FROM User_Teachers WHERE token = ?', token)
    result = db.cursor.fetchone()
    if result is None:
        return False
    return True


def asign_teacher_token_to_user(user: User, token: str) -> bool:
    db.checkConnection()
    if not db.isConnected():
        return None
    if not search_teacher_token(token):
        return False
    db.execute('UPDATE FROM User_Teachers SET user_uuid = ? WHERE token = ?', user.uuid, token)
    db.connection.commit()
    return True


def create_teacher(teacher: Teacher):
    db.checkConnection()
    if not db.isConnected():
        return None
    db.execute(
        'INSERT INTO User_Teachers (user_uuid, schoolDomain, token) VALUES (?, ?, ?)',
        (teacher.user_uuid, teacher.school_domain, teacher.token))
    db.connection.commit()


def delete_teacher(teacher: Teacher):
    db.checkConnection()
    if not db.isConnected():
        return None
    db.execute('DELETE FROM User_Teachers WHERE token = ?', str(teacher.token))
    db.connection.commit()
