import serial, time
from Funciones import *
# arduino = serial.Serial('COM7', 57600)

texto_acelerometro = open('acelerometro.txt', 'w')

cont = 0

while cont < 10:
    # print(acelerometro())
    info_acelerometro = acelerometro()
    t = time.strftime('[%Y-%m-%d, %H:%M:%S]',time.localtime())
    texto_acelerometro.write(t + str(info_acelerometro) + '\n')
    cont += 1


arduino.close()
texto_acelerometro.close()