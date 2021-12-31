from flask import render_template, request
from project import app
from project.app_controller import AppController
from project.db.migrator import Migrator
from project.datamining.clustering import Cluster
import os

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

    
@app.get("/clustering")
def clustering():
   """ Show dataframe with clusters. ONLY DEVELOPMENT METHOD, DELETE IN PRODUCTION """
    migrator = Migrator('./project/static/04 Datos Limpios.xlsx')
    df = migrator.file_to_dataframe()
    cluster = Cluster(df)
    return render_template("index.html", value=cluster.get_clustering(['gender','feeling'], 4))


"""Method to show the graphs"""
@app.get("/graphs")
def graphs():
    CONTROLLER = AppController()
    return render_template("graficado.html")

""" Method to test if the files are uploaded correctly"""
@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == 'POST':
        files = request.files.getlist("file")
        for file in files:
            file.save(os.path.join("./files_upload_folder", file.filename))
          
            print('Archivo subido ' + file.filename +
                  ' correctamente!')
        else:
            print('Solo se aceptan archivos xlsx')
        msg = 'se subio correctamente el archivo'+file.filename
    return "<script>muestra_Alert('Exito!!', '"+msg+"', 1)</script>"
