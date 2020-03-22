from service.user import *
from service.status import *
from service.role import *
from service import database


def user_exists(uuid):
    database.checkConnection()
    if not database.isConnected():
        return None
    database.execute('SELECT uuid FROM User_Users WHERE uuid = ?', uuid)
    return database.cursor.fetchone() is not None


def get_user(uuid):
    database.checkConnection()
    if not database.isConnected():
        return None
    database.execute('SELECT * FROM User_Users WHERE uuid = ?', str(uuid))
    result = database.cursor.fetchone()
    return __extract_user_from_database_request(result)


def activate_user(uuid: str):
    database.checkConnection()
    if not database.isConnected():
        return None
    database.execute('UPDATE User_Users SET status = ? WHERE uuid = ?', (Status.VERIFIED, uuid))
    database.connection.commit()


# returns the matching uuid if existing, or None
def get_user_by_email(email):
    database.checkConnection()
    if not database.isConnected():
        return None
    database.execute('SELECT * FROM User_Users WHERE email = ?', email)
    result = database.cursor.fetchone()
    return __extract_user_from_database_request(result)


def update_user(user: User):
    database.checkConnection()
    if not database.isConnected():
        return None
    if user.email is not None:
        database.execute('UPDATE User_Users SET email = ? WHERE uuid = ?', (user.email, user.uuid))
    if user.password is not None:
        database.execute('UPDATE User_Users SET password = ? WHERE uuid = ?', (user.password, user.uuid))
    if user.first_name is not None:
        database.execute('UPDATE User_Users SET firstName = ? WHERE uuid = ?', (user.first_name, user.uuid))
    if user.last_name is not None:
        database.execute('UPDATE User_Users SET lastName = ? WHERE uuid = ?', (user.last_name, user.uuid))
    if user.status is not None:
        database.execute('UPDATE User_Users SET accountStatus = ? WHERE uuid = ?', (user.status.value, user.uuid))
    if user.role is not None:
        database.execute('UPDATE User_Users SET role = ? WHERE uuid = ?', (user.role.value, user.uuid))
    database.connection.commit()


def create_user(user: User):
    database.checkConnection()
    if not database.isConnected():
        return None
    database.execute(
        'INSERT INTO User_Users (uuid, email, password, firstName, lastName, status, role) VALUES (?, ?, ?, ?, ?, ?, ?)',
        (user.uuid, user.first_name, user.last_name, user.email, user.password, user.status, user.role))
    database.connection.commit()


def delete_user(uuid):
    database.checkConnection()
    if not database.isConnected():
        return None
    database.execute('DELETE FROM User_Users WHERE uuid = ?', str(uuid))
    database.connection.commit()


def __extract_user_from_database_request(request_result):
    data = []
    if request_result is None:
        return None
    for row in request_result:
        if type(row) == bytearray:
            data.append(row.decode("utf-8"))
        else:
            data.append(row)
    return User(data[0], data[1], data[2], data[3], data[4], Status(data[5]), Role(data[6]), data[7])
