# Proyecto de Ciencia de Datos

## TL;TR

## Levantar entorno local

### Sin docker
- Crear entorno virtual `python -m venv env`
- Activar entorno virtual `source env/bin/activate` (varia con el SO)
- Instalar dependencias `pip install -r requirements.txt`
- Renombrar `.env.example` a `.env` (configurar parametros segun entorno)
- Crear base de datos `python manage.py create_db` (elimina en caso de existir)
- (opcional) Cargar datos de prueba a base de datos `python manage.py seed_db`
- Iniciar servidor local `python manage.py run`
- Ingresar a `127.0.0.1:5000`

### Con docker
- Tener instalado docker y docker-compose
- En la carpeta raíz ejecutar `docker-compose up -d --build`
- Crear base de datos `docker-compose exec sentiment-app python manage.py create_db`
- (opcional) Cargar datos de prueba a base de datos `docker-compose exec sentiment-app python manage.py seed_db`
- Ingresar a `127.0.0.1:4000`. En macOs Monterey el puerto 5000 es usado por el sistema, por lo que en docker-compose.yml se redirige del 4000 al 5000 para Flask.

## Producción
- Disponible en https://sentiment.ceballos.dev

## Referencias
