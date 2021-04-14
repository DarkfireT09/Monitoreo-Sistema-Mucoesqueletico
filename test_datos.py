import serial
from Funciones import *
# arduino = serial.Serial('COM7', 57600)
texto_acelerometro = open("acelerometro.txt", 'w')
texto_pulsioximetro = open("pulsioximetro.txt", 'w')
k = time.perf_counter()
r = time.perf_counter()
while time.perf_counter() <= r+60:
    if time.perf_counter() <= k+10:
        try:
            # arduino.write("a".encode())
            # a = arduino.readline()
            # a = a.decode()

            # # a = acelerometro()
            # t = time.strftime('%Y-%m-%d,%H:%M:%S',time.localtime())
            # texto_acelerometro.write(t + ',' + str(a) + '\n')
            # print(a)
            get_data("a", texto_acelerometro, 6)
        except:
            arduino.close()
            texto_acelerometro.close()
            texto_pulsioximetro.close()
    else:
        # arduino.write("p".encode())
        # p = arduino.readline()
        # p = p.decode()
        # # p = pulsioximetro()
        # t = time.strftime('%Y-%m-%d,%H:%M:%S',time.localtime())
        # texto_pulsioximetro.write(t + ',' + str(p) + '\n')
        # print(p)
        try:
            get_data("p", texto_pulsioximetro, 2)
            k = time.perf_counter()
        except:
            arduino.close()
            texto_acelerometro.close()
            texto_pulsioximetro.close()
arduino.close()
texto_acelerometro.close()
texto_pulsioximetro.close()