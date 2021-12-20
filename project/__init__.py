from flask import Flask, render_template, jsonify, request
from werkzeug.utils import secure_filename
import os
import urllib.request
from datetime import datetime
app = Flask('app')
UPLOAD_FOLDER = 'static/archivos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['xlsx'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit(
        '.', 1)[1].lower() in ALLOWED_EXTENSIONS
#URL pagina principal
@app.route('/')
def index():
  #proporcioname los datos del candidato de la BDD (Nombre, id )
    candidatos = {
          "candidato": [
              "Carlos Farias",
              "Indira Vizcaíno",
              "Jorge Preciado"
          ],
          "id":[
              1,
              2,
              3
          ]
    }
    return render_template('index.html', candidato=candidatos)
#URL pagina de graficado
@app.route('/chart')
def graficado():
    candidato = request.args.get('candidato')
    print('candidato:',candidato)
    #proporcioname los datos del candidato de la BDD (utiliza el id de la variable  'candidato' )
    data = {
        "labels": [
            "Mujer",
            "Hombre",
            "Otro"
        ],
        "data":[
            50,
            30,
            23
        ]
    }
    return render_template('graficado.html', dato=data)
#URL auxiliar que nos proporciona la opcion de subir el archivo excel
@app.route("/upload", methods=["POST", "GET"])
def upload():

    if request.method == 'POST':
        files = request.files.getlist("file")
        for file in files:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            print('Archivo subido ' + file.filename +
                  ' correctamente!')
        else:
            print('Solo se aceptan archivos xlsx')
        msg = 'se subio correctamente el archivo'+file.filename
    return "<script>muestra_Alert('Exito!!', '"+msg+"', 1)</script>"

app.run(debug=True, host='0.0.0.0', port=8080)