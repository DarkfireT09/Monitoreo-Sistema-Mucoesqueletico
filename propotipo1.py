import time, random 
import pandas as pd #para crear tablas donde se almacenaran los datos monitoreados

#--------------------------FUNCIONES---------------------------

# 1. SENSORES
# Para el primer prototipo, se usan generadores random del rango y tipo de dato
# que suelen obtenerse a partir de los sensores, las funciones se modificarán cuando
# tengamos los materiales

def acelerometro(): 
    a = random.randint(0,100)
    return a

def pulso():
    p = random.randint(0, 200)
    return p

def fuerza():
    f = random.randint(0, 100)
    return f

def bateria():
    b = random.randint(0, 100)
    if b <= 15:
        print("ALERTA! Bateria baja (menos del 15%)")
    return b
    

# 2. CONEXION BLUETOOTH
# El programa empieza a ejecutarse una vez se establezca la conexión bluetooth
# Por ahora, generamos o un 0 o un 1 aleatorios, donde 1 significa conexión establecida
# y cero lo contrario

def conexion_bt():
    bt = random.randint(0, 1)
    return bt

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
        presion = []
         
        while tmp <= 30:
            
            time.sleep(180)
            
            a = acelerometro()
            p = pulso()
            f = fuerza()
            bateria()
            
            movimiento.append(a)
            pulsaciones.append(p)
            presion.append(f)
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

print ("¡Hasta la próxima!")
