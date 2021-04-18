import serial
from Funciones import *
# arduino = serial.Serial('COM7', 57600)
texto_acelerometro = open("acelerometro.txt", 'w')
texto_pulsioximetro = open("pulsioximetro.txt", 'w')
k = time.perf_counter()
r = time.perf_counter()
cont = 0
while time.perf_counter() <= r+60:
    if time.perf_counter() <= k+10:
        try:
            l = get_data("a", texto_acelerometro, 6)
            l = l.split(",")
            print(l)
            
            if(float(l[6]) < -6):
                cont += 1
                print(cont)
                alerta(cont)
            time.sleep(1)
        except:
            arduino.close()
            texto_acelerometro.close()
            texto_pulsioximetro.close()
            raise ValueError("Error en acelerometro")
    else:
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