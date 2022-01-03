<<<<<<< HEAD
import json
from flask import render_template, request
=======
from flask import render_template, request, jsonify
>>>>>>> main
from project import app
from project.app_controller import AppController
from project.db.migrator import Migrator
from project.datamining.clustering import Cluster
import os
<<<<<<< HEAD

UPLOAD_FOLDER = 'project/static/archivos/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['xlsx'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit(
        '.', 1)[1].lower() in ALLOWED_EXTENSIONS
=======
>>>>>>> main

@app.get("/")
def index():
    CONTROLLER = AppController()
    data = CONTROLLER.get_pages()
  #proporcioname los datos del candidato de la BDD (Nombre, id )
<<<<<<< HEAD
    filtro = CONTROLLER.get_filters_fields()
=======
    filtro = {
             "page_name": [
                "Irene Herrera",
                "Virgilio Mendoza"
                ],
              "political_party": [
                "Partido Revolucionario Institucional",
                "Partido Verde Ecologista de México"
                ],
              "kind": [
                "Presidencia Municipal",
                "Gubernatura"
                ],
              "region": [
                "Colima",
                "Manzanillo"
                ]
    }
>>>>>>> main
    return render_template('index.html', candidato=filtro)


@app.get("/filter_fields")
def get_filter_fields():
    """Show possible filter fields. ONLY DEVELOPMENT METHOD, DELETE IN PRODUCTION"""
    CONTROLLER = AppController()
<<<<<<< HEAD
    return render_template("test.html", value=CONTROLLER.get_filters_fields())
=======
    return render_template("index.html", value=CONTROLLER.get_filters_fields())
>>>>>>> main

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
<<<<<<< HEAD
    CONTROLLER = AppController()
    filtro = CONTROLLER.get_filters_fields()
    return render_template("test.html", value=CONTROLLER.get_algorithm_info(filtro))

    
=======
    filters = {
        "page_name": [
            "Irene Herrera",
            "Virgilio Mendoza"
        ],
        "political_party": [
            "Partido Revolucionario Institucional",
            "Partido Verde Ecologista"
        ],
        "kind": [
            "Presidencia Municipal",
            "Gobernatura"
        ],
        "region": [
            "Estado Colima",
            "Manzanillo"
        ]
    }
    CONTROLLER = AppController()
    return render_template("test.html", value=CONTROLLER.get_algorithm_info(filters))


>>>>>>> main
@app.get("/clustering")
def clustering():
    """Show dataframe with clusters. ONLY DEVELOPMENT METHOD, DELETE IN PRODUCTION"""
    migrator = Migrator('./project/static/04 Datos Limpios.xlsx')
    df = migrator.file_to_dataframe()
    cluster = Cluster(df)
<<<<<<< HEAD
    return render_template("test.html", value=cluster.get_clustering(['gender','feeling'], 4))

=======
    return render_template("index.html", value=cluster.get_clustering(['gender','feeling'], 4))
>>>>>>> main


"""Method to show the graphs"""
@app.route('/chart')
def graficado():
    CONTROLLER = AppController()
<<<<<<< HEAD
    filtro1 = request.args.get('filtro')
    filtro1 = json.loads(filtro1)[0]
    print(filtro1)
    metodo = CONTROLLER.get_algorithm_info(filtro1)
    filtro = CONTROLLER.get_filters_fields()

    #proporcioname los datos del candidato de la BDD (utiliza el id de la variable  'candidato' )

    return render_template('graficado.html', dato=metodo,datos2=filtro)
=======
    filtro = request.args.get('filtro')
    print('candidato:',filtro)
    #proporcioname los datos del candidato de la BDD (utiliza el id de la variable  'candidato' )
    data ={
  "clusters_name": [
    0,
    1,
    2,
    3
  ],
  "clusters": [
    {
      "name": 0,
      "total_elements": 1342,
      "count_values": [
        {
          "feeling": {
            "neutros": 700,
            "positivo": 637,
            "neutro": 5
          }
        },
        {
          "gender": {
            "M": 831,
            "H": 470,
            "I": 24,
            "O": 17
          }
        }
      ]
    },
    {
      "name": 1,
      "total_elements": 7125,
      "count_values": [
        {
          "feeling": {
            "muy positivo": 6240,
            "muy negativo": 849,
            "negativo": 36
          }
        },
        {
          "gender": {
            "H": 6855,
            "I": 270
          }
        }
      ]
    },
    {
      "name": 2,
      "total_elements": 10438,
      "count_values": [
        {
          "feeling": {
            "muy positivo": 10351,
            "negativo": 63,
            "muy negativo": 20,
            "neutro": 4
          }
        },
        {
          "gender": {
            "M": 10272,
            "O": 166
          }
        }
      ]
    },
    {
      "name": 3,
      "total_elements": 1351,
      "count_values": [
        {
          "feeling": {
            "muy negativo": 1351
          }
        },
        {
          "gender": {
            "M": 1351
          }
        }
      ]
    }
  ]
}
    filtro = {
             "page_name": [
                "Irene Herrera",
                "Virgilio Mendoza"
                ],
              "political_party": [
                "Partido Revolucionario Institucional",
                "Partido Verde Ecologista de México"
                ],
              "kind": [
                "Presidencia Municipal",
                "Gubernatura"
                ],
              "region": [
                "Colima",
                "Manzanillo"
                ]
    }
    return render_template('graficado.html', dato=data,datos2=filtro)
>>>>>>> main

""" Method to test if the files are uploaded correctly"""
@app.route("/upload", methods=["POST", "GET"])
def upload():
<<<<<<< HEAD
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
=======
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
>>>>>>> main
