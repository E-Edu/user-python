from service.email_verification import *
from service import database


def get_user_verification(token: str) -> EmailVerification:
    database.checkConnection()
    if not database.isConnected():
        return None
    database.execute('SELECT * FROM User_Verification WHERE token = ?', token)
    result = database.cursor.fetchone()
    if result is not None:
        result = EmailVerification(result.user_uuid, result.verification_code, result.createdAt)
    return result


def delete_user_verification(email_verification: EmailVerification):
    database.checkConnection()
    if not database.isConnected():
        return None
    database.execute('DELETE FROM User_Verification WHERE token = ?', str(email_verification.token))
    database.connection.commit()
