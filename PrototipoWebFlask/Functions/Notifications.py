"""
Este modulo contiene las funciones relacionadas con el sistema de notificaciones
de la app
"""

import threading


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


numero_de_notificaciones = 0


def update_if_new_notification(cursor) -> bool:
    """
    Detecta y actualiza si hay una nueva notificacion comparando la variable
    'numero_de_notificaciones' con get_number_of_notifications(cursor) que es el
    numero de filas en la base de datos en la tabla 'Notificaciones'

    Input:
        cursor (psycopg2.connect.cursor()): cursor conectado a la base de datos
    Output:
        aumento (bool)
    """
    aumento = False

    valor_actual = numero_de_notificaciones
    valor_de_la_base_de_datos = get_number_of_notifications(cursor)

    if (valor_de_la_base_de_datos > valor_actual):
        aumento = True
        numero_de_notificaciones = valor_de_la_base_de_datos
    
    return aumento

def manage_notifications(cursor) -> None:
    """
    Revisa si hay una nueva notificacion en la base de datos y en caso de ser 
    positivo, manda una notificacion push.\

    Utiliza threading para estar constantemente revisando si la tabla de 
    'Notificaciones' se ve alterada en cuanto a inserciones.

    Implementa un helper para llamaro con mediante los threads.

    Input:
        cursor (psycopg2.connect.cursor()): cursor conectado a la base de datos
    Output:
        None
    """

    def manage_notifications_helper(cursor):

        while True:
            # Si una nueva fila en la tabla 'Notificaciones' es detectada
            # Mandar una notificacion push
            if (update_if_new_notification(cursor)):




