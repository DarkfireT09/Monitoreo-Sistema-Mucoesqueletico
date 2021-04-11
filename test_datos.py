import serial

arduino = serial.Serial('COM6', 57600)


def get_information(s):
    info = s.split(",")
    infofloat = []
    for i in info:
        infofloat.append(float(i))

    return infofloat

def acelerometro(): 
    """
    Se obtiene informacion de la forma aceleracion(a), rotacion(g)
    (ax,ay,az,gx,gy,gz)

    Se devuelve la lista l. 
    """
    # a = random.randint(0,100)
    a = arduino.readline()
    a = str(a)
    a = a[2:len(a)-5]
    l = get_information(a)
    return l


cont = 0

while cont < 10:
    print(acelerometro())
    cont += 1


arduino.close()