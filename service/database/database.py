import mysql.connector as mariadb
import os


class Database:  # TODO check if we can reduce function calls for isConnected and chechConnection

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
        setup_script_text = setup_script.read()
        setup_script_statements = setup_script_text.split(";")
        setup_script.close()
        for i in setup_script_statements:
            if not i.strip():
                continue
            self.execute(i)
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
