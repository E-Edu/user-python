import mysql.connector as mariadb
from service.status import *
from service.role import *
import uuid
import os


class Database:

    def __init__(self):
        self.host, self.port, self.username, self.password, self.database = os.environ["DATABASE_HOSTNAME"], str(
            os.environ["DATABASE_PORT"]), os.environ["DATABASE_USERNAME"], os.environ["DATABASE_PASSWORD"], os.environ[
                                                                                "DATABASE_DATABASE"]
        self.connection, self.cursor = None, None

    def connect(self):
        try:
            self.connection = mariadb.connect(host=self.host, port=str(
                self.port), user=self.username, password=self.password, database=self.database)
            self.cursor = self.connection.cursor(prepared=True)
            self.connection.commit()
            print("[DATABASE] Database connected to '" +
                  self.host + ":" + str(self.port) + "'")
        except:
            print("[DATABASE] Error: Failed to connect!")

    def setup(self):
        # TODO check path
        setup_script = open("resources/setup.sql")
        self.execute(setup_script.read())
        setup_script.close()
        self.connection.commit()

    def isConnected(self):
        return self.connection is not None and self.connection.is_connected()

    def checkConnection(self):
        try:
            self.connection.ping(reconnect=True, attempts=3, delay=1)
        except mariadb.Error:
            self.connect()

    def execute(self, sql, values=()):
        try:
            return self.cursor.execute(sql, values)
        except mariadb.Error as error:
            print("[DATABASE] Error:" + str(error))

    def exist_user(self, uuid):
        self.checkConnection()
        if not self.isConnected():
            return None
        self.execute('SELECT uuid FROM User_Users WHERE uuid = ?', uuid)
        return self.cursor.fetchone() is not None

    def create_user(self, email: str, firstName: str, lastName: str, password: str, status: int, role: int):
        self.checkConnection()
        if not self.isConnected():
            return None
        # TODO implement uuid
        self.execute(
            'INSERT INTO User_Users (uuid, firstName, lastName, email, password, status, role) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (uuid, firstName, lastName, email, password, status, role))
        self.connection.commit()

    def delete_user(self, uuid):
        self.checkConnection()
        if not self.isConnected():
            return None
        self.execute('DELETE FROM User_Users WHERE uuid = ?', str(uuid))
        self.connection.commit()

    def get_user_password(self, uuid):
        self.checkConnection()
        if not self.isConnected():
            return None
        self.execute('SELECT password FROM User_Users WHERE uuid = ?', uuid)
        return self.cursor.fetchone()[0].decode("utf-8")

    def get_user_info(self, uuid):
        self.checkConnection()
        if not self.isConnected():
            return None
        self.execute('SELECT * FROM User_Users WHERE uuid = ?', str(uuid))
        info = []
        result = self.cursor.fetchone()
        if result is None:
            return None
        for row in result:
            if type(row) == bytearray:
                info.append(row.decode("utf-8"))
            else:
                info.append(row)
        info[5] = Status(info[5])
        info[7] = Role(info[7])
        return info

    def update_user_info(self, uuid, firstName=None, lastName=None, email=None, hashedPassword=None,
                         status: Status = None):
        self.checkConnection()
        if not self.isConnected():
            return None
        if firstName is not None:
            self.execute('UPDATE User_Users SET firstName = ? WHERE uuid = ?', (firstName, uuid))
        if lastName is not None:
            self.execute('UPDATE User_Users SET lastName = ? WHERE uuid = ?', (lastName, uuid))
        if email is not None:
            self.execute('UPDATE User_Users SET email = ? WHERE uuid = ?', (email, uuid))
        if hashedPassword is not None:
            self.execute('UPDATE User_Users SET password = ? WHERE uuid = ?', (hashedPassword, uuid))
        if status is not None:
            self.execute('UPDATE User_Users SET accountStatus = ? WHERE uuid = ?', (status.value, uuid))
        self.connection.commit()

    # returns the matching uuid if existing, or None
    def get_uuid_by_email(self, email):
        self.checkConnection()
        if not self.isConnected():
            return None
        self.execute('SELECT uuid FROM User_Users WHERE email = ?', email)
        res = self.cursor.fetchone()
        if res is None:
            return None
        return res[0]


    def getTeacherTokenExisting(self, teacher_token):
        self.checkConnection()
        if not self.isConnected():
            return None
        self.execute('SELECT COUNT(token) FROM User_Teacher WHERE token = ?', teacher_token)
        res = self.cursor.fetchone()
        if res is None:
            return None
        return res[0] > 0
