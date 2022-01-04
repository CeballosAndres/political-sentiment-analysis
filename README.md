# Proyecto de Ciencia de Datos
 Sistema que permite subir archivos con información limpia de diferentes candidatos para realizar análisis de sentimientos sobre los comentarios de los seguidores de su página de Facebook.

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

## Staging 
- Disponible en https://dev-sentiment.ceballos.dev

## Producción
- Disponible en https://sentiment.ceballos.dev

## Recurso para la clasificacion de sentimientos
### Intruciones de uso
1.- Ingresar a la siguiente liga
https://colab.research.google.com/drive/1vpsXq3H83tvdilU95gHkHVttFmrV6-UX?usp=sharing

2.- Hacer una copia del recurso

3.- Una vez creada la copia del script, localizar el apartado de files en la barra lateral
    izquierda y abrirla

4.- Dar click derecho y upload para cargar tu archivo de datos limpios

5.- Verificar el nombre de tu archivo excel en el código

6.- Elegir el nombre del archivo de salida al final del script

7.- Ejecutar celda por celda

8.- Al finalizar la ejecución revisar la barra de files para ubicar tu archivo de resultado

9.- Seleccionar dicho archivo y dar click derecho para descargarlo en tu máquina

10.- Revisar archivo, en especial los campos create_date 
     y darle el formato correcto de dd/mm/aaaa en caso de que haya cambiado