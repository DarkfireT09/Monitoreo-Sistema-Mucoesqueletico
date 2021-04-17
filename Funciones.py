import serial, time

#----------------------Conexion con arduino -------------------

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
    t = time.strftime('%Y,%m,%d%H:%M:%S',time.localtime())
    if len(i.split(',')) == n:
        archivo.write(t + ',' + str(i) + '\n')
        return t + ',' + str(i) + '\n'




