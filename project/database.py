import pymysql
from dotenv import load_dotenv
import os


def test_database():
    return pymysql.connect(
        host=os.environ.get("MYSQL_HOST"),
        user=os.environ.get("MYSQL_USER"),
        passwd=os.environ.get("MYSQL_PASSWORD"),
        db=os.environ.get("MYSQL_DATABASE")
    )
