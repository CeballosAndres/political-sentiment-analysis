from flask import render_template
from project import app
from project.app_controller import AppController


@app.get("/")
def index():
    CONTROLLER = AppController()
    data = CONTROLLER.get_pages()
    return render_template("index.html", value=data)


@app.get("/filter_fields")
def get_filter_fields():
    """Show possible filter fields. ONLY DEVELOPMENT METHOD, DELETE IN PRODUCTION"""
    CONTROLLER = AppController()
    return render_template("index.html", value=CONTROLLER.get_filters_fields())

@app.get("/insert_data_from_file")
def insert_data():
    """Call the insert_data_from_file function from controller.
    ONLY DEVELOPMENT METHOD, DELETE IN PRODUCTION"""
    CONTROLLER = AppController()
    data = CONTROLLER.insert_data_from_file()
    return render_template("index.html", value=data)

@app.get("/algorithm_info")
def get_algorithm_info():
    """Show possible filter fields. ONLY DEVELOPMENT METHOD, DELETE IN PRODUCTION"""
    CONTROLLER = AppController()
    return render_template("index.html", value=CONTROLLER.get_algorithm_info())
