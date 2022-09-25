import pymysql


connection = pymysql.connect(user = 'root', password = '123323', host = '127.0.0.1', port = 3306, database = 'direcciones')

#PAGINAS WEBS
def consultar_webs_n():
    try:
        cur = connection.cursor()
        sql = "SELECT nombre_pw FROM paginasweb"
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
    except:
        pass
    
    return datos

def consultar_webs_d():
    try:
        cur = connection.cursor()
        sql = "SELECT direccion_pw FROM paginasweb"
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
    except:
        pass
    
    return datos

def insertar_pw(nombre, direccion):
    try:
        cur = connection.cursor()
        name = nombre
        direc = direccion
        sql = f'INSERT INTO aplicaciones (nombre_pw, direccion_pw) VALUES ("{name} ", "{direc}")' #.format(VALUES)
        cur.execute(sql)
        connection.commit()
        cur.close()
    except:
        pass



#APLICACIONES
def consultar_apps_n():
    
    try:
        cur = connection.cursor()
        sql = "SELECT nombre_app FROM aplicaciones"
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
    except:
        pass
    
    return datos

def consultar_apps_d(name):
    try:
        cur = connection.cursor()
        sql = f"SELECT direccion_app FROM aplicaciones WHERE nombre_app LIKE '{name}'"
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
    except:
        pass
    
    return datos


def insertar_app(nombre, direccion):
    try:
        print("hola, estoy insertando...")
        cur = connection.cursor()
        name = nombre
        direc = direccion
        sql = f'INSERT INTO aplicaciones (nombre_app, direccion_app) VALUES ("{name} ", "{direc}")' #.format(values)
        cur.execute(sql)
        connection.commit()
        cur.close()
        print("Termine...")
    except:
        pass
    




#datos = consultar_apps_n()
#print(datos)
#dato = Path(rf"{datos}") #elimina la doble \ de los directorios
#print(dato)


