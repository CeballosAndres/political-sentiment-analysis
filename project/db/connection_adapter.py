"""Module for connection to database"""
import pymysql

class ConnectionAdapter():
    """Generic connector for database queries"""
    def __init__(self):
        self.__host = ""
        self.__user = ""
        self.__password = ""
        self.__db = ""
        self.connection = None

    def cursor(self):
        """Makes the db connection and returns cursor"""
        self.connection = pymysql.connect(
            host=self.__host,
            user=self.__user,
            passwd=self.__password,
            db=self.__db
        )
        return self.connection.cursor(pymysql.cursors.DictCursor)

    def commit(self):
        """Commits the connection"""
        self.connection.commit()
