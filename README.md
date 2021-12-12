# Proyecto de Ciencia de Datos

## TL;TR

## Levantar entorno

### Sin docker
- Ingresar a la carpeta web `cd services/web`
- Crear entorno virtual `python -m venv env`
- Activar entorno virtual `source env/bin/activate` (varia con el SO)
- Instalar dependencias `pip install -r requirements.txt`
- Exportar variable de entorno `export FLASK_APP=app/__init__py`
- Modo debug (opcional) `export FLASK_ENV=development`
- Iniciar servidor local `python manage.py run`

### Con docker
- Tener instalado docker y docker-compose
- En la carpeta raíz ejecutar `docker-compose up -d --build`
- Ingresar a `127.0.0.1:4000`. En macOs Monterey el puerto 5000 es usado por el sistema, por lo que en docker-compose.yml se redirige del 4000 al 5000 para Flask.

## Referencias
