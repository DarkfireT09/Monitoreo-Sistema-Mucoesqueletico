import serial
import time
import psycopg2
# ----------------------Conexion con arduino -------------------

try:
    arduino = serial.Serial('COM9', 9600, timeout=1)
except:
    raise ValueError("Dispositivo no en linea")
    # send_to_JS("consol.error('dipositivo no esta en linea')")

"""
Función para la obtención de datos de los sensores
Toma:
    Sensor: 'a'/'p' dependiendo del Sensor
    Archivo: 'acelerometro'/'pulsioximetro' se almacenan los datos
    n: '2'/'5'
"""


def get_data(sensor, archivo, n):
    arduino.write(sensor.encode())
    time.sleep(0.1)
    i = arduino.readline()
    i = i.decode()
    # print(i)
    t = time.strftime('%Y,%m,%d,%H,%M,%S', time.localtime())
    if len(i.split(',')) == n:
        archivo.write(t + ',' + str(i) + '\n')
        return t + ',' + str(i) + '\n'
    return t + ",0,0,0,0,0,1" + "\n"

def alerta(l, archivo):
    cont = 0
    while (float(l[6]) < -6):
        cont +=1
        time.sleep(1)
        if cont == 3:
            break
        l = get_data("a", archivo, 6)
        l = l.split(",")

    if cont >= 3:
        arduino.write("v".encode())
        while True:
            cont = 0
            print ("alerta")
            i = arduino.readline()
            i = i.decode()
            try:
                i = int(i)
                print("exito")
            except :
                pass
            if i == 1:
                break

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
                                user='postgres', password='1234')
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
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("No username Found")

    
def data_base_send_acelerometer(conexion, gx: str, gy: str, gz: str, correo_usuario: str) -> None:
    """
    Inserta en la tabla acelerometro

    Input:
        conexion (psycopg2 connection): Conexion con la base de datos
        mensaje (str): mensaje que tendrá la notificación
        
    Output:
        None
    """
    cursor = conexion.cursor()

    try:
        sql_sentence = """
            INSERT INTO acelerometro (fecha, gx, gy, gz, correo_usuario)
            VALUES (now()::timestamp, 1, 2, 3, 'david.melendez@urosario.edu.co')
            """.format(gx, gy, gz, correo_usuario)
        cursor.execute(sql_sentence)
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("No username Found")


#def data_send_pulsometer():