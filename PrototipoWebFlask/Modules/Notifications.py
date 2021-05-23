"""
Este modulo contiene las funciones relacionadas con el sistema de notificaciones
de la app
"""

from threading import Thread
import time
import Modules.global_variables
from spontit import SpontitResource
import requests


def get_number_of_notifications(cursor) -> int:
    """
    Obtiene el numero de notificaciones (numero de filas) en la tabla 
    'notificaciones'

    Input:
        cursor (psycopg2.connect.cursor()): cursor conectado a la base de datos

    Output:
        numero_de_notificaciones (int): numero de notificaciones/filas 
                                        en la tabla
    """

    try:
        cursor.execute(
            """
            SELECT count(*) 
            FROM Notificaciones
            """
        )
        rows = cursor.fetchall()
    except:
        raise NameError(
            "El sistema de notificaciones no pudo ser inicializado")

    numero_de_notificaciones = rows[0][0]

    return numero_de_notificaciones


def update_if_new_notification(cursor) -> bool:
    """
    Detecta y actualiza si hay una nueva notificacion comparando la variable
    'Modules.global_variables.numero_notificaciones_actuales' con 
    get_number_of_notifications(cursor) que es el numero de filas en la base de 
    datos en la tabla 'Notificaciones'

    Input:
        cursor (psycopg2.connect.cursor()): cursor conectado a la base de datos

    Output:
        aumento (bool)
    """
    aumento = False

    valor_actual = Modules.global_variables.numero_notificaciones_actuales
    valor_de_la_base_de_datos = get_number_of_notifications(cursor)

    if (valor_de_la_base_de_datos > valor_actual):
        aumento = True
        Modules.global_variables.numero_notificaciones_actuales = valor_de_la_base_de_datos

    return aumento


def manage_notifications(cursor) -> None:
    """
    Revisa si hay una nueva notificacion en la base de datos y en caso de ser 
    positivo, manda una notificacion push.

    Utiliza threading para estar constantemente revisando si la tabla de 
    'Notificaciones' se ve alterada en cuanto a inserciones.

    Implementa un helper para llamaro con mediante los threads.

    Input:
        cursor (psycopg2 connection): cursor conectado a la base de datos

    Output:
        None
    """

    def manage_notifications_helper(cursor):
        it = 0
        resource = SpontitResource(
            "daniel_leyva4642", "LLJPM2VU1YO8UF4SG8H46LQFJGMXED8VROWQVDV74IUZQRFRZJVZAVRLH7LGPBIC5JVXWQI3PB53GZV05XF20X4LNYW9T8XCY4ZE")
        while True:
            # Si una nueva fila en la tabla 'Notificaciones' es detectada
            # Mandar una notificacion push
            if (update_if_new_notification(cursor)):
                print("Insercion en la base de datos, activando notificacion!")
                cursor.execute(
                    """
                    SELECT mensaje
                        FROM Notificaciones
                        ORDER BY fecha desc
                    """
                )
                data = cursor.fetchall()
                # print(data[0][0])
                r = resource.push(data[0][0])
            # print("it ", it)
            it += 1
            time.sleep(1)

    print("PREPARACION EN CAMINO, ESTADO 001!")

    thread = Thread(target=manage_notifications_helper, args=(cursor,))

    # El thread debe ser daemon
    thread.daemon = True
    thread.start()

def get_number_of_notifications_given_day(cursor, user, timestamp) -> int:
    """
    Obtiene el numero de notificaciones (numero de filas) en la tabla 
    'notificaciones' en un dia especifico dado un usuario

    Input:
        cursor (psycopg2.connect.cursor()): cursor conectado a la base de datos
        user (str): correo del usuario
        timestamp

    Output:
        numero_de_notificaciones (int): numero de notificaciones/filas 
                                        en la tabla
    """

    try:
        sql_sentence = """
            SELECT count(*) 
            FROM Notificaciones
            WHERE correo_usuario = '{}' AND fecha > '{} 0:0:0' AND fecha < '{} 23:59:59'
            """.format(user, timestamp, timestamp)
        cursor.execute(sql_sentence)
        rows = cursor.fetchall()
    except:
        raise NameError(
            "El numero de notificaciones de un usuario no pudo ser extraido")

    numero_de_notificaciones = rows[0][0]
    return numero_de_notificaciones

"""
insert into Notificaciones (fecha, mensaje, Correo_Usuario)
Values (current_timestamp, 'Test 4', 'david.melendez@urosario.edu.co')"
"""
