// escalar_valores.ino
// Librerias I2C para controlar el mpu6050 con Arduino,
// la libreria MPU6050.h necesita I2Cdev.h y la libreria I2Cdev.h necesita Wire.h
/* 
 Conociendo los rangos con los que está configurado nuestro MPU6050, 
 dichos rangos pueden ser 2g/4g/8g/16g para el acelerómetro y 
 250/500/1000/2000(°/s) para el giroscopio.
 Los rangos por defecto (2g y 250°/s)
 
 Variable        valor mínimo  valor central  valor máximo
 Lectura MPU6050    -32768        0             +32767 
 Aceleración         -2g          0g            +2g
 Velocidad angular  -250°/s       0°/s          +250°/s
*/
 
#include "I2Cdev.h"
#include "MPU6050.h"
#include "Wire.h"
 
// La dirección del MPU6050 puede ser 0x68 o 0x69, dependiendo 
// del estado de AD0. Si no se especifica, 0x68 estará implicito
MPU6050 sensor;
 
// Valores RAW (sin procesar) del acelerometro y giroscopio en los ejes x,y,z
int ax, ay, az;
int gx, gy, gz;
 
void setup() {
  Serial.begin(57600);    //Iniciando puerto serial
  Wire.begin();           //Iniciando I2C  
  sensor.initialize();    //Iniciando el sensor
 
  if (sensor.testConnection()) Serial.println("Sensor iniciado correctamente");
  else Serial.println("Error al iniciar el sensor");
}
 
void loop() {
  // Leer las aceleraciones y velocidades angulares
  sensor.getAcceleration(&ax, &ay, &az);
  sensor.getRotation(&gx, &gy, &gz);
  float ax_m_s2 = ax * (9.81/16384.0);
  float ay_m_s2 = ay * (9.81/16384.0);
  float az_m_s2 = az * (9.81/16384.0);
  float gx_deg_s = gx * (250.0/32768.0);
  float gy_deg_s = gy * (250.0/32768.0);
  float gz_deg_s = gz * (250.0/32768.0);
 
  //Mostrar las lecturas separadas por un [tab]
  // Serial.print("a[x y z](m/s2) g[x y z](deg/s):,");
  Serial.print(ax_m_s2); Serial.print(",");
  Serial.print(ay_m_s2); Serial.print(",");
  Serial.print(az_m_s2); Serial.print(",");
  Serial.print(gx_deg_s); Serial.print(",");
  Serial.print(gy_deg_s); Serial.print(",");
  Serial.println(gz_deg_s);
 
  delay(100);
}
