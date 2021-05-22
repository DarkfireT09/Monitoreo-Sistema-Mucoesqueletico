
import serial
import time
import psycopg2
# ----------------------Conexion con arduino -------------------

try:
    arduino = serial.Serial('COM9', 9600, timeout=1)
except:
    raise ValueError("Dispositivo no en linea")
    # send_to_JS("consol.error('dipositivo no esta en linea')")

def connect_to_data_base():
    """
    Se conecta a una base de datos postresql.

    Input:
        None
    Output:
        conexion (psycopg2 connection): Conexion con la base de datos
    """

    try:
        conexion = psycopg2.connect(host='127.0.0.1', port='5432', dbname='Cornerstone',
                                    user='postgres', password='0000')
        print("Conexion con la base de datos exitosa!")
    except:
        raise Exception("Connection with the database failed")
    return conexion


def data_base_send_notificacion(conexion, mensaje: str, correo_usuario: str) -> None:
    """
    Inserta en la tabla notificaciones una fila indicando que una notificacion
    debe ser creada. La hora en la que se inserta es generada por la propia base 
    de datos.
    Input:
        conexion (psycopg2 connection): Conexion con la base de datos
        mensaje (str): mensaje que tendrá la notificación

    Output:
        None
    """
    cursor = conexion.cursor()

    try:
        sql_sentence = """
            INSERT INTO notificaciones (fecha, mensaje, correo_usuario)
            VALUES (now()::timestamp, '{}', '{}')
            """.format(mensaje, correo_usuario)
        cursor.execute(sql_sentence)
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        print("No username Found")


def data_base_send_acelerometer(conexion, gx: str, gy: str, gz: str, correo_usuario: str) -> None:
    """
    Inserta en la tabla acelerometro

    Input:
        conexion (psycopg2 connection): Conexion con la base de datos
        gx (float): posicion en x
        gy (float): posicion en y
        gz (float): posicion en z
        correo_usuario (str): correo del usuario actual

    Output:
        None
    """
    cursor = conexion.cursor()

    try:
        sql_sentence = """
            INSERT INTO acelerometro (fecha, gx, gy, gz, correo_usuario)
            VALUES (now()::timestamp, {}, {}, {}, '{}')
            """.format(gx, gy, gz, correo_usuario)
        cursor.execute(sql_sentence)
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        print("data_base_send_acelerometer Error: No se pudo mandar ")


def data_send_pulsometer(conexion, pulso: float, correo_usuario: str):
    """
    Inserta en la tabla pulsometro

    Input:
        conexion (psycopg2 connection): Conexion con la base de datos
        pulso (float): Pulso actual
        correo_usuario (str): correo del usuario actual

    Output:
        None
    """
    cursor = conexion.cursor()
    try:
        sql_sentence = """
            INSERT INTO pulsometro (fecha, pulso, correo_usuario)
            VALUES (now()::timestamp, '{}', '{}')
            """.format(pulso, correo_usuario)
        cursor.execute(sql_sentence)
        conexion.commit()
    except Exception as e:
        print(e)
        conexion.rollback()
        print("data_send_pulsometer Error: No se pudo mandar ")

conexion = connect_to_data_base()
