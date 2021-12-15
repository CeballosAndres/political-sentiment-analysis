from flask import render_template
from project import app, database


@app.get("/")
def index():
    conn = database.test_database()
    cur = conn.cursor()
    cur.execute("select * from test")
    data = cur.fetchall()
    return render_template("index.html", value=data)
