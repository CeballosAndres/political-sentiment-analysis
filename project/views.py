from flask import render_template
from project import app
from project.schemas.post_schema import PostSchema
from project.schemas.page_schema import PageSchema
from project.schemas.comment_schema import CommentSchema


@app.get("/")
def index():
    page_db = PageSchema() 
    data = page_db.get_all()
    return render_template("index.html", value=data)
