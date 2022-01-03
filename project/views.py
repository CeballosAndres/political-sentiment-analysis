import json
from flask import render_template, request
from project import app
from project.app_controller import AppController
from project.db.migrator import Migrator
from project.datamining.clustering import Cluster
import os

UPLOAD_FOLDER = 'project/static/archivos/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['xlsx'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit(
        '.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.get("/")
def index():
    CONTROLLER = AppController()
    data = CONTROLLER.get_pages()
  #proporcioname los datos del candidato de la BDD (Nombre, id )
    filtro = CONTROLLER.get_filters_fields()
    return render_template('index.html', candidato=filtro)


@app.get("/filter_fields")
def get_filter_fields():
    """Show possible filter fields. ONLY DEVELOPMENT METHOD, DELETE IN PRODUCTION"""
    CONTROLLER = AppController()
    return render_template("test.html", value=CONTROLLER.get_filters_fields())

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
    filtro = CONTROLLER.get_filters_fields()
    return render_template("test.html", value=CONTROLLER.get_algorithm_info(filtro))

    
@app.get("/clustering")
def clustering():
    """Show dataframe with clusters. ONLY DEVELOPMENT METHOD, DELETE IN PRODUCTION"""
    migrator = Migrator('./project/static/04 Datos Limpios.xlsx')
    df = migrator.file_to_dataframe()
    cluster = Cluster(df)
    return render_template("test.html", value=cluster.get_clustering(['gender','feeling'], 4))



"""Method to show the graphs"""
@app.route('/chart')
def graficado():
    CONTROLLER = AppController()
    filtro1 = request.args.get('filtro')
    filtro1 = json.loads(filtro1)[0]
    print(filtro1)
    metodo = CONTROLLER.get_algorithm_info(filtro1)
    filtro = CONTROLLER.get_filters_fields()

    #proporcioname los datos del candidato de la BDD (utiliza el id de la variable  'candidato' )

    return render_template('graficado.html', dato=metodo,datos2=filtro)

""" Method to test if the files are uploaded correctly"""
@app.route("/upload", methods=["POST", "GET"])
def upload():
  CONTROLLER = AppController()
  if request.method == 'POST':
      file = request.files.getlist("file")[0]
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
      path="project/static/archivos/"+file.filename
      data = CONTROLLER.insert_data_from_file(path)
      if isinstance(data, Exception):
        return "<script>window.open('/error','_self');</script>"
      print('Archivo subido ' + file.filename +' correctamente!')
      print(data)
      msg = 'se subio correctamente el archivo'+file.filename
      print(f"<script>exitoso('{msg}','{data}')</script>")
      return f"<script>exitoso('{msg}','{data}')</script>"
  
@app.get("/error")
def error():
  return render_template("errores.html")