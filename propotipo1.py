import time, random
from Funciones import *
import pandas as pd #para crear tablas donde se almacenaran los datos monitoreados



# 3. ACTUADORES
# Activar modulos de vibración para notificaciones
# Vibrar y apagar al no recibir datos o recibir datos sin sentido por más de 10 minutos

def vibrar(): #Luego definiremos las instrucciones para generar la vibración
    return 1

def apagar(): #Luego definiremos las instrucciones para apagar el dispositivo
    return 1

# 4. RESTRICCIONES DE TIEMPO
# Funciones que permiten apagar el dispositivo si no recibe respuestas en un periodo definido de tiempo.

# 5. MONITOREO
   

#-------------------INICIO DEL PROGRAMA--------------
def main():
    k = time.perf_counter()
    while True:
        
        if time.perf_counter() <= k+1500:

            arduino.write(bytes("a", 'utf-8')) # Aun no implementado en arduino.
            time.sleep(0.05)
            try:
                info_acelerometro = acelerometro()
            except:
                arduino.close()
                raise ValueError("Leyendo datos incorrectos en acelerometro")
            
            """
            
            SISTEMA DE ALERTA
            Y ENVIO DE DATOS A JS

            """

        else:

            arduino.write(bytes("p", 'utf-8')) # Aun no implementado en arduino.
            time.sleep(0.05)

            try:
                info_pulsioximetro = pulsioximetro()
            except:
                arduino.close()
                raise ValueError("Leyendo datos incorrectos en pulsioximetro")
            info_pulsioximetro = pulsioximetro()

            """
            
            SISTEMA DE ALERTA
            Y ENVIO DE DATOS A JS

            """

            k = time.perf_counter()
    else:
        print("")
        time.sleep(1.5)
        print ("El dispositivo se apagará en ", end="")
        time.sleep(2.5)
        print ("3 ", end="")
        time.sleep(1)
        print ("2 ", end="")
        time.sleep(1)
        print ("1 ...")
        time.sleep(1)

        print ("¡Hasta la próxima!")
    arduino.close()

        

main()


#Apagar



