from Funciones import *
import pandas as pd #para crear tablas donde se almacenaran los datos monitoreados

#-------------------INICIO DEL PROGRAMA--------------
def main():
    while True:
        try:
            lectura = arduino.readline()
            lectura = lectura.decode()
            lectura = lectura.replace("\r", '')
            lectura = lectura.replace("\n", '')
            lectura = lectura.split(",")
    
            if int(lectura[3]) == 1:
                print("Alerta: ", lectura)
                data_base_send_notificacion(conexion, "Mala posicion detectada, angulo = {0}".format(lectura[4]), 'ejemplo@ejemplo.com')
            elif lectura[0] == "p":
                print("Pulsometro: ", lectura)
                data_base_send_notificacion(conexion, "Pon tu dedo en el sensor.", 'ejemplo@ejemplo.com')
                data_send_pulsometer(conexion, lectura[1], 'ejemplo@ejemplo.com')
            else:
                print("Acelerometro: ", lectura)
                data_base_send_acelerometer(conexion, lectura[0], lectura[1], lectura[2], 'ejemplo@ejemplo.com')
        except:
            pass


main()


#Apagar
