from flask.json import jsonify
from project import User, app, db


@app.get("/")
def read_root():
    users = User.query.all()
    return jsonify(users)
