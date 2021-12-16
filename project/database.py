import pymysql
import os


def test_database():
    # Los valores los toma de .env
    return pymysql.connect(
        host=os.environ.get("MYSQL_HOST"),
        port=int(os.environ.get("MYSQL_PORT")),
        user=os.environ.get("MYSQL_USER"),
        passwd=os.environ.get("MYSQL_PASSWORD"),
        db=os.environ.get("MYSQL_DATABASE")
    )
