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

def ciclo_monitoreo():
        
    while True:
        
        tmp = 0
    
        movimiento = []
        pulsaciones = []
         
        while tmp <= 30:
            
            time.sleep(180)
            
            a = acelerometro()
            p = pulsioximetro()
            
            movimiento.append(a)
            pulsaciones.append(p)
            tmp += 3
        
        print ("Ciclo de monitoreo completo")
        print ("")
        i = input ("Ingrese 1 para continuar, y cualquier otro valor para apagar: ")
        
        if int(i) != 1:
            break
        

   

#-------------------INICIO DEL PROGRAMA--------------

while True:
    
    # Establecer la conexión bluetooth al dispositivo
    
    a = 0
    
    while True:
        print("Estableciendo Conexión...")
        cnx = conexion_bt()
        time.sleep(2)
        print("")
        
        if cnx == 1:
            print ("¡Conexión exitosa!")
            a = 1
            time.sleep(1)
            break
        
        else:
            print ("No se pudo conectar al dispositivo ¿Volver a intentar?")
            a = input ("Sí [1] ; No [0] :")
            if int(a) == 0:
                break
        
        time.sleep(1)
        print("")
        
    if int(a) == 0: 
        break
    
    #Continuar con la ejecución si la conexión fue exitosa  
    
    print("")
    print ("Coloquese el dipositivo y active el monitoreo") 
    time.sleep(1)
            
    #Si no recibe respuesta en 60 segundos, o no es 1, apagar el dispositivo
    #NOTA: NO HE PODIDO CREAR EL INPUT RESTRINGIDO POR EL TIEMPO - Ana
     
    activar = int(input("Ingrese [1] para activar el monitoreo, y cualquier otro valor para cancelar: "))
    
    if activar != 1:
        break
    
    time.sleep(1)
    

    
    #Comenzar a registrar los datos de salud
    
    print("")
    print ("Inicio del monitoreo: Desarrolle sus actividades cotidianas y de trabajo de forma normal")
    
            
    break
    

#Apagar
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
arduino.close()

print ("¡Hasta la próxima!")
