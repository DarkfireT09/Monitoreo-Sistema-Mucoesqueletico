#include "I2Cdev.h"
#include "MAX30105.h"
#include "MPU6050.h"
#include "Wire.h"
#include "spo2_algorithm.h"

// La dirección del MPU6050 puede ser 0x68 o 0x69, dependiendo
// del estado de AD0. Si no se especifica, 0x68 estará implicito

MPU6050 sensor;
MAX30105 particleSensor;

#define MAX_BRIGHTNESS 255

#if defined(__AVR_ATmega328P__) || defined(__AVR_ATmega168__)
// Arduino Uno doesn't have enough SRAM to store 100 samples of IR led data and
// red led data in 32-bit format To solve this problem, 16-bit MSB of the
// sampled data will be truncated. Samples become 16-bit data.
uint16_t irBuffer[100];   // infrared LED sensor data
uint16_t redBuffer[100];  // red LED sensor data
#else
uint32_t irBuffer[100];   // infrared LED sensor data
uint32_t redBuffer[100];  // red LED sensor data
#endif

int32_t bufferLength;  // data length
int32_t spo2;          // SPO2 value
int8_t validSPO2;      // indicator to show if the SPO2 calculation is valid
int32_t heartRate;     // heart rate value
int8_t
    validHeartRate;  // indicator to show if the heart rate calculation is valid

byte pulseLED = 11;  // Must be on PWM pin
byte readLED = 13;   // Blinks with each data read

// Valores RAW (sin procesar) del acelerometro y giroscopio en los ejes x,y,z
int ax, ay, az;
int gx, gy, gz;

void setup() {
    Serial.begin(57600);
    Wire.begin();         // Iniciando I2C
    sensor.initialize();  // Iniciando el sensor acelerometro

    if (!particleSensor.begin(
            Wire, I2C_SPEED_FAST))  // Use default I2C port, 400kHz speed
    {
        Serial.println(F("MAX30105 was not found. Please check wiring/power."));
        while (1)
            ;
    }
    byte ledBrightness = 60;  // Options: 0=Off to 255=50mA
    byte sampleAverage = 4;   // Options: 1, 2, 4, 8, 16, 32
    byte ledMode =
        2;  // Options: 1 = Red only, 2 = Red + IR, 3 = Red + IR + Green
    byte sampleRate = 100;  // Options: 50, 100, 200, 400, 800, 1000, 1600, 3200
    int pulseWidth = 411;   // Options: 69, 118, 215, 411
    int adcRange = 4096;    // Options: 2048, 4096, 8192, 16384

    particleSensor.setup(ledBrightness, sampleAverage, ledMode, sampleRate,
                         pulseWidth,
                         adcRange);  // Configure sensor with these settings

    pinMode(8, OUTPUT);  // led
    pinMode(9, OUTPUT);  // vibrador
}

void loop() {
    bufferLength = 100;  // buffer length of 100 stores 4 seconds of samples
                         // running at 25sps
    if (Serial.available()) {
        // Serial.println(Serial.read());
        switch (Serial.read()) {
            case (118): {  // alerta
                // Serial.print("v");
                digitalWrite(8, HIGH);
                digitalWrite(9, HIGH);
                delay(3000);
                digitalWrite(8, LOW);
                digitalWrite(9, LOW);
                Serial.println(1);
                // delay(1000);
            } break;
            case (97): {  // acelerometro
                // Serial.print("a");

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
                // delay(1000);
            } break;
            case (112): {  // pulsioximetro
                maxim_heart_rate_and_oxygen_saturation(
                    irBuffer, bufferLength, redBuffer, &spo2, &validSPO2,
                    &heartRate, &validHeartRate);
                for (byte i = 25; i < 100; i++) {
                    redBuffer[i - 25] = redBuffer[i];
                    irBuffer[i - 25] = irBuffer[i];
                }

                // take 25 sets of samples before calculating the heart rate.
                for (byte i = 75; i < 100; i++) {
                    while (particleSensor.available() ==
                           false)                // do we have new data?
                        particleSensor.check();  // Check the sensor for new
                                                 // data

                    digitalWrite(
                        readLED,
                        !digitalRead(readLED));  // Blink onboard LED
                                                 // with every data read

                    redBuffer[i] = particleSensor.getRed();
                    irBuffer[i] = particleSensor.getIR();
                    particleSensor
                        .nextSample();  // We're finished with this sample so
                                        // move to next sample

                    // send samples and calculation result to terminal program
                    // through UART
                }

                // After gathering 25 new samples recalculate HR and SP02

                Serial.print(heartRate, DEC);
                Serial.print(",");
                Serial.println(spo2, DEC);

                maxim_heart_rate_and_oxygen_saturation(
                    irBuffer, bufferLength, redBuffer, &spo2, &validSPO2,
                    &heartRate, &validHeartRate);
                sensor.initialize();
                // delay(1000);
            } break;

                // delay(1000);
        }
    }
}
