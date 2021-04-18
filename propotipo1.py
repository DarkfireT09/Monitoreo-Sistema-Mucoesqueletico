from Funciones import *
import pandas as pd #para crear tablas donde se almacenaran los datos monitoreados

#-------------------INICIO DEL PROGRAMA--------------
def main():
    k = time.perf_counter()

    texto_acelerometro = open('acelerometro.txt', 'w')
    texto_pulsioximetro = open('pulsioximetro.txt', 'w')
    while True:
        """
        Ciclo cada 25 min lee el pulsioximetro, si detecta
        valores anomalos manda alerta
        """
        if time.perf_counter() <= k+1500:

            """
            El formato actual es:
                Acelerometro: YYYY,MM,DD,AX,AY,AZ,GX,GY,GZ
                Pulsioximetro: YYYY,MM,DD,P,O
            """

            try:
                l = get_data("a", texto_acelerometro, 6)
                l = l.split(",")
                print(l)
                
                if(float(l[6]) < -6):
                    alerta(l, texto_acelerometro)
                time.sleep(1)
            except:
                arduino.close()
                texto_acelerometro.close()
                texto_pulsioximetro.close()
                raise ValueError("Error en acelerometro")

        else:
             # NO implementado, se obtiene por defecto 0,1.

            try:
                l = get_data("p", texto_acelerometro, 2)
                l = l.split(",")

                if(float(l[6]) < 66):
                    alerta(l, texto_pulsioximetro)
                time.sleep(1)
            except:
                arduino.close()
                texto_pulsioximetro.close()
                texto_acelerometro.close()
                raise ValueError("Error en pulsioximetro")


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
    texto_pulsioximetro.close()
    texto_acelerometro.close()


main()


#Apagar


