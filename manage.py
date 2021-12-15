from dotenv import load_dotenv
from flask.cli import FlaskGroup

from project import app, database

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    my_connection = database.test_database()
    cursor = my_connection.cursor()
    cursor.execute(
        "create table test (nombre varchar(50), apellido varchar(50)) ")
    my_connection.commit()


@cli.command("seed_db")  # new
def seed_db():
    my_connection = database.test_database()
    cursor = my_connection.cursor()
    cursor.execute(
        """insert into test (nombre, apellido) values ("andres","ceballos")""")
    my_connection.commit()


if __name__ == "__main__":
    cli()
