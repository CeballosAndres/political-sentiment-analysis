from dotenv import load_dotenv
from flask.cli import FlaskGroup
from project import app
from project.schemas.schema import Schema
import os

cli = FlaskGroup(app)

project_folder = os.path.expanduser('./')
load_dotenv(os.path.join(project_folder, '.env'))


@cli.command("create_db")
def create_db():
    conn = Schema()
    conn.exec_query("DROP TABLE IF EXISTS comment, page, post;")
    stmts = conn.parse_sql('./project/db/db_candidatos.sql')
    for stmt in stmts:
        conn.exec_query(stmt)

@cli.command("seed_db")  # new
def seed_db():
    conn = Schema()
    stmt = """ INSERT INTO page (page_id, page_name, page_name_id, political_party, kind, region) VALUES (1, "Candidato", 121, "PRD", "Presi", "Colima"); """
    conn.exec_query(stmt)


if __name__ == "__main__":
    cli()
