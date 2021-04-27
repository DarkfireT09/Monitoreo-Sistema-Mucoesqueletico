"""
Este modulo contiene las funciones relacionadas con el sistema de notificaciones
de la app
"""

from threading import Thread
import time

numero_notificaciones_actuales = 0


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
            FROM "Notificaciones"
            """
        )
        rows = cursor.fetchall()
    except:
        raise NameError(
            "El sistema de notificaciones no pudo ser inicializado")

    numero_de_notificaciones = rows[0][0]

    return numero_de_notificaciones


def update_if_new_notification(cursor, numero_notificaciones_actuales) -> bool:
    """
    Detecta y actualiza si hay una nueva notificacion comparando la variable
    'numero_notificaciones_actuales' con get_number_of_notifications(cursor) que 
    es el numero de filas en la base de datos en la tabla 'Notificaciones'

    Input:
        cursor (psycopg2.connect.cursor()): cursor conectado a la base de datos
        numero_notificaciones_actuales (int): ultimo update del numero de  
                                              notificaciones
    Output:
        aumento (bool)
    """
    aumento = False

    valor_actual = numero_notificaciones_actuales
    valor_de_la_base_de_datos = get_number_of_notifications(cursor)

    if (valor_de_la_base_de_datos > valor_actual):
        aumento = True
        numero_notificaciones_actuales = valor_de_la_base_de_datos

    return aumento


def manage_notifications(cursor, numero_notificaciones_actuales) -> None:
    """
    Revisa si hay una nueva notificacion en la base de datos y en caso de ser 
    positivo, manda una notificacion push.

    Utiliza threading para estar constantemente revisando si la tabla de 
    'Notificaciones' se ve alterada en cuanto a inserciones.

    Implementa un helper para llamaro con mediante los threads.

    Input:
        cursor (psycopg2.connect.cursor()): cursor conectado a la base de datos
        numero_notificaciones_actuales (int): ultimo update del numero de  
                                              notificaciones
    Output:
        None
    """

    def manage_notifications_helper(cursor, numero_notificaciones_actuales):

        it = 0
        while it < 100:
            # Si una nueva fila en la tabla 'Notificaciones' es detectada
            # Mandar una notificacion push
            if (update_if_new_notification(cursor, numero_notificaciones_actuales)):
                pass
            print("it ", it)
            it += 1
            time.sleep(1)

    print("PREPARACION EN CAMINO, ESTADO 001!")

    thread = Thread(target=manage_notifications_helper, args=(cursor, numero_notificaciones_actuales))

    # El thread debe ser daemon
    thread.daemon = True
    thread.start()
