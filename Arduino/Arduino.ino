#include <SoftwareSerial.h>

SoftwareSerial Lily(10,11);


void setup() {
  // put your setup code here, to run once:
  Serial.print(9600);
  Lily.begin(38400);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Lily.available()){
    Serial.write(Lily.read());
  }


  if(Serial.available()){
    Lily.write(Serial.read());
  }
}
