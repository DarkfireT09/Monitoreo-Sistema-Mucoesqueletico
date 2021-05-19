from Funciones import *
import pandas as pd #para crear tablas donde se almacenaran los datos monitoreados

#-------------------INICIO DEL PROGRAMA--------------
def main():
    while True:
        lectura = arduino.readline()
        lectura = lectura.decode()
        lectura = lectura.replace("\r", '')
        lectura = lectura.replace("\n", '')
        lectura = lectura.split(",")
        if lectura != ['']:
            if len(lectura) == 3:
                print("Acelerometro: ", lectura)
                data_base_send_acelerometer(conexion, lectura[0], lectura[1], lectura[2], 'ejemplo@ejemplo.com')
            else:
                if int(lectura[1]) == 1:
                    print("Alerta")
                    data_base_send_notificacion(conexion, "Mala posicion detectada", 'ejemplo@ejemplo.com')
                else:
                    print("Pulsometro: ", lectura)
                    data_base_send_notificacion(conexion, "Pon tu dedo en el sensor.", 'ejemplo@ejemplo.com')
                    data_send_pulsometer(conexion, lectura[1], 'ejemplo@ejemplo.com')


main()


#Apagar


