// Liibreria BT
#include <SoftwareSerial.h>

// Librerias MPU
#include "I2Cdev.h"
#include "MPU6050.h"
#include "Wire.h"

// Librerias pulsometro

#define USE_ARDUINO_INTERRUPTS true    // Set-up low-level interrupts for most acurate BPM math.
#include <PulseSensorPlayground.h>     // Includes the PulseSensorPlayground Library.   

// Variables
// BT
SoftwareSerial BT(5, 6);  // rx -> 6; tx -> 5
// Acelerometro
MPU6050 sensor;

int ax, ay, az;
int gx, gy, gz;

// Pulsometro
const int PulseWire = 0;       // PulseSensor PURPLE WIRE connected to ANALOG PIN 0
const int LED13 = 13;          // The on-board Arduino LED, close to PIN 13.
int Threshold = 550;           // Determine which Signal to "count as a beat" and which to ignore.
                               // Use the "Gettting Started Project" to fine-tune Threshold Value beyond default setting.
                               // Otherwise leave the default "550" value. 
                               
PulseSensorPlayground pulseSensor;  // Creates an instance of the PulseSensorPlayground object called "pulseSensor"
int myBPM = pulseSensor.getBeatsPerMinute();


// ciclos

int cont;
int a1 = 0;



void setup() {
    // put your setup code here, to run once:
    Serial.begin(9600);
    BT.begin(9600);

    // 
    Wire.begin();         // Iniciando I2C
    sensor.initialize();  // Iniciando el sensor acelerometro

    pinMode(10, OUTPUT);
    pinMode(11, OUTPUT);
}

void loop() {
    float avrBPM = 0;
    for (cont = 0; cont < 1800; cont++) {
        sensor.getRotation(&gx, &gy, &gz);
        float gx_deg_s = gx * (250.0 / 32768.0);
        float gy_deg_s = gy * (250.0 / 32768.0);
        float gz_deg_s = gz * (250.0 / 32768.0);

        Serial.print(gx_deg_s);
        Serial.print(",");
        Serial.print(gy_deg_s);
        Serial.print(",");
        Serial.println(gz_deg_s);
        
        BT.print(gx_deg_s);
        BT.print(",");
        BT.print(gy_deg_s);
        BT.print(",");
        BT.println(gz_deg_s);
        delay(1000);

        if (gz_deg_s < -3) { // condicion de alerta
            a1++;
            delay(1000);
        } else {
            a1 = 0;
        }

        if (a1 > 3) {
            BT.print(1);
            digitalWrite(10, 1);
            digitalWrite(11, 1);
            delay(3000);
            digitalWrite(10, 0);
            digitalWrite(11, 0);
        }
        for(cont = 0; cont < 10; cont ++){ // se toma el promedio de 10 medidas
            myBPM = pulseSensor.getBeatsPerMinute();
            avrBPM += myBPM;
        }
        // BT.println(avrBPM);
        int testBPM = random(60, 100);
    }
}
