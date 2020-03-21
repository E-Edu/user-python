import mysql.connector as mariadb
from enum import Enum
import os

class Role(Enum):
    USER = 0
    TEACHER = 1
    ADMIN = 2

class AccountStatus(Enum):
    UNVERIFIED = 0
    VERIFIED = 1
    REPORTED = 2
    BANNED = 3

class Database():

    #def __init__(self, host, port, username, password, database):
    #    self.host, self.port, self.username, self.password, self.database = host, port, username, password, database
    #    self.connection, self.cursor = None, None

    def __int__(self):
        self.host, self.port, self.username, self.password, self.database = "localhost", "3306", os.environ["MYSQL_USER"], os.environ["MYSQL_PASSWORD"], os.environ["MYSQL_RANDOM_ROOT_PASSWORD"]
        self.connection, self.cursor = None, None

    def connect(self):
        self.connection = mariadb.connect(host=self.host, port=str(self.port), user=self.username, password=self.password, database=self.database)
        self.cursor = self.connection.cursor(prepared=True)
        self.connection.commit()
        print("Database connected to '" + self.host + ":" + str(self.port) + "'")

    def isConnected(self):
        return self.connection is not None and self.connection.is_connected()

    def checkConnection(self):
        if not self.isConnected():
            self.connect()

    def execute(self, sql, values=()):
        try:
            return self.cursor.execute(sql, values)
        except mariadb.Error as error:
            print("Error:" + str(error))

    def existUser(self, email):
        self.checkConnection()
        if not self.isConnected(): return None
        self.execute('SELECT userId FROM Users WHERE email = ?', (email,))
        return self.cursor.fetchone() is not None

    def createUser(self, firstName, lastName, email, hashedPassword, role: Role):
        self.checkConnection()
        if not self.isConnected(): return None
        self.execute('INSERT INTO Users (firstName, lastName, email, password, accountStatus, role) VALUES (?, ?, ?, ?, ?, ?)', (firstName, lastName, email, hashedPassword, 0, role.value))
        self.connection.commit()

    def deleteUser(self, userId):
        self.checkConnection()
        if not self.isConnected(): return None
        self.execute('DELETE FROM Users WHERE userId = ?', (str(userId),))
        self.connection.commit()

    def getUserPassword(self, email):
        self.checkConnection()
        if not self.isConnected(): return None
        self.execute('SELECT password FROM Users WHERE email = ?', (email,))
        return self.cursor.fetchone()[0].decode("utf-8")

    def getUserInfo(self, userId):
        self.checkConnection()
        if not self.isConnected(): return None
        self.execute('SELECT * FROM Users WHERE userId = ?', (str(userId),))
        info = []
        result = self.cursor.fetchone()
        if result is None: return None
        for row in result:
            if type(row) == bytearray: info.append(row.decode("utf-8"))
            else: info.append(row)
        info[5] = AccountStatus(info[5])
        info[7] = Role(info[7])
        return info

    def updateUserInfo(self, userId, firstName=None, lastName=None, email=None, hashedPassword=None, accountStatus=None):
        self.checkConnection()
        if not self.isConnected(): return None
        if firstName is not None:
            self.execute('UPDATE Users SET firstName = ? WHERE userId = ?', (firstName, userId))
        if lastName is not None:
            self.execute('UPDATE Users SET lastName = ? WHERE userId = ?', (lastName, userId))
        if email is not None:
            self.execute('UPDATE Users SET email = ? WHERE userId = ?', (email, userId))
        if hashedPassword is not None:
            self.execute('UPDATE Users SET password = ? WHERE userId = ?', (hashedPassword, userId))
        if accountStatus is not None:
            self.execute('UPDATE Users SET accountStatus = ? WHERE userId = ?', (accountStatus, userId))
        self.connection.commit()

    def getUserIdByEmail(self, email):
        self.checkConnection()
        if not self.isConnected(): return None
        self.execute('SELECT userId FROM Users WHERE email = ?', (email,))
        return self.cursor.fetchone()[0]