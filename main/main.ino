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
  
  Serial.begin(57600); 
  Wire.begin();           //Iniciando I2C  
  sensor.initialize();    //Iniciando el sensor
  }

void loop() {
    if (Serial.available()) {
        if (Serial.read() == 'a') {
            sensor.getAcceleration(&ax, &ay, &az);
            sensor.getRotation(&gx, &gy, &gz);
            float ax_m_s2 = ax * (9.81 / 16384.0);
            float ay_m_s2 = ay * (9.81 / 16384.0);
            float az_m_s2 = az * (9.81 / 16384.0);
            float gx_deg_s = gx * (250.0 / 32768.0);
            float gy_deg_s = gy * (250.0 / 32768.0);
            float gz_deg_s = gz * (250.0 / 32768.0);

            // Mostrar las lecturas separadas por un [tab]
            // Serial.print("a[x y z](m/s2) g[x y z](deg/s):,");
            Serial.print(ax_m_s2);
            Serial.print(",");
            Serial.print(ay_m_s2);
            Serial.print(",");
            Serial.print(az_m_s2);
            Serial.print(",");
            Serial.print(gx_deg_s);
            Serial.print(",");
            Serial.print(gy_deg_s);
            Serial.print(",");
            Serial.println(gz_deg_s);
            delay(1000);
        } else {
            Serial.println("0,1");
            delay(1000);
        }
    }
}
