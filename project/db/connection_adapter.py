"""Module for connection to database"""
import pymysql
import os

class ConnectionAdapter():
    """Generic connector for database queries"""
    def __init__(self):
        self.__host = os.environ.get("MYSQL_HOST")
        self.__user = os.environ.get("MYSQL_USER")
        self.__password = os.environ.get("MYSQL_PASSWORD")
        self.__db = os.environ.get("MYSQL_DATABASE") 
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
