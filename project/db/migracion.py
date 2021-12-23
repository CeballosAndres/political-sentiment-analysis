# Requerimiento
#!pip install pymysql

#Importar
import pymysql

#conexion a base de datos
miConexion = pymysql.connect(
    host='127.0.0.1',
    user='root',
    passwd='',
    db='db_candidatos'
)
cur = miConexion.cursor()

# Requerimiento
#!pip install pandas

# Importar modulo pandas
import pandas as pd

#Importar archivo exel
File = pd.ExcelFile('04 Datos Limpios_Gera.xlsx')

# Extarer las hojas del archivo
df=File.parse('Posts')
Hoja_Comments=File.parse('Comments')

#Crear los dataframes con las columnas que necesitamos en la base de datos
df_page = pd.DataFrame(list(zip(df['page_id'],df['page_name'],df['page_name_id'],df['political_party'],df['kind'],df['region'])), 
                       columns = ['page_id', 'page_name', 'page_name_id', 'political_party', 'kind', 'region'])
df_page = df_page[0:1]
df_posts = pd.DataFrame(list(zip(df['post_id'],df['created_date'],df['created_time'],df['react_angry'],df['react_haha'],df['react_like'],df['react_love'],df['react_sad'],df['react_wow'],df['react_care'],df['share'],df['page_id'])), 
                       columns = ['post_id', 'created_date', 'created_time', 'react_angry', 'react_haha', 'react_like', 'react_love', 'react_sad', 'react_wow', 'react_care', 'share', 'page_id'])

df_comments = pd.DataFrame(list(zip(Hoja_Comments['profile_id'],Hoja_Comments['from_name'],Hoja_Comments['gender'],Hoja_Comments['created_date'],Hoja_Comments['created_time'],Hoja_Comments['reactions'],Hoja_Comments['post_id'])), 
                       columns = ['profile_id', 'from_name', 'gender', 'created_date', 'created_time', 'reactions', 'post_id'])

#Cambiar la fecha del Posts al formato aceptado por mysql
if(df_posts['created_date'].dtypes == 'object'):
    df_posts['created_date']=df_posts['created_date'].astype('datetime64')

#Cambiar la fecha del Comments al formato aceptado por mysql
if(df_comments['created_date'].dtypes == 'object'):
    df_comments['created_date']=df_comments['created_date'].astype('datetime64')

# Limpiar datos de from_name - remplazar comilla simple por comilla doble para evitar errores en la inserción a mysql
df_comments['from_name'] = df_comments['from_name'].str.replace("'",'"')

#Insertar datos en tabla page de la base de datos
cur.execute("INSERT INTO page (page_id, page_name, page_name_id, political_party, kind, region) VALUES ("+str(df_page.page_id[0])+",'"+df_page.page_name[0]+"','"+df_page.page_name_id[0]+"','"+df_page.political_party[0]+"','"+df_page.kind[0]+"','"+df_page.region[0]+"')")
miConexion.commit()

#Insertar datos en tabla post de base de datos
for i in range(len(df_posts)):
    cur.execute("IF "+str(df_posts.page_id[i])+" IN (SELECT page_id FROM page) THEN INSERT INTO post (post_id, created_date, created_time, react_angry, react_haha, react_like, react_love, react_sad, react_wow, react_care, share, page_id) VALUES ("+str(df_posts.post_id[i])+",'"+str(df_posts.created_date[i])+"','"+str(df_posts.created_time[i])+"',"+str(df_posts.react_angry[i])+","+str(df_posts.react_haha[i])+","+str(df_posts.react_like[i])+","+str(df_posts.react_love[i])+","+str(df_posts.react_sad[i])+","+str(df_posts.react_wow[i])+","+str(df_posts.react_care[i])+","+str(df_posts.share[i])+","+str(df_posts.page_id[i])+"); END IF")
miConexion.commit()

#Insertar datos en tabla comment de base de datos
for i in range(len(df_comments)):
    cur.execute("IF "+str(df_comments.post_id[i])+" IN (SELECT post_id FROM post) THEN INSERT INTO comment (profile_id, from_name, gender, created_date, created_time, reactions, post_id) VALUES ("+str(df_comments.profile_id[i])+",'"+df_comments.from_name[i]+"','"+df_comments.gender[i]+"','"+str(df_comments.created_date[i])+"','"+str(df_comments.created_time[i])+"',"+str(df_comments.reactions[i])+","+str(df_comments.post_id[i])+"); END IF")
miConexion.commit()

#Terminar conexion con base de datos
miConexion.close()