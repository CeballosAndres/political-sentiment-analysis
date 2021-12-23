from flask import render_template
from project import app
from project.app_controller import AppController

CONTROLLER = AppController()

@app.get("/")
def index():
    data = CONTROLLER.get_pages()
    return render_template("index.html", value=data)

@app.get("/filter_fields")
def get_filter_fields():
    """Show possible filter fields. ONLY DEVELOPMENT METHOD, DELETE IN PRODUCTION"""
    return render_template("index.html", value=CONTROLLER.get_filters_fields())
