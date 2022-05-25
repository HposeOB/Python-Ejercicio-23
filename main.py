import sqlite3
from sqlite3 import Error


def create_connection(database):
    conn = None

    try:
        conn = sqlite3.connect(database)
        print(sqlite3.version)

    except Error as e:
        print(e)
    return conn


def create_table(conn, sql_create):
    try:
        cur = conn.cursor()
        cur.execute(sql_create)
    except Error as e:
        print(e)

def insertar_alumno(conn, id, nombre, apellido):

    sql = f"INSERT INTO alumnos(id, nombre, apellido)VALUES({id}, '{nombre}', '{apellido}')"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def seleccionar_nombre(conn, nombre):

    sql = f"SELECT * FROM alumnos WHERE nombre='{nombre}'"
    cur = conn.cursor()
    cur.execute(sql)
    print(cur.fetchone())

def main():
    database = "alumnos.db"
    conn = create_connection(database)
    sql_create_table = """ CREATE TABLE IF NOT EXISTS alumnos (
                                        id integer PRIMARY KEY,
                                        nombre text NOT NULL,
                                        apellido text
                                    ); """



    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_table)
        '''insertar_alumno(conn, 1, "Juan","Alvarez")
        insertar_alumno(conn, 2, "Manuel", "Rodriguez")
        insertar_alumno(conn, 3, "Pepe", "Docampo")
        insertar_alumno(conn, 4, "Jacinta", "Puertas")
        insertar_alumno(conn, 5, "Sabrina", "Martinez")
        insertar_alumno(conn, 6, "Carlos", "Casas")
        insertar_alumno(conn, 7, "Oscar", "Alcorta")
        insertar_alumno(conn, 8, "Laura", "Estevez")'''
        nombre = input("Introduce el nombre a buscar: ")
        seleccionar_nombre(conn, nombre)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()