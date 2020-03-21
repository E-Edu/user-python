import mysql.connector as mariadb
import os
from database import accountStatus, role

class Database():

    def __init__(self):
        self.host, self.port, self.username, self.password, self.database = os.environ["DATABASE_HOSTNAME"], str(os.environ["DATABASE_PORT"]), os.environ["DATABASE_USERNAME"], os.environ["DATABASE_PASSWORD"], os.environ["DATABASE_DATABASE"]
        self.connection, self.cursor = None, None

    def connect(self):
        try:
            self.connection = mariadb.connect(host=self.host, port=str(self.port), user=self.username, password=self.password, database=self.database)
            self.cursor = self.connection.cursor(prepared=True)
            self.connection.commit()
            print("[DATABASE] Database connected to '" + self.host + ":" + str(self.port) + "'")
        except: print("[DATABASE] Error: Failed to connect!")
        
    def setup(self):
        self.execute('CREATE TABLE IF NOT EXISTS User_Users (userId INT NOT NULL AUTO_INCREMENT, firstName VARCHAR(255), lastName VARCHAR(255), email VARCHAR(255), password VARCHAR(255), accountStatus INT, createdAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(), role INT, PRIMARY KEY (userId))')
        self.connection.commit()

    def isConnected(self):
        return self.connection is not None and self.connection.is_connected()

    def checkConnection(self):
        try:
            self.connection.ping(reconnect=True, attempts=3, delay=1)
        except mariadb.Error:
            self.connect()

    def execute(self, sql, values=()):
        try: return self.cursor.execute(sql, values)
        except mariadb.Error as error:
            print("[DATABASE] Error:" + str(error))

    def existUser(self, email):
        self.checkConnection()
        if not self.isConnected(): return None
        self.execute('SELECT userId FROM User_Users WHERE email = ?', (email,))
        return self.cursor.fetchone() is not None

    def createUser(self, firstName, lastName, email, hashedPassword, role: role.Role):
        self.checkConnection()
        if not self.isConnected(): return None
        self.execute('INSERT INTO User_Users (firstName, lastName, email, password, accountStatus, role) VALUES (?, ?, ?, ?, ?, ?)', (firstName, lastName, email, hashedPassword, 0, role.value))
        self.connection.commit()

    def deleteUser(self, userId):
        self.checkConnection()
        if not self.isConnected(): return None
        self.execute('DELETE FROM User_Users WHERE userId = ?', (str(userId),))
        self.connection.commit()

    def getUserPassword(self, email):
        self.checkConnection()
        if not self.isConnected(): return None
        self.execute('SELECT password FROM User_Users WHERE email = ?', (email,))
        return self.cursor.fetchone()[0].decode("utf-8")

    def getUserInfo(self, userId):
        self.checkConnection()
        if not self.isConnected(): return None
        self.execute('SELECT * FROM User_Users WHERE userId = ?', (str(userId),))
        info = []
        result = self.cursor.fetchone()
        if result is None: return None
        for row in result:
            if type(row) == bytearray: info.append(row.decode("utf-8"))
            else: info.append(row)
        info[5] = accountStatus.AccountStatus(info[5])
        info[7] = role.Role(info[7])
        return info

    def updateUserInfo(self, userId, firstName=None, lastName=None, email=None, hashedPassword=None, accountStatus: accountStatus.AccountStatus=None):
        self.checkConnection()
        if not self.isConnected(): return None
        if firstName is not None:
            self.execute('UPDATE User_Users SET firstName = ? WHERE userId = ?', (firstName, userId))
        if lastName is not None:
            self.execute('UPDATE User_Users SET lastName = ? WHERE userId = ?', (lastName, userId))
        if email is not None:
            self.execute('UPDATE User_Users SET email = ? WHERE userId = ?', (email, userId))
        if hashedPassword is not None:
            self.execute('UPDATE User_Users SET password = ? WHERE userId = ?', (hashedPassword, userId))
        if accountStatus is not None:
            self.execute('UPDATE User_Users SET accountStatus = ? WHERE userId = ?', (accountStatus.value, userId))
        self.connection.commit()

    def getUserIdByEmail(self, email):
        self.checkConnection()
        if not self.isConnected(): return None
        self.execute('SELECT userId FROM User_Users WHERE email = ?', (email,))
        return self.cursor.fetchone()[0]