from service.email_verification import *
from service.repository import db
from service.user import *


def create_user_verification(user: User, token: str):
    db.checkConnection()
    if not db.isConnected():
        return None
    db.execute(
        'INSERT INTO User_Verification (user_uuid, verification_code) VALUES (?, ?)',
        (user.uuid, token))
    db.connection.commit()


def get_user_verification(token: str) -> EmailVerification:
    db.checkConnection()
    if not db.isConnected():
        return None
    db.execute('SELECT * FROM User_Verification WHERE token = ?', token)
    result = db.cursor.fetchone()
    if result is not None:
        result = EmailVerification(result.user_uuid, result.verification_code, result.createdAt)
    return result


def delete_user_verification(email_verification: EmailVerification):
    db.checkConnection()
    if not db.isConnected():
        return None
    db.execute('DELETE FROM User_Verification WHERE token = ?', str(email_verification.token))
    db.connection.commit()
