import serial
import time
import psycopgs2
# ----------------------Conexion con arduino -------------------

try:
    arduino = serial.Serial('COM7', 57600, timeout=1)
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
    print(i)
    t = time.strftime('%Y,%m,%d%H:%M:%S', time.localtime())
    if len(i.split(',')) == n:
        archivo.write(t + ',' + str(i) + '\n')
        return t + ',' + str(i) + '\n'


def connect_to_data_base():
    """
    Connects to a 'local' postgreSQL database.
    Returns an exception if the connection failed.
    """
    
    try:
        conexion = psycopg2.connect(host='127.0.0.1', port='5432', dbname='Cornerstone',
                                user='postgres', password='1234')
        print("Conexion con la base de datos exitosa!")
    except:
        raise Exception("Connection with the database failed")


def data_base_send_data(data: str) -> None:
    """
    Sends the given data 
    """
    assert type(data) == str, f"The type of data must be of the class str, got \
                                {type(data)}"
    # TODO: implement sql sentence

