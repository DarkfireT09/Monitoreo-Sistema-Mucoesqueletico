from Funciones import *
# arduino = serial.Serial('COM7', 57600, timeout=1)

# a = input("caracter: ")
# arduino.write(a.encode())
# print(arduino.readline())
cont = 0
while cont< 10:
    arduino.write("a".encode())
    print(arduino.readline())
    cont += 1

arduino.close()